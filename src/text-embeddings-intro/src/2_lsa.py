from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import TruncatedSVD
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

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

# Generate term-document matrix using CountVectorizer
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(meal_names)

# Apply LSA using TruncatedSVD
lsa = TruncatedSVD(n_components=3)
meal_embeddings = lsa.fit_transform(X)


# Print embeddings
print("Embeddings:")
for text, embedding in zip(meal_names, meal_embeddings):
    print(f"{text} -> {embedding}")
print(meal_embeddings)
print("Embeddings shape:")
print(np.array(meal_embeddings).shape)


# Function to find similar meals
def find_similar_meals_lsa(target_meal, meal_names, meal_embeddings, top_n=15):
    target_index = meal_names.index(target_meal)
    target_embedding = meal_embeddings[target_index]
    similarities = cosine_similarity([target_embedding], meal_embeddings)[0]
    similar_indices = similarities.argsort()[-top_n:][::-1]
    similar_meals = [(meal_names[i], similarities[i]) for i in similar_indices]
    return similar_meals


# Find similar meals to "Apricot salad"
target_meal = "Apricot salad"
similar_meals = find_similar_meals_lsa(target_meal, meal_names, meal_embeddings)

# Print the results
print(f"Meals similar to '{target_meal}' using LSA:")
for meal, similarity in similar_meals:
    print(f"{meal} (similarity: {similarity:.10f})")
