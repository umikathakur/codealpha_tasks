import json
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Download tokenizer
nltk.download('punkt', quiet=True)

# Load FAQs
with open('faqs.json', 'r') as file:
    data = json.load(file)

questions = [faq['question'] for faq in data['faqs']]
answers = [faq['answer'] for faq in data['faqs']]

# Convert text into vectors
vectorizer = TfidfVectorizer()
question_vectors = vectorizer.fit_transform(questions)

print("===== FAQ CHATBOT =====")
print("Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break

    user_vector = vectorizer.transform([user_input])

    similarity = cosine_similarity(
        user_vector,
        question_vectors
    )

    best_match = similarity.argmax()
    score = similarity[0][best_match]

    if score > 0.5:
        print("Chatbot:", answers[best_match])
    else:
        print("Chatbot: Sorry, I don't understand your question.")