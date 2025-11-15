#!/usr/bin/env python3
"""
Advent of Code 2024 - Day 1: Historian Hysteria
"""

def parse_input(filename):
    """Parse the input file and return two lists of numbers."""
    left_list = []
    right_list = []

    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if line:
                left, right = line.split()
                left_list.append(int(left))
                right_list.append(int(right))

    return left_list, right_list


def calculate_total_distance(left_list, right_list):
    """
    Calculate the total distance between two lists.

    Pairs are formed by sorting both lists and pairing corresponding elements.
    Distance is the absolute difference between paired numbers.
    """
    # Sort both lists
    sorted_left = sorted(left_list)
    sorted_right = sorted(right_list)

    # Calculate distances
    total_distance = 0
    for left, right in zip(sorted_left, sorted_right):
        distance = abs(left - right)
        total_distance += distance

    return total_distance


def main():
    # Parse input
    left_list, right_list = parse_input('input.txt')

    # Part 1: Calculate total distance
    total_distance = calculate_total_distance(left_list, right_list)
    print(f"Part 1 - Total distance: {total_distance}")


if __name__ == "__main__":
    main()
