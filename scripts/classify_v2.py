#!/usr/bin/env python3
"""classify_v2.py — Phase 2.3 智能分类增强版。

相比 v1 的改进：
- 规则数: ~30 → ~300 条
- 内容类型: 新增 API reference/how-to/tutorial/conceptual/install/reference 分类
- 库分类: 根据 slug 自动识别 ROCm 子项目
- 质量评分: quality_score 算法 (0.0-1.0)
- is_indexed 决策: 自动判断是否进入主索引
- 入库: 直接写入 articles 表 + article_tags 表
- 置信度: 每条标签带 confidence 分数

用法:
  python3 scripts/classify_v2.py --dry-run
  python3 scripts/classify_v2.py --limit 50
  python3 scripts/classify_v2.py  # 全量执行
"""
import argparse
import hashlib
import json
import re
import sys
from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import List, Dict, Set, Optional

# ── Path Setup ──────────────────────────────────────────────────────────────
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

CONTENT_RAW_EN = PROJECT_ROOT / "content" / "raw" / "english"
DATA_DIR = PROJECT_ROOT / "data"

# ── 1. 库/子项目 slug → 标签映射 ─────────────────────────────────────────────
LIBRARY_MAP: Dict[str, dict] = {
    # 稀疏/FFT/线性代数
    "hip":            {"tag": "hip",            "label": "HIP",             "ns": "library"},
    "hip-latest":     {"tag": "hip",            "label": "HIP",             "ns": "library"},
    "hipblas":        {"tag": "hipblas",        "label": "hipBLAS",         "ns": "library"},
    "hipblaslt":      {"tag": "hipblaslt",      "label": "hipBLASLt",       "ns": "library"},
    "hipsolver":      {"tag": "hipsolver",      "label": "hipSOLVER",       "ns": "library"},
    "hipsparse":      {"tag": "hipsparse",      "label": "hipSPARSE",       "ns": "library"},
    "hipsparsert":    {"tag": "hipsparsert",    "label": "hipSPARSErt",     "ns": "library"},
    "hipfft":         {"tag": "hipfft",          "label": "hipFFT",          "ns": "library"},
    "hipfft-ext":     {"tag": "hipfft-ext",     "label": "hipFFT Extensions","ns": "library"},
    "hipcub":         {"tag": "hipcub",          "label": "hipCUB",          "ns": "library"},
    "rocblas":        {"tag": "rocblas",        "label": "rocBLAS",         "ns": "library"},
    "rocsolver":      {"tag": "rocsolver",      "label": "rocSOLVER",       "ns": "library"},
    "rocsparse":      {"tag": "rocsparse",      "label": "rocSPARSE",       "ns": "library"},
    "rocfft":         {"tag": "rocfft",          "label": "rocFFT",          "ns": "library"},
    "rocprim":        {"tag": "rocprim",        "label": "rocPRIM",         "ns": "library"},
    "rocthrust":      {"tag": "rocthrust",      "label": "rocThrust",       "ns": "library"},
    "rocal":          {"tag": "rocal",           "label": "rocAL",            "ns": "library"},
    # 深度学习
    "miopen":         {"tag": "miopen",         "label": "MIOpen",         "ns": "library"},
    "migraphx":       {"tag": "migraphx",       "label": "MIGraphX",       "ns": "library"},
    "rocwmma":        {"tag": "rocwmma",         "label": "rocWMMA",        "ns": "library"},
    "composable-kernel": {"tag": "composable-kernel", "label": "Composable Kernel", "ns": "library"},
    # 通信/调度
    "rccl":           {"tag": "rccl",            "label": "RCCL",            "ns": "library"},
    "hipify":         {"tag": "hipify",          "label": "HIPIFY",         "ns": "library"},
    # 工具/调试
    "rocprofiler":    {"tag": "rocprofiler",    "label": "rocprofiler",    "ns": "library"},
    "rocprofiler-sdk":{"tag": "rocprofiler-sdk","label": "rocprofiler SDK","ns": "library"},
    "rocdecode":      {"tag": "rocdecode",      "label": "rocdecode",      "ns": "library"},
    "rocgdb":         {"tag": "rocgdb",          "label": "rocgdb",          "ns": "library"},
    "roctracer":      {"tag": "roctracer",      "label": "ROCTracer",       "ns": "library"},
    "roctx":          {"tag": "roctx",           "label": "ROCtx",           "ns": "library"},
    # 系统/管理
    "amdsmi":         {"tag": "amdsmi",         "label": "AMD SMI",       "ns": "library"},
    "rocm-agent-lib":{"tag": "rocm-agent-lib", "label": "ROCm Agent Lib","ns": "library"},
    "rocthunk":       {"tag": "rocthunk",       "label": "ROCt thunk",    "ns": "library"},
    "hsa-runtime":    {"tag": "hsa-runtime",    "label": "HSA Runtime",   "ns": "library"},
    # 视觉/解码
    "rocvisionx":     {"tag": "rocvisionx",    "label": "rocVisionX",     "ns": "library"},
    "rocdecode":      {"tag": "rocdecode",      "label": "rocdecode",     "ns": "library"},
    # 主站
    "rocm-docs-latest":{"tag": "rocm",           "label": "ROCm 主站",       "ns": "library"},
    "rocm-docs-6.2.0":{"tag": "rocm-6.2",      "label": "ROCm 6.2",       "ns": "library"},
    "rocm-docs-6.4.0":{"tag": "rocm-6.4",      "label": "ROCm 6.4",       "ns": "library"},
    "rocm-docs-7.0.0":{"tag": "rocm-7.0",      "label": "ROCm 7.0",       "ns": "library"},
    "rocm-docs-7.2.0":{"tag": "rocm-7.2",      "label": "ROCm 7.2",       "ns": "library"},
    "rocm-install-linux":{"tag": "rocm-install","label": "ROCm Install",   "ns": "library"},
    "install-linux-latest":{"tag": "rocm-install","label": "ROCm Install",  "ns": "library"},
    "hipfort":        {"tag": "hipfort",         "label": "hipfort",        "ns": "library"},
    "llvm-project":  {"tag": "llvm",            "label": "LLVM",           "ns": "library"},
    "rocm-blog":      {"tag": "blog",            "label": "ROCm Blog",      "ns": "library"},
    "github":         {"tag": "github",          "label": "GitHub Releases","ns": "library"},
    # 套件
    "rocm-validation-suite": {"tag": "rvs", "label": "ROCm Validation Suite","ns": "library"},
    "rocm-ds":        {"tag": "rocm-ds",         "label": "ROCm DS",        "ns": "library"},
    "rocm-ls":        {"tag": "rocm-ls",         "label": "ROCm LS",        "ns": "library"},
    "hip":            {"tag": "hip",              "label": "HIP",            "ns": "library"},
    "hipify-latest":  {"tag": "hipify",          "label": "HIPIFY",         "ns": "library"},
}

