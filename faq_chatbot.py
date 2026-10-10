from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

faqs = [
    {
        "question": "What is your name?",
        "answer": "I am an FAQ chatbot."
    },
    {
        "question": "How can I contact support?",
        "answer": "You can contact support by email."
    },
    {
        "question": "What are your working hours?",
        "answer": "Our working hours are 9 AM to 5 PM."
    },
    {
        "question": "What services do you offer?",
        "answer": "We offer customer support services."
    },
    {
        "question": "How can I get help?",
        "answer": "You can ask me a question anytime."
    }
]

questions = [faq["question"] for faq in faqs]

vectorizer = TfidfVectorizer()
question_vectors = vectorizer.fit_transform(questions)

print("FAQ Chatbot started!")
print("Type 'exit' to stop.")

while True:
    user_question = input("\nYou: ")

    if user_question.lower() == "exit":
        print("Chatbot: Goodbye!")
        break

    user_vector = vectorizer.transform([user_question])
    similarities = cosine_similarity(
        user_vector, question_vectors
    )[0]

    best_match = similarities.argmax()

    if similarities[best_match] < 0.15:
        print("Chatbot: Sorry, I don't know that answer.")
    else:
        print("Chatbot:", faqs[best_match]["answer"])