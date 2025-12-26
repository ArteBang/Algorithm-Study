def solution(friends, gifts):
    """
    [Problem]: The Most Received Gift (2024 Kakao Winter Internship)
    [Link]: https://school.programmers.co.kr/learn/courses/30/lessons/258712

    [Approach]:
    1. Record gift exchanges between friends using a nested dictionary (Adjacency Matrix equivalent).
    2. Calculate the 'Gift Index' for each friend: (Gifts Given) - (Gifts Received).
    3. Predict next month's gifts based on two rules:
       - Rule A: If one gave more gifts to the other, the giver receives a gift.
       - Rule B: If exchanges are equal (or zero), the one with the higher Gift Index receives a gift.

    [Complexity]:
    - Time Complexity: O(N + F^2), where N is the number of gifts (parsing) and F is the number of friends (comparison).
    - Space Complexity: O(F^2) to store the gift exchange history.
    """

    # Stores the number of gifts each friend will receive next month
    next_month = {name: 0 for name in friends}

    # Records who gave gifts to whom: record[giver][receiver] = count
    gift_history = {giver: {receiver: 0 for receiver in friends} for giver in friends}

    # Gift Index: Gifts Given - Gifts Received
    gift_index = {name: 0 for name in friends}

    # 1. Parse the gift data
    for info in gifts:
        giver, receiver = info.split()
        gift_history[giver][receiver] += 1

        gift_index[giver] += 1
        gift_index[receiver] -= 1

    # 2. Compare every pair of friends to determine next month's gifts
    for me in friends:
        for you in friends:
            if me == you:
                continue

            # Count of gifts exchanged between 'me' and 'you'
            gifts_given = gift_history[me][you]
            gifts_received = gift_history[you][me]

            # Apply Rule A: Compare direct exchanges
            if gifts_given > gifts_received:
                next_month[me] += 1

            # Apply Rule B: If exchanges are equal, compare Gift Indices
            elif gifts_given == gifts_received:
                if gift_index[me] > gift_index[you]:
                    next_month[me] += 1

    return max(next_month.values()) if next_month else 0