class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def get(self, index):
        current = self.head
        for _ in range(index):
            current = current.next
        return current.data

    def remove(self, index):
        if index == 0:
            self.head = self.head.next
            return
        current = self.head
        for _ in range(index - 1):
            current = current.next
        current.next = current.next.next

    def insert(self, n, val):
        new_node = Node(val)
        if n == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        for _ in range(n - 1):
            current = current.next
        new_node.next = current.next
        current.next = new_node

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next


my_list = LinkedList()

my_list.push(10)
my_list.push(20)
my_list.push(30)

print(my_list.get(0))
print(my_list.get(1))
print(my_list.get(2))
print()

my_list.remove(1)
print(list(my_list))
print()

my_list.insert(1, 25)
print(list(my_list))
print()

for item in my_list:
    print(item)
