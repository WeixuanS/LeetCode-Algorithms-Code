# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 16:11:20 2021

@author: SunnySun
"""

# Q1 find target number in a sorted int array
def binary_search(nums, target):
  if not nums:       #nums is a sorted list nums = [1,2,4,5,7,8,9]
    return None     #target is the number we want to search like target = 4
  left = 0
  right = len(nums) - 1
  while left <= right:   #[left, right]是要搜索的范围
        mid = (left + right) // 2   #不用关心溢出问题
    if nums[mid] > target:
        right = mid - 1
    elif nums[mid] < target:
        left = mid + 1
    else:
        return mid
  return None



#变种1 apply binary search in 2d array
def binary_search_in_2d_array(matrix, target):
    if not matrix:
        return None
N, M = len(matrix), len(matrix[0])
left, right = 0, N*M-1
while left <= right:
    mid = (left+right) // 2
    row_num = mid // M
    col_num = mid % M
    if matrix[row_num][col_num] > target:
        right = mid - 1
    elif matrix[row_num][col_num] < target:
        left = mid + 1
    else:
        return(row_num, col_num)
    return None



#变种2 找最近的number
def find_closest_num(nums, target):
    if not nums:
        return None
    left = 0
    right = len(nums)-1
    while left < right - 1:
        mid = (left + right) // 2
        if nums[mid] > target:
            right = mid
        elif nums[mid] < target:
            left = mid
        else:
            return mid
    return left if abs(nums[left]-target) < abs(nums[right]-target) else right
    

#其他变种：find the index of the first occurence of an element
def find_first_occurence(nums, target):
    if not nums:
        return None
    left = 0
    right = len(nums) - 1
    while left < right - 1:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            right = mid
    if nums[left] == target:
        return left
    if nums[right] == target:
        return right
    return None


#其他变种：find the index of the last occurence of an element 
def find_last_occurence(nums, target):
    if not nums:
        return None
    left = 0
    right = len(nums) - 1
    while left < right - 1:
        mid = (left + right) // 2
        if nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            left = mid
    if nums[right] == target:
        return right
    if nums[left] == target:
        return left
    return None

