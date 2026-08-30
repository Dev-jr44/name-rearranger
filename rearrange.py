#!/usr/bin/env python3
"""
Rearrange first and last name.
Usage: python rearrange.py <first_name> <last_name>
Example: python rearrange.py John Doe  ->  "Doe, John"
"""

import sys

def rearrange(first, last):
    # Simple swap – change this to "last first" or any other format
    return f"{last}, {first}"

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python rearrange.py <first_name> <last_name>")
        sys.exit(1)
    first = sys.argv[1]
    last = sys.argv[2]
    print(rearrange(first, last))
