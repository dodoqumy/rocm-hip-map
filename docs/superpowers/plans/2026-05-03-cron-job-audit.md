# Cron Job Audit & Manual Execution Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Audit all scheduled cron workflows by manually running the underlying programs in dependency order, verifying outputs against expectations, deferring credential-blocked eBay live validation, and performing translation verification last.

**Architecture:** First execute the `sync.yml` dependency chain to refresh source data, then run independent non-translation tasks (`papers`, `sync-prices` dry-run/TODO), then execute local translation with whatever translation model is currently configured in the local environment, and finally run `verify.py` plus translation quality inspection at the very end. eBay live fetch/normalize is explicitly parked as a TODO until `EBAY_APP_ID` and `EBAY_CERT_ID` are ready.

**Tech Stack:** Python 3.11, requests, PyYAML, BeautifulSoup4, markdownify, PyMuPDF, local shell environment variables for translation provider/model/base URL/API key.

---

## Scope Adjustments From User Input

1. `EBAY_APP_ID` and `EBAY_CERT_ID` are not ready yet. Any step that requires live eBay access is **deferred** and must be recorded as TODO instead of being treated as executable now.
2. `TRANSLATE_API_KEY` is configured for GitHub Actions, but local execution should use the **currently available local translation configuration** instead of assuming GitHub secrets are present.
3. **Translation verification must run last** after all other executable audit tasks complete.

---

## Dependency Map & Final Execution Order

```text
Phase 1: sync.yml chain (must run first)
  1. fetch-official.py
  2. sync-github.py
  3. classify.py
  4. release-watch.py

Phase 2: independent non-translation tasks
  5. fetch-papers.py
  6. extract-pdf.py --limit 3
  7. sync-prices dry-run only + TODO record

Phase 3: translation and final verification (must run last)
  8. translate.py --incremental --max-files 5   # local env model
  9. verify.py --stamp
 10. translation quality inspection + final audit summary
```

---

## classify.py vs classify_v2.py

| Aspect | classify.py | classify_v2.py |
|--------|-------------|----------------|
| Rules | ~30 patterns | ~300 patterns |
| Output | `data/articles.json` | `data/articles_classified.json` |
| Used by workflow | **Yes** (`sync.yml`) | **No** |
| Features | Basic OS/GPU/arch/driver/framework tagging | Adds library detection, quality score, content type, confidence, `is_indexed` |
| Status | Production | Prototype / not integrated |

**Verdict:** keep `classify.py` for the current cron audit. `classify_v2.py` is not needed for scheduled workflows unless the richer schema is intentionally adopted later.

---

### Task 1: Prepare Local Python Environment

**Files:**
- Create locally: `.venv/`

- [ ] **Step 1: Create virtual environment**

```bash
python3 -m venv .venv
```

Expected: `.venv/` is created.

- [ ] **Step 2: Install required dependencies**

```bash
. .venv/bin/activate && pip install --upgrade pip requests beautifulsoup4 markdownify pyyaml PyMuPDF
```

Expected: dependencies install without error.

- [ ] **Step 3: Verify imports**

```bash
. .venv/bin/activate && python3 -c "import requests, bs4, markdownify, yaml, fitz, json, re, sys, pathlib; print('All imports OK')"
```

Expected: `All imports OK`

---

### Task 2: Execute sync.yml Program Chain

**Files:**
- Run: `scripts/fetch-official.py`
- Run: `scripts/sync-github.py`
- Run: `scripts/classify.py`
- Run: `scripts/release-watch.py`
- Output: `content/raw/english/*.md`, `data/articles.json`, `data/fetch-state.json`, `data/known-issues.json`, `data/versions.json`

- [ ] **Step 1: Dry-run official fetch**

```bash
. .venv/bin/activate && python3 scripts/fetch-official.py --dry-run
```

Expected: previews sources/files without writing.

- [ ] **Step 2: Run official fetch**

```bash
. .venv/bin/activate && python3 scripts/fetch-official.py
```

Expected: raw article files are refreshed and `data/fetch-state.json` is updated.

- [ ] **Step 3: Verify fetch outputs**

```bash
. .venv/bin/activate && python3 -c "import json, pathlib; root = pathlib.Path('.'); files = list(root.glob('content/raw/english/*.md')); print('English articles:', len(files)); aj = root/'data'/'articles.json'; fs = root/'data'/'fetch-state.json'; print('articles.json exists:', aj.exists()); print('fetch-state.json exists:', fs.exists()); print('fetch-state.json size:', fs.stat().st_size if fs.exists() else 0)"
```

