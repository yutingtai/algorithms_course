class Node:
    def __init__(self):
        self.item = 0
        self.next: None | Node = None

    def print_list(self):
        print(self.item, end=" ")
        if self.next is not None:
            self.next.print_list()

    def remove_next(self):
        self.next = self.next.next

    def insert_next(self, el: int):
        new_node = Node()
        new_node.item = el
        new_node.next = self.next
        self.next = new_node

    def print_reverse(self):
        if self.next is None:
            print(self.item, end=" ")
        else:
            self.next.print_reverse()
            print(self.item, end=" ")

    def reverse(self):
        if self.next is None:
            return self
        else:
            end = self.next.reverse()
            self.next.next = self
            self.next = None
            return end

    def append_el(self, el: int):
        if self.next is None:
            new_node = Node()
            new_node.item = el
            self.next = new_node
        else:
            self.next.append_el(el)

    def pop_el(self):
        if self.next.next is None:
            self.next = None
        else:
            self.next.pop_el()

    def get_item(self, index: int):
        return self.item if index == 0 else self.next.get_item(index - 1)


def remove_duplicates(node: Node):
    target = node
    while target is not None:
        pointer = target.next
        delete_pt = target
        while pointer is not None:
            if target.item == pointer.item:
                delete_pt.next = delete_pt.next.next
                pointer = pointer.next
            else:
                pointer = pointer.next
                delete_pt = delete_pt.next
        target = target.next


def main():
    one = Node()
    one.item = 1
    two = Node()
    two.item = 2
    three = Node()
    three.item = 3
    four = Node()
    four.item = 4
    five = Node()
    five.item = 5
    one.next = two
    two.next = three
    three.next = four
    four.next = five
    # one.print_list()
    # print('<--------- created list and printed it -----------')
    # one.remove_next()
    # one.print_list()
    # one.insert_next(2)
    # one.print_list()
    print('<------ removed element 2 and inserted back -----------')
    # one.print_reverse()
    # print('<------ print reverse list -----------')
    one.append_el(12)
    two.insert_next(12)
    # two.insert_next(5)
    # three.append_el(7)
    four.insert_next(7)
    # one.print_list()
    # print('<------ append and pop -----------')
    # one.remove_duplicates()
    # one.print_list()
    print()
    print('<------ remove duplicate -----------')
    one.print_list()
    print()
    remove_duplicates(one)
    one.print_list()
    # print()


if __name__ == '__main__':
    main()
