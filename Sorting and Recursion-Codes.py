# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 11:56:00 2021

@author: SunnySun
"""

# selection sort laicode题
class Solution(object):
  def solve(self, array):
    for i in range(len(array)-1, 0 ,-1):
      max_index = 0
      for j in range(i+1):
        if(array[j] > array[max_index]):
          max_index = j
      array[i], array[max_index] = array[max_index], array[i]
    return array