Expected: article count is non-zero, `articles.json` exists, `fetch-state.json` exists.

- [ ] **Step 4: Dry-run GitHub sync**

```bash
. .venv/bin/activate && python3 scripts/sync-github.py --dry-run
```

Expected: previews watched repos and sync scope.

- [ ] **Step 5: Run GitHub sync**

```bash
. .venv/bin/activate && python3 scripts/sync-github.py
```

Expected: `data/known-issues.json` and `content/raw/english/github_*.md` are refreshed.

- [ ] **Step 6: Verify GitHub outputs**

```bash
. .venv/bin/activate && python3 -c "import json, pathlib; root = pathlib.Path('.'); files = sorted(root.glob('content/raw/english/github_*.md')); print('GitHub markdown files:', len(files)); print('First file:', files[0].name if files else 'NONE'); ji = root/'data'/'known-issues.json'; print('known-issues.json exists:', ji.exists()); print('known-issues.json size:', ji.stat().st_size if ji.exists() else 0)"
```

Expected: GitHub markdown files exist and `known-issues.json` exists.

- [ ] **Step 7: Dry-run classification**

```bash
. .venv/bin/activate && python3 scripts/classify.py --dry-run
```

Expected: classification summary prints without writing.

- [ ] **Step 8: Run classification**

```bash
. .venv/bin/activate && python3 scripts/classify.py
```

Expected: `data/articles.json` is rewritten with `stats` and `articles` keys.

- [ ] **Step 9: Verify classification output**

```bash
. .venv/bin/activate && python3 -c "import json; data = json.load(open('data/articles.json')); stats = data.get('stats', {}); articles = data.get('articles', []); print('Scanned:', stats.get('total')); print('Classified:', stats.get('classified')); print('Articles stored:', len(articles)); print('Sample keys:', sorted(list(articles[0].keys()))[:12] if articles else [])"
```

Expected: `stats.classified` is non-zero and sample article keys include classification fields.

- [ ] **Step 10: Run release watch**

```bash
. .venv/bin/activate && python3 scripts/release-watch.py
```

Expected: `data/versions.json` is refreshed.

- [ ] **Step 11: Verify release output**

```bash
. .venv/bin/activate && python3 -c "import json; data = json.load(open('data/versions.json')); versions = data if isinstance(data, list) else data.get('versions', []); print('Tracked products:', len(versions)); print('Sample:', [(v.get('product'), v.get('version')) for v in versions[:5]])"
```

Expected: tracked product count is non-zero.

---

### Task 3: Execute papers.yml Program Chain

**Files:**
- Run: `scripts/fetch-papers.py`
- Run: `scripts/extract-pdf.py --limit 3`
- Output: `data/papers.json`, `content/raw/papers/*.md`, `website/static/data/papers.json`

- [ ] **Step 1: Dry-run paper fetch**

```bash
. .venv/bin/activate && python3 scripts/fetch-papers.py --dry-run
```

Expected: previews papers without writing.

- [ ] **Step 2: Run paper fetch**

```bash
. .venv/bin/activate && python3 scripts/fetch-papers.py
```

Expected: `data/papers.json` is written/updated.

- [ ] **Step 3: Run limited PDF extraction**

```bash
. .venv/bin/activate && python3 scripts/extract-pdf.py --limit 3
```

Expected: up to 3 new paper markdown files are extracted.

- [ ] **Step 4: Copy papers data to website**

```bash
mkdir -p website/static/data && cp data/papers.json website/static/data/papers.json
```

Expected: `website/static/data/papers.json` exists.

- [ ] **Step 5: Verify paper outputs**

```bash
. .venv/bin/activate && python3 -c "import json, pathlib; data = json.load(open('data/papers.json')); papers = data.get('papers', []); extracted = list(pathlib.Path('content/raw/papers').glob('*.md')); print('Total papers:', len(papers)); print('Top-level keys:', list(data.keys())[:5]); print('Extracted markdown files:', len(extracted)); print('Sample paper keys:', sorted(list(papers[0].keys()))[:12] if papers else [])"
```

Expected: `papers.json` contains papers and extracted markdown count is non-negative.

---

### Task 4: Record sync-prices.yml As Deferred TODO

**Files:**
- Run: `scripts/fetch-prices-ebay.py --dry-run`
- Create: `docs/cron-jobs-audit-2026-05-03.md`

