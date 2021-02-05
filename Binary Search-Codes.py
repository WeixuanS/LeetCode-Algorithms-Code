# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 17:48:16 2021

@author: SunnySun
"""


# 14. Classical Binary Search

class Solution(object):
  def binarySearch(self, array, target):
    if array is None or len(array) == 0:
      return -1
    left = 0
    right = len(array) - 1
    while left < right - 1:
      mid = (left + right ) // 2
      if array[mid] == target:
        return mid
      if array[mid] < target:
        left = mid
      else:
        right = mid
    if array[left] == target:
      return left
    if array[right] == target:
      return right
    return -1