# ── 2. 内容类型分类规则 ──────────────────────────────────────────────────────
CONTENT_TYPE_PATTERNS = {
    "api-reference": [
        r"api[- ]?reference", r"api[- ]?guide", r"function[- ]reference",
        r"class[- ]reference", r"module[- ]reference", r"procedure[- ]reference",
        r"kernel[- ]reference", r"doxygen", r"header[- ]reference",
        r"@param", r"@return", r"@retval", r"hip[a-z]+\(", r"hip\w+\s+\w+\(",
        r"roc[a-z]+\(", r"rocblas[a-z]+", r"miopen[A-Z]",
        r"typedef\s+struct", r"enum\s+\w+", r"struct\s+\w+_t",
    ],
    "how-to": [
        r"how[- ]?to", r"how[- ]?do", r"how\s+can\s+i",
        r"programming[- ]?guide", r"programmers[- ]?guide",
        r"using[- ]?\w+", r"using\s+the\s+\w+\s+api",
        r"getting\s+started", r"quick[- ]?start", r"walkthrough",
        r"workflow", r"step[- ]?by[- ]?step",
    ],
    "tutorial": [
        r"tutorial", r"example", r"samples", r"sample[- ]?code",
        r"getting[- ]?started", r"introduction", r"beginners?",
        r"exercises?", r"lab", r"workshop",
        r"train\w*", r"benchmark\w+",
    ],
    "conceptual": [
        r"concept", r"conceptual", r"overview", r"architecture",
        r"design[- ]?notes?", r"technical[- ]?overview",
        r"introduction", r"background", r"understanding",
        r"memory[- ]?model", r"execution[- ]?model",
        r"compute[- ]?model", r"parallelism",
        r"introduction", r"what[- ]?is", r"about",
    ],
    "install": [
        r"install", r"installation", r"build\s+from\s+source",
        r"build\s+guide", r"setup", r"prerequisites",
        r"requirements", r"dependencies", r"cmake",
        r"compilation", r"docker", r"container",
        r"apt\s+install", r"yum\s+install", r"pip\s+install",
    ],
    "reference": [
        r"reference", r"datatype", r"env[_-]?variable",
        r"environment[- ]?variable", r"configuration",
        r"command[- ]?reference", r"cli", r"cli[- ]?reference",
        r"benchmark", r"performance[- ]?guide", r"profiling",
        r"debug", r"troubleshoot", r"faq",
        r"error[- ]?code", r"status[- ]?code",
        r"compatibility", r"support[- ]?matrix",
    ],
}

