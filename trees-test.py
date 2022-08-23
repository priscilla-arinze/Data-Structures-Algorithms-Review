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
    ## Checks height of node or tree
    #def height(self,):

    ## Check depth of node or tree
    #def depth(self,):

    ## Print out string representation of tree ???
    #def __repr__(self):

    ## Get parent of current node
    #def getParent(self):

    ## Get children for parent node (will help determine if node is a leaf node)
    #def getParent(self):

    ## Get sibling (left or right or NULL)
    #def getSibling(self):

    ## Search specific node
        # Return height, depth, parent and value of this node (might need to separate)
    #def search(self,):
    
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

                # If the current left child node does not equal the given node 
                # AND it is not GREATER THAN the left child node, 
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

                # RECURSION: If the current right child node does not equal the given node AND it is not LESS THAN the right child node, 
                # invoke the same contains() method recursively until either condition becomes true
                # Also, set current to the right node
                else:
                    self.current = self.current.right
        

        try:  
            # Revert self.current back to root node when finished
            self.resetCurrentNode() # EXECUTE THIS LAST
        finally:
            return returnstmt # EXECUTE THIS FIRST




    ## Returns node object based on a given number that exists inside tree
    def getNode(self, data):

        # If the node doesn't exist or if the tree is completely empty, then return False
        # Will NOT execute while loop at all if given number does not exist in the tree
        if self.contains(data) != True:
            return False


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

                # If the current left child node does not equal the given node, then set current node to the left child node & continue while loop
                else:
                    self.current = self.current.left



            # If GREATER THAN current node (RIGHT SIDE)
            else:
                # If the given number is equal to the number in the right child node, then return right child node object
                if self.current.right.data == data:
                    returnstmt = self.current.right
                    break


                # If the current right child node does not equal the given node, then set current node to the right child node & continue while loop
                else:
                    self.current = self.current.right
        

        try:  
            # Revert self.current back to root node when finished
            self.resetCurrentNode() # EXECUTE THIS LAST
        finally:
            return returnstmt # EXECUTE THIS FIRST






    ## Print tree nodes in the order of LEFT --> ROOT --> RIGHT
    def printInorder(self, rootNode):

        # If rootNode is None, then return nothing (to avoid a NoneType error) and move back up the recursive function in the call stack
        if rootNode == None:
            return
    
        
        # Start by recursively going to all of the leftmost nodes of the root node (w/o printing them out just yet)
        # Then start the Inorder traversal process once you reach the left/bottom-most node in tree
        self.printInorder(rootNode.left)

        # Then start off by printing out the left/bottom-most node in tree
        print(rootNode.data, end = ", ")    

        # Then when finished with above, got to all the rightmost nodes & print them out
        self.printInorder(rootNode.right)




    ## Print tree nodes in the order of ROOT --> LEFT --> RIGHT
    def printPreorder(self, rootNode):

        # If rootNode is None, then return nothing (to avoid a NoneType error) and move back up the recursive function in the call stack
        if rootNode == None:
            return
    
    
        # Start to print the root node
        print(rootNode.data, end = ", ")

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
        print(rootNode.data, end = ", ")

    


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
                self.resetCurrentNode()
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
                self.resetCurrentNode()
                return maxNode


            self.current = self.current.right


        
    ## Get the height of the tree (using root node) or of a specified given node
    def getHeight(self, givenNode):

        # height is calculated from top (root) to bottom (node or bottommost leaf node)
        if givenNode == None:
            # since the height of leaf nodes are 0, they should not be included in the height count
            # so once you reach the leaf node, you will need to return -1 instead of 0 so that the leaf node won't be counted
            return -1

        leftside = self.getHeight(givenNode.left)
        rightside = self.getHeight(givenNode.right)

        return max(leftside, rightside) + 1





tree1 = BinarySearchTree()

tree1.insert(10)
tree1.insert(9)
tree1.insert(16)
#tree1.insert(5)
tree1.insert(5)
tree1.insert(6)
tree1.insert(11)
tree1.insert(18)
tree1.insert(3)
tree1.insert(25)


print(tree1.getHeight(tree1.getNode(10)))