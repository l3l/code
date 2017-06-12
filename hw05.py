import os


class Node:
    def __init__(self, newval):
        self.val = newval
        self.left = None
        self.right = None
        self.parent = None


class RB:
    nil = Node(None)
    nil.left = nil
    nil.right = nil
    nil.parent = nil
    nil.color = 'BLACK'

    def __init__(self):
        self.root = self.nil
        self.count = 0
        self.node_num = 0
        self.bn_num = 0
        self.bh_num = 0
        self.insert_num = 0
        self.delete_num = 0
        self.miss_num = 0
        self.string = []

    def left_rotate(self, tree, x):
        y = x.right
        x.right = y.left
        if y.left != self.nil:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == self.nil:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, tree, x):
        y = x.left
        x.left = y.right
        if y.right != self.nil:
            y.right.parent = x
        y.parent = x.parent
        if x.parent == self.nil:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def insert_fixup(self, tree, z):
        while z.parent.color == 'RED':
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                if y.color == 'RED':
                    z.parent.color = 'BLACK'
                    y.color = 'BLACK'
                    z.parent.parent.color = 'RED'
                    z = z.parent.parent
                elif z == z.parent.right:
                    z = z.parent
                    self.left_rotate(tree, z)
                    z.parent.color = 'BLACK'
                    z.parent.parent.color = 'RED'
                    self.right_rotate(tree, z.parent.parent)
                else:
                    z.parent.color = 'BLACK'
                    z.parent.parent.color = 'RED'
                    self.right_rotate(tree, z.parent.parent)
            else:
                y = z.parent.parent.left
                if y.color == 'RED':
                    z.parent.color = 'BLACK'
                    y.color = 'BLACK'
                    z.parent.parent.color = 'RED'
                    z = z.parent.parent
                elif z == z.parent.left:
                    z = z.parent
                    self.right_rotate(tree, z)
                    z.parent.color = 'BLACK'
                    z.parent.parent.color = 'RED'
                    self.left_rotate(tree, z.parent.parent)
                else:
                    z.parent.color = 'BLACK'
                    z.parent.parent.color = 'RED'
                    self.left_rotate(tree, z.parent.parent)
        self.root.color = 'BLACK'

    def insert(self, tree, z):
        y = self.nil
        x = self.root
        while x != self.nil:
            y = x
            if z.val < x.val:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y == self.nil:
            self.root = z
        elif z.val < y.val:
            y.left = z
        else:
            y.right = z
        z.left = self.nil
        z.right = self.nil
        z.color = 'RED'
        self.insert_fixup(tree, z)

    def tree_minimum(self, z):
        while z.left != self.nil:
            z = z.left
        return z

    def tree_maximum(self, z):
        while z.right != self.nil:
            z = z.right
        return z

    def transplant(self, tree, u, v):
        if u.parent == self.nil:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def delete_fixup(self, tree, x):
        while x != self.root and x.color == 'BLACK':
            if x == x.parent.left:
                w = x.parent.right
                if w.color == 'RED':
                    w.color = 'BLACK'
                    x.parent.color = 'RED'
                    self.left_rotate(tree, x.parent)
                    w = x.parent.right
                if w.left.color == 'BLACK' and w.right.color == 'BLACK':
                    w.color = 'RED'
                    x = x.parent
                elif w.right.color == 'BLACK':
                    w.left.color = 'BLACK'
                    w.color = 'RED'
                    self.right_rotate(tree, w)
                    w = x.parent.right
                    w.color = x.parent.color
                    x.parent.color = 'BLACK'
                    w.right.color = 'BLACK'
                    self.left_rotate(tree, x.parent)
                    x = self.root
                else:
                    w.color = x.parent.color
                    x.parent.color = 'BLACK'
                    w.right.color = 'BLACK'
                    self.left_rotate(tree, x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if w.color == 'RED':
                    w.color = 'BLACK'
                    x.parent.color = 'RED'
                    self.right_rotate(tree, x.parent)
                    w = x.parent.left
                if w.right.color == 'BLACK' and w.left.color == 'BLACK':
                    w.color = 'RED'
                    x = x.parent
                elif w.left.color == 'BLACK':
                    w.right.coor = 'BLACK'
                    w.color = 'RED'
                    self.left_rotate(tree, w)
                    w = x.parent.left
                    w.color = x.parent.color
                    x.parent.color = 'BLACK'
                    w.left.color = 'BLACK'
                    self.right_rotate(tree, x.parent)
                    x = self.root
                else:
                    w.color = x.parent.color
                    x.parent.color = 'BLACK'
                    w.left.color = 'BLACK'
                    self.right_rotate(tree, x.parent)
                    x = self.root
        x.color = 'BLACK'

    def delete(self, tree, z):
        y = z
        y_original_color = y.color
        if z.left == self.nil:
            x = z.right
            self.transplant(tree, z, z.right)
        elif z.right == self.nil:
            x = z.left
            self.transplant(tree, z, z.left)
        else:
            y = self.tree_minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.transplant(tree, y, y.right)
                y.right = z.right
                y.right.parent = y
            self.transplant(tree, z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_original_color == 'BLACK':
            self.delete_fixup(tree, x)

    def print(self, node, level):
        if node.right.val is not None:
            self.print(node.right, level + 1)
        if node.val is not None:
            for i in range(level):
                print('     ', end='')
                # print('             ', end = '')
            print(node.val, end=' ')
            if node.color == 'BLACK':
                print('B')
            else:
                print('R')
            # print(node.color)
            print()
        if node.left.val is not None:
            self.print(node.left, level + 1)

    def search(self, x, k):
        if x.val == None:
            self.count += 1
            return 0
        if k == x.val:
            return x
        if k < x.val:
            return self.search(x.left, k)
        else:
            return self.search(x.right, k)

    def do_search(self, k):
        if k > 0:
            self.insert_num += 1
            self.insert(self, Node(k))
        elif k < 0:
            k = -k
            key = self.search(self.root, k)
            if key:
                self.delete_num += 1
                self.delete(rb, key)
            else:
                self.miss_num += 1
        else:
            return self.count

    def node_count(self, tree):
        if tree.val is None:
            if tree is self.tree_maximum(self.root):
                return print(self.node_num)
        else:
            self.node_count(tree.left)
            self.node_num += 1
            self.node_count(tree.right)

    def node_count1(self):
        self.node_count(self.root)
        return print('total = ' + str(self.node_num))

    def bn_count(self, node, level, mini):
        if node.right.val is not None:
            self.bn_count(node.right, level + 1, mini)
        if node.val is not None and node.color == 'BLACK':
            self.bn_num += 1
        if mini == node:
            print('nb = ' + str(self.bn_num))
        if node.left.val is not None:
            self.bn_count(node.left, level + 1, mini)

    def bh_count(self, node):
        self.bh_num = 0
        while node != self.nil:
            if node.color == 'BLACK':
                self.bh_num += 1
            node = node.left
        return print('bh = ' + str(self.bh_num))

    def inorder(self, node):
        if node.val is None:
            return
        else:
            self.inorder(node.left)
            print(node.val, end=' ')
            if node.color == 'BLACK':
                print('B')
            else:
                print('R')
            self.inorder(node.right)

    def insert_count(self):
        return print('insert = %d' % self.insert_num)

    def delete_count(self):
        return print('deleted = %d' % self.delete_num)

    def miss_count(self):
        return print('miss = %d' % self.miss_num)

    def file_search(self):
        filenames = os.listdir('./rbtest')
        for filename in filenames:
            self.string.append(filename)

    def print_all(self, string):
        print('filename = ' + string)
        self.node_count1()
        self.insert_count()
        self.delete_count()
        self.miss_count()
        self.bn_count(self.root, 0, self.tree_minimum(rb.root))
        self.bh_count(self.root)
        self.inorder(self.root)
        print('--------------------------------------------------------------------------------')
        print()


rb1 = RB()
rb1.file_search()
for string in rb1.string:
    rb = RB()
    f = open('./rbtest/' + string, 'r')
    lines = f.readlines()
    for line in lines:
        rb.do_search(int(line))
        if int(line) == 0:
            break
    rb.print_all(string)
    f.close()




