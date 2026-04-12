class Node: 
    def __init__(self,val:int):
        self.val=val
        self.next=None

class LinkedList:
    '''
    a singly linked list is just : 
    - head pointer (start of list)
    - each node has : val,next
    to make insertTail fast, it's smart to also keep: 
    - tail pointer 
    '''
    
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0 #not required but helps with bounds
    
    def get(self, index: int) -> int:
        #use a cursor pointer 
        cur = self.head 

        if index >= self.size:
            return -1
        
        #move cur=cur.next index times 
        for i in range(index):
            cur = cur.next

        if cur is None: 
            return -1

        return cur.val

    def insertHead(self, val: int) -> None:
        node = Node(val)

        if self.size==0:
            self.head=node
            self.tail=node 
        else:
            node.next=self.head
            self.head=node
        
        self.size+=1

    def insertTail(self, val: int) -> None:
        node=Node(val)
        if self.size==0:
            self.head=node
            self.tail=node
        else:
            self.tail.next=node
            self.tail=node
        
        self.size+=1

    def remove(self, index: int) -> bool:
        if index >= self.size:
            return False
        
        #remove head 
        if index==0:
            self.head=self.head.next
            self.size-=1
            if self.size==0:
                self.tail=None
            return True
        
        #remove middle/tail : find node BEFORE the one to remove
        prev=self.head
        for i in range(index-1):
            prev=prev.next
        
        target=prev.next #node to remove 
        prev.next=target.next #remove node

        #if removing the tail, move tail back to prev
        if target==self.tail:
            self.tail=prev
        
        self.size-=1
        return True

    def getValues(self) -> List[int]:
        array=[]
        cur=self.head
        while cur is not None:
            array.append(cur.val)
            cur=cur.next
    
        return array
