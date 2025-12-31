def solution(n):
    """
    Problem: Ternary Flip
    Link: https://school.programmers.co.kr/learn/courses/30/lessons/68935
    """
    ternary = ""
    # Step 1: Convert Decimal to Base-3 (Naturally reversed via modulo)
    while n > 0:
        n, remainder = divmod(n, 3)
        ternary += str(remainder)

    # Step 2: Convert Base-3 String back to Decimal
    return int(ternary, 3)