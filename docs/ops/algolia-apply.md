# Algolia DocSearch 申请指南

## 状态：待申请

> 本地搜索（@easyops-cn/docusaurus-search-local）已上线，Algolia 作为增强方案需单独申请。

## 申请步骤

1. 前往 https://docsearch.algolia.com/apply/
2. 填写：
   - **Website URL**: `https://dodoqumy.github.io/rocm-hip-map/`
   - **Email**: 你的邮箱
   - **I am the maintainer**: ✅
3. Algolia 审核通过后（通常 2-5 天），会发送：
   - `appId`
   - `apiKey`（search-only key）
   - `indexName`
4. 在 GitHub Secrets 配置 `ALGOLIA_APP_ID` 和 `ALGOLIA_API_KEY`
5. 在 `docusaurus.config.ts` 的 `themeConfig` 中添加：

```typescript
themeConfig: {
  algolia: {
    appId: process.env.ALGOLIA_APP_ID,
    apiKey: process.env.ALGOLIA_API_KEY,
    indexName: 'rocm-hip-map',
    contextualSearch: true,
    searchParameters: {},
  },
}
```

6. 在 `deploy.yml` 中注入环境变量：

```yaml
- name: Build website
  env:
    ALGOLIA_APP_ID: ${{ secrets.ALGOLIA_APP_ID }}
    ALGOLIA_API_KEY: ${{ secrets.ALGOLIA_API_KEY }}
  run: cd website && npm run build
```

## 当前方案

- **本地搜索**: `@easyops-cn/docusaurus-search-local` — 中英双语分词，CI 构建时自动生成索引
- **无需申请**: 本地搜索零依赖，构建后立即在 navbar 出现搜索框
- **体验升级**: Algolia 通过后可无缝切换，体验更流畅（模糊搜索、即时建议）
