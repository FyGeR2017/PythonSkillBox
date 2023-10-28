class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def put(self, value):
        node = Node(value)
        if self.tail:
            self.tail.next = node
            node.prev = self.tail
        else:
            self.head = node
        self.tail = node

    def get(self):
        if self.head:
            value = self.head.value
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            return value

    def min(self):
        node = self.head
        min_value = node.value
        while node:
            min_value = min(min_value, node.value)
            node = node.next
        return min_value

    def max(self):
        node = self.head
        max_value = node.value
        while node:
            max_value = max(max_value, node.value)
            node = node.next
        return max_value

queue = Queue()

# Добавляем элементы
queue.put(10)
queue.put(5)
queue.put(20)

# Проверяем минимум
print("Минимум:", queue.min())

# Добавляем еще
queue.put(3)

# Проверяем минимум снова
print("Новый минимум:", queue.min())

# Проверяем максимум
print("Максимум:", queue.max())

# Добавляем еще
queue.put(30)

# Проверяем новый максимум
print("Новый максимум:", queue.max())
