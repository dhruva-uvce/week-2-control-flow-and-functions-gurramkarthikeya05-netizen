# Q08. Sum of Digits (while loop)
#
# Ask the user for a positive integer.
# Print the sum of its digits using a while loop.
#
# Sample Input:   Enter a number: 9876
# Sample Output:  Sum of digits of 9876 = 30

# --- YOUR CODE HERE ---
original_n = int(input("Enter a number: "))
n = original_n
sum_digits = 0
while n > 0:
    sum_digits += n % 10
    n = n // 10
print(f"Sum of digits of {original_n} = {sum_digits}")
