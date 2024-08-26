#!/usr/bin/env python3

import argparse
from collections import defaultdict

def analyze_passwords(file_path):
    length_count = defaultdict(int)
    total_passwords = 0
    invalid_spaces = 0

    with open(file_path, 'r') as file:
        passwords = [line.rstrip() for line in file]

    for pwd in passwords:
        total_passwords += 1
        if pwd.endswith(' '):
            invalid_spaces += 1
            pwd = pwd.rstrip()
        
        length_count[len(pwd)] += 1

    # Detect if the majority of passwords ended in spaces
    if invalid_spaces > 0.9 * total_passwords:
        print("Warning: Majority of passwords had trailing spaces. Consider cleaning the input file.")

    # Format and print the results
    print("\nPassword Length Analysis")
    print("=========================")
    max_length = max(length_count.keys()) if length_count else 0
    for length in sorted(length_count):
        count = length_count[length]
        label = "password" if count == 1 else "passwords"
        print(f"{length:>3}    |    {count:>5} {label}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analyze password lengths from a list of passwords.")
    parser.add_argument("-i", "--input", required=True, help="Input file containing one password per line.")
    args = parser.parse_args()

    analyze_passwords(args.input)
