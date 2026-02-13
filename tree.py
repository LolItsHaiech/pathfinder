class TNode:
    def __init__(self, value, parent=None):
        self.value = value
        self.right = None
        self.parent = parent
        self.child = None


class Tree:
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, value, parent_value=None):
        if self.root is None:
            self.root = TNode(value)
            self.size = 1
            return self.root

        parent_node = None
        if parent_value is None:
            parent_node = self.root
        else:
            parent_node = self.find(parent_value)
            if parent_node is None:
                raise ValueError(f"Parent node with value {parent_value} not found")

        new_node = TNode(value, parent_node)

        if parent_node.child is None:
            parent_node.child = new_node
        else:
            cur = parent_node.child
            while cur.right is not None:
                cur = cur.right
            cur.right = new_node

        self.size += 1
        return new_node

    def find(self, value, start_node=None):
        if start_node is None:
            start_node = self.root

        if start_node is None:
            return None

        if start_node.value == value:
            return start_node

        child = start_node.child
        while child is not None:
            result = self.find(value, child)
            if result is not None:
                return result
            child = child.right

        return None

    def remove(self, value):
        node = self.find(value)
        if node is None:
            return False

        if node == self.root:
            self.root = None
            self.size = 0
            return True

        parent = node.parent
        if parent.child == node:
            parent.child = node.right
        else:
            curr = parent.child
            while curr.right != node:
                curr = curr.right
            curr.right = node.right

        count = self._count_descendants(node) + 1
        self.size -= count
        return True

    def _count_descendants(self, node):
        if node is None:
            return 0

        count = 0
        child = node.child
        while child is not None:
            count += 1 + self._count_descendants(child)
            child = child.right
        return count

    def get_children(self, value):
        node = self.find(value)
        if node is None:
            return []

        children = []
        child = node.child
        while child is not None:
            children.append(child.value)
            child = child.right
        return children

    def get_parent(self, value):
        node = self.find(value)
        if node is None or node.parent is None:
            return None
        return node.parent.value

    def traverse_preorder(self, node=None, result=None):
        if result is None:
            result = []

        if node is None:
            node = self.root

        if node is not None:
            result.append(node.value)
            child = node.child
            while child is not None:
                self.traverse_preorder(child, result)
                child = child.right

        return result

    def traverse_postorder(self, node=None, result=None):
        if result is None:
            result = []
        if node is None:
            node = self.root
        if node is not None:
            child = node.child
            while child is not None:
                self.traverse_postorder(child, result)
                child = child.right
            result.append(node.value)

        return result

    def is_empty(self):
        return self.root is None