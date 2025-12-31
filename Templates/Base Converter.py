def to_ternary(n):
    if n == 0: return 0  # Except 0

    answer = 0
    multiplier = 1  # (10^0)

    while n > 0:
        remainder = n % 3
        answer += remainder * multiplier

        n = n // 3
        multiplier *= 10  # (1 -> 10 -> 100...)

    return answer


def ter_to_dec(n):
    answer = 0
    multiplier = 1  # (3^0)

    while n > 0:
        digit = n % 10
        answer += digit * multiplier

        n = n // 10
        multiplier *= 3  # (1 -> 3 -> 9...)

    return answer