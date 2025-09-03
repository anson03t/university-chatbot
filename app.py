import streamlit as st
import base64

st.set_page_config(page_title="UTAR University Life Chatbot", page_icon="🎓", layout="wide")

# --- Custom Banner at Top Left (below Streamlit navbar) ---
st.markdown(
    """
    <style>
    .custom-banner {
        position: fixed;    /* Fixed so it stays on top */
        top: 60px;          /* Distance from top */
        left: 0px;         /* Distance from left */
        background-color: #111;
        color: white;
        padding: 15px 30px;
        font-size: 22px;
        font-weight: bold;
        z-index: 1000;
        display: flex;
        align-items: center;
        box-shadow: 0 2px 6px rgba(0,0,0,0.3);
    }
    .custom-banner span {
        margin-left: 10px;
    }
    .block-container {
        max-width: 900px;
        margin: auto;
    }
    </style>

    <div class="custom-banner">
        🎓 <span>UTAR University Life Chatbot</span>
    </div>
    """,
    unsafe_allow_html=True
)

def add_bg_from_local(image_file):
    with open(image_file, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}
        .block-container, .block-container p, .block-container h1, .block-container h2, .block-container h3 {{
            color: black !important;
        }}
        .chat-box {{
            background: rgba(255, 255, 255, 0.9);
            padding: 15px;
            border-radius: 12px;
            margin-top: 10px;
            max-width: 800px;
            max-height: 300px;   
            overflow-y: auto;    
        }}
        .chat-box p {{
            margin: 5px 0;
            font-size: 16px;
        }}
        .chat-box b {{
            color: #e74c3c; 
        }}
        .chat-box hr {{
            border: 0;
            border-top: 1px dashed #bbb;  
            margin: 8px 0;
        }}
        .stTextInput input {{
            color: white !important;
        }}
        .stButton>button {{
            background-color: #e74c3c;   
            color: white;
            border-radius: 8px;
            border: none;
            padding: 6px 16px;
            font-weight: bold;
        }}
        .stButton>button:hover {{
            background-color: #c0392b;  
            color: white;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

add_bg_from_local("graduation_background.png")

if "history" not in st.session_state:
    st.session_state.history = []

def chatbot_response(user_input):
    user_input = user_input.lower()

    faq = {
        ("library", "books", "reading room"): " The library is located at Block I, open from 8AM–9PM (Mon–Sat).",
        ("register for exam", "exam registration", "exam sign up"): " You can register for exams through the student portal under 'Academic Services'.",
        ("cafeteria", "canteen", "food", "dining hall"): " The cafeteria is at Block C, offering both halal and vegetarian meals.",
        ("sports", "gym", "sports hall", "fitness", "exercise"): " The sports complex includes a gym, basketball, and badminton courts.",
        ("wifi", "wi-fi", "internet", "connection"): " Connect to 'UTAR-WiFi' using your student ID and password.",
        ("bus", "shuttle", "transport"): " You can catch the university shuttle bus at the main entrance, every 30 minutes.",
        ("administration office", "admin office", "office"): " The administration office is at Block A, ground floor. Open from 9AM–5PM.",
        ("lecturer", "contact lecturer", "email lecturer", "professor", "teacher"): " You can contact lecturers via their university email or during consultation hours posted on the portal.",
    }

    for keywords, response in faq.items():
        if any(word in user_input for word in keywords):
            return response

    return " Sorry, I do not know anything about that. Attempt to inquire about library, exams, cafeteria, sports, WiFi, bus, admin office or lecturers."

user_input = st.text_input("Questions about life in the university:")

st.markdown(
    """
    <style>
    .stTextInput>label {
        font-size: 50px;  /* Larger font size for the label */
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

if st.button("Ask") and user_input:
    response = chatbot_response(user_input)

    st.session_state.history.append(("You", user_input))
    st.session_state.history.append(("Bot", response))

if st.session_state.history:
    st.subheader("💬 Conversation History")

    conversation_html = ""
    for i, (speaker, text) in enumerate(st.session_state.history):
        # Add message
        conversation_html += f"<p><b>{speaker}:</b> {text}</p>"

        # Add line after each user+bot pair
        if i % 2 == 1 and i != len(st.session_state.history) - 1:
            conversation_html += "<hr style='border:1px solid #ddd; margin:8px 0;'>"

    st.markdown(
        f"""
        <div class="chat-box">
            {conversation_html}
        </div>
        """,
        unsafe_allow_html=True
    )
