from collections import deque


###### DEQUE OBJECTS ######
class Stack_Deque:
    def __init__(self):
        self.stack = deque() # create a new deque() object upon class object creation

    # Add items to stack
    def push(self, data):
        return self.stack.append(data)

    # Retrieve last added item & remove from deque object
    def pop(self):
        return self.stack.pop()
    
    # Retrieve last added item, but DO NOT remove from deque object
    def peek(self):
        return self.stack[-1]

    # Check to see if deque object is empty; returns a boolean of True if it is empty
    def is_empty(self):
        return len(self.stack) == 0

    # Returns the number of items in the deque object
    def size(self):
        return len(self.stack)

    # What to print out when Stack_Deque object name is invoked
    def __repr__(self):
        if self.is_empty():
            return "No items have been added to deque yet"
        
        else:
            items = []
            reverse_index = self.size() - 1
            max_index = self.size() - 1

        while reverse_index >= 0:
            # First item added
            if reverse_index == 0:
                items.append("[FIRST: %s]" % self.stack[reverse_index])
            
            # Last item added
            elif reverse_index == max_index:
                items.append("[LAST: %s]" % self.stack[max_index])

            # All the rest of the items
            else:
                items.append("[%s]" % self.stack[reverse_index])


            reverse_index -= 1
        
        
        return '\n'.join(items)




###### LIST OBJECTS ######
class Stack_List:
    def __init__(self):
        self.stack = [] # create a new list object upon class object creation

    # Add items to stack
    def push(self, data):
        return self.stack.append(data)

    # Retrieve last added item & remove from list
    def pop(self):
        return self.stack.pop()
    
    # Retrieve last added item, but DO NOT remove from list
    def peek(self):
        return self.stack[-1]

    # Check to see if list is empty; returns a boolean of True if it is empty
    def is_empty(self):
        return len(self.stack) == 0

    # Returns the number of items in the list
    def size(self):
        return len(self.stack)

    # What to print out when Stack_List object name is invoked
    def __repr__(self):
        if self.is_empty():
            return "No items have been added to list yet"
        
        else:
            items = []
            reverse_index = self.size() - 1
            max_index = self.size() - 1

        while reverse_index >= 0:
            # First item added
            if reverse_index == 0:
                items.append("[FIRST: %s]" % self.stack[reverse_index])
            
            # Last item added
            elif reverse_index == max_index:
                items.append("[LAST: %s]" % self.stack[max_index])

            # All the rest of the items
            else:
                items.append("[%s]" % self.stack[reverse_index])


            reverse_index -= 1
        
        
        return '\n'.join(items)