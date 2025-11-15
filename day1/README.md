# Advent of Code 2024 - Day 1: Historian Hysteria

## Problem Summary

The Historians need to reconcile two lists of location IDs. To find the total distance between the lists:

1. Sort both the left and right lists
2. Pair up corresponding elements (smallest with smallest, etc.)
3. Calculate the absolute difference for each pair
4. Sum all the differences

### Example

Given:
```
3   4
4   3
2   5
1   3
3   9
3   3
```

After sorting:
- Left list: `[1, 2, 3, 3, 3, 4]`
- Right list: `[3, 3, 4, 5, 9, 3]` → sorted: `[3, 3, 3, 4, 5, 9]`

Pairs and distances:
- 1 and 3: distance = 2
- 2 and 3: distance = 1
- 3 and 3: distance = 0
- 3 and 4: distance = 1
- 3 and 5: distance = 2
- 4 and 9: distance = 5

**Total distance: 11**

## Usage

1. Add your puzzle input to `input.txt`
2. Run the solution:
   ```bash
   python3 solution.py
   ```

## Testing with Example

To test with the example data:
```bash
python3 test_example.py
```

## Files

- `solution.py` - Main solution code
- `input.txt` - Your puzzle input (needs to be filled in)
- `example.txt` - Example input from problem description
- `test_example.py` - Test script using example data
- `README.md` - This file
