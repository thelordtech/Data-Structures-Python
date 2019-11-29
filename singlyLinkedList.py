class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        presNode = self.head
        while presNode:
            print(presNode.data)
            presNode = presNode.next

    def addNode(self, data):
        newNode = Node(int(data))
        if self.head is None:
            self.head = newNode
            return True

        lastNode = self.head
        while lastNode.next:
            lastNode = lastNode.next
        lastNode.next = newNode


    def sizeofll(self):
        count = 0
        cur_node = self.head

        while cur_node:
            count += 1
            cur_node = cur_node.next
        return count

    def deleteNode(self, key):

        presNode = self.head

        if presNode and presNode.data == key:
            self.head = presNode.next
            presNode = None
            return

        prev = None 
        while presNode and presNode.data != key:
            prev = presNode
            presNode = presNode.next

        if presNode is None:
            print("Value not found in the list!")
            return 

        prev.next = presNode.next
        presNode = None

    def reverseoflist(self):
        prev = None
        n = self.head
        while n is not None:
            next = n.next
            n.next = prev
            prev = n
            n = next
        self.head = prev

myList = LinkedList()
while True:
    option1 = int(input("\nWhat Operation You Want to do?\nOptions: ins(1) (or) del(2) (or) print(3) (or) size(4) (or) rev(5)\n"))
    print("\n")
    if option1 == 1:
        count = int(input("Enter the no.of.values you want to add: "))
        for i in range(count):
            myList.addNode(input())
    elif option1 == 2:
        myList.printList()
        dval = int(input("Enter the value you want to delete: "))
        myList.deleteNode(dval)
        myList.printList()

    elif option1 == 3:
        myList.printList()

    elif option1 == 4:
        print("Size of LL: ",myList.sizeofll())
    elif option1 == 5:
        myList.reverseoflist()
        myList.printList()
    else:
        print("Invalid Option!")


