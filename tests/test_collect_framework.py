import pytest
import collect_framework


def test_counting_unique_characters():
    assert collect_framework.counting_unique_characters('abbbccdf') == 3
    assert collect_framework.counting_unique_characters('aabcdfee') == 4


def test_counting_unique_characters_assertion():
    with pytest.raises(TypeError):
        collect_framework.counting_unique_characters(123)

