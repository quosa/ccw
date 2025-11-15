#!/usr/bin/env python3
"""
Advent of Code 2024 - Day 1: Historian Hysteria
"""

from collections import Counter


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


def calculate_similarity_score(left_list, right_list):
    """
    Calculate the similarity score between two lists.

    For each number in the left list, multiply it by the number of times
    it appears in the right list, then sum all these products.
    """
    # Count occurrences of each number in the right list
    right_counts = Counter(right_list)

    # Calculate similarity score
    similarity_score = 0
    for num in left_list:
        count = right_counts.get(num, 0)
        similarity_score += num * count

    return similarity_score


def main():
    # Parse input
    left_list, right_list = parse_input('input.txt')

    # Part 1: Calculate total distance
    total_distance = calculate_total_distance(left_list, right_list)
    print(f"Part 1 - Total distance: {total_distance}")

    # Part 2: Calculate similarity score
    similarity_score = calculate_similarity_score(left_list, right_list)
    print(f"Part 2 - Similarity score: {similarity_score}")


if __name__ == "__main__":
    main()
