from collections import Counter
from functools import lru_cache
import argparse
import os


class Parser:

    def __init__(self):
        """init function of parser, adding arguments"""
        self.parser_cli = argparse.ArgumentParser(description="Counter of unique characters")
        self.parser_cli.add_argument("--file",
                                     type=str,
                                     help="file for counting")  # add --file argument

        self.parser_cli.add_argument("--string",
                                     type=str,
                                     help="string for counting")  # add --sting argument

    def parse_cli_function(self):
        """
        function for parse our command line
        function have three priority of return, that is: 1) file 2) text 3) nothing
        function return text
        """
        cli_args = self.parser_cli.parse_args()  # getting all arguments in CLI
        if cli_args.file is not None:
            return self.parse_file(file=cli_args.file)

        elif cli_args.string is not None:
            return cli_args.string

    @staticmethod
    def parse_file(file):
        """function for parse files, checks if path exists and that is file"""
        if os.path.isfile(file):
            with open(file, 'r') as file:
                return file.read()
        else:
            raise FileNotFoundError("file doesn't exist or that is folder")


@lru_cache(maxsize=None)
def counting_unique_characters(text: str) -> int:
    """function for counting unique characters"""
    if not isinstance(text, str):  # if text not str, raise exception
        raise TypeError('you wrote wrong type argument')
    counter = Counter(text)
    return len([num for num in counter.values() if num == 1])


def main():  # pragma: no cover
    argument_of_cli = Parser().parse_cli_function()
    counter = counting_unique_characters(argument_of_cli)
    response = f'{argument_of_cli}: {counter}'
    print(response)


if __name__ == '__main__':
    main()  # pragma: no cover
