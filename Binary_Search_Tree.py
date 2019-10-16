import random 
class Node:
    def __init__(self, value):
        self.value = value 
        self.right = None 
        self.left = None 

        
class Tree:
    def __init__(self):
        self.root = None 
        
        
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
            
        self._insert(value, self.root)
        
    def _insert(self, value, cur_node):
        if value > cur_node.value:
            if cur_node.right is None:
                cur_node.right = Node(value)       
            else:
                return self._insert(value, cur_node.right)
            
        elif value < cur_node.value:
            if cur_node.left is None:
                cur_node.left = Node(value)
            else:
                return self._insert(value, cur_node.left)
            
        else:
            return "Value is already in the Tree"
        
    def get(self, value):
        return self._get(value, self.root)
    
    def _get(self, value, cur_node):
        if not cur_node:
            return False 
        if value == cur_node.value:
            return True 
        elif value < cur_node.value:
            return self._get(value, cur_node.left)
        else:
            return self._get(value, cur_node.right)
        
        return False 
    
    def find(self, value): 
        if self.root != None:
            return self._find(value, self.root)
        else:
            return None 
        
    def _find(self, value, cur_node):
        if value == cur_node.value:
            return cur_node.value
        elif value < cur_node.value:
            if cur_node.left != None:
                return self._find(value, cur_node.left)
        else:
            if cur_node.right != None:
                return self._find(value, cur_node.right)
    
        
    def delete(self, value):
        #Set the root equal to the delete recursive call 
        self.root = self._delete(value, self.root)
        
    def _delete(self, value, cur_node):
        #If there is no root Node then return none
        if not cur_node:
            return None
        
        #If pased in value is bigger than the current node value, traverse rightside of tree 
        if cur_node.value < value:
            cur_node.right = self._delete(value, cur_node.right)
            
        #If passed in value is less than the current node value, traverse leftside of tree
        elif cur_node.value > value:
            cur_node.left = self._delete(value, cur_node.left) 
        
        #If the passed in value is equal to the current node value, start handling the 3 cases. 
        else:
            
            #Case 1 has no children 
            if not cur_node.left and cur_node.right:
                return None 
            
            #Case 2 has two children 
            elif cur_node.left and cur_node.right:
            
                #Find the smallest element in right subtree
                smallest = self.getsmallest(cur_node.right)
                
                #Delete smallest element
                cur_node.right = self._delete(smallest.value, cur_node.right) 
                
                #Now replace current node with the smallest node 
                smallest.left = cur_node.left 
                smallest.right = cur_node.right 
                return smallest 
            
            #Case 3 has one child 
            else:
                if cur_node.left:
                    return cur_node.left 
                else:
                    return cur_node.right 
                
        return cur_node
            
        
                
    def getsmallest(self, cur_node):
        while cur_node.left:
            cur_node = cur_node.left 
            
        return cur_node 
            
    def find_closest(self, target):
        closest = float('inf')
        cur_node = self.root
        while cur_node:
            if abs(closest - target) > abs(target - cur_node.value):
                closest = cur_node.value
            if target < cur_node.value:
                cur_node = cur_node.left
            elif target > cur_node.value:
                cur_node = cur_node.right 
            else:
                break 
        return closest 
    
    def validate(self):
        return self.validate_helper(self.root, float("-inf"), float("inf"))
    
    def validate_helper(self, cur_node, minValue, maxValue):
        if not cur_node:
            return True 
        if cur_node.value < minValue or cur_node.value >= maxValue:
            return False 
        else:
            leftIsValid = self.validate_helper(cur_node.left, minValue, maxValue)
        return leftIsValid and self.validate_helper(cur_node.right, minValue, maxValue) 
    
    def inorder(self):
        return self._inorder(self.root, array = [])
    
    def _inorder(self, root, array = []):
        if not root:
            return None 
        self._inorder(root.left, array)
        array.append(root.value)
        self._inorder(root.right, array)
        return array 

        
    def print(self):
        if self.root != None:
            return self._print(self.root)
            
    def _print(self, cur_node):
        if cur_node != None:
            self._print(cur_node.left)
            print(str(cur_node.value))
            self._print(cur_node.right) 
        

            
def fill_tree(tree, num_elements = 10, max_int = 1000):
    from random import randint 
    for i in range(num_elements):
        cur_element = randint(0, max_int)
        tree.insert(cur_element) 
    return tree 
            
tree = Tree()
'''tree = fill_tree(tree)
tree.print()

tree.find_closest(40)'''
