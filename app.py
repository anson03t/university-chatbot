import streamlit as st

# Title
st.title("🎓 University Life Chatbot")

# Conversation history storage
if "history" not in st.session_state:
    st.session_state.history = []

# Rule-based Q&A function
def chatbot_response(user_input):
    user_input = user_input.lower()

    if "library" in user_input:
        return " The library is located at Block B, open from 8AM–9PM (Mon–Sat)."
    elif "register for exam" in user_input or "exam registration" in user_input:
        return " You can register for exams through the student portal under 'Academic Services'."
    elif "cafeteria" in user_input or "food" in user_input:
        return " The cafeteria is at Block C, offering both halal and vegetarian meals."
    elif "sports" in user_input or "gym" in user_input:
        return " The sports complex includes a gym, basketball, and badminton courts."
    elif "wifi" in user_input or "internet" in user_input:
        return " Connect to 'UTAR-WiFi' using your student ID and password."
    else:
        return " Sorry, I don’t know that yet. Try asking about library, exams, cafeteria, sports, or WiFi."

# Input box
user_input = st.text_input("Ask me anything about university life:")

if st.button("Ask") and user_input:
    response = chatbot_response(user_input)

    # Save to history
    st.session_state.history.append(("You", user_input))
    st.session_state.history.append(("Bot", response))

# Display conversation
if st.session_state.history:
    st.subheader("💬 Conversation History")
    for speaker, text in st.session_state.history:
        st.write(f"**{speaker}:** {text}")
