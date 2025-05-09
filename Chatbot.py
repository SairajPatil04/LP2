import nltk
from nltk.tokenize import word_tokenize

# Download once
nltk.download('punkt')

def preprocess(text):
    # Lowercase + tokenization
    return word_tokenize(text.lower())

def respond(tokens):
    if any(word in tokens for word in ["order", "status", "track"]):
        return "You can track your order at https://booknest.com/orders using your order ID."
    elif any(word in tokens for word in ["return", "refund", "replace"]):
        return "We accept returns within 7 days of delivery in unused condition."
    elif any(word in tokens for word in ["shipping", "delivery", "charges"]):
        return "Shipping is free for orders above ₹499. A charge of ₹49 applies otherwise."
    elif any(word in tokens for word in ["payment", "methods", "pay", "cod"]):
        return "We accept UPI, credit/debit cards, net banking, and Cash on Delivery."
    elif any(word in tokens for word in ["contact", "support", "help", "email"]):
        return "You can contact us at support@booknest.com or call +91-9876543210."
    elif any(word in tokens for word in ["exit", "quit", "bye"]):
        return "Thank you for chatting with BookNest. Goodbye!"
    else:
        return "Sorry, I didn't understand that. Can you rephrase?"

def run_chatbot():
    print("Welcome to BookNest Customer Support")
    print("Type your question or type 'exit' to quit.\n")
    
    while True:
        user_input = input("You: ")
        tokens = preprocess(user_input)
        reply = respond(tokens)
        print("Bot:", reply)
        if "goodbye" in reply.lower():
            break

if __name__ == "__main__":
    run_chatbot()
