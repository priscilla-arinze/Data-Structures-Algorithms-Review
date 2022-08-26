class HeapHelperMethods:

    ################   HELPER METHODS FOR MinHeap() AND MaxHeap()  ################

    ### GETTERS: INDEX
    def getLeftChildIndex(self, parentIndex):
        try:
            return (parentIndex * 2) + 1 # add 1 for LEFT CHILD
        except:
            raise Exception("Not a valid index number")

    def getRightChildIndex(self, parentIndex):
        try:
            return (parentIndex * 2) + 2 # add 2 for RIGHT CHILD
        except:
            raise Exception("Not a valid index number")

    def getParentIndex(self, childIndex):
        try:
            # If 1st element (root)
            if childIndex == 0:
                # so instead of returning None, return -1 so int comparisons can occur in the push & heapify methods
                # Also, if there is only one element in the list (root), luckily in Python you can index the last (in this case, the ONLY) element with -1
                return -1 

            # If index is even
            elif childIndex % 2 == 0:
                return int( (childIndex - 2) / 2 )

            # If index is odd
            else:
                return int( ((childIndex - 2) / 2) + 0.5 )
        except:
            raise Exception("Not a valid index number")


    ### CHECK IF EXISTS
    def hasLeftChild(self, currentIndex):
        if self.getLeftChildIndex(currentIndex) < self.heapList_length:
            return True
        else:
            return False

    def hasRightChild(self, currentIndex):
        if self.getRightChildIndex(currentIndex) < self.heapList_length:
            return True
        else:
            return False

    def hasParent(self, currentIndex):
        parentIndex = self.getParentIndex(currentIndex)

        if parentIndex == -1:
            return False

        elif parentIndex < self.heapList_length:
                return True

        else:
            return False


    ### GETTERS: VALUE
    def getLeftChild(self, currentIndex):
        if self.hasLeftChild(currentIndex):
            return self.heapList[self.getLeftChildIndex(currentIndex)]
        else:
            return "This current node, " + str(currentIndex) + " does not have a left child"

    def getRightChild(self, currentIndex):
        if self.hasRightChild(currentIndex):
            return self.heapList[self.getRightChildIndex(currentIndex)]
        else:
            return "This current node, " + str(currentIndex) + " does not have a right child"

    def getParent(self, currentIndex):
        if self.hasParent(currentIndex):
            return self.heapList[self.getParentIndex(currentIndex)]
        else:
            return "This current node, " + str(currentIndex) + " does not have a parent"


    ## Swaps elements from one index to another
    def swap(self, index1, index2):
        try:
            temp = self.heapList[index1]

            self.heapList[index1] = self.heapList[index2]
            self.heapList[index2] = temp
        except:
            raise Exception("Not a valid index number")






class MaxHeap(HeapHelperMethods):
    
    ## CONSTRUCTOR
    def __init__(self):
        self.heapList = []
        self.heapList_length = 0 # need to initilize at 0 rather than using len() because it will always be 0 for some reason, so will have to manually increase/decrease


    ## retrieves (but doesn't pop) 1st element in list (which is the maximum element in the heap)
    def peekMax(self):
        if self.heapList.length == 0:
            return "Heap is completely empty"
        else:
            return self.heapList[0]



    ## REMINDER: Max heap nodes generally get smaller as you go down the heap tree; parents > children



    ## Time Complexity for Heapify methods: AVERAGE --> O(log n), WORST --> O(n)

    ## From bottom to top: Rearrange binary heap list, swapping parent nodes to child nodes if necessary
    ## After heapPush() [last element in list --> start at index 0]
    def maxHeapifyPush(self):
        currentIndex = self.heapList_length - 1 # start at END (bottom)

        # Keep looping if:
            # the current node (currentIndex) has a parent node, AND
            # the parent node is LARGER than the current node (we want parent < current child)
        while( self.hasParent(currentIndex) and self.getParent(currentIndex) < self.heapList[currentIndex] ):
            # if parent < child in max heap --> swap parent to child (current)
            self.swap(self.getParentIndex(currentIndex), currentIndex)

            # continue up the heap tree, parent by parent
            currentIndex = self.getParentIndex(currentIndex)


    ## Rearrange heap list to follow the order of a binary heap ("heap property") after adding a new element at the end
    ## After heapPop() [first element in list --> start at last index]
    def maxHeapifyPop(self):
        currentIndex = 0 # start at BEGINNING (top)

        # Keep looping if a left child exists
            # NOTE: Since heaps are complete binary trees, they are skewed to the left, so there is no need to base while loop condition
            # on whether the current node has a right child or not since all of the leaves will be lined up from left to right
        while self.hasLeftChild(currentIndex):
            # initially, set bigger child index variable to the left child
            biggerChildIndex = self.getLeftChildIndex(currentIndex)

            # If it right child also exists for the current node, then find the max node between the left & right and set it to the
            # bigger child index variable
            if self.hasRightChild(currentIndex):
                biggerChildIndex = max(self.getLeftChildIndex(currentIndex), self.getRightChildIndex(currentIndex))

            # If the current index (parent) is greater than the maximum child node, then we're good, so break out of loop
            if self.heapList[currentIndex] > self.heapList[biggerChildIndex]:
                break
            # If not, swap parent (current) to child
            else:
                self.swap(currentIndex, biggerChildIndex)

            # After swapping, set the current index to the index of where the smallest child used to be
            currentIndex = biggerChildIndex




    ## Remove max (root) element, rearrange to conform with heap property (max in this case) & return list
    def heapPop(self):
        if self.heapList_length == 0:
            return "Heap is completely empty"
        
        # Setting the max (root) value in the list to the last element in the list
        self.heapList[0] = self.heapList[self.heapList_length - 1]

        # Remove last element to avoid a duplicate element
        self.heapList.pop()

        # Manually decrease the length of the list
        self.heapList_length -= 1

        # Rearrange heap list to follow the order of a binary heap ("heap property") after removing min (root) element
        self.maxHeapifyPop()

        # return the updated list
        return self.heapList


    # Add new element at the end of the list, rearrange to conform with heap property (max in this case)
    def heapPush(self, item):
        # Add new element to the very end of the list
        self.heapList.append(item)

        # Manually increase the length of the list
        self.heapList_length += 1

        # Rearrange heap list to follow the order of a binary heap ("heap property") after adding a new element at the end
        self.maxHeapifyPush()


    # Invokes heapPush but will allow you to pass in a pre-populated list
    def heapPushList(self, list):
        for item in list:
            self.heapPush(item)

        return "Added " + str(len(list)) + " elements to the min heap tree/list"




    # Return heap list elements
    def __repr__(self):
        display_list = []

        for item in self.heapList:
            display_list.append(str(item))

        return " ".join(display_list)

        
        
        
    

heap2 = MaxHeap()


ls = [1,2,3,4,5]

heap2.heapPushList(ls)


print(heap2)