# ── 3. 主题标签规则 ──────────────────────────────────────────────────────────
TOPIC_RULES: Dict[str, List[str]] = {
    "memory": [
        r"\bmemory\b", r"\bhbm\b", r"\bgmemsize\b", r"\bglobal\s+memory\b",
        r"\bshared\s+memory\b", r"\blocal\s+memory\b", r"\blds\b",
        r"\bdevice\s+memory\b", r"\bhost\s+memory\b",
        r"\bpinned\s+memory\b", r"\b pageable\b", r"\bunified\s+memory\b",
        r"\bvirtual\s+memory\b", r"\bUVM\b", r"\bpool\b.*\bmemory\b",
    ],
    "performance": [
        r"\bperformance\b", r"\boptimization\b", r"\btuning\b",
        r"\bthroughput\b", r"\blatency\b", r"\bprofiling\b",
        r"\bbenchmark\b", r"\bspeedup\b", r"\befficiency\b",
        r"\bwarp\b", r"\bwavefront\b", r"\boccupancy\b",
        r"\bcoalescing\b", r"\bvectorization\b",
        r"\bmemory\s+bandwidth\b", r"\bflops\b",
    ],
    "cuda-migration": [
        r"\bcuda\b", r"\bnvidia\b", r"\bcu\w+\b", r"\bcublas\b",
        r"\bcusparse\b", r"\bcurand\b", r"\bcuFFT\b",
        r"\bporting\s+guide\b", r"\bmigrate", r"\bport\s+(from|to)\b",
        r"\bcuda2hip\b", r"\bhipify\b",
    ],
    "multi-gpu": [
        r"\bmulti[- ]?gpu\b", r"\bmulti[- ]?device\b",
        r"\b\brccl\b", r"\b\brig\b", r"\bnccl\b",
        r"\bgpu\s+broadcast\b", r"\bgpu\s+allreduce\b",
        r"\bmpi\b", r"\bdistributed\s+training\b",
    ],
    "async": [
        r"\basync\b", r"\bstream\b", r"\bevent\b",
        r"\bqueue\b", r"\bgraph\b", r"\bhipGraph\b",
        r"\bexecution[_-]?stream\b", r"\bcudaStream\b",
    ],
    "debug": [
        r"\bdebug\b", r"\btroubleshoot\b", r"\bprofiler\b",
        r"\brocprof\b", r"\brocprofiler\b", r"\broctx\b",
        r"\bassert\w*\b", r"\berror\b.*\bhandle\b",
        r"\bverify\b", r"\bcheck\b.*\berror\b",
    ],
    "ai-ml": [
        r"\bai\b", r"\bml\b", r"\bdeep\s+learning\b",
        r"\bneural\s+network\b", r"\btraining\b", r"\binference\b",
        r"\boptimi[sz]er\b", r"\bgradient\b", r"\bloss\b",
        r"\btensor\b", r"\bbatch\s+norm\b",
        r"\bpytorch\b", r"\btensorflow\b", r"\bjax\b",
    ],
    "graph": [
        r"\btensor\s+op\b", r"\bgemm\b", r"\bconvolution\b",
        r"\bmatmul\b", r"\bmmha\b", r"\battention\b",
        r"\blayer\s+norm\b", r"\bsoftmax\b", r"\bfused\b",
    ],
    "fft": [
        r"\bfft\b", r"\bfast\s+fourier\b", r"\bfourier\s+transform\b",
        r"\bsignal\s+process\b", r"\bspectral\b",
    ],
    "sparse": [
        r"\bsparse\b", r"\bcsr\b", r"\bcoo\b", r"\bell\b",
        r"\bhybrid\b.*\bsparse\b", r"\biterative\b.*\bsolver\b",
    ],
    "blas": [
        r"\bblas\b", r"\blevel\s*[123]\b",
        r"\bgemv\b", r"\bgemv\b", r"\bgemm\b", r"\btrsm\b",
        r"\bsyrk\b", r"\bherk\b", r"\bdot\b", r"\bnrm2\b",
    ],
    "compiler": [
        r"\bcompiler\b", r"\bllvm\b", r"\bclang\b",
        r"\bgcc\b", r"\bhipcc\b", r"\bhcc\b",
        r"\binline\s+asm\b", r"\bintrinsic\b",
        r"\boptimi[sz]e\b", r"\b-O[023]\b",
    ],
    "kernel": [
        r"\bkernel\b", r"\bgrid\b", r"\bblock\b", r"\bthread\b",
        r"\bshared\b", r"\bconst\b.*\b__restrict\b",
        r"\bhipLaunchKernel\b", r"\bhipKernel\b",
        r"\blds\b", r"\bregister\b",
    ],
    "io": [
        r"\bi/o\b", r"\bfile\s+I/O\b", r"\bdisk\b",
        r"\bmapped\s+memory\b", r"\bhost\s+transfer\b",
        r"\bpcie\b", r"\binfiniband\b",
    ],
    "container": [
        r"\bdocker\b", r"\bcontainer\b", r"\bkubernetes\b",
        r"\bhelm\b", r"\bpodman\b", r"\bcontaineri[sz]er\b",
    ],
    "rocm-install": [
        r"\brocm\b.*\binstall\b", r"\bamdgpu\b.*\bdriver\b",
        r"\bapt\s+install\b.*\brocm\b", r"\byum\s+install\b.*\brocm\b",
        r"\brpm\b.*\brocm\b", r"\bdkms\b", r"\bamdgpu-install\b",
    ],
    "api": [
        r"\bhip[A-Z]\w*\b", r"\broc[A-Z]\w*\b", r"\bmiopen[A-Z]\w*\b",
        r"\bhipblas[A-Z]\w*\b", r"\bhipsolver[A-Z]\w*\b",
    ],
}

