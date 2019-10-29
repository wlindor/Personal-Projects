class Node:
    def __init__(self, value):
        self.value = value 
        self.next = None 
        
class SLL:
    def __init__(self):
        self.head = None 
        self.size = 0
    
    def __str__(self):
        output = ""
        cur = self.head
        while cur:
            output += str(cur.value) + "|"
            cur = cur.next 
        return output 
        
    def insert(self, value):
        new = self.head
        self.head = Node(value)
        self.head.next = new 
        self.size += 1 
        
    def remove(self):
        self.head = self.head.next 
        self.size -= 1 
    
    def removeval(self, value):
        if self.head.value == value:
            self.head = self.head.next
        
        cur = self.head 
        
        while cur.next:
            if cur.next.value == value:
                cur.next = cur.next.next 
            cur = cur.next 
        return None 
        self.size -= 1 
        
    def items(self):
        return self.size 
                
                

        
        
        
S = SLL()    

for i in range(10):
    S.insert(i)
    
print(S)    
           

#1 -> 2 -> 3
#3 -> 2 -> 1 -> None

# None

# 1 ->

# cur - 2       <- 1    <- 2    <- 3
# prev  - 1
# next  = 3

def reverseLinkedList(head):
    cur = head
    prev = None

    while cur:
        next = cur.next
        cur.next = prev
        prev = cur
        cur = next
