from sllist import List, Node


def merge_lists(first_list, second_list):
    """
    Merges two sorted (in ascending order) lists into one new sorted list in
    an ascending order. The resulting new list is created using new nodes
    (copies of the nodes of the given lists). Assumes both lists are sorted in
    ascending order. The original lists should not be modified.
    """
    newList = List()
    firstNode , secondNode = first_list.head , second_list.head
    #merge until one of the lists is 'over'
    while firstNode is not None and secondNode is not None:
        if firstNode.data <= secondNode.data:
            newList.add_first(firstNode.data)
            firstNode = firstNode.next
        else:
            newList.add_first(secondNode.data)
            secondNode = secondNode.next
    #check if the remain list is the first list. if so add. else add second
    if firstNode is not None:
        while firstNode is not None:
            newList.add_first(firstNode.data)
            firstNode = firstNode.next
    elif secondNode is not None:
        while secondNode is not None:
            newList.add_first(secondNode.data)
            secondNode = secondNode.next
    #because we used the 'add_first' function, our list is now reversed.
    reverse(newList)
    return newList



def contains_cycle(sll):
    """
    Checks if the given list contains a cycle.
    A list contains a cycle if at some point a Node in the list points to
    a Node that already appeared in the list. Note that the cycle does not
    necessarily contain all the nodes in the list. The original list should
    not be modified.
    Returns true iff the list contains a cycle

    in this function i  used a method that takes two pointers:
    1. current - move "slower" on the List
    2. ahead   - move "faster" on the List
    and as long as I'm still in the List, i will check if 'current' Node and
    the 'ahead' Node is equal.
    """
    
    current = sll.head
    ahead = sll.head
    #while still in List, move 'current' one step ahead and 'ahead' two steps
    #ahead. if is equal, then it's cycle
    while ahead is not None and ahead.next is not None:
        current = current.next
        ahead = ahead.next.next
        if ahead == current:
            return True
    return False


def reverse(sll):
    """
    Reverses the given list (so the head becomes the last element, and every
    element points to the element that was previously before it). Runs in O(n).
    No new object is created.
    """
    if sll.head is None:
        return
    current = sll.head
    nxt = sll.head.next
    #we change the first value to be our new last ,in order to not make
    # cycled List
    sll.head.next = None
    if nxt is None:
        return
    while nxt is not None:
    #we used 3 var:
    # 1. current - the current value we want to change
    # 2. nxt - the next value we want to change
    # 3. tmp - temporary value to save so we can change between values
        tmp = nxt.next
        nxt.next = current
        current = nxt
        nxt = tmp
    sll.head = current
    return

def is_palindrome(sll):
    """
    Checks if the given list is a palindrome. A list is a palindrome if
    for j=0...n/2 (where n is the number of elements in the list) the
    element in location j equals to the element in location n-j.
    Note that you should compare the data stored in the nodes and
    not the node objects themselves. The original list should not be modified.
    Returns true iff the list is a palindrome
    """
    
    countToEnd = 0
    countFromStart = 0
    iterNode = sll.head
    nodeFirst = sll.head
    
    if nodeFirst is None:
        return True
    #count to the end of the list
    while iterNode.next is not None:
        countToEnd += 1
        iterNode = iterNode.next
    #run over half of the list
    for index in range(countToEnd // 2 + countToEnd % 2):
        compareVal = nodeFirst
        #move nodeFirst to the other half of the list
        for index1 in range(countToEnd - countFromStart):
            nodeFirst = nodeFirst.next
        #compare
        if nodeFirst.data != compareVal.data:
            return False
        countFromStart += 1
        countToEnd -= 1
        nodeFirst = compareVal.next
    return True

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
    
    if first_list.head is None or second_list.head is None:
        return False
    
    lastNodeFrstLst = first_list.head
    iterNodeScndLst = second_list.head
    #move first iterator node to the end of the list
    while lastNodeFrstLst.next is not None:
        lastNodeFrstLst = lastNodeFrstLst.next
        
    #check every if every seconfNode.next is equal to the last of the first
    #if they interesect they should be equal
    while iterNodeScndLst.next is not None:
        if iterNodeScndLst.next == lastNodeFrstLst:
            return True
        iterNodeScndLst = iterNodeScndLst.next
    return False


def get_item(sll, k):
    """
    Returns the k'th element from of the list.
    If k > list_size returns None, if k<0 returns the k element from the end.
    """
    
    if sll.head is None:
        return None
    iterNode = sll.head
    countLen = 0
    #count the length of the list
    while iterNode.next is not None:
        countLen += 1
        iterNode = iterNode.next
    
    iterNode = sll.head
    #check if k is vaild
    if k > countLen or k < (0 - countLen - 1):
        return None
    #if k is positive, run to the k'th element, remove and return the data
    if k >= 0:
        for index in range(k):
            iterNode = iterNode.next
        return iterNode.data
    #likwise if k is negative
    else:
        for index in range (k + countLen + 1):
            iterNode = iterNode.next
        return iterNode.data

def slice(sll, start, stop = None, step = None):
    """ Returns a new list after slicing the given list from start to stop
    with a step.
    Imitates the behavior of slicing regular sequences in python.
    slice(sll, [start], stop, [step]):
    With 4 arguments, behaves the same as using list[start:stop:step],
    With 3 arguments, behaves the same as using list[start:stop],
    With 2 arguments, behaves the same as using list[:stop],
    """
    counter = 0
    iterNode = sll.head

    while iterNode is not None:
        counter += 1
        iterNode = iterNode.next

    if start >= counter or stop < 0:
        return List()

    if start is None:
        start, stop = 0, counter
    elif stop is None:
        start, stop = 0, start

    myList = List()
    iterNode = sll.head
    for index in range(start):
        iterNode = iterNode.next

    myList.add_first(iterNode.data)
    while start + abs(step) < stop:
        for index in range(abs(step)):
            iterNode = iterNode.next
        start += abs(step)
        myList.add_first(iterNode.data)
    if step > 0:
        reverse(myList)

    return myList




def merge_sort(sll):
    """
    Sorts the given list using the merge-sort algorithm.
    Resulting list should be sorted in ascending order. Resulting list should
    contain the same node objects it did originally, and should be stable,
    i.e., nodes with equal data should be in the same order they were in in the
    original list. You may create a constant number of new to help sorting.
    """
    def recursive_sort(nodeHead):
        """Sorts the given list using the merge-sort algorithm.
        I implement "Locality Of Reference" I found online"""
 
        #if list contains only one node, return it
        if not nodeHead.next:
            return nodeHead
 
        #find the middle of the list
        middle, ahead = nodeHead, nodeHead.next
        while ahead and ahead.next:
            middle, ahead = middle.next, ahead.next.next
 
        #split both list
        leftList = nodeHead
        rightList = middle.next
        middle.next = None
 
        #send splitted lists again
        leftList = recursive_sort(leftList)
        rightList = recursive_sort(rightList)
    
        #merge the two lists and return the first node
        tail = reference
 
        #sort in dicreasing order
        while rightList is not None and leftList is not None:
            if rightList.data < leftList.data:
                tail.next = rightList
                rightList = rightList.next
            else:
                tail.next = leftList
                leftList = leftList.next
            tail = tail.next
 
        #until we have only one node
        if rightList is not None:
            tail.next = rightList
        else:
            tail.next = leftList
 
        #return the node after the reference node
        return reference.next
  
    if sll.head is not None:
        #create new reference node to simplify merging sublists.
        reference = Node(None)
        sll.head = recursive_sort(sll.head)
