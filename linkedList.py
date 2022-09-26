class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def traverse(head):
    if head is None:
        return
    print(head.data)
    traverse(head.next)


item1 = Node("cat")
item2 = Node("dog")
item3 = Node("cow")
item1.next = item2
item2.next = item3

# head = Node("dog", Node("cat", Node("cow", None)))
# traverse(head)
traverse(item1)