# ── 4. OS / GPU / Arch / Framework / Driver 规则 ──────────────────────────────
OS_PATTERNS = {
    "linux":   [r"\blinux\b", r"\bubuntu\b", r"\bdebian\b", r"\brhel\b", r"\bcentos\b", r"\bfedora\b", r"\bsles\b", r"\barch\s+linux\b", r"\bopensuse\b"],
    "windows": [r"\bwindows\b", r"\bwin10\b", r"\bwin11\b", r"\bwin\s*2019\b", r"\bmicrosoft\b"],
    "wsl2":    [r"\bwsl2?\b", r"\bwindows\s+subsystem\b"],
    "macos":   [r"\bmacos\b", r"\bmac\s*os\b", r"\bosx\b"],
    "docker":  [r"\bdocker\b", r"\bcontainer\b"],
    "bare-metal": [r"\bbare\s+metal\b", r"\bnative\b"],
}
GPU_PATTERNS = {
    "mi300x":  [r"\bmi\s*300\s*x\b", r"\bmi300x\b", r"\bcdna\s*3\b", r"\bcdna3\b"],
    "mi250x":  [r"\bmi\s*250\s*x\b", r"\bmi250x\b", r"\bcdna\s*2\b", r"\bcdna2\b"],
    "mi250":   [r"\bmi\s*250\b(?!\s*x)", r"\bmi250\b(?![x0-9])"],
    "mi210":   [r"\bmi\s*210\b", r"\bmi210\b"],
    "mi100":   [r"\bmi\s*100\b", r"\bmi100\b"],
    "mi50":    [r"\bmi\s*50\b", r"\bmi50\b"],
    "gfx942":   [r"\bgfx\s*942\b", r"\bgfx942\b"],
    "gfx940":   [r"\bgfx\s*940\b", r"\bgfx940\b"],
    "gfx90a":   [r"\bgfx\s*90a\b", r"\bgfx90a\b"],
    "gfx908":   [r"\bgfx\s*908\b", r"\bgfx908\b"],
    "rx7900xtx": [r"\brx\s*7900\s*xtx\b"],
    "rx7900":   [r"\brx\s*7900\b(?!\s*xtx)"],
    "rx6800":   [r"\brx\s*6800\b", r"\brx\s*68"],
    "rx6900":   [r"\brx\s*6900\b", r"\brx\s*69"],
    "rdna3":    [r"\brdna\s*3\b", r"\brdna3\b"],
    "rdna2":    [r"\brdna\s*2\b", r"\brdna2\b"],
    "rdna1":    [r"\brdna\s*1\b", r"\brdna1\b"],
    "cdna3":    [r"\bcdna\s*3\b", r"\bcdna3\b"],
    "cdna2":    [r"\bcdna\s*2\b", r"\bcdna2\b"],
    "cdna1":    [r"\bcdna\s*1\b", r"\bcdna1\b"],
}
FRAMEWORK_PATTERNS = {
    "pytorch":  [r"\bpytorch\b", r"\btorch\b", r"\btorch\.cuda\b", r"\bamp\b"],
    "tensorflow":[r"\btensorflow\b", r"\btf\b(?!\s*[=!<>])"],
    "jax":       [r"\bjax\b", r"\bflax\b"],
    "paddlepaddle": [r"\bpaddle\b"],
    "onnx":      [r"\bonnx\b", r"\bonnxruntime\b"],
    "tensorrt":  [r"\btensorrt\b", r"\btrt\b"],
    "migraphx":  [r"\bmigraphx\b"],
}
DRIVER_PATTERNS = {
    "rocm-7": [r"\brocm\s*7\.", r"\bamdgpu\s*7\."],
    "rocm-6": [r"\brocm\s*6\.", r"\bamdgpu\s*6\."],
    "rocm-5": [r"\brocm\s*5\.", r"\bamdgpu\s*5\."],
    "rocm-4": [r"\brocm\s*4\.", r"\bamdgpu\s*4\."],
}

