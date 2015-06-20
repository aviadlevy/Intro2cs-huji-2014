from sllist import List,Node

def merge_lists(first_list, second_list):
    """
    Merges two sorted (in ascending order) lists into one new sorted list in 
    an ascending order. The resulting new list is created using new nodes 
    (copies of the nodes of the given lists). Assumes both lists are sorted in 
    ascending order. The original lists should not be modified.
    """


def contains_cycle(sll):
    """
    Checks if the given list contains a cycle. 
    A list contains a cycle if at some point a Node in the list points to 
    a Node that already appeared in the list. Note that the cycle does not 
    necessarily contain all the nodes in the list. The original list should 
    not be modified.
    Returns true iff the list contains a cycle
    """
    "*** YOUR CODE HERE ***"

def reverse(sll):
    """
    Reverses the given list (so the head becomes the last element, and every 
    element points to the element that was previously before it). Runs in O(n). 
    No new object is created.
    """
    "*** YOUR CODE HERE ***"

def is_palindrome(sll):
    """
    Checks if the given list is a palindrome. A list is a palindrome if 
    for j=1...n/2 (where n is the number of elements in the list) the 
    element in location j equals to the element in location n-j. 
    Note that you should compare the data stored in the nodes and 
    not the node objects themselves. The original list should not be modified.
    Returns true iff the list is a palindrome
    """
    "*** YOUR CODE HERE ***"

def have_intersection(first_list, second_list):
    """
    Checks if the two given lists intersect. 
    Two lists intersect if at some point they start to share nodes. 
    Once two lists intersect they become one list from that point on and 
    can no longer split apart. Assumes that both lists does not contain cycles. 
    Note that two lists might intersect even if their lengths are not equal. 
    No new object is created, and niether list is modified.
    Returns true iff the lists intersect.
    """
    "*** YOUR CODE HERE ***"
    
def get_item(sll, k):
    """
    Returns the k'th element from of the list. 
    If k > list_size returns None, if k<0 returns the k element from the end.
    """
    "*** YOUR CODE HERE ***"

def slice(sll, start, stop=None, step=1):
    """ Returns a new list after slicing the given list from start to stop
    with a step.
    Behaves the same as using list[start:step:stop], so stop is not in the
    returned list.
    """
    slicedList = []
    for index in range(start):
        sll.remove_first()

    if stop == None:
            stop = start * 2

    for index in range(stop-start):
        slicedList.append(sll.head.get_data())
        sll.remove_first()
        for index2 in range(step - 1):
            sll.remove_first()

    return slicedList

def merge_sort(sll):
    """
    Sorts the given list using the merge-sort algorithm. 
    Resulting list should be sorted in ascending order. Resulting list should 
    contain the same node objects it did originally, and should be stable, 
    i.e., nodes with equal data should be in the same order they were in in the 
    original list. You may create a constant number of new to help sorting.
    """
    "*** YOUR CODE HERE ***"
