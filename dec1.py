"""
Find the largest sum of integers in a file in sets that are separated by
an empty line
"""

# Open the file and process lines
#   If the line contains a number, add it to a current total
#   If the line contains nothing, enter the number in a list of sums
#   If the line is the final line, enter the number in a list of sums

def get_sum_list(path: str) -> list[int]:
    sums: list[int] = []
    with open(path, 'r') as f:
        current_sum: int = 0
        
        for line in f.readlines():
            
            #Strip the \n
            if line[:-1].isdigit():
                
                current_sum += int(line)

            elif line.isspace():
                sums.append(current_sum)
                current_sum = 0
            
            else:
                pass
        
        #Add final sum to list
        sums.append(current_sum)
    return sums


def get_idx_of_elf(nums: list[int]) -> int:
    return nums.index(max(nums)) + 1

def get_top_n_sum(nums: list[int], n: int) -> int:
    top_n = []
    for i in range(n):
        max_num = max(nums)
        top_n.append(max_num)
        nums.pop(nums.index(max_num))
    return sum(top_n)

def main():
    print(get_top_n_sum(get_sum_list('dec1/input.txt'), 3))

if __name__ == "__main__":
    main()
