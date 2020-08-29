
# first lets get a data structure going 
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        

class SLinkedList:
    def __init__(self):
        self.head = None
    
    def addNode(self, val):
        if not self.head:
            self.head = Node(val)
            return self.head
        else:
            current = self.head
            while(current.next != None):
                current = current.next
            current.next = Node(val)
            return current
    def addNodeRef(self, ref):
        if not self.head:
            self.head = Node(ref)
            return self.head
        else:
            current = self.head
            while(current.next != None):
                current = current.next
            current.next = ref
            return current
    def printList(self):
        if not self.head:
            return 
        else:
            current = self.head
            while(current.next != None):
                print(current.val)
                current = current.next
            print(current.val)
    #now lets solve some problems !
    # for sake of ease, let us assume there is always a head, could check easily though 
    #2.1
    def removeDups(self):
        vals = set() # O (1) look up
        vals.add(self.head.val) 
        current = self.head
        while(current.next != None):
            if current.next.val not in vals:
                vals.add(current.next.val)
            else:
                current.next = current.next.next
            current = current.next
        # to do so with no extra stroage is a O(n^2) operation, 2 for loops to loop through entire structure
    # 2.2
    def returnKthFromLast(self, n): # can be done in O(n) time
        count = 1
        current = self.head
        returnVal = self.head
        while(current.next != None):
            count = count + 1
            current = current.next
            if count >= n:
                returnVal = returnVal.next
                count = 1
        return returnVal
    #2.3
    def deleteGivenNode(self, c): # O(n) time
        current = self.head
        if c == current:
            self.head = current.next
        while(current.next != None):
            if current.next == c:
                current.next = current.next.next
            current = current.next
    #2.4
    def partition(self, n): # O(n) time
        smallList = SLinkedList()
        bigList = SLinkedList()
        current = self.head
        while(current.next != None):
            if current.val < n:
                smallList.addNode(current.val)
            else:
                bigList.addNode(current.val)
            current = current.next
        if current.val < n: 
            smallList.addNode(current.val)
        else:
            bigList.addNode(current.val)
        smallList.addNodeRef(bigList.head)
        self.head = smallList.head

    # 2.5 is a great whiteboard problem but a bore to code
    # 2.6 is just a repeat of a string problem with linked list, all the fun of strings with worse access time 
    # 2.7 is just detect duplicates again but between two list rather than one, set for nodes instead of values
    # 2.8 is jsut detect interesection between a linked list and itself
    # No hate crack the coding interview, good problems just boring in rapid sucessesiion
            

l = SLinkedList()
l.addNode(7)
l.addNode(9)
l.addNode(1)
l.addNode(3)
tempNode = l.addNode(5)
l.addNode(7)
l.addNode(7)
l.addNode(9)

l.printList()



# Tested and working, woot woot 
# l.printList()
# l.removeDups()
# print(l.returnKthFromLast(3).val)
# l.deleteGivenNode(tempNode)
# l.partition(5)