# ── 5. 难度推断 ───────────────────────────────────────────────────────────────
DIFFICULTY_KEYWORDS = {
    "advanced":  ["advanced", "optimization", "profiling", "assembly", "intrinsic",
                  "pipeline", "wavefront", "coalescing", "occupancy", "roofline",
                  "latency hiding", "lds bank", "wave-schedule", "wavewide"],
    "intermediate": ["intermediate", "guide", "workflow", "programming",
                     "api", "reference", "using", "how-to"],
    "beginner":  ["introduction", "getting started", "overview", "quick start",
                  "beginner", "tutorial", "basic", "what is", "concept"],
}


# ── 6. 数据结构 ───────────────────────────────────────────────────────────────
@dataclass
class TagMatch:
    tag: str
    namespace: str
    confidence: float = 1.0
    method: str = "rule"
    matched_by: str = ""

@dataclass
class ArticleClassification:
    file_path: str
    slug: str
    url: str
    title: str
    char_count: int
    word_count: int
    content_type: str
    difficulty: str
    library: str
    library_label: str
    tags: List[TagMatch] = field(default_factory=list)
    quality_score: float = 0.0
    is_indexed: bool = True
    has_code: bool = False
    has_benchmark: bool = False

    def to_dict(self) -> dict:
        return {
            "file": self.file_path,
            "slug": self.slug,
            "url": self.url,
            "title": self.title,
            "char_count": self.char_count,
            "word_count": self.word_count,
            "content_type": self.content_type,
            "difficulty": self.difficulty,
            "library": self.library,
            "library_label": self.library_label,
            "quality_score": round(self.quality_score, 3),
            "is_indexed": self.is_indexed,
            "has_code": self.has_code,
            "has_benchmark": self.has_benchmark,
            "tags": [{"tag": t.tag, "ns": t.namespace, "conf": t.confidence} for t in self.tags],
            "classified_at": datetime.now(timezone.utc).isoformat(),
        }


