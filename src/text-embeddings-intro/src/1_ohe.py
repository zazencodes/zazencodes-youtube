import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Sample dataset of meal names
meal_names = [
    "Apricot salad",
    "Chicken salad",
    "Tuna salad",
    "Beef stew",
    "Vegetable soup",
    "Fruit salad",
    "Pasta primavera",
    "Garlic bread",
    "Grilled cheese sandwich",
    "Roast chicken",
    "Apple pie",
    "Banana smoothie",
    "Mango salsa",
    "Avocado toast",
    "Roasted nuts and dried apricots",
]

# Generate one-hot encodings for each meal name
unique_meals = meal_names
one_hot_encodings = np.eye(len(unique_meals))

# Print embeddings
print("Embeddings:")
for text, embedding in zip(unique_meals, one_hot_encodings):
    print(f"{text} -> {embedding}")
print(one_hot_encodings)
print("Embeddings shape:")
print(np.array(one_hot_encodings).shape)


# Function to get one-hot encoding for a meal
def get_one_hot_encoding(meal, one_hot_encodings, unique_meals):
    index = unique_meals.index(meal)
    return one_hot_encodings[index]


# Function to find similar meals
def find_similar_meals_one_hot(
    target_meal, meal_names, one_hot_encodings, unique_meals, top_n=5
):
    target_encoding = get_one_hot_encoding(target_meal, one_hot_encodings, unique_meals)
    similarities = cosine_similarity([target_encoding], one_hot_encodings)[0]
    similar_indices = np.argsort(similarities)[-top_n:][::-1]
    similar_meals = [(meal_names[i], similarities[i]) for i in similar_indices]
    return similar_meals


# Find similar meals to "Apricot salad"
target_meal = "Apricot salad"
similar_meals = find_similar_meals_one_hot(
    target_meal, meal_names, one_hot_encodings, unique_meals
)

# Print the results
print(f"Meals similar to '{target_meal}' using One-Hot Encoding:")
for meal, similarity in similar_meals:
    print(f"{meal} (similarity: {similarity:.10f})")
