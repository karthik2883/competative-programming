class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data,self.head)
        self.head = node


    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + ' --> ' if itr.next else str(itr.data)
            itr = itr.next
        print(llstr)

    def insert_values(self, data):
        self.head = None
        for i in data:
            # node = Node(i, self.head)
            # self.head = node
           self.insert_at_beginning(i)
    def insert_at(self):

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values([45,33,334,332,234])
    ll.insert_at_beginning(43)

    ll.print()