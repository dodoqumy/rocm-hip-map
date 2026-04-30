# docs/plan/rocm-hip-map-v2-roadmap.md

# rocm-hip-map V2 Roadmap（总体计划）

## 项目目标

将当前 rocm-hip-map 从静态 GitHub Pages 文档站升级为：

* ROCm / HIP 中文第一情报站
* AMD GPU 跑模型入口站
* ROCm 搜索入口
* 高质量双语知识库
* 可持续增长内容平台

---

## 核心指标（6个月）

* 月访问 UV：100,000+
* 已收录文章：10,000+
* GitHub / 社区情报：20,000+
* 中文翻译页：3,000+
* SEO 长尾词排名：500+

---

## 技术架构

## 前端

* Next.js
* Tailwind CSS
* ISR / SSR
* Sitemap / RSS / SEO

## 后端

* Python FastAPI（可选）
* Worker Queue
* Cron Jobs

## 数据层

* PostgreSQL
* Redis（任务队列）
* Object Storage（图片 / 备份）

---

## 五层采集架构

## Layer 1 官方源

* ROCm docs
* HIP docs
* HIPIFY docs
* AMD Blog
* Release Notes

## Layer 2 开源生态

* GitHub Issues
* PR
* Releases
* Discussions

## Layer 3 学术论文

* arXiv
* OpenReview
* PapersWithCode

## Layer 4 第三方内容

* PyTorch Blog
* HuggingFace
* vLLM
* Phoronix
* 中文技术博客

## Layer 5 社区舆情

* Reddit
* Hacker News
* Discord
* Telegram（后期）

---

## 内容加工系统

* 自动翻译
* 自动摘要
* 自动标签
* 热度评分
* 去重
* 多版本追踪

---

## SEO 战略

## 内容型关键词

* ROCm 安装教程
* 7900XTX 跑大模型
* HIP vs CUDA
* MI300X 部署 DeepSeek

## 技术 SEO

* sitemap.xml
* schema.org
* 自动内链
* Tag landing pages

---

## 运营系统

* 每日快报
* 周报
* 邮件订阅
* Telegram / X 分发

---

## 商业化路线

## 阶段1

* 广告
* 联盟链接
* GPU 主机推荐

## 阶段2

* 会员知识库
* 实测数据库

## 阶段3

* 企业咨询
* 私有部署方案

---

## 开发周期

## Phase 1（day 1）

基础设施重构

## Phase 2（day 2-3）

Crawler 升级

## Phase 3（day 4-5）

AI 内容加工

## Phase 4（day 6-7）

前端站点升级

## Phase 5（day 8）

增长系统上线

---

## 最终定位

AI 时代 AMD GPU 基础设施入口站
