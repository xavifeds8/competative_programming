# There are N flowers arranged in a row. For each i (1≤i≤N), the height and beauty of the i-th flower from the left are h_i and a_i, respectively.
# The heights h_1, h_2, ..., h_N are all distinct.
# Taro wants to remove some flowers such that the heights of the remaining flowers are monotonically increasing from left to right.
# Find the maximum possible sum of the beauties of the remaining flowers.


"""
Since the remaining flowers are in the increasing subsequence order 
We can think of this as an LIS problem 
Since we want the maximize the sum of beautities. 
"""  


def LIS(height, beauty):
    dp = [0 for i in range(len(height))]
    dp[0] = beauty[0]
    for i in range(1, len(height)):
        dp[i] = beauty[i]
        for j in range(i+1):
            if height[j] < height[i]:
                dp[i] = max(dp[i], dp[j] + beauty[i])
    return max(dp)


print(LIS([3,1,4,2],[10,20,30,40]))
print(LIS([4,2,5,8,3,6,1,7,9],[6,8,8,4,6,3,5,7,5]))
