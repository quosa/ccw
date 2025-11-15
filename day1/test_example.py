#!/usr/bin/env python3
"""
Test the solution with the example data from the problem description.
Part 1 expected result: 11
Part 2 expected result: 31
"""

from solution import parse_input, calculate_total_distance, calculate_similarity_score


def test_example():
    """Test with the example data."""
    # Parse example input
    left_list, right_list = parse_input('example.txt')

    print(f"Example data:")
    print(f"Left list:  {left_list}")
    print(f"Right list: {right_list}")
    print(f"\nSorted left:  {sorted(left_list)}")
    print(f"Sorted right: {sorted(right_list)}")

    # Test Part 1
    total_distance = calculate_total_distance(left_list, right_list)
    print(f"\n--- Part 1 ---")
    print(f"Total distance: {total_distance}")
    print(f"Expected: 11")
    part1_pass = total_distance == 11
    print(f"Test {'PASSED' if part1_pass else 'FAILED'}!")

    # Test Part 2
    similarity_score = calculate_similarity_score(left_list, right_list)
    print(f"\n--- Part 2 ---")
    print(f"Similarity score: {similarity_score}")
    print(f"Expected: 31")
    part2_pass = similarity_score == 31
    print(f"Test {'PASSED' if part2_pass else 'FAILED'}!")

    return part1_pass and part2_pass


if __name__ == "__main__":
    success = test_example()
    exit(0 if success else 1)
