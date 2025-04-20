import streamlit as st
import google.generativeai as genai

api_key = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=api_key)

# Create the GenerativeModel for business advice chatbot
model = genai.GenerativeModel(model_name="models/gemini-2.0-flash-thinking-exp")

# Function to generate responses using the model
def get_business_advice(user_input, conversation_history):
    # Append the user's input to the conversation history
    conversation_history.append(f"You: {user_input}")
    # Include the entire conversation history to maintain context
    full_conversation = "\n".join(conversation_history)
    response = model.generate_content(full_conversation)
    conversation_history.append(f"Chatbot: {response.text}")
    return response.text, conversation_history

# Check if the user input is business-related
def is_business_related(user_input):
    business_keywords = ["business", "marketing", "finance", "strategy", "startup", "management", "growth", "investment", "economy", "sales", "profit", "loss"]
    return any(keyword.lower() in user_input.lower() for keyword in business_keywords)

# Streamlit frontend UI
st.title("Business Advisor Chatbot")

# Add some instructions for users
st.markdown("""
    I'm your business advisor chatbot! You can ask me about business strategies, marketing, finance, and more.
    Type 'exit' or 'quit' to end the chat, or 'clear' to reset the conversation.
""")

# Initialize conversation history as a session state variable
if 'conversation_history' not in st.session_state:
    st.session_state.conversation_history = []

# Text input field for user query
user_input = st.text_input("You: ", "")

# If the user provides input
if user_input:
    if user_input.lower() in ["exit", "quit", "bye"]:
        st.write("Goodbye! Feel free to reach out if you need more advice.")
        st.session_state.conversation_history = []  # Optionally clear history when ending
    elif user_input.lower() == "clear":
        st.session_state.conversation_history = []  # Clear conversation history
        st.write("Conversation history cleared! Feel free to ask anything.")
    else:
        if is_business_related(user_input):
            # Get the response from the model and update conversation history
            response, updated_history = get_business_advice(user_input, st.session_state.conversation_history)
            st.session_state.conversation_history = updated_history  # Update conversation history
            st.write(f"Chatbot: {response}")
        else:
            st.write("Please ask business-related questions (e.g., marketing, finance, strategy, etc.).")

# Display the conversation history in the UI (optional)
st.write("### Conversation History")
for message in st.session_state.conversation_history:
    st.write(message)
