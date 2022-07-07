from typing import TypeVar


T = TypeVar("T", dict, set, list)


def nonones(iterable: T) -> T:
    if isinstance(iterable, dict):
        return {k: v for k, v in iterable.items() if v is not None}

    filtered = filter(lambda x: x, iterable)

    if isinstance(iterable, list):
        return list(filtered)

    if isinstance(iterable, set):
        return set(filtered)
