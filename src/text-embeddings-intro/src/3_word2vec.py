import numpy as np
from gensim.models import Word2Vec
from sklearn.metrics.pairwise import cosine_similarity
import re

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


# Preprocessing function
def preprocess_text(text):
    text = text.lower()  # Convert to lowercase
    text = re.sub(r"[^\w\s]", "", text)  # Remove punctuation
    return text.split()  # Split into words


# Preprocess the meal names
processed_meals = [preprocess_text(meal) for meal in meal_names]

# Train a Word2Vec model
model = Word2Vec(sentences=processed_meals, vector_size=50, window=5, min_count=1, sg=0)


# Generate embeddings for each meal by averaging word vectors
def get_embedding(text):
    words = preprocess_text(text)
    word_vectors = [model.wv[word] for word in words if word in model.wv]
    if word_vectors:
        return np.mean(word_vectors, axis=0)
    else:
        return np.zeros(model.vector_size)


meal_embeddings = np.array([get_embedding(meal) for meal in meal_names])


# Print embeddings
print("Embeddings:")
for text, embedding in zip(meal_names, meal_embeddings):
    print(f"{text} -> {embedding}")
print(meal_embeddings)
print("Embeddings shape:")
print(np.array(meal_embeddings).shape)


# Function to find similar meals
def find_similar_meals(target_meal, meal_names, meal_embeddings, top_n=15):
    target_embedding = get_embedding(target_meal)
    similarities = cosine_similarity([target_embedding], meal_embeddings)[0]
    similar_indices = similarities.argsort()[-top_n:][::-1]
    similar_meals = [(meal_names[i], similarities[i]) for i in similar_indices]
    return similar_meals


# Find similar meals to "Apricot salad"
target_meal = "Apricot salad"
similar_meals = find_similar_meals(target_meal, meal_names, meal_embeddings)

# Print the results
print(f"Meals similar to '{target_meal}':")
for meal, similarity in similar_meals:
    print(f"{meal} (similarity: {similarity:.2f})")
