class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insert(self, key):
        if self.root is None:
            self.root = TreeNode(key)
        else:
            self._insert_rec(self.root, key)
    
    def _insert_rec(self, node, key):
        if key < node.val:
            if node.left is None:
                node.left = TreeNode(key)
            else:
                self._insert_rec(node.left, key)
        else:
            if node.right is None:
                node.right = TreeNode(key)
            else:
                self._insert_rec(node.right, key)

    def in_order(self, node):
        return (self.in_order(node.left) + [node.val] + self.in_order(node.right)) if node else []

    def pre_order(self, node):
        return [node.val] + self.pre_order(node.left) + self.pre_order(node.right) if node else []

    def post_order(self, node):
        return self.post_order(node.left) + self.post_order(node.right) + [node.val] if node else []

    def delete(self, key):
        self.root = self._delete_rec(self.root, key)
    
    def _delete_rec(self, node, key):
        if node is None:
            return node

        if key < node.val:
            node.left = self._delete_rec(node.left, key)
        elif key > node.val:
            node.right = self._delete_rec(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            min_larger_node = self._min_value_node(node.right)
            node.val = min_larger_node.val
            node.right = self._delete_rec(node.right, min_larger_node.val)
        
        return node

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

if __name__ == "__main__":
    btree = BinaryTree()
    btree.insert(55)
    btree.insert(32)
    btree.insert(20)
    btree.insert(40)
    btree.insert(77)
    btree.insert(61)
    btree.insert(80)

    print("In-order traversal:", btree.in_order(btree.root))
    print("Pre-order traversal:", btree.pre_order(btree.root))
    print("Post-order traversal:", btree.post_order(btree.root))

    btree.delete(20)
    print("In-order after deleting 20:", btree.in_order(btree.root))

    btree.delete(32)
    print("In-order after deleting 32:", btree.in_order(btree.root))

    btree.delete(55)
    print("In-order after deleting 55:", btree.in_order(btree.root))