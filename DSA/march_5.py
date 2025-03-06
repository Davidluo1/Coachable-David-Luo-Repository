class ListNode:

    def __init__(self, val = 0, next = None) -> None:
        self.val = val
        self.next = next

class stack:

    def __init__(self) -> None:
        self.stack = None

    def push(item):
        new_node = ListNode(item)
        new_node.next = self.stack
        self.stack = new_node

    def pop():
        if not self.stack:
            return "Empty"
        res = self.stack.val
        self.stack = self.stack.next
        return res

    def peek():
        if not self.stack:
            return "Empty"
        return self.stack.val

class ListNode:

    def __init__(self, val = 0, next = None) -> None:
        self.val = val
        self.next = next

class Queue:

    def __init__(self) -> None:
        self.queue = None
        self.top = None

    def enqueue(item):
        new_node = ListNode(item)
        if self.queue:
            self.queue.next = new_node
            self.queue = new_node
        else:
            self.top = new_node
            self.queue = new_node

    def dequeue(item):
        if not self.top:
            return "Empty"
        res = self.top.val
        self.top = self.top.next
        return res

    def peek(item):
        if self.top:
            return self.top.val
        return "Empty"
