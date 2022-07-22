"""
See Data Structure - Linked Lists.ipynb for more interactive examples on both classes below
"""



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



    # Returns the head element
    def get_head(self):
        return self.head



    # Returns the tail element
    def get_tail(self):
        current = self.head
        
        while current != None:
            if current.next_node == None:
                return current
            else:
                current = current.next_node


    # Prints out a string of all the nodes (similar to __repr__()), but also includes the index number of each node
    def get_index_positions(self):
        nodes = [] # regular list containing all the nodes
        current = self.head
        index = 0
        
        while current != None:
            # Add head element to regular list
            if current is self.head:
                nodes.append("[Head: %s] (Index %d)" % (current.data, index))
            
            # Add tail element to regular list
            elif current.next_node is None:
                nodes.append("[Tail: %s] (Index %d)" % (current.data, index))

            # Add all of the other elements b/w the head & tail
            else:
                nodes.append("[%s] (Index %d)" % (current.data, index))

            index += 1
            
            current = current.next_node # go to the next node in LinkedList
        
        return '--> '.join(nodes)


    # With a given index position, return the node at the specified index
    def get_node_at_index(self, index):
        current = self.head
        current_position = 0


        # Makes sure index is an integer number
        try:
            int(index) == index
        except:
            return "Please enter an integer for the index position"


        while current != None:
            # If negative number or if index # is greater than the last index number in list:
            if index < 0 or index > self.size():
                return "Index is out of bounds, enter a valid index"
                break
            
            # Once position equals the specified index number:
            elif current_position == index:
                return current

            else:
                current = current.next_node
                current_position += 1




    ## Allows you to add new node with data, prepending to BEGINNING of list as new head element; O(1) time
    def prepend_item(self, data):
        new_node = Node(data)
        new_node.next_node = self.head # have the new node point to the current head element
        self.head = new_node # THEN, prepend insert to beginning of list & make the new insert the new head element



    ## Allows you to add new node with data, appending to END of list as new head element; O(1) time
    def append_item(self, data):
        if self.is_empty():
            self.prepend_item(data)
            
        else:
            new_node = Node(data)

            current = self.head

            while current != None:
                if current.next_node == None:
                    current.next_node = new_node
                    break
                else:
                    current = current.next_node




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

    # def insert_test(self):
    #     current = self.head
    #     count = 0 # increments for each node visited

    #     # Go through list until the very end (tail node)
    #     while current != None:
    #         print(count)
    #         count += 1

    #         current = current.next_node # go to the next node in LinkedList

    #     return count




    ## Insert new nodes in list, before specified index position
    def insert(self, data, index):
        current = self.head
        previous = None
        current_position = 0


        # Makes sure index is an integer number
        try:
            int(index) == index
        except:
            return "Please enter an integer for the index position"


        # O(1) time to insert; O(n) to search for index position ---> overall O(n) time
        # Need to change pointers for node BEFORE and AFTER new insertion
        while current != None:

            # If negative number or 0, insert at the very beginning of list ---> just invoke prepend_item() method
            if index <= 0:
                self.prepend_item(data)
                break
            
            # If index number greater than list size, insert at the very end of list ---> just invoke append_item() method
            elif index > self.size():
                self.append_item(data)
                break
            
            # Once position equals the specified index number:
            elif current_position == index:
                new_insert = Node(data) # create new node

                # EXAMPLE: 
                #           1 (previous) --> 3 (previous.next_node / current)
                #           1 (previous) --> 2 (previous.next_node / new_insert)
                #           2 (new_insert) --> 3 (new_insert.next_node / current)
                #           1 (previous) --> 2 (previous.next_node / new_insert) --> 3 (new_insert.next_node / current)
                
                previous.next_node = new_insert
                new_insert.next_node = current
                break

            else:
                previous = current
                current = current.next_node
                current_position += 1

        return self.__repr__()





    ## Deletes 1st matching node of the passed in data value ("key"); O(n) time; updating node pointers of before and after nodes
    ## Returns node or None if key doesn't exist
    ## O(1) time to delete; O(n) to search ---> overall O(n) time
    def delete(self, key):
        current = self.head
        previous = None
        found = False

        while current != None and not found:
            # If you want to delete head node element:
            if current.data == key and current is self.head:
                # changing the pointer nodes will automatically remove any nodes that no longer have anything pointing to it
                self.head = current.next_node 
                found = True

            # if the node after is the key:
            elif current.data == key:
                previous.next_node = current.next_node
                found = True
            
            else:
                previous = current
                current = current.next_node # go to the next node in LinkedList
        return current




    ## What to display when LinkedList object name is invoked
    ## Returns a string representation of list; O(n) time
    def __repr__(self):
        nodes = [] # regular list containing all the nodes
        current = self.head
        count = 0
        
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

            count += 1
            
            current = current.next_node # go to the next node in LinkedList
        
        return '--> '.join(nodes)


