import os
from unittest.mock import Mock
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
    """test class  for testing func: 'parse_file' """
    def test_function_for_parse_file(self):
        """function tests 'parse_file', any case which have"""

        # creating file with someone text
        path_to_temp_file = 'tempText.txt'
        text_of_file_to_write = """Hello, my name is Ihor"""
        with open(path_to_temp_file, 'w') as temporary_file:
            temporary_file.write(text_of_file_to_write)
            temporary_file.close()

        # trying to access a existent file
        assert collect_framework.parse_file(path_to_temp_file) == text_of_file_to_write,\
            'input text and file text do not match'

        # trying to access a non-existent file
        with pytest.raises(FileNotFoundError):
            name_file_which_not_exist = 'non_existentText.txt'
            collect_framework.parse_file(name_file_which_not_exist)

        # deleting temp file after test
        os.remove(path_to_temp_file)
        assert not os.path.isfile(path_to_temp_file), "file hasn't deleted"

    def test_parse_cli_function(self):
        """test function of 'parse_cli_function' """
        # collect_framework.parse_cli_function()