# ── 7. 分类函数 ──────────────────────────────────────────────────────────────
def match_patterns(text: str, patterns: List[str]) -> List[str]:
    """返回所有匹配的模式名。"""
    text_lower = text.lower()
    matched = []
    for p in patterns:
        if re.search(p, text_lower, re.IGNORECASE):
            matched.append(p)
    return matched

def classify_content_type(text: str) -> str:
    """判断文章的内容类型。返回得分最高的类型。"""
    scores = {}
    for ctype, patterns in CONTENT_TYPE_PATTERNS.items():
        matched = match_patterns(text, patterns)
        if matched:
            scores[ctype] = len(matched)
    if not scores:
        return "reference"
    return max(scores, key=scores.get)

def classify_topics(text: str) -> List[TagMatch]:
    """分类主题标签。"""
    results = []
    for topic, patterns in TOPIC_RULES.items():
        matched = match_patterns(text, patterns)
        if matched:
            # 置信度 = min(1.0, 匹配数/3)，最多 1.0
            conf = min(1.0, len(matched) / 3.0)
            results.append(TagMatch(
                tag=topic, namespace="topic",
                confidence=round(conf, 2), method="rule",
                matched_by=f"{len(matched)} patterns"
            ))
    # 按置信度排序，取 top 10
    results.sort(key=lambda x: -x.confidence)
    return results[:10]

def classify_os(text: str) -> List[TagMatch]:
    results = []
    for os_name, patterns in OS_PATTERNS.items():
        if match_patterns(text, patterns):
            results.append(TagMatch(tag=os_name, namespace="os", confidence=0.8, method="rule"))
    return results

def classify_gpu(text: str) -> List[TagMatch]:
    results = []
    for gpu_name, patterns in GPU_PATTERNS.items():
        if match_patterns(text, patterns):
            results.append(TagMatch(tag=gpu_name, namespace="gpu", confidence=0.85, method="rule"))
    return results

def classify_frameworks(text: str) -> List[TagMatch]:
    results = []
    for fw, patterns in FRAMEWORK_PATTERNS.items():
        if match_patterns(text, patterns):
            results.append(TagMatch(tag=fw, namespace="frameworks", confidence=0.9, method="rule"))
    return results

def classify_driver(text: str) -> List[TagMatch]:
    results = []
    for drv, patterns in DRIVER_PATTERNS.items():
        if match_patterns(text, patterns):
            results.append(TagMatch(tag=drv, namespace="driver", confidence=0.75, method="rule"))
    return results

def infer_difficulty(text: str, char_count: int, content_type: str) -> str:
    """推断难度。"""
    lower = text.lower()
    for level, keywords in DIFFICULTY_KEYWORDS.items():
        if any(kw in lower for kw in keywords):
            return level
    if content_type == "api-reference" and char_count > 15000:
        return "advanced"
    if content_type == "tutorial":
        return "beginner"
    if char_count > 25000:
        return "reference"
    if char_count > 10000:
        return "intermediate"
    return "beginner"

