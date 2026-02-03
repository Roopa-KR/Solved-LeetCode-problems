def generate_row(row):
    ans = 1                 # Stores current nCr value
    ans_row = [1]           # First element of every row is 1

    for col in range(1, row):
        ans = ans * (row - col)   # Multiply numerator part
        ans = ans // col          # Divide denominator part
        ans_row.append(ans)       # Add value to row

    return ans_row

def pascal_triangle(N):
    ans = []                # Stores all rows

    for i in range(1, N + 1):
        ans.append(generate_row(i))  # Generate each row

    return ans

# --- User Input ---
try:
    N = int(input("Enter the number of rows for Pascal's Triangle: "))
    if N <= 0:
        print("Please enter a positive integer.")
    else:
        triangle = pascal_triangle(N)
        print("\nPascal's Triangle:")
        for row in triangle:
            print(' '.join(map(str, row)).center(N*3))  # Centered formatting
except ValueError:
    print("Invalid input! Please enter an integer.")
