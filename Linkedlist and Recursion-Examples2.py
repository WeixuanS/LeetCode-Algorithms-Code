# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 14:16:26 2021

@author: SunnySun
"""

# write a function to accept a list of things and then produce a corresponding signly linkedin list
def buildList(seq):
    #seq is a list of objects
    f = ListNode(None)
    c = f
    for obj in seq:
        c.next = ListNode(obj)
        c = c.next
    return f.next
h = buildList([1,2,3,4])

#how to design a linkedlist class
class _ListNode(object):
    def __init__(self,val):
        self.value = val
        self.next = None
class MyLinkedList(object):
    def __init__(self):    #initialize data structure, construct an empty linkedlist
    
    def get(self, index): #get the value of the index node in the linkedlist, if the index is invalid, return -1
    
    def addAtHead(self, val):
# add a node of value val before the first element of the linked list
# after the insertion, the new node will be the first node
    def addAtTail(self, val):
        
    def addAtIndex(self, index, val):
        
    def deleteAtIndex(self, index):
        