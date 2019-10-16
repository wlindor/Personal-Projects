from LinkedList import LinkedList
#Linked Lists: "A data structure that stores a sequence of objects"

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
