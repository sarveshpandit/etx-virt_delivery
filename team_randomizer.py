#!/usr/bin/python
import random

def randomize_range(start, end):
    if start > end:
        start, end = end, start

    available_numbers = list(range(start, end + 1))
    result = []

    while available_numbers:
        num = random.choice(available_numbers)
        result.append(num)
        available_numbers.remove(num)

    return result

# Entry point
if __name__ == "__main__":
    start = int(input("Enter start of team range (first team): "))
    end = int(input("Enter end of team range (last team): "))

    randomized = randomize_range(start, end)

    print("The team presentation order for today is:")
    for number in randomized:
        print(f"Team: {number}")