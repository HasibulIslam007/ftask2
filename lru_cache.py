class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class Cache:

    def __init__(self, capacity):
        if capacity <= 0:
            raise ValueError("Capacity must be positive")

        self.capacity = capacity
        self.cache = {}

        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head


    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev


    def add_front(self, node):

        node.next = self.head.next
        node.prev = self.head

        self.head.next.prev = node
        self.head.next = node


    def get(self, key):

        if key not in self.cache:
            print(f"GET {key}: -1")
            return -1

        node = self.cache[key]

        self.remove(node)
        self.add_front(node)

        print(f"GET {key}: {node.value}")

        return node.value



    def put(self, key, value):

        if key in self.cache:

            node = self.cache[key]
            node.value = value

            self.remove(node)
            self.add_front(node)

        else:

            node = Node(key,value)

            self.cache[key] = node
            self.add_front(node)


            if len(self.cache) > self.capacity:

                lru = self.tail.prev

                self.remove(lru)

                del self.cache[lru.key]

                print(f"Evicted: {lru.key}")

        print(f"PUT ({key},{value})")


    def display(self):

        current = self.head.next

        result=[]

        while current != self.tail:
            result.append(
                f"{current.key}:{current.value}"
            )
            current=current.next

        print("Cache Order(MRU->LRU):",result)