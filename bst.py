import random
from queue_and_stack import Queue, Stack


class BSTNode:
    def __init__(self, value: object) -> None:
        self.value = value  # to store node's data
        self.left = None  # pointer to root of left subtree
        self.right = None  # pointer to root of right subtree

    def __str__(self) -> str:
        return 'BST Node: {}'.format(self.value)


class BST:
    """
    Binary Search Tree class
    """

    def __init__(self, start_tree=None) -> None:
        """
        Initialize new Binary Search Tree
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._root = None

        # populate BST with initial values (if provided)
        # before using this feature, implement add() method
        if start_tree is not None:
            for value in start_tree:
                self.add(value)

    def __str__(self) -> str:
        """
        Override string method; display in pre-order
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        values = []
        self._str_helper(self._root, values)
        return "BST pre-order { " + ", ".join(values) + " }"

    def _str_helper(self, node: BSTNode, values: []) -> None:
        """
        Helper method for __str__. Does pre-order tree traversal
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if not node:
            return
        values.append(str(node.value))
        self._str_helper(node.left, values)
        self._str_helper(node.right, values)

    def get_root(self) -> BSTNode:
        return self._root

    def is_valid_bst(self) -> bool:
        stack = Stack()
        stack.push(self._root)
        while not stack.is_empty():
            node = stack.pop()
            if node:
                if node.left and node.left.value >= node.value:
                    return False
                if node.right and node.right.value < node.value:
                    return False
                stack.push(node.right)
                stack.push(node.left)
        return True

    # ------------------------------------------------------------------ #

    def add(self, value: object) -> None:
        if node is None:
            return Node(data)
        else:
            if data < node.data:
                node.left = self._add(node.left, data)
            else:
                node.right = self._add(node.right, data)
            return node

    def remove(self, value: object) -> bool:
        data = value
        self.root = self._remove(self.root, data)

    def _remove(self, node, data):
        if node is None:
            return node
        if data == node.data:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                min_right = self._find_min(node.right)
                node.data = min_right.data
                node.right = self._remove(node.right, min_right.data)
        elif data < node.data:
            node.left = self._remove(node.left, data)
        else:
            node.right = self._remove(node.right, data)
        return node

    def _remove_no_subtrees(self, remove_parent: BSTNode, remove_node: BSTNode) -> None:
        self.root = self._remove_no_node(remove_parentt, remove_node)

    def _remove_no_node(self, root, key):
        if not root:
            return root
        elif key < root.key:
            root.left = self._remove_node(root.left, key)
        elif key > root.key:
            root.right = self._remove_node(root.right, key)
        else:
            if not root.left and not root.right:
                root = None
            elif not root.left:
                root = root.right
            elif not root.right:
                root = root.left
            else:
                temp = self.find_min(root.right)
                root.key = temp.key
                root.right = self._remove_node(root.right, temp.key)
        return root

    def _remove_one_subtree(self, remove_parent: BSTNode, remove_node: BSTNode) -> None:
        if remove_parent is None:
            return remove_parent

            # find the node to be removed and its parent node
        parent = None
        current = remove_parent
        while current is not None and current.data != data:
            parent = current
            if data < current.data:
                current = current.left
            else:
                current = current.right

        # node not found
        if current is None:
            return remove_parent

        # node has only left subtree
        if current.right is None:
            if parent is None:
                remove_parent = current.left
            elif parent.left == current:
                parent.left = current.left
            else:
                parent.right = current.left

        # node has only right subtree
        elif current.left is None:
            if parent is None:
                self.root = current.right
            elif parent.left == current:
                parent.left = current.right
            else:
                parent.right = current.right

        # node has both left and right subtrees
        else:
            successor_parent = current
            successor = current.right
            while successor.left is not None:
                successor_parent = successor
                successor = successor.left

            current.data = successor.data

            if successor_parent.left == successor:
                successor_parent.left = successor.right
            else:
                successor_parent.right = successor.right

        return remove_parent


def contains(self, value: object) -> bool:
    data = value
    return self._contains(self.root, data)


def _contains(self, node, data):
    if node is None:
        return False
    elif data == node.data:
        return True
    elif data < node.data:
        return self._contains(node.left, data)
    else:
        return self._contains(node.right, data)


def inorder_traversal(self) -> Queue:
    self._inorder_traversal(self.root)
    print()


def _inorder_traversal(self, node):
    if node is not None:
        self._inorder_traversal(node.left)
        print(node.data, end=" ")
        self._inorder_traversal(node.right)


def find_min(self) -> object:
    return self._find_min(self.root)


def _find_min(self, node):
    if node.left is None:
        return node
    else:
        return self._find_min(node.left)


def find_max(self) -> object:
    return self._find_max(self.root)


def _find_max(self, node):
    if node.right is None:
        return node
    else:
        return self._find_max(node.right)


def is_empty(self) -> bool:
    return self.root is None


def make_empty(self) -> None:
    self.root = None