from sllist import SkipiNode as Node

class SkipiList:
    """
    This class represents a special kind of a doubly-linked list
    called a SkipiList. A SkipiList is composed of Nodes (SkipiNode from
    sllist).cIn addition to the data, each Node has one pointer to the
    next Node in the list, and another pointer to the prev-prev Node in the 
    list (hence the name "skipi"). The only data members the class contains 
    are the head and the tail of the list.
    """
    def __init__(self):
        """Constructs an empty SkipiList."""
        self.head = None
        self.tail = None
        
    def add_first(self, data):
        """
        Adds an item to the beginning of a list.
        data - the item to add
        """
        if self.head is not None:
            #push current self.head with our new one
            self.head = Node(data,self.head,None)
            #check, and if needed, make new skip_back to the 3rd item on the list
            if self.head.next.next is not None:
                self.head.next.next.skip_back = self.head
        else:
            self.head = Node(data,self.head)
            self.tail = self.head
    
    def remove_first(self):
        """
        Removes the first Node from the list and return its data.
        Returns that data of the removed node
        """
        if self.head is None:
            return
        
        dataToReturn = self.head.data

        self.head = self.head.next
        if self.head is None:
            self.tail = None
        elif self.head.next is not None:
            self.head.next.skip_back = None
        return dataToReturn

    def add_last(self, data):
        """
        Adds an item to the end of a list.
        data - the item to add
        """
        if self.head is not None:
            if self.tail.skip_back is not None:
                self.tail = Node(data,None,self.tail.skip_back.next)
                self.tail.skip_back.next.next = self.tail
            elif self.head != self.tail:
                self.tail = Node(data,None,self.head)
                self.tail.skip_back.next.next = self.tail
            else:
                self.tail = Node(data)
                self.head.next = self.tail
        else:
            self.add_first(data)
        
    def remove_last(self):
        """
        Removes the last Node from the list and return its data.
        The data of the removed node
        """
        if self.tail is None:
            return

        if self.tail is self.head:
            return self.remove_first()
        
        dataToReturn = self.tail.data
        
        if self.tail.skip_back is not None:
            self.tail = self.tail.skip_back.next
            self.tail.next = None
        else:
            self.tail = self.head
            self.tail.next = None
        return dataToReturn
    
    def remove_node(self, node):
        """
        Removes a given Node from the list, and returns its data. 
        Assumes the given node is in the list. Runs in O(1).
        """
        if node is None:
            return
        if node is self.head:
            return self.remove_first()
        if node is self.tail:
            return self.remove_last()

        dataToReturn = node.data
        node.next.skip_back.next = node.next
        if node.next.next is not None:
            node.next.next.skip_back = node.next.skip_back
        node.next.skip_back = node.skip_back
        return dataToReturn
        

    def __getitem__(self, k):
        """
        Returns the data of the k'th item of the list.
        If k is negative return the data of k'th item from the end of the list.
        If abs(k) > length of list raise IndexError."""
        #when k is positive run over k items (if possible and list is
        # smaller then k.
        if k >= 0:
            iterNode = self.head
            counter = 0
            while iterNode is not None:
                if counter == k:
                    return iterNode.data
                counter += 1
                iterNode = iterNode.next

        #if k is negative, run from the end with 2 steps per loop.
        else:
            iterNode = self.tail
            counter = -1
            while iterNode is not None:
                if counter == k:
                    return iterNode.data
                #in case the k is odd
                if counter == k + 1:
                    #if we are on the edge, we have to raise Error
                    if iterNode is self.head:
                        break
                    #if we are one step from the end' we have to return the
                    # head
                    if iterNode is self.head.next:
                        return self.head.data
                    #if none of the above, we found the k'th element
                    return iterNode.skip_back.next.data
                counter -= 2
                iterNode = iterNode.skip_back
        #in case we can't find the k'th element within the list, it means
        # the list is smaller then k. so- ERROR
        raise IndexError


