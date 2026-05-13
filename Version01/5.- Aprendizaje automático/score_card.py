#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Score Card Calculation for credit applications.
Calculates a final discrete score based on predefined binings for various applicant features.
"""
import argparse
from bisect import bisect_right
from typing import Optional

def get_bin_score(score_hash: dict[int, int], value: int) -> int:
    """
    Retrieve the score for a specific value based on right-bisected binning.

    Args:
        score_hash: A dictionary defining the bin lower-bounds as keys and scores as values.
        value: The value to be binned.

    Returns:
        The integer score corresponding to the bin the value falls into.
    """
    sorted_keys = sorted(list(score_hash.keys()))
    # bisect_right returns an insertion point which comes after any existing entries.
    # Subtracting 1 gives the index of the largest key less than or equal to 'value'.
    idx = bisect_right(sorted_keys, value) - 1
    
    # Handle cases where value is smaller than the smallest bin (fallback to 0 index)
    if idx < 0:
        idx = 0
        
    selected_key = sorted_keys[idx]
    return score_hash[selected_key]

def score_card(tca: int, amount: int, pet: int, age: int) -> int:
    """
    Calculate the total score card value.

    Args:
        tca: Time credit account value.
        amount: Credit amount.
        pet: Present employment time.
        age: Age of the applicant.

    Returns:
        The total computed score as an integer.
    """
    # Predefined score tables
    tca_hash: dict[int, int] = {0: 7, 20: 3, 40: 0, 60: 0, 80: 0}
    amount_hash: dict[int, int] = {1: 7, 5000: 1, 10000: 0, 15000: 0, 20000: 0}
    pet_hash: dict[int, int] = {1: 1, 2: 1, 3: 6, 4: 8, 5: 8}
    age_hash: dict[int, int] = {18: 3, 34: 5, 50: 3, 66: 3, 83: 0}

    tca_score = get_bin_score(tca_hash, tca)
    amount_score = get_bin_score(amount_hash, amount)
    pet_score = get_bin_score(pet_hash, pet)
    age_score = get_bin_score(age_hash, age)

    return tca_score + amount_score + pet_score + age_score

def main() -> Optional[int]:
    """
    CLI entry point to parse arguments and calculate the score card.
    """
    parser = argparse.ArgumentParser(description="Calculate credit score card value.")
    parser.add_argument("-t", "--tca", dest="tca", type=int, required=True,
                        help="time credit account")
    parser.add_argument("-a", "--amount", dest="amount", type=int, required=True,
                        help="amount")
    parser.add_argument("-p", "--pet", dest="pet", type=int, required=True,
                        help="present employment time")
    parser.add_argument("-g", "--age", dest="age", type=int, required=True,
                        help="age")
    
    args = parser.parse_args()
    
    result = score_card(tca=args.tca, amount=args.amount, pet=args.pet, age=args.age)
    return result

if __name__ == "__main__":
    score_result = main()
    print(score_result)
