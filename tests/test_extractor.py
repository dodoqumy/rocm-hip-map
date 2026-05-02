from __future__ import annotations

from crawlers.extractor import ContentExtractor, extract_title, is_doxygen_page, is_js_rendered


LONG_HTML = '''
<html>
  <head><title>ROCm Guide</title></head>
  <body>
    <main>
      <p>This is a sufficiently long paragraph about ROCm and HIP development that should survive extraction into readable markdown text for downstream processing.</p>
      <p>This second paragraph adds more GPU-related content so the fallback extractor has enough material to return a non-empty document body.</p>
    </main>
  </body>
</html>
'''


def test_content_extractor_extracts_main_body_text():
    extractor = ContentExtractor()

    result = extractor.extract(LONG_HTML, 'https://example.com/guide')

    assert result is not None
    assert 'ROCm and HIP development' in result


def test_extractor_helpers_detect_special_cases():
    doxygen_html = '<html><meta name="generator" content="Doxygen 1.9"><div class="memitem"></div></html>'
    js_html = '<html><body>Please enable JavaScript</body></html>'

    assert extract_title('<html><head><title>Sample Title</title></head></html>') == 'Sample Title'
    assert is_doxygen_page(doxygen_html) is True
    assert is_js_rendered(js_html) is True
