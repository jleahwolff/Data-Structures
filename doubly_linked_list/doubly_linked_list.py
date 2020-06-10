"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        #create new node
        new_node = ListNode(value, None, None)
        #Check if DLL is empty:
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            self.length = self.length + 1

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        #find the head
        if self.length is None:
            return None
        else:
            print("Else?")
            self.head.delete()
            self.length -= 1
            
    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        new_node = ListNode(value, None, None)

        if self.head is None:
            return
        else:
            print(self.tail.value)
            self.length += 1
            self.tail.insert_after(value)
            self.tail = self.tail.next


    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        if self.length == 0:
            return None
        else:
            print(self.tail.value)
            self.length -= 1
            if self.length == 0:
                next_val = self.tail
                self.head == None
                self.tail == None
                return next_val.value
            self.tail.delete()
            self.tail = self.tail.prev


    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        if node is self.head:
            return None
        value = node.value
        if node is self.tail:
            self.remove_from_tail()
        else:
            node.delete()
            self.length -= 1
        self.add_to_head(value)

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        if node is self.tail:
            return None
        value = node.value
        if node is self.head:
            self.remove_from_head()
        else:
            node.delete()
            self.length -= 1
        self.add_to_tail(value)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):

        #if DLL is empty, there is nothing to delete, we should return
        if not self.head and not self.tail:
            return

        #decrement length of DLL
        #would allow DLL to have a negative length
        # so put after first if of len = 0
        self.length -= 1
        
        #if DLL has one element, remove it by
        # setting head and tail pointers to None
        if self.head == self.tail:
            self.head = None
            self.tail = None
        
        # if node to delete is head
        #set DLL head pointer to node.next
        #delete node connections
        elif self.head == node:
            self.head = node.next
            node.delete()
        
        #if node to delete is tail
        #reset DLL tail pointer
        # delete node connections
        elif self.tail == node:
            self.tail = node.prev
            node.delete()

        #more than three nodes in our DLL
        #not head or tail to be deleted
        else:
            node.delete()

        
    """Returns the highest value currently in the list"""
    def get_max(self):
        pass
