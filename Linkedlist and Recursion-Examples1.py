# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 12:41:14 2021

@author: SunnySun
"""

# How to present a node in a singly linkedlist in python
class ListNode(object):
    def __init__(self, value):
        self.next = None
        self.value = value
node1 = ListNode("H")
node2 = ListNode("E")
node1.next = node2

# traverse遍历
def print_all_nodes(head):
    while head is not None:
        print(head.val)
        head = head.next

#search by index
def search_by_index(head, index):
    #assuming valid index should >= 0
    #return a node object if found, None otherwise
    if head is None or index < 0:
        return None
    for move_times in range(index):
        head = head.next
        if not head:
            return None
    return head

#search by value
def search_by_value(head, value):
    if not head:
        return None
    current_node = head
    while current_node is not None:
        if current_node.val == value:
            return current_node
        current_node = current_node.next
    return None

#__eq__ id的问题 id(obj1)==id(obj2)
class ListNode(object):
    def__init__(self, value):
        self.value = value
        self.next = None
    def__eq__(self, other):
        return isinstance(other, ListNode) and self,value == other.value
    

# add to index
def add_to_index(head, index, value):
    if index == 0:
        new_head = ListNode(value)
        new_head.next = head
        return new_head
    else:
        #prevnode points to the node that preceds the node at the insertion position
        prevNode = search_by_index(head, index-1)
        if prevNode is None:
            return head
        new_node = ListNode(value)
        new_node.next = prevNode.next
        prevNode.next = new_node
        return head
    

# add to index, 加dummy node
def add_to_index(head, index, val):
    #assuming valid index should >= 0
    #this function will try to insert a new node at position indicated by index
    #if such position does not exist, this function will be a no-op
    fake_head = ListNode(None)
    fake_head.next = head
    insert_place = search_by_index(fake_head, idex)
    if insert_place is None:
        return fake_head.next
    new_node = ListNode(val)
    new_node.next = insert_place.next
    insert_place.next = new_node
    return fake_head.next


# remove from index
def remove_from_index(head, index):
    #assuming valid index should >= 0
    #this function will try to insert a new node at position indicated by index
    #if such position does not exist, this function will be a no-op
    fake_head = ListNode(None)
    fake_head.next = head
    remove_place = search_by_index(fake_head, index)
    if remove_place is None or remove_place.next is None:
        #it is likely that we find the predecessor of the node we want to remove but not the node itself
        return fake_head.next
    remove_node = remove_palce.next
    remove_place.next = remove_node.next
    remove_node.next = None
    return fake_head.next
        
    
    
