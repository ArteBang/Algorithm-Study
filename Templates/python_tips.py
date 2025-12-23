"""
Python Algorithm Interview Cheatsheet
Author: ArteBang
"""

# ==========================================
# 1. Matrix & Grid Utilities
# ==========================================

def transpose(matrix):
    """
    Transpose a 2D matrix (swap rows and columns).
    Input: [[1, 2], [3, 4]] -> Output: [[1, 3], [2, 4]]
    Technique: Unpacking (*) and zip
    """
    return list(map(list, zip(*matrix)))

def rotate_grid_simulation(n):
    """
    Simulation of 2D grid movement using direction vectors.
    Useful for: Spiral Matrix, Robot Simulation, DFS/BFS on grid.
    """
    board = [[0] * n for _ in range(n)]

    # Direction vectors: Right, Down, Left, Up (Clockwise)
    # y: row index, x: column index
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]

    y, x, direction = 0, 0, 0

    # Example logic for moving forward
    # ny = y + dy[direction]
    # nx = x + dx[direction]

# ==========================================
# 2. Math & Logic Optimization
# ==========================================

def clamp(val, min_val, max_val):
    """
    Constrain a value within a specific range [min_val, max_val].
    Avoids messy if-else statements for boundary checks.
    """
    return max(min_val, min(max_val, val))

def is_odd(num):
    """
    Check if a number is odd using bitwise AND optimization.
    Performance: Slightly faster than '%' operator due to CPU architecture!
    """
    return num & 1

def compare(a, b):
    """
    Compare two values and return integer flag.
    Returns: 1 if a > b, -1 if a < b, 0 if a == b
    Useful for: Custom sorting comparators.
    """
    return (a > b) - (b > a)

def boolean_switch(flag):
    """
    Toggle between character 'A' and 'B' based on boolean flag.
    Input: True -> 'B', False -> 'A'
    """
    return 'AB'[flag]

# ==========================================
# 3. String Parsing & Handling
# ==========================================

def calculator_dispatch(op, a, b):
    """
    Execute operations without long if-elif chains using a Dictionary Dispatch.
    Clean and extensible design pattern.
    """
    ops = {
        '+': lambda: a + b,
        '-': lambda: a - b,
        '*': lambda: a * b
    }
    return ops[op]()

def get_substring_smart(text, pattern):
    """
    Slice string up to the *last* occurrence of a pattern.
    Useful for: File path parsing, URL handling.
    """
    if pattern not in text: return text
    return text[:text.rfind(pattern) + len(pattern)]

# ==========================================
# 4. Time & Date Calculation
# ==========================================

def to_minutes(time_str):
    """
    Convert 'HH:MM' string format to total minutes (integer).
    Why: Simplifies time difference calculations (avoids base-60 headaches).
    """
    h, m = map(int, time_str.split(':'))
    return h * 60 + m