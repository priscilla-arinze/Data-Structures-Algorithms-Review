class Node:
    def __init__(self, data):  
        self.data = data
        self.left = None # less than parent & ancestor nodes
        self.right = None # greater than parent & ancestor nodes




class BinarySearchTree:
    ## Constructor
    def __init__(self):
        self.root = None
        self.current = self.root # will always start at the root node initially



    ## Checks to see if binary tree is completely empty (no root)
    def is_empty(self):
        return self.root == None



    ## Return root of tree
    def getRoot(self):
        return self.root



    #### BRAINSTORMING ADDITIONAL METHODS ####

    ## Check depth of node or tree
    #def depth(self,):

    
    ## Get path of search
    #def searchPath(self,)



    # reset the current node instance variable to the root variable
    def resetCurrentNode(self):
        self.current = self.root


    ## Insert new nodes in tree; needs to be tested w/ self.current
    def insert(self, data):

        # If tree is completely empty (no root), set the root node to the new node
        if self.is_empty():
            self.root = Node(data)
        
        # If there are already nodes in the trees (Each node need to be put in a SPECIFIC position in a BST)
        # Reminder: Left is less than, Right is greater than
        else:

            # If LESS THAN current node (LEFT SIDE)
            if data < self.current.data:
                # If there left child node is None, than insert new node there
                if self.current.left == None:
                    self.current.left = Node(data)

                # RECURSION: If a left child node already exists, invoke the same insert() method recursively until
                # there is an empty left child node
                # Also, set current to the left node
                else:
                    self.current = self.current.left
                    self.insert(data)


            # DUPLICATES (lazy implementation)
            # If EQUAL TO current node (LEFT or RIGHT if null; OR continue traversal until you find an empty spot)
            elif data == self.current.data:
                # If there left child node is None, than insert new node there
                if self.current.left == None:
                    self.current.left = Node(data)
                
                # If there right child node is None, than insert new node there
                elif self.current.right == None:
                    self.current.right = Node(data)
                
                # If no empty spots to insert at current node, then continue traversing through tree until you find an empty spot to insert
                # Duplicate nodes will skew to the left in this implementation, trying to align with complete binary tree definition
                else:
                    self.current = self.current.left
                    self.insert(data)


            # If GREATER THAN current node (RIGHT SIDE)
            else:
                # If there right child node is None, than insert new node there
                if self.current.right == None:
                    self.current.right = Node(data)

                # RECURSION: If a right child node already exists, invoke the same insert() method recursively until
                # there is an empty right child node
                # Also, set current to the right node
                else:
                    self.current = self.current.right
                    self.insert(data)



        # Revert self.current back to root node when finished
        self.resetCurrentNode()



    # Returns a boolean if a given node exists in the tree or not
    def contains(self, data):

        # Will either remain False (completely empty tree) OR become True if node exists
        returnstmt = False
        

        # If the tree is NOT completely empty OR if you haven't reached a NULL node, continue loop
        while self.current != None:

            # If the given node is equal to the current (root) node, then return True
            if data == self.current.data:
                returnstmt = True
                break



            # If LESS THAN current node (LEFT SIDE)
            elif data < self.current.data:
                # If there left child node is None, than return True
                if data == self.current.left.data:
                    returnstmt = True
                    break

                # Since BSTs have their nodes put in a specific ordered position, if the given node has not been found yet 
                # AND it is GREATER THAN the left child node of the current node,
                # then there is no point in searching anymore because the more left you go, the lesser the numbers become
                elif data > self.current.left.data:
                    returnstmt = False
                    break

                # If the current left child node does not equal the given node AND it is not GREATER THAN the left child node, 
                # set current node to the left child node & continue while loop
                else:
                    self.current = self.current.left



            # If GREATER THAN current node (RIGHT SIDE)
            else:
                # If the right child node is None, then return True
                if data == self.current.right.data:
                    returnstmt = True
                    break

                # Since BSTs have their nodes put in a specific ordered position, if the given node has not been found yet 
                # AND it is LESS THAN the right child node of the current node,
                # then there is no point in searching anymore because the more right you go, the greater the numbers become
                elif data < self.current.right.data:
                    returnstmt = False
                    break

                # If the current right child node does not equal the given node AND it is not GREATER THAN the left child node, 
                # set current node to the right child node & continue while loop
                else:
                    self.current = self.current.right
        

        try:  
            # Revert self.current back to root node when finished
            self.resetCurrentNode() # EXECUTE THIS LAST
        finally:
            return returnstmt # EXECUTE THIS FIRST




    ## Returns node object based on a given number that exists inside tree
    def getNode(self, data):

        # Will either remain False OR will return the current node object
        returnstmt = False

        # If the tree is NOT completely empty OR if you haven't reached a NULL node, continue loop
        while self.current != None:

            # If the given node is equal to the current (root) node, then return True
            if data == self.current.data:
                returnstmt = self.current
                break



            # If LESS THAN current node (LEFT SIDE)
            elif data < self.current.data:

                # If the given number is equal to the number in the left child node, then return left child node object
                if data == self.current.left.data:
                    returnstmt = self.current.left
                    break

                # Similar to login in contains(); return False if node doesn't exist
                elif data > self.current.left.data:
                    returnstmt = "Either node doesn't exist or the binary search tree is invalid"
                    break

                # If the current left child node does not equal the given node, then set current node to the left child node & continue while loop
                else:
                    self.current = self.current.left



            # If GREATER THAN current node (RIGHT SIDE)
            else:
                # If the given number is equal to the number in the right child node, then return right child node object
                if self.current.right.data == data:
                    returnstmt = self.current.right
                    break

                # Since BSTs have their nodes put in a specific ordered position, if the given node has not been found yet 
                # AND it is LESS THAN the right child node of the current node,
                # then there is no point in searching anymore because the more right you go, the greater the numbers become
                elif data < self.current.right.data:
                    returnstmt = "Either node doesn't exist or the binary search tree is invalid"
                    break


                # If the current right child node does not equal the given node, then set current node to the right child node & continue while loop
                else:
                    self.current = self.current.right
        

        try:  
            # Revert self.current back to root node when finished
            self.resetCurrentNode() # EXECUTE THIS LAST
        finally:
            return returnstmt # EXECUTE THIS FIRST



    ## Retrieve parent (root) node of a specified node
    def getParentNode(self, data):

        # If the node doesn't exist or if the tree is completely empty, then return the following statement
        # Will NOT execute while loop at all if given number does not exist in the tree
        if self.contains(data) != True:
            return "This node does not exist in the tree."


        # Initialize parent node to be none in case user requests parent of root node
        # Serves as reference to the previous node as we traverse
        parentNode = None

        # Initialize a temp current node (set to the root node) in order to be able to save the previous node in parentNode rather than continually pointing to the same self.current reference
        # Also, to avoid having to reset self.current back to self.root
        tempCurrent = self.root


        # If the tree is NOT completely empty OR if you haven't reached a NULL node, continue loop
        while tempCurrent != None:

            # If the given node is equal to the current (root) node, then return True
            if data == tempCurrent.data:
                break


            # If LESS THAN current node (LEFT SIDE)
            elif data < tempCurrent.data:

                parentNode = tempCurrent

                # If the given number is equal to the number in the left child node, then return left child node object
                if data == tempCurrent.left.data:
                    break

                # If the current left child node does not equal the given node, then set current node to the left child node & continue while loop
                else:
                    tempCurrent = tempCurrent.left



            # If GREATER THAN current node (RIGHT SIDE)
            else:

                parentNode = tempCurrent

                # If the given number is equal to the number in the right child node, then return right child node object
                if tempCurrent.right.data == data:
                    break


                # If the current right child node does not equal the given node, then set current node to the right child node & continue while loop
                else:
                    tempCurrent = tempCurrent.right
        

        
        return parentNode



    ## Print tree nodes in the order of LEFT --> ROOT --> RIGHT
    def printInorder(self, rootNode):

        # If rootNode is None, then return nothing (to avoid a NoneType error) and move back up the recursive function in the call stack
        if rootNode == None:
            return
    
        
        # Start by recursively going to all of the leftmost nodes of the root node (w/o printing them out just yet)
        # Then start the Inorder traversal process once you reach the left/bottom-most node in tree
        self.printInorder(rootNode.left)

        # Then start off by printing out the left/bottom-most node in tree
        print(rootNode.data, end = ", ") # "VISIT" NODE   

        # Then when finished with above, got to all the rightmost nodes & print them out
        self.printInorder(rootNode.right)




    ## Print tree nodes in the order of ROOT --> LEFT --> RIGHT
    def printPreorder(self, rootNode):

        # If rootNode is None, then return nothing (to avoid a NoneType error) and move back up the recursive function in the call stack
        if rootNode == None:
            return
    
    
        # Start to print the root node
        print(rootNode.data, end = ", ") # "VISIT" NODE

        # Then recursively go to all of the leftmost nodes of the root node & print them out
        self.printPreorder(rootNode.left)

        # Then when finished with above, got to all the rightmost nodes & print them out
        self.printPreorder(rootNode.right)



 
    ## Print tree nodes in the order of LEFT --> RIGHT --> ROOT
    def printPostorder(self, rootNode):

        # If rootNode is None, then return nothing (to avoid a NoneType error) and move back up the tree with the recursive function in the call stack
        if rootNode == None:
            return
    

        # Start by recursively going to all of the leftmost nodes of the root node (w/o printing them out just yet)
        # Then start the Postorder traversal process once you reach the left/bottom-most node in tree
        self.printPostorder(rootNode.left)

        # Then when finished with above recursion, go to all of the rightmost nodes of the root node (w/o printing them out just yet)
        self.printPostorder(rootNode.right)

        # Print in the following traversal order: LEFT --> RIGHT --> ROOT
        # So main root of tree will be the very last item in list
        print(rootNode.data, end = ", ") # "VISIT" NODE

    


    ## Print out all the leaves of the tree (bottom-most nodes)
    def printLeafNodes(self, rootNode):

        # If rootNode is None, then return nothing (to avoid a NoneType error) and move back up the recursive function in the call stack
        if rootNode == None:
            return

        # If there is no children on the current node, then print the current node
        if (rootNode.left == None and rootNode.right == None):
            print(rootNode.data, end = ", ")  
            return 
        
        # Start by recursively going to all of the leftmost nodes of the root node (w/o printing them out just yet)
        # Then start the Inorder traversal process once you reach the left/bottom-most node in tree
        if rootNode.left != None:
            self.printLeafNodes(rootNode.left)

        # Then do the same for the right nodes
        if rootNode.right != None:
            self.printLeafNodes(rootNode.right)



    ## Get the minimum value node (leftmost node)
    def getMinNode(self):
        minNode = 0

        if self.is_empty():
            return "Tree is completely empty."

        while self.current != None:
            minNode = self.current.data

            if self.current.left == None:
                self.resetCurrentNode() # reset to self.root
                return minNode


            self.current = self.current.left




    ## Get the maximum value node (rightmost node)
    def getMaxNode(self):
        maxNode = 0

        if self.is_empty():
            return "Tree is completely empty."

        while self.current != None:
            maxNode = self.current.data

            if self.current.right == None:
                self.resetCurrentNode() # reset to self.root
                return maxNode


            self.current = self.current.right


        
    ## Get the height of the tree (using root node) or of a specified given node
        # Time Complexity of entire tree (use root as givenNode): O(n)
        # Time Complexity for a specific node: 
            # Using getNode(), allowing users to only pass in a number:  O(n + log(n)) --> getHeight(): n, getNode(): log(n)
            # Hard-coded Node object being passed in: O(n)
    def getHeight(self, givenNode):
        
        # height is calculated from top (root) to bottom (node or bottommost leaf node)
        if givenNode == None:
            # since the height of leaf nodes are 0, they should not be included in the height count
            # so once you reach the leaf node, you will need to return -1 instead of 0 so that the leaf node won't be counted
            return -1


        # Utilize VS Code debugger to understand the recursive flow if forgotten

        # START by going to the leftmost subtree (or leftmost leaf node), reaching base case of a null left child node & returning -1 for the left edge
        leftside = self.getHeight(givenNode.left)
        # THEN when finished with leftside of leftmost subtree, go back up to node, then reach base care of a null RIGHT child node & return -1 for the right edge
        rightside = self.getHeight(givenNode.right)

        # Once finished with leftside & rightside for each subtree/node, execute the below return for height of that node
        return max(leftside, rightside) + 1

        # Do the above three lines for each subtree/node as you go up the tree in the recursive call stack



    # Level = Depth
    # Will print out the nodes in each level from left to right
    def printCurrentLevel(self, rootNode, level):
        if rootNode is None:
            return

        # Each node will be treated as a root node (from left to right as the recursion functions show below)
        # once the "root node" is reached and the level is set to 1, the node will print out
        if level == 0:
           print(rootNode.data, end = " ")

        elif level > 0:
            self.printCurrentLevel(rootNode.left, level-1)
            self.printCurrentLevel(rootNode.right, level-1)


    # For each level in a tree, this method executes printCurrentLevel()
    def printLevelOrder(self, rootNode):
        if self.is_empty() == True:
            return "The tree is completely empty."

        h = self.getHeight(self.getRoot())

        # e.g. Root node is level 0, bottom most leaf nodes are level 3 (flipped compared to tree height)
        # So range of 0 to 4(NON-INCLUSIVE)
        for i in range(0, h+1):
            # e.g. 4 levels; so root 10 will be passed in for each level: (10, 1), (10, 2), etc...
            # Level number will count down as you go down the tree, level by level
            self.printCurrentLevel(rootNode, i)



    # Main BSTValidation (utility) method that does all the work & comparisons
    def BSTValidationUtil(self, rootNode, minValue, maxValue):
        if rootNode == None:
            return True

        # maxValue is represented as positive infinity
        # minValue is represented as negative infinity

        # Using infinity (- & +) as the min and max values respectively,
            # 1st: make sure that the MAIN root node is GREATER than -infinity AND LESS than +infinity

            # 2nd: recur the function and pass in the LEFT node as the root node, keeping minValue at -infinity
                # SUMMARY: -infinity (don't replace) < LEFT (CURRENT) NODE < RECENT ROOT NODE or MAIN ROOT NODE (see IMPORTANT NOTE below)
                # IMPORTANT NOTE: the ENTIRE left subtree of the main root node will be contained in the FIRST recursive function,
                    # Therefore, WITHIN this first recursive function:
                        # if any of the sub-left trees go to the RIGHT node (2nd recursive function), DEFAULT maxValue will be the main root node (e.g. 10)
                        # if any of the sub-left trees go to the LEFT node (1st recursive function), maxValue will change to the most recent root node
                # Do this until you reach the base case (NULL left node), then move back up the tree

            # 3rd: Once finished with the left side of a node, pass in the RIGHT node as the root node, keeping maxValue at +infinity
                # SUMMARY: RECENT ROOT NODE or MAIN ROOT NODE (see IMPORTANT NOTE below) < RIGHT (CURRENT) NODE  < +infinity (don't replace)
                # IMPORTANT NOTE: the ENTIRE right subtree of the main root node will be contained in the SECOND recursive function,
                    # Therefore, WITHIN this second recursive function:
                        # if any of the sub-right trees go to the LEFT node (1st recursive function), DEFAULT minValue will be the main root node (e.g. 10)
                        # if any of the sub-right trees go to the RIGHT node (1st recursive function), minValue will change to the most recent root node
                # Do this until you reach the base case (NULL right node), then move back up the tree
        if(rootNode.data > minValue and rootNode.data < maxValue 
            and self.BSTValidationUtil(rootNode.left, minValue, rootNode.data) 
            and self.BSTValidationUtil(rootNode.right, rootNode.data, maxValue)):
            return True

        else:
            return False

    # Method that invokes BSTValidationUtil() so the user doesn't have to pass in any arguments when calling this method
    def BSTValidation(self):
        return self.BSTValidationUtil(self.getRoot(), float("-inf"), float("inf"))




    ## Retrieves the node that comes AFTER the specified node in numerical order
    def inOrderSuccessor(self, data):
        successor = None

        currentTemp = self.root

        while currentTemp != None:
            if data >= currentTemp.data:
                currentTemp = currentTemp.right
            
            else:
                successor = currentTemp
                currentTemp = currentTemp.left
        
        return successor

    ## Retrieves the node that comes BEFORE the specified node in numerical order
    def inOrderPredecessor(self, data):
        predecessor = None

        currentTemp = self.root

        while currentTemp != None:
            if data <= currentTemp.data:
                currentTemp = currentTemp.left
            
            else:
                predecessor = currentTemp
                currentTemp = currentTemp.right
        
        return predecessor




    # Looks for the lowest value in the right sub tree of the node you want to delete
    # Will keep going left until there are no more left nodes
    # The last non-NULL left node will be the new root --> to replace the node you want to delete
    def deleteNode_minValueNode(self, givenNode):
        currentTemp = givenNode
    
        while currentTemp.left != None:
            currentTemp = currentTemp.left
    
        return currentTemp

    # Main utility function that removes a node from tree and reorganizes any child nodes if any
    def deleteNodeUtil(self, rootNode, data):

        if rootNode == None:
            return rootNode
    

        # See whether node is within LEFT subtree (LESS than root)
        if data < rootNode.data:
            rootNode.left = self.deleteNodeUtil(rootNode.left, data)
    
        # See whether node is within RIGHT subtree (GREATER than root)
        elif(data > rootNode.data):
            rootNode.right = self.deleteNodeUtil(rootNode.right, data)
    


        # Once we reach the node we want to delete:
        else:
            
            # CASE 1: Leaf node (no children) --> easiest; just make the node NULL
            if rootNode.left == None and rootNode.right == None:
                rootNode = None
                
            # CASE 2: Node with one child --> slightly harder; replace the parent's current child (about to be deleted) with the deleted node's child
            elif rootNode.left == None:
                temp = rootNode.right
                rootNode = None
                return temp
    
            elif rootNode.right == None:
                temp = rootNode.left
                rootNode = None
                return temp
    
            # CASE 3: Node with two children --> hardest; will need to replace the node with the lowest number in the right subtree
                # Then, you'll need to remove the duplicate leaf lowest right sub tree node after replacing node
            else:
                # Looks for the lowest value (LEAF NODE) in the right sub tree of the node you want to delete
                temp = self.deleteNode_minValueNode(rootNode.right)
        
                # Keeping the same memory address as the node you want to delete, but changing the data (number) within the node object
                # This will result in a temporarily duplicate node values (newly changed current root node & temp variable)
                rootNode.data = temp.data
        
                # Reminder: We kept the same memory address for the node we "replaced", so therefore the left and right child nodes are still in tact
                # Remove duplicate node value (leaf node)
                rootNode.right = self.deleteNodeUtil(rootNode.right, temp.data)
    
        return rootNode
                  

    # Allows you to invoke the main delete utility function without having to pass in the root
    # you only need to pass in the data you want to delete
    def deleteNode(self, data):
        return self.deleteNodeUtil(self.root, data)




    # String representation of tree (in order list):
    def __repr__(self):
        # For some reason (probably because printInorder() is printing values & not returning),
        # there was an extra 'None' printing at the end of the list of tree nodes
        
        # So below was the way to avoid the extra None:
        print("List of tree nodes in order: ", end="")
        self.printInorder(self.getRoot())

        return ""