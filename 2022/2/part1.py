#!/usr/bin/env python3
# A, X - rock
# B, Y - paper
# C, Z - scissors

def get_input():
    data = []

    with open("input.txt", "r", encoding="utf-8") as f:
        for line in f:
            data.append(tuple(line.strip().split(" ")))
    
    return data


def main():
    data = get_input()
    hashmap = {
        ('A', 'X'): 4,
        ('A', 'Y'): 8,
        ('A', 'Z'): 3,
        ('B', 'X'): 1,
        ('B', 'Y'): 5,
        ('B', 'Z'): 9,
        ('C', 'X'): 7,
        ('C', 'Y'): 2,
        ('C', 'Z'): 6
    }

    result = 0

    for arr in data:
        result += hashmap[arr]

    print(result)


if __name__ == "__main__":
    main()