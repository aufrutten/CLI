from collections import Counter
from functools import lru_cache


@lru_cache(maxsize=None)
def counting_unique_characters(text: str) -> int:
    if not isinstance(text, str):
        raise TypeError('you wrote wrong type argument')
    counter = Counter(text)
    return len([num for num in counter.values() if num == 1])


if __name__ == '__main__':
    print(counting_unique_characters('abbbccdf'))  # pragma: no cover
