from src.ocr.compare import levenshtein, cer, wer

def test_levenshtein_simple():
    assert levenshtein("", "") == 0
    assert levenshtein("a", "") == 1
    assert levenshtein("", "abc") == 3
    assert levenshtein("kitten", "sitting") == 3

def test_cer():
    assert cer("hello", "hello") == 0.0
    assert cer("", "a") == 1.0

def test_wer_basic():
    assert wer("this is a test", "this is a test") == 0.0
    assert wer("", "one two") == 1.0
