# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 22:06:59 2021

@author: SunnySun
"""

#冒泡排序 bubble sort
# solution 1

def bubble_sort(list):
    for n in range(len(list)-1, 0 ,-1): #n-1, n-2, n-3,...3,2,1
        print("level:",n)    #for debugging
        for j in range(n):   #[0,n)
            print("compare:", j)
            if (list[j] > list[j+1]):
                #swap
                list[j], list[j+1] = list[j+1], list[j]
                print("after swap:", list)   #for debug
                
#test
alist = [2,3,1,0,5,-1]
bubble_sort(alist)     #in place
print(alist)    


#solution 2
def bubble_sort(list):
    for n in range(0, len(list)):   #0 1 2 3 4 5
        for j in range(len(list)-n-1):   #[0-5), [0-4)...
            if (list[j]>list[j+1]):
                #swap
                list[j], list[j+1] = list[j+1], list[j]
                
#test
alist = [2,3,1,0,5,-1]
bubble_sort(alist)
print(alist)


# selection sort选择排序 如何在数组里找到最大的数字
# 冒泡法每次比较和移动相邻的两项 ；选择排序每次交换当前项和第n项
def find_max(list):
    max_index = 0
    for j in range(len(list)):
        if list[j] > list[max_index]:
            max_index = j
    print(max_index)
    
# test
find_max([1,3,6,8])


def selection_sort(list):
    for i in range(len(list)-1, 0 ,-1):  # i = 6,5,4,3,2,1
        max_index = 0
        for j in range(i+1):       #j = [0,7)
            if (list[j]>list[max_index]):    #update least number index
                max_index = j   
        #swap with the current last number
        list[i], list[max_index] = list[max_index], list[i]

#解法2 swap min交换最小值
def selection_sort(list):
    for i in range(len(list)):
        print("level", i)
        min_index = i
        for j in range(i, len(list)):
            if (list[j] < list[min_index]):
                print(list[j], "compare with", list[min_index]) #update least number index
                min_index = j
                #swap
        list[i], list[min_index] = list[min_index], list[i]
        
        
#插入排序 insertion sort
def insert_num(array, number):
    array.append(number)
    idx = len(array) - 1
    while idx > 0:
        if (array[idx-1] > array[idx]):
            array[idx-1], array[idx] = array[idx], array[idx-1]
        else:
            break
        idx = idx -1
    print(array)   #debug
    
def insertion_sort(array):
    new_arr = []   #这不是一个inplace的操作了
    for i in range(len(array)):
        insert_num(new_arr, array[i])
    return new_arr

#test
alist=[1,5,6,3,2]
new_arr = insertion_sort(alist)
print(alist)
print(new_arr)


#优化一下
def insertion_sort(list):
    for i in range(1, len(list)):
        cur_value = list[i]
        k = i
        while k > 0 and cur_value < list[k-i]:
            list[k] = list[k-1]   #挪动比自己大的数字往后一个位置
            k -= 1               #k = k-1
        list[k] = cur_value
        

# 找到新的数字所应该被插入的位置
def insert_num(array,n):
    idx = len(array)
# binary search find the smallest number larger than n, or find the largest number smaller than n
    insert_index = binary_search(array, n)
    array.append(n)
    while idx > insert_index:
        array[idx] = array[idx-1]
        idx -= 1
    array[insert_index] = n

def insertion_sort(array):
    new_arr = []
    for i in range(len(array)):
        insert_num(new_arr,array[i])
    return new_arr



#recursion 斐波那契数列
# 循环解法一
def fib(n):
    if n <= 1:
        return n
    num_a = 0
    num_b = 1
    for i in range(n-1):
        temp = num_b
        num_b += num_a    #num_b = num_b + num_a
        num_a = temp
    return num_b

# 解法二 recursion递归
    def fib(n):
        if n <= 1:
            return n
        return fib(n-1) + fib(n-2)
    print(fib(5))
    
