class TreeNode:
    def __init__(self):
        self.value = 0
        self.right: TreeNode | None = None
        self.left: TreeNode | None = None
        self.parent: TreeNode | None = None

    def is_root(self):
        return self.parent is None

    def is_left_child(self):
        if self.parent.left == self:
            return True

    def is_right_child(self):
        if self.parent.right == self:
            return True

    def has_no_children(self):
        return self.left is None and self.right is None

    def has_two_children(self):
        return self.left and self.right

    def print_tree_in_order(self):
        if self.left:
            self.left.print_tree_in_order()
        print(self.value, end=" ")
        if self.right:
            self.right.print_tree_in_order()

    def successor(self):
        head = self.right
        while head.left is not None:
            head = head.left
        return head

    def predecessor(self):
        head = self.left
        while head.right is not None:
            head = head.right
        return head


def insert_node(node: TreeNode, target: int):
    head = node
    if target < head.value and head.left is None:
        new_node_to_insert = TreeNode()
        new_node_to_insert.value = target
        new_node_to_insert.parent = head
        head.left = new_node_to_insert

    elif target < head.value and head.left:
        head = head.left
        insert_node(head, target)
    elif target > head.value and head.right is None:
        new_node_to_insert = TreeNode()
        new_node_to_insert.value = target
        new_node_to_insert.parent = head
        head.right = new_node_to_insert
    elif target > head.value and head.right:
        head = head.right
        insert_node(head, target)


def find_the_el(node: TreeNode, target: int):
    current_node = node
    while current_node.left is not None or current_node.right is not None:
        if target > current_node.value and current_node.right:
            current_node = current_node.right
        elif target < current_node.value and current_node.left:
            current_node = current_node.left
        elif current_node.value == target:
            return current_node


def delete(node: TreeNode, target: int):
    target_node = find_the_el(node, target)
    if target_node is None:
        return "this node is not in this tree"

    elif target_node.has_no_children():
        if target_node.is_left_child():
            target_node.parent.left = None
        elif target_node.is_right_child():
            target_node.parent.right = None

    elif target_node.left and target_node.right:
        p_node = target_node.predecessor()
        delete(p_node.parent, p_node.value)
        target_node.value = p_node.value

    elif target_node.left and target_node.is_left_child():
        target_node.parent.left = target_node.left
    elif target_node.left and target_node.is_right_child():
        target_node.parent.right = target_node.left
    elif target_node.right and target_node.is_right_child():
        target_node.parent.right = target_node.right
    elif target_node.right and target_node.is_left_child():
        target_node.parent.left = target_node.right


def main():
    one = TreeNode()
    one.value = 10
    two = TreeNode()
    two.value = 20
    three = TreeNode()
    three.value = 30
    four = TreeNode()
    four.value = 40
    five = TreeNode()
    five.value = 50
    six = TreeNode()
    six.value = 60
    root = three
    root.left = two
    two.left = one
    root.right = five
    five.left = four
    five.right = six
    one.parent = two
    two.parent = root
    four.parent = five
    five.parent = root
    six.parent = five

    # root.print_tree_in_order()
    # print()
    # insert_node(root,55)
    # root.print_tree_in_order()
    # print()
    # delete(root, 20)
    # print()

    print(find_the_el(root,23).value)


if __name__ == '__main__':
    main()
