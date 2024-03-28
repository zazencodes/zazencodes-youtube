# list of squares for numbers from 1 to 5.
squares = [x**2 for x in range(1, 6)]

# tuple of squares for numbers from 1 to 5.
squares_tup = tuple(x**2 for x in range(1, 6))

# generator object of squares for numbers from 1 to 5.
squares = (x**2 for x in range(1, 6))

# dict of squares for numbers from 1 to 5.
squares_dict = {x: x**2 for x in range(1, 6)}

# dict from 2 lists
names = ["Alice", "Bob", "Charlie"]
ages = [24, 30, 28]
name_age_dict = {name: age for name, age in zip(names, ages)}

# list of even squares from 1 to 10.
even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]

# list of numbers from 1 to 20 that are divisible by 2 or 3.
divisible_by_2_or_3 = [x for x in range(1, 21) if x % 2 == 0 or x % 3 == 0]

# dict from a list of numbers where the key is the number and the value is "even" or "odd".
odd_even_dict = {x: "even" if x % 2 == 0 else "odd" for x in range(1, 6)}

# dict with word lengths for words longer than 3 characters.
words = ["hello", "world", "python", "is", "awesome"]
word_length_dict = {word: len(word) for word in words if len(word) > 3}

# a flat list from a matrix (list of lists), containing only the elements that are not divisible by 2.
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat_list = [item for sublist in matrix for item in sublist if item % 2 != 0]

# dict where keys are indices of prime numbers in a given list and values are the prime numbers themselves.
from math import sqrt

numbers = range(2, 50)
prime_numbers = {
    i: num
    for i, num in enumerate(numbers)
    if all(num % d != 0 for d in range(2, int(sqrt(num)) + 1))
}

# dict where each key is the first letter of a word and the value is a list of words starting with that letter.
words = ["apple", "bat", "bar", "atom", "book"]
grouped_words = {
    k: [word for word in words if word[0] == k] for k in set(word[0] for word in words)
}

# dictionary mapping each name to their score only if the score is above a threshold
data = [("Alice", 88), ("Bob", 75), ("Charlie", 90), ("Dave", 65)]
threshold = 80
score_dict = {
    f"{name}_{i}": score for i, (name, score) in enumerate(data) if score > threshold
}

# dictionary where the outer keys are unique categories from the original list, the inner keys are items filtered by a condition, and the values are transformed by a lambda function
records = [
    {"category": "A", "value": 10},
    {"category": "B", "value": 15},
    {"category": "A", "value": 20},
    {"category": "B", "value": 25},
]
transformed = {
    k: {
        (d["value"], i): (lambda x: x**2)(d["value"])
        for i, d in enumerate(records)
        if d["category"] == k and d["value"] > 10
    }
    for k in set(d["category"] for d in records)
}
