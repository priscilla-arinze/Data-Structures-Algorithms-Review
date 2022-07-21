
###### A class object for storing a single node of a linked list: ######
class Node:
    ## Attributes
    data = None # actual list element
    next_node = None # pointer to the next node of the list

    ## Constructor
    def __init__(self, data):
        self.data = data
    
    ## What to display when object name is invoked
    def __repr__(self):
        return "<Node data %s>" % self.data




###### A class object that defines a singly linked list: ######
class LinkedList:
    ## Constructor
    def __init__(self):
        self.head = None


    ## Boolean check to see if list is empty or not
    def is_empty(self):
        return self.head == None


    ## Output the size (numbr of nodes) of the list; O(n) time
    def size(self):
        current = self.head
        count = 0 # increments for each node visited

        # Go through list until the very end (tail node)
        while current != None:
            count += 1

            current = current.next_node # go to the next node in LinkedList

        return count


    ## Allows you to add new node with data, prepending to beginning of list as new head element; O(1) time
    def add(self, data):
        new_node = Node(data)
        new_node.next_node = self.head # have the new node point to the current head element
        self.head = new_node # THEN, prepend insert to beginning of list & make the new insert the new head element


    ## Search for the 1st matching node of the passed in data value ("key"); O(n) time
    ## "key" parameter is the actual value being searched for in the linkedlist
    def search(self, key):
        current = self.head

        while current != None:
            if current.data == key:
                return current
            else:
                current = current.next_node # go to the next node in LinkedList
            
        return "Not in list" # Return if finished w/ above while loop & key is not found in list


    ## What to display when LinkedList object name is invoked
    ## Returns a string representation of list; O(n) time
    def __repr__(self):
        nodes = [] # regular list containing all the nodes
        current = self.head

        while current != None:
            # Add head element to regular list
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            
            # Add tail element to regular list
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)

            # Add all of the other elements b/w the head & tail
            else:
                nodes.append("[%s]" % current.data)


            current = current.next_node # go to the next node in LinkedList
        
        return '--> '.join(nodes)
