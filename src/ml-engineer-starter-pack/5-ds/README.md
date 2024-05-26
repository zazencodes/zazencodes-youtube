# Data structures


## Cheat sheet

https://www.bigocheatsheet.com/

## General notes

- Data structures are foundational, they are used everywhere and largely abstracted so that we often don't have to think about them
- More complicated data structures are of more practical use for ML engineering, e.g. handling sparse arrays, optimizing training of neural networks on high-dimensional matrices, etc...)
- Like anything, having a solid grasp on the fundamentals is necessary in order to understand more advanced





## Array
- Definition: A collection of elements, identified by index.
- Usage: Storing a fixed-size sequential collection of elements.
- Operations:
    - Access: O(1)
    - Insert: O(1)-O(n)
    - Delete: O(1)-O(n)
    - Search: O(n)

```python
# Array demo using Python list
array = [1, 2, 3, 4, 5]

# Access
print(array[2])  # Output: 3

# Insert
array.append(6)
print(array)  # Output: [1, 2, 3, 4, 5, 6]

# Delete
array.remove(3)
print(array)  # Output: [1, 2, 4, 5, 6]

# Search
print(4 in array)  # Output: True
```





## Linked list
- Definition: A sequence of nodes where each node points to the next node.
- Usage: Inserting and deleting elements frequently.
- Operations:
    - Access: O(n)
    - Insert: O(1)-O(n)
    - Delete: O(1)-O(n)
    - Search: O(n)
```python

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def append(head, x):
    new_node = ListNode(x)
    if not head:
        return new_node
    last = head
    while last.next:
        last = last.next
    last.next = new_node
    return head

def insert(prev_node, x):
    if not prev_node:
        print("The given previous node must not be None")
        return
    new_node = ListNode(x)
    new_node.next = prev_node.next
    prev_node.next = new_node

def delete(head, key):
    temp = head

    if temp is not None:
        if temp.val == key:
            head = temp.next
            temp = None
            return head

    while temp is not None:
        if temp.next and temp.next.val == key:
            break
        temp = temp.next

    if temp is None:
        print("The key is not present in the linked list")
        return head

    next = temp.next.next
    temp.next = None
    temp.next = next
    return head

def search(head, key):
    current = head

    while current is not None:
        if current.val == key:
            return True
        current = current.next
    return False

def get(head, index):
    current = head
    count = 0

    while current:
        if count == index:
            return current.val
        count += 1
        current = current.next

    return None  # If index is out of range

def display(head):
    elements = []
    current = head
    while current:
        elements.append(current.val)
        current = current.next
    print("Linked List:", elements)

# Demo
head = None

# Append elements
head = append(head, 1)
head = append(head, 2)
head = append(head, 3)
print("After appending 1, 2, 3:")
display(head)

# Insert element
insert(head.next, 4)
print("After inserting 4 after second node:")
display(head)

# Delete element
head = delete(head, 2)
print("After deleting node with value 2:")
display(head)

# Search element
print("Searching for 3:", search(head, 3))
print("Searching for 5:", search(head, 5))

# Get element by index
print("Element at index 1:", get(head, 1))
print("Element at index 3:", get(head, 3))

```





## Stacks
- Definition: A collection of elements with Last In First Out (LIFO) access.
- Usage: e.g. Undo mechanism.
- Operations:
    - Push: O(1)
    - Pop: O(1)
    - Peek: O(1)

```python
from collections import deque

# Stack demo using deque
stack = deque([1, 2, 3, 4, 5])

# Access the top element (peek)
print(stack[-1])  # Output: 5

# Push (insert)
stack.append(6)
print(list(stack))  # Output: [1, 2, 3, 4, 5, 6]

# Pop (delete)
top_element = stack.pop()
print(top_element)  # Output: 6
print(list(stack))  # Output: [1, 2, 3, 4, 5]

# Search (check if an element exists)
print(4 in stack)  # Output: True
```





## Queues
- Definition: A collection of elements with First In First Out (FIFO) access.
- Usage: e.g. Order processing.
- Operations:
    - Enqueue: O(1)
    - Dequeue: O(1)
    - Peek: O(1)

```python
from collections import deque

# Queue demo using deque
queue = deque([1, 2, 3, 4, 5])

# Access the front element (peek)
print(queue[0])  # Output: 1

# Enqueue (insert)
queue.append(6)
print(list(queue))  # Output: [1, 2, 3, 4, 5, 6]

# Dequeue (delete)
front_element = queue.popleft()
print(front_element)  # Output: 1
print(list(queue))  # Output: [2, 3, 4, 5, 6]

# Search (check if an element exists)
print(4 in queue)  # Output: True
```




## Hash Tables
- Definition: A collection of key-value pairs with unique keys.
- Usage: Fast data retrieval.
- Operations:
    - Insert: O(1)
    - Delete: O(1)
    - Search: O(1)

```python
# Hash table demo using Python dictionary
hash_table = {}

# Insert
hash_table["key1"] = "value1"
hash_table["key2"] = "value2"
print(hash_table)  # Output: {'key1': 'value1', 'key2': 'value2'}

# Delete
del hash_table["key1"]
print(hash_table)  # Output: {'key2': 'value2'}

# Search
print("key2" in hash_table)  # Output: True
```




## Trees
- Definition: A hierarchical data structure with nodes.
- Usage: Hierarchical data representation, e.g. Binary Search Tree (BST)
- Operations:
    - Insert: O(log n)
    - Delete: O(log n)
    - Search: O(log n)

```
    1
   / \
  2   3
 / \
4   5
```




## Graphs
- Definition: A collection of nodes (vertices) and edges connecting pairs of nodes.
- Usage: e.g. Network representation.
- Operations: Varies based on representation.

```
A - B
|   |
C - D
```
