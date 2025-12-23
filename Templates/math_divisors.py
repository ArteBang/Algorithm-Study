"""
Math Algorithms: Divisor Analysis (Sieve Approach)
Author: ArteBang
Description: Optimized algorithms to calculate count/sum of divisors for ALL numbers up to N.
Complexity: Time O(N log N) | Space O(N)
Reference: Based on the concept of Harmonic Series.
"""

from typing import List


def get_divisor_counts(n: int) -> List[int]:
    """
    Generates a list containing the number of divisors for every number from 0 to n.

    Logic:
        Instead of finding factors for each number (O(N*sqrt(N))),
        we iterate through multiples of each number 'i' and increment their count.
        This is similar to the 'Sieve of Eratosthenes'.

    Args:
        n (int): The maximum number to analyze.

    Returns:
        List[int]: Index i holds the divisor count of number i.
                   (e.g., counts[6] = 4 because divisors are 1, 2, 3, 6)
    """
    # Initialize array with 0. Size is n + 1 to handle 1-based indexing easily.
    counts = [0] * (n + 1)

    # Iterate from 1 to n
    for i in range(1, n + 1):
        # Update all multiples of i
        # range(start, stop, step) -> Jump by i
        for j in range(i, n + 1, i):
            counts[j] += 1

    return counts


def get_divisor_sums(n: int) -> List[int]:
    """
    (Bonus) Generates a list containing the SUM of divisors for every number from 0 to n.

    Example:
        For 6: 1 + 2 + 3 + 6 = 12
        sums[6] will be 12.
    """
    sums = [0] * (n + 1)

    for i in range(1, n + 1):
        for j in range(i, n + 1, i):
            sums[j] += i  # Add the divisor 'i' to its multiple 'j'

    return sums


# ==========================================
# Example Usage
# ==========================================
if __name__ == "__main__":
    N = 10
    print(f"Divisor Counts up to {N}: {get_divisor_counts(N)}")
    # Expected: [0, 1, 2, 2, 3, 2, 4, 2, 4, 3, 4]

    print(f"Divisor Sums up to {N}:   {get_divisor_sums(N)}")
    # Expected: [0, 1, 3, 4, 7, 6, 12, 8, 15, 13, 18]