def set_all_quarter_values(quarter, value):
    """
    Sets all values in the given quarter of the matrix to the specified value.

    Parameters:
    quarter (list of lists): The quarter of the matrix to modify.
    value (int): The value to set in all cells of the quarter.

    Returns:
    tuple: The updated quarter of the matrix and the number of changes made.
    """
    changes_count = 0
    for row in range(len(quarter)):
        for col in range(len(quarter)):
            if quarter[row][col] != value:  # Only change if value is different
                changes_count += 1
                quarter[row][col] = value
    return quarter, changes_count


def make_fake_card(matrix, zero_quarter_index, one_quarter_index):
    """
    Disrupts the matrix recursively to minimize the difference in a quarter of the matrix.

    Parameters:
    matrix (list of lists): The original matrix to disrupt.
    zero_quarter_index (int): The index of the quarter to fill with zeros.
    one_quarter_index (int): The index of the quarter to fill with ones.

    Returns:
    tuple: The disrupted matrix and the total number of changes made.
    """
    if len(matrix) == 1:  # Base case: single element
        return matrix, 0

    half_matrix = len(matrix) // 2  # Divide into 4 quarters
    quarter1 = [row[:half_matrix] for row in matrix[:half_matrix]]
    quarter2 = [row[half_matrix:] for row in matrix[:half_matrix]]
    quarter3 = [row[:half_matrix] for row in matrix[half_matrix:]]
    quarter4 = [row[half_matrix:] for row in matrix[half_matrix:]]

    # Group quarters into a list for easier manipulation
    quarters = [quarter1, quarter2, quarter3, quarter4]

    # Fake the specified quarters with zeros and ones
    quarters[zero_quarter_index], changes_zero = set_all_quarter_values(quarters[zero_quarter_index], 0)
    quarters[one_quarter_index], changes_one = set_all_quarter_values(quarters[one_quarter_index], 1)

    total_changes = changes_zero + changes_one
    # Process the remaining quarters recursively
    for k in range(4):
        if k != zero_quarter_index and k != one_quarter_index:
            # Call recursively
            quarters[k], sub_changes = find_minimal_fake_card(quarters[k])
            total_changes += sub_changes  # Update changes from recursive calls

    # Merge the quarters back into a full matrix
    first_half = [q1_row + q2_row for q1_row, q2_row in zip(quarters[0], quarters[1])]
    second_half = [q3_row + q4_row for q3_row, q4_row in zip(quarters[2], quarters[3])]

    return first_half + second_half, total_changes


def validate_input(matrix):
    """
    Validates the input matrix. Checks if the matrix is square and its size is a power of 2.

    Parameters:
    matrix (list of lists): The matrix to validate.

    Returns:
    bool: True if the matrix is valid, False otherwise.
    """
    size = len(matrix)
    if size == 0 or any(len(row) != size for row in matrix):
        return False
    # Check if size is a power of 2
    while size % 2 == 0:
        size //= 2
    return size == 1


def find_minimal_fake_card(matrix):
    """
    Finds the fake solution for the matrix with the minimal number of changes.

    Parameters:
    matrix (list of lists): The original matrix to fake.

    Returns:
    tuple: The matrix with the minimal changes and the number of changes made.
    """

    min_changes = float('inf')  # Initialize with a large number
    best_fake_matrix = None

    # Iterate through all quarter combinations
    for zero_quarter_index in range(4):
        for one_quarter_index in range(4):
            if zero_quarter_index != one_quarter_index:  # Ensure different quarters
                current_fake_matrix, changes_count = make_fake_card(matrix, zero_quarter_index, one_quarter_index)
                if changes_count < min_changes:
                    min_changes = changes_count
                    best_fake_matrix = current_fake_matrix

    return best_fake_matrix, min_changes

# Test the algorithm with the original matrix
original_matrix = [[0, 1, 0, 1, 1, 0, 1, 1],
                   [0, 0, 1, 0, 0, 0, 1, 0],
                   [1, 1, 0, 1, 1, 1, 1, 1],
                   [1, 0, 1, 0, 1, 1, 1, 0],
                   [0, 1, 0, 1, 0, 1, 1, 0],
                   [0, 0, 1, 0, 0, 0, 1, 1],
                   [1, 1, 0, 1, 0, 0, 0, 1],
                   [1, 0, 1, 0, 0, 0, 0, 1]]

# Check matrix validation only once, before recursion
if validate_input(original_matrix):
    min_changes_matrix, min_changes = find_minimal_fake_card(original_matrix)
    print("Matrix with minimal changes:", min_changes_matrix)
    print("Minimal number of changes:", min_changes)
else:
    print("The input matrix must be square and its size must be a power of 2.")

#prints:
# Matrix with minimal changes: [[0, 0, 0, 1, 1, 1, 1, 1],
# [0, 0, 1, 0, 1, 1, 1, 1],
# [1, 1, 0, 1, 1, 1, 1, 1],
# [1, 1, 1, 0, 1, 1, 1, 1],
# [0, 0, 0, 1, 0, 0, 0, 0],
# [0, 0, 1, 0, 0, 0, 0, 0],
# [1, 1, 0, 1, 0, 0, 0, 0],
# [1, 1, 1, 0, 0, 0, 0, 0]]
# Minimal number of changes: 15
