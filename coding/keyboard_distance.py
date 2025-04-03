def get_distance(pos1: tuple[int, int], pos2: tuple[int, int]) -> int:
    """Calculate Manhattan distance between two positions"""
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])


def dp(finger1_pos: tuple[int, int], finger2_pos: tuple[int, int], idx: int, word: str, memo: dict, keyboard: dict) -> int:
    n = len(word)
    if idx == n:  # Typed all characters
        return 0
    
    # Check memo for state
    state = (finger1_pos, finger2_pos, idx)
    if state in memo:
        return memo[state]
    
    curr_letter = word[idx]
    curr_pos = keyboard[curr_letter]
    
    # Try moving finger1 to current letter
    cost1 = get_distance(finger1_pos, curr_pos) if finger1_pos != (-1, -1) else 0
    move_finger1 = cost1 + dp(curr_pos, finger2_pos, idx + 1, word, memo, keyboard)
    
    # Try moving finger2 to current letter
    cost2 = get_distance(finger2_pos, curr_pos) if finger2_pos != (-1, -1) else 0
    move_finger2 = cost2 + dp(finger1_pos, curr_pos, idx + 1, word, memo, keyboard)
    
    memo[state] = min(move_finger1, move_finger2)
    return memo[state]


def minDistance(word: str) -> int:
    """
    memo is a dictionary that stores the minimum distance to type a word with fingers at a given position
    """
    memo = {}
    # Create keyboard layout mapping each letter to its coordinates
    keyboard = {}
    for i in range(5):  # rows
        for j in range(6):  # columns
            if i * 6 + j < 26:  # Only map valid letters A-Z
                letter = chr(ord('A') + i * 6 + j)
                keyboard[letter] = (i, j)

    # Start with both fingers at (-1, -1) to indicate they haven't been placed yet
    return dp((-1, -1), (-1, -1), 0, word, memo, keyboard)

# Test cases
test_cases = [
    "CAKE", 
    "HAPPY"]
for word in test_cases:
    result = minDistance(word)
    print(f"Minimum distance for {word}: {result}") 