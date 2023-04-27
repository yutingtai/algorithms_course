class TreeNode:
    def __init__(self, value=0):
        self.value = value
        self.left: None | TreeNode = None
        self.right: None | TreeNode = None
        self.parent: None | TreeNode = None

    def is_left_child(self):
        return self.parent.left == self

    def is_right_child(self):
        return self.parent.right == self

    def has_two_child(self):
        return self.left and self.right

    def has_left_child(self):
        return self.left and self.right is None

    def has_right_child(self):
        return self.right and self.left is None

    def is_leaf_node(self):
        return self.left is None and self.right is None


def print_in_order(node: TreeNode):
    if node and node.left:
        print_in_order(node.left)
    print(node.value, end=" ")
    if node and node.right:
        print_in_order(node.right)


def print_pre_order(node: TreeNode):
    if node:
        print(node.value, end=" ")
    if node and node.left:
        print_pre_order(node.left)
    if node and node.right:
        print_pre_order(node.right)


def print_post_order(node: TreeNode):
    if node and node.left:
        print_pre_order(node.left)
    if node and node.right:
        print_pre_order(node.right)
    print(node.value, end=" ")


def find_successor(node: TreeNode):
    if node and node.right:
        head = node.right
        while head.left:
            head = head.left
    else:
        head = None
    return head


def find_predecessor(node: TreeNode):
    if node and node.left:
        head = node.left
        while head.right:
            head = head.right
    else:
        head = None
    return head


def insert_node(node: TreeNode, val: int):
    head = node
    if val < head.value and head.left is None:
        new_node = TreeNode(value=val)
        new_node.parent = head
        head.left = new_node
    elif val < head.value:
        insert_node(head.left, val)

    elif val > head.value and head.right is None:
        new_node = TreeNode(value=val)
        new_node.parent = head
        head.right = new_node

    elif val > head.value:
        insert_node(head.right, val)


def main():
    one = TreeNode(value=10)
    two = TreeNode(value=20)
    three = TreeNode(value=30)
    four = TreeNode(value=40)
    five = TreeNode(value=50)
    six = TreeNode(value=60)
    seven = TreeNode(value=70)
    eight = TreeNode(value=80)
    nine = TreeNode(value=90)
    ten = TreeNode(value=100)

    root = five
    root.left = three
    three.left = two
    three.right = four
    two.left = one

    root.right = seven
    seven.right = nine
    seven.left = six
    nine.left = eight
    nine.right = ten

    three.parent = five
    two.parent = three
    one.parent = two
    four.parent = three
    six.parent = seven
    nine.parent = six
    seven.parent = five
    eight.parent = nine
    ten.parent = nine

    print_in_order(root)
    print()
    print_pre_order(root)
    print()
    print_post_order(root)
    print()
    insert_node(root, 11)
    print_in_order(root)
    # print(find_predecessor(five).value)
    # print()
    # print(two)
    # print()
    # print(find_the_node(root, 20))
    # print()
    # insert(root, 21)
    # root.print_in_order()
    # insert(root, 28)
    # print()
    # root.print_in_order()
    # print()


if __name__ == '__main__':
    main()
