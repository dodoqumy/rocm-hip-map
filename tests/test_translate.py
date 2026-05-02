from __future__ import annotations

from pathlib import Path

from scripts import translate


def test_load_glossary_builds_mapping(tmp_path, monkeypatch):
    glossary = tmp_path / 'glossary.yaml'
    glossary.write_text(
        'terms:\n'
        '  - en: ROCm\n'
        '    zh: ROCm 平台\n'
        '    keep_original: true\n'
        '  - en: driver\n'
        '    zh: 驱动\n',
        encoding='utf-8',
    )
    monkeypatch.setattr(translate, 'GLOSSARY_PATH', glossary)

    loaded = translate.load_glossary()

    assert len(loaded['terms']) == 2
    assert loaded['mapping']['ROCm']['zh'] == 'ROCm 平台'
    assert loaded['mapping']['driver']['zh'] == '驱动'


def test_translate_uses_opencode_env_configuration(monkeypatch):
    calls = {}

    def fake_translate_deepseek(text, api_key, model, base_url, mode):
        calls.update({
            'text': text,
            'api_key': api_key,
            'model': model,
            'base_url': base_url,
            'mode': mode,
        })
        return '已翻译'

    monkeypatch.setenv('TRANSLATE_PROVIDER', 'opencode')
    monkeypatch.setenv('TRANSLATE_API_KEY', 'test-key')
    monkeypatch.setenv('TRANSLATE_MODEL', 'deepseek-v4-pro')
    monkeypatch.setenv('TRANSLATE_BASE_URL', 'https://opencode.ai/zen/go/v1')
    monkeypatch.setattr(translate, 'translate_deepseek', fake_translate_deepseek)

    result = translate.translate('ROCm driver guide', {'mapping': {}, 'terms': []}, mode='paper')

    assert result == '已翻译'
    assert calls == {
        'text': 'ROCm driver guide',
        'api_key': 'test-key',
        'model': 'deepseek-v4-pro',
        'base_url': 'https://opencode.ai/zen/go/v1',
        'mode': 'paper',
    }


def test_is_valid_translation_rejects_incomplete_or_mostly_untranslated(tmp_path):
    invalid = tmp_path / 'bad_zh.md'
    invalid.write_text(
        '---\ntitle: bad\n---\n\n'
        f"{translate.TRANSLATION_INCOMPLETE_MARKER}\n\n"
        'This remains English and should fail validation because it is long enough to count as untranslated content.\n',
        encoding='utf-8',
    )

    valid = tmp_path / 'good_zh.md'
    valid.write_text(
        '---\ntitle: good\n---\n\n'
        '这是一个足够长的中文段落，用于通过翻译完整性校验，并确保文件大小和中文比例都满足要求。\n\n'
        '第二个中文段落也足够长，用于保证翻译率高于阈值。\n',
        encoding='utf-8',
    )

    assert translate.is_valid_translation(invalid) is False
    assert translate.is_valid_translation(valid) is True
