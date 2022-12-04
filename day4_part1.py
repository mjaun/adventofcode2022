from __future__ import annotations

import sys

from typing import List, Tuple


def main():
    result = 0

    for first_range, second_range in read_input_pairs():
        first_elf = Elf(first_range)
        second_elf = Elf(second_range)

        if Elf.fully_contains_sections(first_elf, second_elf):
            result += 1

    print(result)


class Elf:
    def __init__(self, section_range: str):
        section_range_ids = [int(id) for id in section_range.split('-')]
        assert len(section_range_ids) == 2
        assert section_range_ids[0] <= section_range_ids[1]

        self.section_ids: List[int] = list(range(section_range_ids[0], section_range_ids[1] + 1))

    @staticmethod
    def fully_contains_sections(first: Elf, second: Elf):
        common_sections = set(first.section_ids) & set(second.section_ids)
        return len(common_sections) in [len(first.section_ids), len(second.section_ids)]


def read_input_pairs() -> List[Tuple[str, str]]:
    pairs: List[Tuple[str, str]] = []

    for line in sys.stdin.readlines():
        line = line.strip()
        pair = line.split(',')
        assert len(pair) == 2
        pairs.append((pair[0], pair[1]))

    return pairs


if __name__ == '__main__':
    main()
