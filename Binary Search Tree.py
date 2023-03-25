class Node:
    def __init__(self, value):
        self.right_child = None
        self.left_child = None
        self.parent = None
        self.value = value
        self.root = False

    def is_root(self):
        return self.root

    def get_value(self):
        return self.value

    def get_right_child(self):
        return self.right_child
    
    def get_left_child(self):
        return self.left_child

    def has_children(self):
        if self.left_child != None or self.right_child != None:
            return True
        else:
            return False

    def has_both_children(self):
        if self.left_child != None and self.right_child != None:
            return True
        else:
            return False

    def get_parent(self):
        return self.parent
#-------------------------------------------------------------------------------------------------
class BST:
    def __init__(self):
        self.root = None
    
    #Searches for a value in the BST and tells its parent and whether if the node is a left or a right child
    def search(self, root, key):
        curr_key = key
        if root == None:
            print('It cannot be found!')
        elif root.value == key:
            if root.parent == None: 
                print(str(key) + ' is the root of the binary search tree.')
            elif root.value < root.parent.value: 
                print(str(key) + ' is the left child of ' + str(root.parent.value))
            else: 
                print(str(key) + ' is the right child of ' + str(root.parent.value))
            return root
        elif key < root.value:
            return self.search(root.left_child, curr_key)
        elif key > root.value:
            return self.search(root.right_child, curr_key)

    def remove(self, node):
        #Leaf node case
        if node.has_children() == False and node.root == False:
            if node.value < node.parent.value:
                node.parent.left_child = None
            elif node.value > node.parent.value:
                node.parent.right_child = None
        #Leaf node case with root
        elif node.has_children() == False and node.root == True:
            self.root = None
        #One child case
        elif node.right_child == None and node.left_child != None and node.root == False:
            if node.value < node.parent.value:
                node.parent.left_child = node.left_child
            elif node.value > node.parent.value:
                node.parent.right_child = node.left_child
        #One child case
        elif node.right_child != None and node.left_child == None and node.root == False:
            if node.value < node.parent.value:
                node.parent.left_child = node.right_child
            elif node.value > node.parent.value:
                node.parent.right_child = node.right_child
        #One child case with root
        elif node.right_child == None and node.left_child != None and node.root == True:
            left_child = node.left_child
            self.root = left_child
            self.root.root = True
            self.root.parent = None
        #One child case with root
        elif node.right_child != None and node.left_child == None and node.root == True:
            right_child = node.right_child
            self.root = right_child
            self.root.root = True
            self.root.parent = None
        #Two child case not root node
        elif node.has_both_children() == True and node.root == False:
            if node.parent.value < node.value:
                node.parent.right_child = node.right_child
                node.right_child.left_child = node.left_child
                node.left_child.parent = node.right_child
                node.right_child.parent = node.parent
            elif node.parent.value > node.value:
                node.parent.left_child = node.right_child
                node.right_child.left_child = node.left_child
                node.left_child.parent = node.right_child
                node.right_child.parent = node.parent
        #Two child case with root node
        elif node.has_both_children() == True and node.root == True:
            left_child = self.root.left_child
            right_child = self.root.right_child
            self.root.root = False
            self.root = right_child
            self.root.root = True
            self.root.left_child = left_child
            left_child.parent = self.root

    def add(self, node):
        #If there is no nodes in the BST
        if self.root == None:
            self.root = node
            node.root = True
        #If root has no left child
        elif self.root != None and self.root.value > node.value and self.root.left_child == None:
            self.root.left_child = node
            node.parent = self.root  
        #If root has no right child          
        elif self.root != None and self.root.value < node.value and self.root.right_child == None:
            self.root.right_child = node
            node.parent = self.root
        #If simply adding to the already built tree
        else:
            prev_node = None
            curr_node = self.root
            while curr_node != None:
                if curr_node.value > node.value:
                    prev_node = curr_node
                    curr_node = curr_node.left_child
                elif curr_node.value < node.value:
                    prev_node = curr_node
                    curr_node = curr_node.right_child
            if curr_node != None:
                if curr_node.value > node.value:
                    curr_node.left_child = node
                    node.parent = curr_node
                elif curr_node.value < node.value:
                    curr_node.right_child = node
                    node.parent = curr_node
            else:
                if prev_node.value > node.value:
                    prev_node.left_child = node
                    node.parent = prev_node
                elif prev_node.value < node.value:
                    prev_node.right_child = node
                    node.parent = prev_node
        
    #This prints the tree using recursion
    def print_tree(self, root, space = 0):
        if (root == None): 
            return
        space += 5
        self.print_tree(root.right_child, space)

        for i in range(5, space): 
            print(end = " ")  
        print("|" + str(root.value) + "|<")
        self.print_tree(root.left_child, space)
    
tree = BST()
count = 0
while True:
    if count == 0:
        node_value = int(input('What value do you want your root node to be?'))
        root_node = Node(node_value)
        tree.add(root_node)
        tree.print_tree(tree.root)
        count+=1
        print()
    user_option = input("Enter \'a\' if you want to add, \'r\' if you want to remove a node, \'s\' if you want to search for a node, \'p\' if you want to print the tree, \'e\' if you want to exit")
    if user_option == 'e':
        print()
        tree.print_tree(tree.root)
        break
    elif user_option == 'a':
        node_value = int(input('What value do you want your node to be?'))
        node = Node(node_value)
        tree.add(node)
        tree.print_tree(tree.root)
        print()
    elif user_option == 'r':
        node_to_remove = None
        node_value = None
        while node_to_remove == None:
            node_value = int(input('What node do you want to remove from the tree?'))
            node_to_remove = tree.search(tree.root, node_value)
        
        if node_to_remove.root == False:
            tree.remove(node_to_remove)
            tree.print_tree(tree.root)
        elif node_to_remove.root == True and node_to_remove.has_children() == True:
            tree.remove(node_to_remove)
            tree.print_tree(tree.root)
        elif node_to_remove.root == True and node_to_remove.has_children() == False:
            tree.remove(node_to_remove)
            count = 0
            tree.print_tree(tree.root)
    elif user_option == 's':
        node_value = int(input('What value do you want to search for in the tree?'))
        tree.search(tree.root, node_value)
        tree.print_tree(tree.root)
    elif user_option == 'p':
        tree.print_tree(tree.root)
                    
    
