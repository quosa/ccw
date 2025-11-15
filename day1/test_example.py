#!/usr/bin/env python3
"""
Test the solution with the example data from the problem description.
Expected result: 11
"""

from solution import parse_input, calculate_total_distance


def test_example():
    """Test with the example data."""
    # Parse example input
    left_list, right_list = parse_input('example.txt')

    # Calculate total distance
    total_distance = calculate_total_distance(left_list, right_list)

    print(f"Example data:")
    print(f"Left list:  {left_list}")
    print(f"Right list: {right_list}")
    print(f"\nSorted left:  {sorted(left_list)}")
    print(f"Sorted right: {sorted(right_list)}")
    print(f"\nTotal distance: {total_distance}")
    print(f"Expected: 11")
    print(f"Test {'PASSED' if total_distance == 11 else 'FAILED'}!")

    return total_distance == 11


if __name__ == "__main__":
    success = test_example()
    exit(0 if success else 1)
