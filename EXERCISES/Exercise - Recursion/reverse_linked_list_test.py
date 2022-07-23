# Custom LinkedList import
from DS_LinkedList import LinkedList



def reverse(linked_list, node):
    if node == None or node.next_node == None:
        return node
    
    # Will execute this line until it reaches the last recursion, sets the final recursion value to "temp_tail" (last node in original list)
    temp_tail = reverse(linked_list, node.next_node)

    # NOTE: node variable is set to the node before the very last node ("temp tail" variable)

    # Update the current node's pointer to 2 nodes ahead 
    # e.g. move 4 at the end, [1->-2->3->4->5] ---> [5-X 1->2->3->4]; see visualiation)
    node.next_node.next_node = node

    linked_list.head = temp_tail

    node.next_node = None


    print("Linked list:", linked_list)

    
    return temp_tail




def print_linked_list(node):
    tmp = node

    while tmp != None:
        print(tmp.data, " ")

        tmp = tmp.next_node


ls = LinkedList()

ls.append_item(10)
ls.append_item(20)
ls.append_item(30)
ls.append_item(40)
ls.append_item(50)
ls.append_item(60)

#ls


# still using ls linkedlist from above

reversed_ls2 = reverse(ls, ls.head)

reversed_ls2

print(ls)

print_linked_list(ls.head)