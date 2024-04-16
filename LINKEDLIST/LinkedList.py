class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        ltr = self.head
        while ltr.next:
            ltr = ltr.next

        ltr.next = Node(data)

    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")
        count = 0
        ltr = self.head
        while ltr:
            if count == index - 1:
                node = Node(data, ltr.next)
                ltr.next = node
                break

            ltr = ltr.next
            count += 1

    def remove_at(self, index):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")
        count = 0
        if index == 0:
            self.head = self.head.next
            return

        ltr = self.head
        while ltr:
            if count == index - 1:
                ltr.next = ltr.next.next
                break

            ltr = ltr.next
            count += 1

    def get_length(self):
        count = 0
        ltr = self.head
        while ltr:
            count += 1
            ltr = ltr.next
        return count

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

    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            return
        ltr = self.head
        while ltr:
            if ltr.next.data == data_after:
                node = Node(data_to_insert, ltr.next)
                ltr.next = node
                print(ltr.next.data, ltr.next.next.data)
                return 

            ltr = ltr.next

        # Search for first occurance of data_after value in linked list
        # Now insert data_to_insert after data_after node

    def remove_by_value(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next
        # print(count)


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values([45, 33, 334, 332, 234])
    # ll.insert_at_end(43)
    # ll.insert_at_end(4433)
    # ll.insert_at_end(45)

    # ll.insert_at(6, 28)
    ll.print()
    # ll.remove_at(5)

    # print(ll.get_length())
    # ll.remove_by_value(234)
    ll.insert_after_value(332, 88)
    ll.print()
