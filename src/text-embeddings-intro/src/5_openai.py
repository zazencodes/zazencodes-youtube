import numpy as np
from openai import OpenAI
from sklearn.metrics.pairwise import cosine_similarity
import os

# Set your OpenAI API key
openai_api_key = os.getenv("OPENAI_API_KEY")
if openai_api_key is None:
    raise EnvironmentError("OPENAI_API_KEY env varibale not set")

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


# Function to get OpenAI embeddings
def get_openai_embedding(text, client):
    response = client.embeddings.create(input=[text], model="text-embedding-3-small")
    return np.array(response.data[0].embedding)


# Generate embeddings for each meal name
client = OpenAI()
meal_embeddings = np.array([get_openai_embedding(meal, client) for meal in meal_names])


# Print embeddings
print("Embeddings:")
for text, embedding in zip(meal_names, meal_embeddings):
    print(f"{text} -> {embedding}")
print(meal_embeddings)
print("Embeddings shape:")
print(np.array(meal_embeddings).shape)


# Function to find similar meals
def find_similar_meals(target_meal, meal_names, meal_embeddings, client, top_n=15):
    target_embedding = get_openai_embedding(target_meal, client)
    similarities = cosine_similarity([target_embedding], meal_embeddings)[0]
    similar_indices = similarities.argsort()[-top_n:][::-1]
    similar_meals = [(meal_names[i], similarities[i]) for i in similar_indices]
    return similar_meals


# Find similar meals to "Apricot salad"
target_meal = "Apricot salad"
similar_meals = find_similar_meals(target_meal, meal_names, meal_embeddings, client)

# Print the results
print(f"Meals similar to '{target_meal}':")
for meal, similarity in similar_meals:
    print(f"{meal} (similarity: {similarity:.2f})")
