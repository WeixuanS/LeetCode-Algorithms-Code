# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 14:28:42 2021

@author: SunnySun
"""


# 33. Number of Nodes链表
class Solution(object):
  def numberOfNodes(self, head):
    num = 0
    while head:
      num += 1
      head = head.next
    return num


# 612 design linkedlist 链表
# Solution 1 singly linked list 
class _ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None
        
class Solution(object):
    def __init__(self):
        self._head = None
        self._size = 0
        self._tail = None
        
    def _get(self, index):
        node = self._head
        for _ in range(index):
            node = node.next
        return node
    
    def get(self, index):
        if index < 0 or index >= self._size:
            reurn -1
        return self._get(index).val
    
    def addAtHead(self, val):
        if self._size == 0:
            self._head = self._tail = _ListNode(val)
        else:
            new_head = _ListNode(val)
            new_head.next = self._head
            self._head = new_head
        self._size += 1
        
    def addAtTail(self, val):
        if self._size == 0:
            self._head = self._tail = _ListNode(val)
        else:
            self._tail.next = _ListNode(val)
            self._tail = self._tail.next
        self._size += 1
        
    def addAtIndex(self, index, val):
        if index < 0 or index > self._size:
            return
        if index == 0:
            self.addAtHead(val)
        elif index == self._size:
            self.addAtTail(val)
        else:
            node = self._get(index-1)
            new_node = _ListNode(val)
            new_node.next = node.next
            node.next = new_node
            self._size += 1
            
    def deleteAtIndex(self, index):
        if index < 0 or index >= self._size:
            return
        if index == 0:
            new_head = self._head.next
            self._head.next = None
            self._head = new_head
            #what if I remove the last node in the list?
            if not self._head:
                self._tail = None
        else:
            node = self._get(index-1)
            remove_node = node.next
            node.next = remove_node.next
            remove_node.next = None
            #what if I remove the original tail?
            if index == self._size - 1:
                self._tail = node
        self._size -= 1
        
    def __str__(self):
        strs = []
        node = self._head
        while node is not None:
            strs.append(str(node.val))
            node = node.next
        return '->'.join(strs)
    
# 34 Reverse Linked List (iterative)
class Solution(object):
    def reverse(self, head):
        prev, curr = None, head
        while curr:
            next = curr.next
            curr.next = prev
            prev, curr = curr, next
        return prev
    
# 653. Reverse Linked List (recursive)
class Solution(object):
    def reverse(self, head):
        if not head or head.next:
            return head
        new_head = self.reverse(head.next)
        head.next.next = head
        head.next = None
        return new_head
    
# 40. Merge Two Sorted Linked Lists
class Solution(object):
    def merge(self, one, two):
        fake_head = ListNode(None)
        cur = fake_head
        while one and two:
            if one.val < two.val:
                cur.next = one
                one = one.next
            else:
                cur.next = two
                two = two.next
            cur = cur.next
        if one:
            cur.next = one
        if two:
            cur.next = two
        return fake_head.next
        
        
        