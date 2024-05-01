import pytest
from main import get_word_count, char_count

def main():
    test_three()
    test_count()
    test_char_count()



def test_three():
    assert get_word_count("only three words") == ["only", "three", "words"]

def test_count():
    assert len(get_word_count("five words for us both")) == 5

def test_char_count():
    assert char_count("a")["a"] == 1
    assert char_count("Death, by exile.")["e"] == 3



if __name__ == "__main__":
    main()
