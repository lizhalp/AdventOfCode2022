"""
Part 1:

Some of the pairs have noticed that one of their assignments 
fully contains the other. For example, 2-8 fully contains 3-7, 
and 6-6 is fully contained by 4-6. In pairs where one assignment 
fully contains the other, one Elf in the pair would be exclusively 
cleaning sections their partner will already be cleaning, so 
these seem like the most in need of reconsideration. In this 
example, there are 2 such pairs.

Part 2:
It seems like there is still quite a bit of duplicate work planned. 
Instead, the Elves would like to know the number of pairs that 
overlap at all.

In the above example, the first two pairs (2-4,6-8 and 2-3,4-5) 
don't overlap, while the remaining four pairs (5-7,7-9, 2-8,3-7, 
6-6,4-6, and 2-6,4-8) do overlap:

5-7,7-9 overlaps in a single section, 7.
2-8,3-7 overlaps all of the sections 3 through 7.
6-6,4-6 overlaps in a single section, 6.
2-6,4-8 overlaps in sections 4, 5, and 6.
So, in this example, the number of overlapping assignment pairs is 4.
"""
from dataclasses import dataclass
from time import perf_counter

def print_time(f):
    def wrapper(*args):
        start = perf_counter()
        res = f(*args)
        end = perf_counter()
        print(f"{str(f)} took: {end - start}")
        return res
    return wrapper


@dataclass
class ElfRange:
    start: int
    end: int

    def is_inside(self, other) -> bool:        
        if (self.start <= other.start <= other.end <= self.end):
            return True
        elif (other.start <= self.start <= self.end <= other.end):
            return True
        else:
            return False
    
    def is_partially_inside(self, other) -> bool:
        if (self.end >= other.start) and (other.end >= self.start):
            return True
        else:
            return False

def get_range_list(path: str) -> list[tuple[ElfRange, ElfRange]]:
    ranges: list[tuple[ElfRange, ElfRange]] = []
    with open(path, 'r') as f:
        for line in f.readlines():
            pairs: list[str] = line.split(',')
            endpoints1: list[str] = pairs[0].split('-')
            endpoints2: list[str] = pairs[1].split('-')
            ranges.append((
                ElfRange(int(endpoints1[0]), int(endpoints1[1])),
                ElfRange(int(endpoints2[0]), int(endpoints2[1]))
            ))
    return ranges 


def get_all_overlap_pairs(ranges: list[tuple[ElfRange, ElfRange]]):
    overlap = [p1.is_partially_inside(p2) for p1, p2 in ranges]
    return list(filter(lambda x: x == True, overlap))
    
@print_time
def main():
    print(len(get_all_overlap_pairs(get_range_list("dec4/input.txt"))))

if __name__ == "__main__":
    main()


