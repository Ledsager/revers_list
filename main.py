# 1. Необходимо реализовать метод разворота связного списка (двухсвязного или односвязного на выбор).
# 2. Реализовать сортировку пузырьком для двухсвязного списка

class Node:
    def __init__(self, data):
        self.next = None
        self.prev = None
        self.data = data


class List_2:
    def __init__(self):
        self.start_node = None

    def print_l(self):
        n = self.start_node
        while n is not None:
            print(n.data, end=' ')
            n = n.next
            print()

    def insert_start(self, data):
        new_node = Node(data)
        if self.start_node is None:
            self.start_node = new_node
            return
        new_node.next = self.start_node
        self.start_node.prev = new_node
        self.start_node = new_node

    def insert_end(self, data):
        new_node = Node(data)
        if self.start_node is None:
            self.start_node = new_node
            return

        n = self.start_node
        while n.next:
            n = n.next

        n.next = new_node
        new_node.prev = n

    def delete_start(self):
        if self.start_node is None:
            print("no element")
            return
        if self.start_node.next is None:
            self.start_node = None
            return

        self.start_node = self.start_node.next
        self.start_node.prev = None

    def delete_end(self):
        if self.start_node is None:
            print("no element")
            return
        if self.start_node.next is None:
            self.start_node = None
            return
        n = self.start_node
        while n.next.next is not None:
            n = n.next
        n.next = None

    def search(self, x):
        n = self.start_node
        while n is not None:
            if n.data == x:
                print("+")
                return
            n = n.next
        print("-")

    def revert(self):
        temp = None
        n = self.start_node

        while (n is not None):
            temp = n.prev
            n.prev = n.next
            n.next = temp
            n = n.prev
        if (temp is not None):
            self.start_node = temp.prev

    def sort_bbubl(self):
        swapped = 0
        temp = None

        if self.start_node is None:
            print("no element")
            return

        while True:
            swapped = 0
            # ptr1 = start
            n = self.start_node
            while (n.next != temp):
                if (n.data > n.next.data):
                    n.data, n.next.data = n.next.data, n.data
                    swapped = 1
                n = n.next
            temp = n
            if swapped == 0:
                break
            


l2 = List_2()
l2.delete_start()
l2.insert_start(2)
l2.insert_start(25)
l2.insert_end(3)
l2.insert_end(15)
l2.print_l()
l2.search(4)
l2.revert()
l2.print_l()
l2.sort_bbubl()
l2.print_l()
