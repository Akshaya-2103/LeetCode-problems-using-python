# Function to find the sum of contiguous subarray with maximum sum.
'''Given an integer array nums, find the 
subarray
 with the largest sum, and return its sum.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.'''

def maxSubArraySum(arr, n):
        ##Your code here
        positive = []
        negative = []
        sum = [] 
        max_sum = 0
        for i in arr:
            if i >= 0:
                positive.append(i)
            else:
                negative.append(i)
                
        if positive == arr:
            max_sum = sum(arr)
        elif negative == arr:
            max_sum = min(arr)
        else:
            print(arr)
            for i in arr:
                if i>=0:
                    max_sum += i
                    sum.append(max_sum)
                    print(max_sum)
                else:
                    max_sum = 0
                    print(max_sum)
        print(sum)
        return max(sum)

#OR alternate method
        ##Your code here
        
        positive = []
        negative = []
        max_sum = 0
        arr.sort()
        for i in arr:
            if i >= 0:
                positive.append(i)
            else:
                negative.append(i)
                
        if negative == arr:
            max_sum = min(arr)
            print(max(arr))
        else :
            max_sum = sum(arr)
        return max_sum

