def solution(survey, choices):
    """
    [Kakao Tech Internship] Personality Assessment (성격 유형 검사하기)
    Link: https://school.programmers.co.kr/learn/courses/30/lessons/118666

    Calculates the personality type based on survey results.

    Args:
        survey (list): A list of strings indicating the survey category (e.g., ["RT", "CF"]).
        choices (list): A list of integers (1-7) representing the user's choice for each query.

    Returns:
        str: A string representing the final 4-letter personality type.
    """

    # Define the 8 personality types in order
    typology = ["R", "T", "C", "F", "J", "M", "A", "N"]

    # Initialize score dictionary for each type
    score = {typ: 0 for typ in typology}
    answer = []

    # Adjust choices from 1~7 scale to -3~3 scale
    # 1~3: Disagree (Negative), 4: Neutral (0), 5~7: Agree (Positive)
    for i in range(len(choices)):
        choices[i] -= 4

    # Calculate scores based on survey responses
    for idx, typ in enumerate(survey):
        # Determine the target character based on the choice sign
        # If choice > 0 (Agree), select the second character (index 1)
        # If choice <= 0 (Disagree), select the first character (index 0)
        # typ[index], index = int(choices[idx] > 0)
        target_char = typ[int(choices[idx] > 0)]

        # Add the absolute value of the adjusted choice to the score
        score[target_char] += abs(choices[idx])

    # Determine the winner for each of the 4 indicators
    # Iterate through pairs: (R, T), (C, F), (J, M), (A, N)
    for i in range(0, 8, 2):
        # Select the type with the higher score
        # In case of a tie, max() selects the first element (lexicographically preceding)
        # because the 'typology' list is already sorted by priority for ties
        winner = max([typology[i], typology[i + 1]], key=lambda k: score[k])
        answer.append(winner)

    return ''.join(answer)