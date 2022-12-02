#!/usr/bin/env python3

def get_input():
    data = []

    with open("input.txt", "r", encoding="utf-8") as f:
        for line in f:
            data.append(tuple(line.strip().split(" ")))
    
    return data


def main():
    data = get_input()
    hashmap = {
        ('A', 'X'): 3,
        ('A', 'Y'): 4,
        ('A', 'Z'): 8,
        ('B', 'X'): 1,
        ('B', 'Y'): 5,
        ('B', 'Z'): 9,
        ('C', 'X'): 2,
        ('C', 'Y'): 6,
        ('C', 'Z'): 7
    }

    result = 0

    for arr in data:
        result += hashmap[arr]

    print(result)


if __name__ == "__main__":
    main()