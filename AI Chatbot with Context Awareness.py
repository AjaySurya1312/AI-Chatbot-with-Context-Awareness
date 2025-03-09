import random

class ContextAwareChatbot:
    def _init_(self):
        self.context = {}
        self.responses = {
            "greeting": ["Hello! How can I help you today?", "Hi there! What can I do for you?"],
            "farewell": ["Goodbye! Have a great day!", "See you later!"],
            "default": ["I'm not sure I understand.", "Could you please rephrase that?"]
        }
    
    def get_response(self, user_input):
        user_input = user_input.lower()
        
        if "hello" in user_input or "hi" in user_input:
            self.context["last_intent"] = "greeting"
            return random.choice(self.responses["greeting"])
        
        elif "bye" in user_input or "goodbye" in user_input:
            self.context["last_intent"] = "farewell"
            return random.choice(self.responses["farewell"])
        
        elif "remember" in user_input:
            self.context["memory"] = user_input.replace("remember", "").strip()
            return "Got it! I'll remember that."
        
        elif "what do you remember" in user_input:
            return self.context.get("memory", "I don't remember anything yet.")
        
        return random.choice(self.responses["default"])

if _name_ == "_main_":
    bot = ContextAwareChatbot()
    print("Chatbot: Hello! Start chatting with me. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ["bye", "exit"]:
            print("Chatbot:", bot.get_response(user_input))
            break
        print("Chatbot:", bot.get_response(user_input))
