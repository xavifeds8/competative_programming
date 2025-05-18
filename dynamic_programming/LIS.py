""" Given an array arr[] of size n, the task is to find the length of the Longest Increasing Subsequence (LIS) 
i.e., the longest possible subsequence in which the elements of the subsequence are sorted in increasing order.

Input: arr[] = [3, 10, 2, 1, 20]
Output: 3
Explanation: The longest increasing subsequence is 3, 10, 20

Input: arr[] = [30, 20, 10]
Output:1
Explanation: The longest increasing subsequences are [30], [20] and [10]

Input: arr[] = [2, 2, 2]
Output: 1
Explanation:  We consider only strictly increasing.

Input: arr[] = [10, 20, 35, 80]
Output: 4
Explanation: The whole array is sorted

"""


"""
Approach :-
    If there is any mention of subsequence then try to think in dp terms 
    If there is any index to calculate that if we need some information of the prev elements think in dp terms 

Solution :- 
    for a given index f(i)
    traverse throught the array and calculate the max possible subsequence value at the point and store in a dp array 
    return the max of the dp array
"""


def LIS(arr):
    dp = [1 for _ in range(len(arr))]
    for i in range(1, len(arr)):
        for j in range(i):
            # check if the previous values are smaller than the ith element and if they 
            # can contribute to the solution 
            if arr[j] < arr[i]:
                dp[i] = max(dp[i],dp[j]+1)
    return max(dp)

print(LIS([7,7,7,7,7,7,7]))