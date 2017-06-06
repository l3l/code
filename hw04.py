
# coding: utf-8

# In[216]:

class RB:
    def __init__(self):
        self.nil = Node(None)
        self.nil.color = 'BLACK'
        self.root = self.nil
        self.count = 0
        self.node_num = 0
        self.node_num2 = 0
        self.bn_num = 0
        self.bh_num = 0
    def left_rotate(self, tree, x):
        y = x.right
        x.right = y.left
        if y.left != tree.nil:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == tree.nil:
            tree.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y
    def right_rotate(self, tree, x):
        y = x.left
        x.left = y.right
        if y.right != tree.nil:
            y.right.parent = x
        y.parent = x.parent
        if x.parent == tree.nil:
            tree.root = y
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
                    z.parent.color = 'Black'
                    z.parent.parent.color = 'RED'
                    self.left_rotate(tree, z.parent.parent)
        tree.root.color = 'BLACK'
    def insert(self, tree, z):
        y = tree.nil
        x = tree.root
        while x != tree.nil:
            y = x
            if z.val < x.val:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y == tree.nil:
            tree.root = z
        elif z.val < y.val:
            y.left = z
        else:
            y.right = z
        z.left = tree.nil
        z.right = tree.nil
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
    def transplant(self, u, v):
        if u.parent == self.nil:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v != None:
            v.parent = u.parent
    def delete_fixup(self, x):
        while x != self.root and x.color == 'BLACK':
            if x == x.parent.left:
                w = x.parent.right
                if w.color == 'RED':
                    w.color = 'BLACK'
                    x.parent.color = 'RED'
                    self.left_rotate(self, x.parent)
                    w = w.parent.right
                if w.left.color == 'BLACK' and w.right.color == 'BLACK':
                    w.color = 'RED'
                    x = x.parent
                elif w.right.color == 'BLACK':
                    w.left.color = 'BLACK'
                    w.color = 'RED'
                    self.right_rotate(self, w)
                    w = x.parent.right
                    w.color = x.parent.color
                    x.parent.color = 'BLACK'
                    w.right.color = 'BLACK'
                    self.left_rotate(self, x.parent)
                    x = self.root
                else:
                    w.color = x.parent.color
                    x.parent.color = 'BLACK'
                    w.right.color = 'BLACK'
                    self.left_rotate(self, x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if w.color == 'RED':
                    w.color = 'BLACK'
                    x.parent.color = 'RED'
                    self.left_rotate(self, x.parent)
                    w = w.parent.right
                if w.left.color == 'BLACK' and w.right.color == 'BLACK':
                    w.color = 'RED'
                    x = x.parent
                elif w.right.color == 'BLACK':
                    w.left.color = 'BLACK'
                    w.color = 'RED'
                    self.right_rotate(self, w)
                    w = x.parent.right
                    w.color = x.parent.color
                    x.parent.color = 'BLACK'
                    w.right.color = 'BLACK'
                    self.left_rotate(self, x.parent)
                    x = self.root
                else:
                    w.color = x.parent.color
                    x.parent.color = 'BLACK'
                    w.right.color = 'BLACK'
                    self.left_rotate(self, x.parent)
                    x = self.root
        x.color = 'BLACK'
    def delete(self, z):
        y = z
        y_original_color = y.color
        if z.left == self.nil:
            x = z.right
            self.transplant(z, z.right)
        elif z.right == self.nil:
            x = z.left
            self.transplant(z, z.left)
        else:
            y = self.tree_maximum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_original_color == 'BLACK':
            self.delete_fixup(x)            
            
    def print(self,tree,level):            
        if tree.root.right.val is not None:
            self.print(tree.root.right,level + 1)
        if tree.root.val is not None:
            for i in range(level):
                print('           ', end='')
            print(tree.root.val, end = ' ')
            print(tree.root.color)      
        if tree.root.left.val is not None:
            self.print(tree.root.left, level + 1)
        
        
    def search(self, k):
        if self.root.val == None:
            self.count += 1
            return 0
        if k == self.root.val:
            return self.root
        if k < self.root.val:
            return self.root.left.search(k)
        else:
            return RB.search(self.root.right, k)
    def do_search(self, k):
        if k > 0:
            self.insert(self, Node(k))
        elif k < 0:
            k = -k
            key = self.search(k)
            if key:
                self.delete(key)
        else:
            return self.nil.count
            
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
    def bn_count(self, tree, level, mini):
        if tree.root.right.val is not None:
            self.bn_count(tree.root.right, level + 1, mini)
        if tree.root.val is not None and tree.root.color == 'BLACK':
            self.bn_num += 1
        if mini == tree.root:   
            print('nb = ' + str(self.bn_num))
        if tree.root.left.val is not None:
            self.bn_count(tree.root.left, level + 1, mini)  
            
    def bh_count(self, z):
        while z.left != self.nil:
            if z.color == 'BLACK':
                self.bh_num += 1
            z = z.left
        if z.color == 'BLACK':
            self.bh_num += 1
        return print('bh = ' + str(self.bh_num))
    def inorder(self, tree):
        if tree.val is None:
            return 
        else:
            self.inorder(tree.left)
            print(tree.val)
            self.inorder(tree.right)
    def inorder_arr(self, tree, arr):
        if tree.val is None:
            return
        else:
            self.inorder_arr(tree.left, arr)
            arr.append(tree.val)
            self.inorder_arr(tree.right, arr)
            
        
class Node(RB):
    count = 0
    def __init__(self, newval):
        self.nil = self
        self.val = newval
        self.left = self.nil
        self.right = self.nil
        self.parent = self.nil
        self.color = 'RED'
        self.root = self