- [ ] **Step 1: Confirm script is structurally runnable without credentials**

```bash
. .venv/bin/activate && python3 scripts/fetch-prices-ebay.py --dry-run
```

Expected: dry-run completes without requiring live eBay credentials.

- [ ] **Step 2: Record deferred live validation note**

Create or append the following section in `docs/cron-jobs-audit-2026-05-03.md`:

```markdown
## Deferred TODO: sync-prices.yml live validation

Reason: `EBAY_APP_ID` and `EBAY_CERT_ID` are not ready yet.

Deferred steps:
1. Run `python3 scripts/fetch-prices-ebay.py --site EBAY-US`
2. Run `python3 scripts/fetch-prices-ebay.py --site EBAY-DE`
3. Run `python3 scripts/fetch-prices-ebay.py --site EBAY-UK`
4. Run `python3 scripts/normalize-prices.py`
5. Generate `data/prices/prices-latest.json`
6. Verify normalized multi-region output

Current audit status: script entrypoint verified by dry-run only; live API path intentionally postponed.
```

- [ ] **Step 3: Expected outcome**

Expected: the audit explicitly records that live `sync-prices.yml` execution is pending credentials and is not falsely marked as executed.

---

### Task 5: Inspect Local Translation Runtime Before Running It

**Files:**
- Run: `scripts/translate.py`
- Output later: `content/translated/zh/*_zh.md`

- [ ] **Step 1: Print current local translation configuration**

```bash
. .venv/bin/activate && python3 -c "import os; print({k: os.environ.get(k) for k in ['TRANSLATE_PROVIDER','TRANSLATE_MODEL','TRANSLATE_BASE_URL','TRANSLATE_API_KEY']})"
```

Expected: current local translation environment is visible. If `TRANSLATE_API_KEY` is absent, execution stops here and the audit records a local-blocked state instead of guessing.

- [ ] **Step 2: Dry-run translation candidate selection**

```bash
. .venv/bin/activate && python3 scripts/translate.py --incremental --max-files 5 --dry-run
```

Expected: shows which files would be translated using current local configuration.

---

### Task 6: Run Local Translation For 5 Articles

**Files:**
- Run: `scripts/translate.py --incremental --max-files 5`
- Output: `content/translated/zh/*_zh.md`

- [ ] **Step 1: Capture translation count before execution**

```bash
. .venv/bin/activate && python3 -c "import pathlib; print(len(list(pathlib.Path('content/translated/zh').glob('*_zh.md'))))"
```

Expected: prints baseline translated file count.

- [ ] **Step 2: Run translation with current local model configuration**

```bash
. .venv/bin/activate && python3 scripts/translate.py --incremental --max-files 5
```

Expected: up to 5 files are translated using whichever local provider/model is currently configured.

- [ ] **Step 3: Capture translation count after execution**

```bash
. .venv/bin/activate && python3 -c "import pathlib; files = sorted(pathlib.Path('content/translated/zh').glob('*_zh.md')); print('Total translated files:', len(files)); print('Newest five:', [f.name for f in files[-5:]])"
```

Expected: translated file count increases or resume/skip behavior is explicitly visible.

---

### Task 7: Run verify.py At The Very End

**Files:**
- Run: `scripts/verify.py --stamp`
- Output: `data/verification/*.json`, `data/verification/summary.json`

- [ ] **Step 1: Dry-run verification**

```bash
. .venv/bin/activate && python3 scripts/verify.py --dry-run
```

Expected: previews verification targets.

- [ ] **Step 2: Run final verification**

```bash
. .venv/bin/activate && python3 scripts/verify.py --stamp
```

Expected: writes per-article verification reports and summary output.

- [ ] **Step 3: Verify verification artifacts**

```bash
. .venv/bin/activate && python3 -c "import json, pathlib; ver_dir = pathlib.Path('data/verification'); reports = sorted(ver_dir.glob('*.json')); summary = ver_dir/'summary.json'; print('Verification reports:', len(reports)); print('Summary exists:', summary.exists()); print('First reports:', [f.name for f in reports[:5]]); print('Summary keys:', list(json.load(open(summary)).keys())[:10] if summary.exists() else [])"
```

Expected: verification report count is non-zero if verification succeeds, and `summary.json` exists.

---

### Task 8: Perform Translation Quality Inspection Last

**Files:**
- Inspect: `content/translated/zh/*_zh.md`

- [ ] **Step 1: Inspect the newest five translation files**

