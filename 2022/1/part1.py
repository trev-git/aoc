#!/usr/bin/env python3

def get_input():
    data = []
    tmp = []
    with open("input.txt", "r", encoding="utf-8") as f:
        for line in f:
            if line == "\n":
                data.append(sum(tmp))
                tmp.clear()
            else:
                tmp.append(int(line.strip()))
    
    return data


def main():
    data = get_input()
    print(max(data))


if __name__ == "__main__":
    main()

