# Python

Which python am I using anyway?

```bash
which python
which python3.8
which python3.12
```

Virtual environments

```bash
python3.12 -m venv venv
venv/bin/python
```

Library management

```bash
venv/bin/pip install requests
vim venv/lib/python3.12/site-packages
```

Demo

```bash
# Open Jupyter
touch demo.ipynb
code .
```

namedtuple demo

```python
from collections import namedtuple
namedtuple?
Fruit = namedtuple("Fruit", ["name", "cost", "healthy", "rating"])
apple = Fruit("apple", .28, True, None)
type(apple.name)
type(apple.cost)
type(apple.healthy)
type(apple.rating)
bool(apple.name)
bool(apple.rating)
```

copy example 1

```python
a = [1, 2, 3]
b = a
b.append(4)

print(f"a = {a}")
print(f"b = {b}")

a = [1, 2, 3]
b = a.copy()
b.append(4)
print(f"a = {a}")
print(f"b = {b}")
```

copy example 2

```python
record = {"person": "Alex", "generation": "Millennial"}
record

import json

def print_enriched_record(input_record: dict):
    input_record["is_gen_z"] = input_record.get("generation") == "Zoomer"
    print(json.dumps(input_record, indent=2))

print_enriched_record(record)
record

import json
from copy import deepcopy

def print_enriched_record(input_record: dict):
    record = deepcopy(input_record)
    record["is_gen_z"] = record.get("generation") == "Zoomer"
    print(json.dumps(record, indent=2))

record = {"person": "Alex", "generation": "Millennial"}
print_enriched_record(record)
record

```