```bash
. .venv/bin/activate && python3 -c "import pathlib, re; files = sorted(pathlib.Path('content/translated/zh').glob('*_zh.md'))[-5:]; print('Files inspected:', [f.name for f in files]); print();
for f in files:
    content = f.read_text(encoding='utf-8');
    chinese_chars = len(re.findall(r'[\u4e00-\u9fff]', content));
    print(f.name);
    print('  size_bytes =', f.stat().st_size);
    print('  chinese_chars =', chinese_chars);
    print('  preview =', repr(content[:200]));
    print()"
```

Expected: each inspected file is larger than 200 bytes and contains substantial Chinese text.

- [ ] **Step 2: Run translation validity check against the newest five files**

```bash
. .venv/bin/activate && python3 -c "from pathlib import Path; import importlib.util; spec = importlib.util.spec_from_file_location('translate_mod', 'scripts/translate.py'); mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod); files = sorted(Path('content/translated/zh').glob('*_zh.md'))[-5:]; print([(f.name, mod.is_valid_translation(f)) for f in files])"
```

Expected: newest five files report `True` unless a resume/incomplete marker is present.

---

### Task 9: Write Final Audit Summary And Recommendations

**Files:**
- Create: `docs/cron-jobs-audit-2026-05-03.md`

- [ ] **Step 1: Generate a factual summary snapshot**

```bash
. .venv/bin/activate && python3 -c "import json, pathlib; root = pathlib.Path('.'); summary = {
'sync_raw_english_count': len(list(root.glob('content/raw/english/*.md'))),
'github_raw_count': len(list(root.glob('content/raw/english/github_*.md'))),
'translated_count': len(list(root.glob('content/translated/zh/*_zh.md'))),
'verification_report_count': len(list(root.glob('data/verification/*.json'))),
'papers_markdown_count': len(list(root.glob('content/raw/papers/*.md'))),
'prices_json_count': len(list(root.glob('data/prices/prices-*.json'))),
'has_articles_json': (root/'data'/'articles.json').exists(),
'has_versions_json': (root/'data'/'versions.json').exists(),
'has_known_issues_json': (root/'data'/'known-issues.json').exists(),
'has_papers_json': (root/'data'/'papers.json').exists()
}; print(json.dumps(summary, indent=2, ensure_ascii=False))"
```

Expected: a machine-checkable audit snapshot prints successfully.

- [ ] **Step 2: Write summary document**

Write `docs/cron-jobs-audit-2026-05-03.md` with these sections:

```markdown
# Cron Jobs Audit Report — 2026-05-03

## Executed Successfully
- sync.yml chain: fetch-official.py, sync-github.py, classify.py, release-watch.py
- papers.yml chain: fetch-papers.py, extract-pdf.py --limit 3
- translate.yml local equivalent: translate.py --incremental --max-files 5
- verify.yml equivalent: verify.py --stamp

## Deferred / Blocked
- sync-prices.yml live execution deferred because `EBAY_APP_ID` and `EBAY_CERT_ID` are not ready

## Output Snapshot
- raw English article count
- GitHub raw article count
- translated file count
- verification report count
- paper markdown count
- price json count

## classify.py vs classify_v2.py
- `classify.py` is production and currently required
- `classify_v2.py` is not wired into workflows and can remain parked until intentionally adopted

## Recommendations
- Keep `classify.py` as the current workflow classifier
- Do not claim `sync-prices.yml` validated until live credentials are available
- Keep translation verification at the end of the audit order
- If local translation env differs from CI, document the local provider/model used in this run
```

- [ ] **Step 3: Expected outcome**

Expected: the final audit report clearly separates executed work from deferred credential-gated work.

---

## Self-Review Checklist For This Plan

1. **Spec coverage:** includes plan fixes, deferred eBay TODO, local translation model usage, and translation verification last.
2. **Placeholder scan:** removed `KNOWN`, missing imports, and broken nested shell quoting; no `TODO/TBD` placeholders remain inside executable steps.
3. **Type consistency:** all commands reference real files and real CLI flags already confirmed in the repository.

---

## Execution Handoff

**Plan complete and saved to `docs/superpowers/plans/2026-05-03-cron-job-audit.md`. Two execution options:**

**1. Subagent-Driven (recommended)** - I dispatch a fresh subagent per task, review between tasks, fast iteration

**2. Inline Execution** - Execute tasks in this session using executing-plans, batch execution with checkpoints

**Which approach?**
