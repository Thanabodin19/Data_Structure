class BinaryTree:
    def __init__(self, root):
        self.key = root
        self.left_child = None
        self.right_child = None

    def insert_left(self, new_node):
        if self.left_child == None:
            self.left_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.left_child = self.left_child
            self.left_child = t

    def insert_right(self, new_node):
        if self.right_child == None:
            self.right_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.right_child = self.right_child
            self.right_child = t

    def get_left_child(self):
        return self.left_child

    def get_right_child(self):
        return self.right_child

    def set_root_val(self, obj):
        self.key = obj

    def get_root_val(self):
        return self.key

    def preorder(self):
        print(self.key)
        if self.left_child:
            self.left_child.preorder()
        if self.right_child:
            self.right_child.preorder()

    def inorder(self):
        if self.left_child:
            self.left_child.inorder()
        print(self.key)
        if self.right_child:
            self.right_child.inorder()

    def postorder(self):
        if self.left_child:
            self.left_child.postorder()
        if self.right_child:
            self.right_child.postorder()
        print(self.key)

if __name__ == '__main__':

    r = BinaryTree(5)
    r.insert_left(9)
    r.insert_right(11)
    r.get_left_child().insert_left(14)
    r.get_left_child().insert_right(18)
    r.get_left_child().get_left_child().insert_left(33)
    r.get_left_child().get_left_child().insert_right(17)
    r.get_left_child().get_right_child().insert_left(27)
    r.get_right_child().insert_left(19)
    r.get_right_child().insert_right(21)

    print("preorder")
    r.preorder()
    print()
    print("inorder")
    r.inorder()
    print()
    print("postorder")
    r.postorder()
    print()
