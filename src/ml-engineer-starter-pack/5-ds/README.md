# Data structures


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
from collections import deque

# Linked list demo using deque
linked_list = deque([1, 2, 3, 4, 5])

# Access
# Note: Direct access by index is not efficient with deque and not typically done in linked lists
# but for demonstration purposes, we will convert to a list temporarily to access by index.
print(list(linked_list)[2])  # Output: 3

# Insert
linked_list.append(6)
print(list(linked_list))  # Output: [1, 2, 3, 4, 5, 6]

# Delete
linked_list.remove(3)
print(list(linked_list))  # Output: [1, 2, 4, 5, 6]

# Search
print(4 in linked_list)  # Output: True

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
