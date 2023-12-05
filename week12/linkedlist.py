# how it works:
# each item is a Node
# each Node can only point to the next Node
# functions supported:
# you can create, append to the back, and remove a Node

# eg: 4, 6, 9, -10
# HEAD Node(4) --> Node(6) --> Node(9) --> Node(-10) TAIL

class Node:
    def __init__(self, data):
        self.data = data
        self.next: Node = None


class LinkedList:
    def __init__(self):
        self.head = None

    # add a node at the end of the chain
    def append(self, data):
        # create new node
        new_node = Node(data)
        # update the head if we don't have a head yet
        if not self.head:
            self.head = new_node
            return
        # if not, we traverse the list to find the tail, and append the new node there
        # last_node = self.head
        # while last_node.next:
        #     last_node = last_node.next
        # last_node.next = new_node

        # refactor to use tail computed property to make it better
        self.tail.next = new_node

    # computed tail property
    @property
    def tail(self):
        # find a tail
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        return last_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def remove(self, data):
        current = self.head
        # if the data you're looking for is the head, just chop it off, and then return
        if current and current.data == data:
            self.head = current.next
            return current  # return the removed Node  (depending on specs)

        prev = None
        while current and current.data != data:
            prev = current
            current = current.next
        if current is None:
            return
        prev.next = current.next
        return current  # return the removed node


linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)

linked_list.display()  # Output: 1 -> 2 -> 3 -> 4 -> None

linked_list.remove(3)
linked_list.display()  # Output: 1 -> 2 -> 4 -> None
print(linked_list.tail.data)
