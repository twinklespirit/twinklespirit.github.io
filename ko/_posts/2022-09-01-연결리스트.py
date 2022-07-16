# 연결 리스트
# 메모리 효율을 위해 사용
# ? 메모리 크기가 가변적이라 효율적임

# 단일 연결 리스트: (1) 동적 배열
# head -> Node1[data, next] -> Node2[value, next] -> 🎶🎶🎶 -> NodeN[tail] -> Null

# 1. Start with a single node
#    A Single node of singly linked list
class ListNode:
    # Constructor
    # list is constrain of val, next. val contain data and next contain pointer(next node)
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Creating a single node
#first = ListNode(3)
#print(first.val)

# 2.Join nodes to get a linked list
class LinkedList:
    def __init__(self):
        self.head = None

# Linked list with a single node
LL = LinkedList()
LL.head = ListNode(3)
print(LL.head.val)

# 3. Add required methods to the LinkedList class
# insertion method for the linked list
def insert(self,val):
    newNode = LinkedList(val)
    if(self.head):
        current = self.head
        while(current.next):
            current = current.next
        current.next = newNode
    else:
        self.head = newNode

# print method for the linked list
def printLL(self):
    current = self.head
    while(current):
        print(current.data)
        current = current.next