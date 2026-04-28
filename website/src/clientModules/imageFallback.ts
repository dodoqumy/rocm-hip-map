/**
 * Image Fallback Client Module
 *
 * 当远程图片加载失败时，自动切换到本地缓存的副本。
 *
 * 工作原理：
 *   1. 页面加载后，获取 /data/image-fallbacks.json 映射表
 *   2. 对页面上所有 <img> 元素注册 onerror 处理器
 *   3. 图片加载失败时 → 查找映射表 → 切换 src 到本地缓存
 *
 * 部署：Docusaurus 自动加载 src/clientModules/ 下的所有文件。
 */

// ── 全局 fallback 映射表（只加载一次）──
let fallbackMap: Record<string, string> | null = null;
let fetchPromise: Promise<Record<string, string>> | null = null;

async function loadFallbackMap(): Promise<Record<string, string>> {
  if (fallbackMap) return fallbackMap;
  if (fetchPromise) return fetchPromise;

  fetchPromise = fetch("/data/image-fallbacks.json")
    .then((res) => {
      if (!res.ok) throw new Error(`HTTP ${res.status}`);
      return res.json() as Promise<Record<string, string>>;
    })
    .then((data) => {
      fallbackMap = data;
      return data;
    })
    .catch((err) => {
      console.warn("[image-fallback] 加载映射表失败:", err.message);
      fallbackMap = {};
      return {};
    });

  return fetchPromise;
}

/**
 * 检查图片的 src 是否以 http:// 或 https:// 开头（远程图片）。
 * 跳过本地图片、data URI、SVG placeholder 等。
 */
function isRemoteImage(img: HTMLImageElement): boolean {
  const src = img.src || img.getAttribute("src") || "";
  return src.startsWith("http://") || src.startsWith("https://");
}

/**
 * 从完整的 src URL 中提取纯 URL 部分（去掉查询参数和哈希，用于精确匹配）。
 */
function normalizeUrl(url: string): string {
  try {
    const u = new URL(url);
    return u.origin + u.pathname;
  } catch {
    return url.split("?")[0].split("#")[0];
  }
}

/**
 * 为单个 <img> 注册回退逻辑。
 */
function attachFallback(img: HTMLImageElement, fallbacks: Record<string, string>): void {
  // 跳过已处理的
  if (img.dataset.fallbackReady === "1") return;

  // 只处理远程图片
  if (!isRemoteImage(img)) return;

  // 查找映射表（精确匹配 + 路径规范化）
  const normalizedUrl = normalizeUrl(img.src);
  const fallbackSrc = fallbacks[img.src] || fallbacks[normalizedUrl];

  if (!fallbackSrc) {
    // 无缓存副本，不注册处理器
    img.dataset.fallbackReady = "1";
    return;
  }

  // 注册 onerror
  img.dataset.fallbackReady = "1";

  // 如果图片已经加载失败（complete && naturalWidth === 0），立即切换
  if (img.complete && img.naturalWidth === 0) {
    img.src = fallbackSrc;
    return;
  }

  img.addEventListener(
    "error",
    function handleError() {
      // 防止无限循环
      if (img.dataset.fallbackTried === "1") return;
      img.dataset.fallbackTried = "1";
      img.src = fallbackSrc;
    },
    { once: true }
  );
}

/**
 * 扫描页面中所有 <img> 元素，为其注册回退。
 */
function scanAndAttach(fallbacks: Record<string, string>): void {
  const images = document.querySelectorAll<HTMLImageElement>("img");
  images.forEach((img) => attachFallback(img, fallbacks));
}

/**
 * 监听 DOM 变化（用于 SPA 导航后的新图片）。
 */
let observer: MutationObserver | null = null;

function startObserver(fallbacks: Record<string, string>): void {
  if (observer) return;

  observer = new MutationObserver((mutations) => {
    for (const mutation of mutations) {
      for (const node of mutation.addedNodes) {
        if (node instanceof HTMLImageElement) {
          attachFallback(node, fallbacks);
        } else if (node instanceof HTMLElement) {
          node.querySelectorAll<HTMLImageElement>("img").forEach((img) => {
            attachFallback(img, fallbacks);
          });
        }
      }
    }
  });

  observer.observe(document.body, {
    childList: true,
    subtree: true,
  });
}

// ── Docusaurus Client Module Lifecycle ──

// 页面首次加载：onRouteDidUpdate 也会触发，但首屏加载前我们也可以预加载映射表
// 使用 DOMContentLoaded 做初始扫描更可靠
if (typeof document !== "undefined") {
  // 预加载映射表（不阻塞渲染）
  loadFallbackMap().then((fallbacks) => {
    if (Object.keys(fallbacks).length === 0) return;

    // 扫描已加载的图片
    if (document.readyState === "loading") {
      document.addEventListener("DOMContentLoaded", () => {
        scanAndAttach(fallbacks);
        startObserver(fallbacks);
      });
    } else {
      scanAndAttach(fallbacks);
      startObserver(fallbacks);
    }
  });
}

// Docusaurus SPA 路由切换时重新扫描
// 使用 Docusaurus 的生命周期 hook
export function onRouteDidUpdate({ location, previousLocation }: any): void {
  // 客户端导航后，新页面的图片需要注册回退
  loadFallbackMap().then((fallbacks) => {
    if (Object.keys(fallbacks).length === 0) return;
    // 延迟一帧等 React 渲染完
    requestAnimationFrame(() => {
      scanAndAttach(fallbacks);
      startObserver(fallbacks);
    });
  });
}
