#Doubly Linked List

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class Deque:
    def __init__(self):
      self.size = 0
      self.head = Node("Head")
      self.tail = Node("Tail")
      self.head.next = self.tail
      self.tail.prev = self.head


    def insertFront(self, value):
        new_node = Node(value)
        original_tail = self.head.next

        #Update self.head pointers
        self.head.next.prev = new_node
        self.head.next = new_node

        #Update new nodes pointers
        new_node.prev = self.head
        new_node.next = original_tail
        self.size += 1

    def insertLast(self, value):
        new_node = Node(value)
        original_head = self.tail.prev

        #Update self.tail pointers
        self.tail.prev.next = new_node
        self.tail.prev = new_node

        #Update new nodes pointers
        new_node.prev = original_head
        new_node.next = self.tail
        self.size += 1

    def deleteFront(self):
        self.head.next = self.head.next.next
        self.head.next.next.prev = self.head
        self.size -= 1

    def deleteEnd(self):
        self.tail.prev.prev.next = self.tail
        self.tail.prev = self.tail.prev.prev
        self.size -= 1

    def get(self,value):
        current = self.head.next
        while current.next:
            if current.value == value:
                return True
            current = current.next
        return False 
    

    def __repr__(self):
        lst = ""
        current = self.head.next
        while current.next:
            lst += str(current.value) + "|"
            current = current.next
        return lst
    




                

                
                
    
            
            
            
            
            
            
            

        

        
            
            
        
