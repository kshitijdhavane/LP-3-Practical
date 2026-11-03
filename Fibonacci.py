# Program 3: Program to Generate Fibonacci Series using Dynamic Programming

def fibonacci(n):

    dp = [0] * n

    dp[0] = 0

    if n > 1:
        dp[1] = 1

    for i in range(2, n):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp



n = int(input("Enter number of terms: "))

if n <= 0:
    print("Enter a positive number")
else:
    result = fibonacci(n)

    print("Fibonacci Series:")

    for i in range(n):
        print(result[i], end=" ")
