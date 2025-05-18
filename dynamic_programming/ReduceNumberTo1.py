"""
given a number N reduce that number to 1 
given the following operations
substract by 1 
divide by 2 if  N%2==0
divide by 3 id N%3==0
"""


def ReduceNoTo1(N):
    dp = [0 for i in range(100)]
    dp[0] = 0
    dp[1] = 1
    dp[2] = 2
    dp[3] = 2

    for i in range(4, len(dp)):
        dp[i] = min(dp[i-1] + 1, dp[i//2] + 1 if i%2 == 0 else 10**5, dp[i//3] + 1 if i%3 == 0 else 10**5) 
    print(dp)

ReduceNoTo1(7)