import numpy as np
import torch
from transformers import BertTokenizer, BertModel
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

# Load pre-trained BERT model and tokenizer
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
model = BertModel.from_pretrained("bert-base-uncased")


# Function to get BERT embeddings
def get_bert_embedding(text, tokenizer, model):
    inputs = tokenizer(
        text, return_tensors="pt", truncation=True, padding=True, max_length=512
    )
    with torch.no_grad():
        outputs = model(**inputs)
    return outputs.last_hidden_state.mean(dim=1).squeeze().numpy()


# Generate embeddings for each meal name
meal_embeddings = np.array(
    [get_bert_embedding(meal, tokenizer, model) for meal in meal_names]
)


# Print embeddings
print("Embeddings:")
for text, embedding in zip(meal_names, meal_embeddings):
    print(f"{text} -> {embedding}")
print(meal_embeddings)
print("Embeddings shape:")
print(np.array(meal_embeddings).shape)


# Function to find similar meals
def find_similar_meals(
    target_meal, meal_names, meal_embeddings, tokenizer, model, top_n=15
):
    target_embedding = get_bert_embedding(target_meal, tokenizer, model)
    similarities = cosine_similarity([target_embedding], meal_embeddings)[0]
    similar_indices = similarities.argsort()[-top_n:][::-1]
    similar_meals = [(meal_names[i], similarities[i]) for i in similar_indices]
    return similar_meals


# Find similar meals to "Apricot salad"
target_meal = "Apricot salad"
similar_meals = find_similar_meals(
    target_meal,
    meal_names,
    meal_embeddings,
    tokenizer,
    model,
)

# Print the results
print(f"Meals similar to '{target_meal}':")
for meal, similarity in similar_meals:
    print(f"{meal} (similarity: {similarity:.2f})")
