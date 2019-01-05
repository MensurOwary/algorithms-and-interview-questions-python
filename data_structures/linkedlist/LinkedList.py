class LinkedList:
    def __init__(self):
        self.sentinel = Node("SENTINEL", is_sentinel=True)
        self.current = self.sentinel
        self.length = 0

    def add(self, value):
        self.current.next = Node(value)
        self.current = self.current.next
        self.length += 1

    def remove(self, value, after=-1):
        node = self.sentinel
        prev = None
        counter = 0
        while node:
            if node.value == value and counter > after:
                if node is self.current:
                    self.current = prev
                prev.next = node.next
                self.length -= 1
                break
            prev = node
            node = node.next
            counter += 1
        del counter

    def insert(self, value, position):
        if position == self.length:
            self.current.next = Node(value)
            self.current = self.current.next
        else:
            node = self.sentinel
            prev = None
            inc = 0
            while inc <= position:
                prev = node
                node = node.next
                inc += 1
            prev.next = Node(value)
            prev.next.next = node
        self.length += 1

    def print(self):
        node = self.sentinel
        while node:
            if not node.is_sentinel:
                print(node.value)
            node = node.next

    def remove_duplicates(self):
        register = {}
        prev = self.sentinel
        node = self.sentinel.next
        while node:
            value = node.value
            if value not in register:
                register[value] = value
                prev = node
            else:
                prev.next = node.next
            node = node.next


class Node:
    def __init__(self, value=None, is_sentinel=False):
        self.value = value
        self.is_sentinel = is_sentinel
        self.next = None


def main():
    linked = LinkedList()
    linked.add(1)
    linked.add(2)
    linked.add(3)
    linked.add(4)
    linked.add(2)
    linked.add(3)
    linked.add(2)
    linked.print()
    print("===")
    linked.remove_duplicates()
    linked.print()
    print("===")
    linked.remove(2, 1)
    linked.remove(5)
    linked.print()
    print("===")
    linked.add(45)
    linked.print()
    print("===")
    linked.insert(89, 3)
    linked.print()


if __name__ == '__main__':
    main()