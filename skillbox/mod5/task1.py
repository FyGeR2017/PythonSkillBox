class Node:

    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Stack:

    def __init__(self):
        self.head = None

    def push(self, value):
        node = Node(value)
        if self.head:
            node.next = self.head
        self.head = node

    def pop(self):
        if self.head:
            value = self.head.value
            self.head = self.head.next
            return value

    def peek(self):
        if self.head:
            return self.head.value

    def is_empty(self):
        return not self.head


stack = Stack()


#Добавляем элементы
stack.push(1)
stack.push(2)
stack.push(3)

print ('Удаляем элементы')
print(stack.pop())  # 3
print(stack.pop())  # 2

#Добавляем элемент
stack.push(4)

print('Последнее число списка')
print(stack.peek())  # 4

#Добавляем элемент
stack.push(5)

print ('Очищаем всё элементы списка')
while not stack.is_empty():
    print(stack.pop())  # 5, 4, 1

print ('Проверяем, пуст ли список')
print(stack.is_empty())  # True