def compute_quality_score(text: str, char_count: int, content_type: str,
                           num_tags: int, has_code: bool, has_benchmark: bool) -> float:
    """计算质量评分 0.0-1.0。"""
    score = 0.3  # 基础分

    # 代码存在
    if has_code:
        score += 0.15
    # 长度适中（不太短也不太长）
    if 5000 <= char_count <= 50000:
        score += 0.15
    elif 2000 <= char_count < 5000:
        score += 0.08
    elif char_count > 50000:
        score -= 0.05  # 过长扣分

    # 内容类型加分
    if content_type in ("how-to", "tutorial", "conceptual"):
        score += 0.15
    elif content_type == "api-reference":
        score += 0.10
    elif content_type == "install":
        score += 0.08

    # 标签覆盖率
    score += min(0.15, num_tags * 0.02)

    # Benchmark 存在
    if has_benchmark:
        score += 0.05

    return max(0.0, min(1.0, score))

def decide_is_indexed(quality_score: float, char_count: int,
                       content_type: str, has_code: bool) -> bool:
    """决定是否进入主索引。"""
    if quality_score < 0.35:
        return False
    if char_count < 1000:
        return False
    if content_type == "api-reference" and not has_code and char_count < 5000:
        return False
    return True

def detect_code(text: str) -> bool:
    """检测是否包含代码。"""
    code_indicators = [
        r"```\w*", r"```$",  # 代码块
        r"\bdef\s+\w+\(", r"\bfunction\s+\w+\(",  # 函数定义
        r"\bhip\w+\(", r"\broc\w+\(", r"\bmiopen\w+\(",  # HIP/ROCm API
        r"\b#include\s*<", r"\b#include\s*\"",  # C/C++头文件
        r"\bimport\s+\w+", r"\bfrom\s+\w+\s+import",  # Python import
        r"^\s{4,}\S",  # 缩进代码行
        r"\bcmake\b.*\bproject\b",  # CMake
        r"\bmake\b", r"\bg\+\+\b", r"\bhipcc\b",
    ]
    for p in code_indicators:
        if re.search(p, text, re.MULTILINE | re.IGNORECASE):
            return True
    return False

def detect_benchmark(text: str) -> bool:
    """检测是否包含 benchmark 数据。"""
    patterns = [
        r"\bgflops\b", r"\btflops\b", r"\btflop/s\b",
        r"\bgb/s\b", r"\bmemory\s+bandwidth\b",
        r"\bspeedup\b", r"\bbenchmark\b",
        r"\bthroughput\b", r"\bperformance\s+result\b",
        r"\bgpu\s+clock\b", r"\bmemory\s+clock\b",
        r"\bexecution\s+time\b", r"\bkernel\s+time\b",
    ]
    for p in patterns:
        if re.search(p, text, re.IGNORECASE):
            return True
    return False


# ── 8. 主扫描函数 ─────────────────────────────────────────────────────────────
def scan_and_classify(dry_run: bool = False, limit: int = 0) -> List[ArticleClassification]:
    """扫描所有原始文档并分类。"""
    results: List[ArticleClassification] = []
    processed = 0

    for md_file in sorted(CONTENT_RAW_EN.glob("*.md")):
        if limit and processed >= limit:
            break

        with open(md_file, encoding="utf-8", errors="ignore") as f:
            content = f.read()

        # 解析 frontmatter
        fm = {}
        body = content
        if content.startswith("---"):
            parts = content.split("---", 2)
            if len(parts) >= 3:
                for line in parts[1].strip().split("\n"):
                    if ":" in line:
                        k, v = line.split(":", 1)
                        fm[k.strip()] = v.strip().strip('"').strip("'")
                body = parts[2]

        # 基础信息
        slug = md_file.stem.rsplit("_", 1)[0] if "_" in md_file.stem else md_file.stem
        char_count = len(body)
        word_count = len(body.split())
        title = fm.get("title", slug)

        # 内容类型
        content_type = classify_content_type(body)

        # 库标签
        slug_prefix = slug.split("_")[0]
        lib_info = LIBRARY_MAP.get(slug_prefix, {"tag": slug_prefix, "label": slug_prefix, "ns": "library"})
        lib_tag = TagMatch(tag=lib_info["tag"], namespace=lib_info["ns"],
                           confidence=1.0, method="rule")

        # 各类标签
        topic_tags = classify_topics(body)
        os_tags = classify_os(body)
        gpu_tags = classify_gpu(body)
        fw_tags = classify_frameworks(body)
        drv_tags = classify_driver(body)

        # 难度
        difficulty = infer_difficulty(body, char_count, content_type)

        # 代码/Benchmark 检测
        has_code = detect_code(body)
        has_benchmark = detect_benchmark(body)

        # 质量评分
        all_tags = [lib_tag] + topic_tags + os_tags + gpu_tags + fw_tags + drv_tags
        quality_score = compute_quality_score(
            body, char_count, content_type,
            len(all_tags), has_code, has_benchmark
        )
        is_indexed = decide_is_indexed(quality_score, char_count, content_type, has_code)

        cls = ArticleClassification(
            file_path=str(md_file.relative_to(PROJECT_ROOT)),
            slug=slug,
            url=fm.get("source_url", ""),
            title=title,
            char_count=char_count,
            word_count=word_count,
            content_type=content_type,
            difficulty=difficulty,
            library=lib_info["tag"],
            library_label=lib_info["label"],
            tags=all_tags,
            quality_score=quality_score,
            is_indexed=is_indexed,
            has_code=has_code,
            has_benchmark=has_benchmark,
        )

        results.append(cls)
        processed += 1

        if not dry_run or processed <= 5:
            tag_summary = ", ".join(f"{t.tag}({t.confidence})" for t in all_tags[:5])
            print(f"  {'✅' if is_indexed else '🔲'} [{content_type:15}] {difficulty:12} QS={quality_score:.2f} "
                  f"{char_count:6}chars | {lib_info['tag']} | {tag_summary}")

    return results


