import pytest
import collect_framework


class TestCountingUniqueCharacters:
    """test class for testing func: 'counting_unique_characters' """

    def test_counting_unique_characters(self):
        assert collect_framework.counting_unique_characters('abbbccdf') == 3
        assert collect_framework.counting_unique_characters('aabcdfee') == 4

    def test_counting_unique_characters_assertion(self):
        with pytest.raises(TypeError):
            collect_framework.counting_unique_characters(123)


class TestParseCLI:
    pass
