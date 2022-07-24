from collections import deque


###### DEQUE OBJECTS ######
class Queue_Deque:
    def __init__(self):
        self.queue = deque() # create a new deque() object upon class object creation

    # Add items to queue in order from left to right
    def enqueue(self, data):
        return self.queue.append(data)

    # Retrieve first added item (leftmost item) & remove from deque object
    def dequeue(self):
        return self.queue.popleft()
    
    # Retrieve first added item, but DO NOT remove from deque
    def peek(self):
        return self.queue[0] 

    # Check to see if deque object is empty; returns a boolean of True if it is empty
    def is_empty(self):
        return len(self.queue) == 0

    # Returns the number of items in the deque object
    def size(self):
        return len(self.queue)

    # What to print out when Queue_Deque object name is invoked
    def __repr__(self):
        if self.is_empty():
            return "No items have been added to deque yet"
        
        else:
            items = []
            index = 0
            max_index = self.size() - 1

        while index <= max_index:
            # First item added
            if index == 0:
                items.append("[FRONT: %s]" % self.queue[index])
            
            # Last item added
            elif index == max_index:
                items.append("[BACK: %s]" % self.queue[max_index])

            # All the rest of the items
            else:
                items.append("[%s]" % self.queue[index])


            index += 1
        
        
        return ' --> '.join(items)



###### LIST OBJECTS ######
class Queue_List:
    def __init__(self):
        self.queue = [] # create a new list upon class object creation

    # Add items to list in order from left to right
    def enqueue(self, data):
        return self.queue.append(data)

    # Retrieve first added item (leftmost item) & remove from list
    def dequeue(self):
        return self.queue.pop(0)
    
    # Retrieve first added item, but DO NOT remove from list
    def peek(self):
        return self.queue[0] 

    # Check to see if list is empty; returns a boolean of True if it is empty
    def is_empty(self):
        return len(self.queue) == 0

    # Returns the number of items in the list
    def size(self):
        return len(self.queue)

    # What to print out when Queue_List object name is invoked
    def __repr__(self):
        if self.is_empty():
            return "No items have been added to deque yet"
        
        else:
            items = []
            index = 0
            max_index = self.size() - 1

        while index <= max_index:
            # First item added
            if index == 0:
                items.append("[FRONT: %s]" % self.queue[index])
            
            # Last item added
            elif index == max_index:
                items.append("[BACK: %s]" % self.queue[max_index])

            # All the rest of the items
            else:
                items.append("[%s]" % self.queue[index])


            index += 1
        
        
        return ' --> '.join(items)