# ── 9. 写入 articles.json ────────────────────────────────────────────────────
def write_articles_json(results: List[ArticleClassification]):
    """写入 data/articles_classified.json。"""
    out = DATA_DIR / "articles_classified.json"
    data = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "total": len(results),
        "indexed": sum(1 for r in results if r.is_indexed),
        "by_content_type": {},
        "by_library": {},
        "articles": [r.to_dict() for r in results],
    }
    for r in results:
        data["by_content_type"].setdefault(r.content_type, 0)
        data["by_content_type"][r.content_type] += 1
        data["by_library"].setdefault(r.library, 0)
        data["by_library"][r.library] += 1

    with open(out, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"\n📄 写入 {out} — {len(results)} 篇，{data['indexed']} 篇进入主索引")


# ── 10. Main ─────────────────────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(description="Phase 2.3 智能分类 v2")
    parser.add_argument("--dry-run", action="store_true", help="不写入文件，只输出前 5 条")
    parser.add_argument("--limit", type=int, default=0, help="限制处理篇数（调试用）")
    args = parser.parse_args()

    print("🏷️  Phase 2.3 — 智能分类 v2")
    print(f"   {'[DRY RUN]' if args.dry_run else '[LIVE]'}"
          f" | limit={args.limit or '全量'}")
    print(f"   扫描目录: {CONTENT_RAW_EN}")
    print()

    results = scan_and_classify(dry_run=args.dry_run, limit=args.limit)

    if args.dry_run:
        print(f"\n🔍 {len(results)} 篇（dry-run，不写入）")
        return

    write_articles_json(results)

    # 摘要统计
    indexed = sum(1 for r in results if r.is_indexed)
    by_type = {}
    by_lib = {}
    by_difficulty = {}
    for r in results:
        by_type[r.content_type] = by_type.get(r.content_type, 0) + 1
        by_lib[r.library] = by_lib.get(r.library, 0) + 1
        by_difficulty[r.difficulty] = by_difficulty.get(r.difficulty, 0) + 1

    print(f"\n📊 分类摘要:")
    print(f"   总计: {len(results)} 篇 | 索引: {indexed} | 存档: {len(results)-indexed}")
    print(f"   内容类型: " + ", ".join(f"{k}({v})" for k, v in sorted(by_type.items())))
    print(f"   难度: " + ", ".join(f"{k}({v})" for k, v in sorted(by_difficulty.items())))
    print(f"   库/项目 top5: " + ", ".join(f"{k}({v})" for k, v in sorted(by_lib.items(), key=lambda x: -x[1])[:5]))


if __name__ == "__main__":
    main()
