import streamlit as st
import streamlit.components.v1 as components

# Set page title and icon
st.set_page_config(page_title="A Special Question", page_icon="❤️")

# --- Custom CSS for Styling ---
st.markdown("""
    <style>
    /* This sets the background for the entire app */
    .stApp {
        background-image: linear-gradient(to bottom right, #ffdde1, #ee9ca7);
        background-attachment: fixed;
    }
    
    /* Style for the main title */
    h1 {
        color: #d63384;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
    }

    /* Style for the 'Yes' button */
    div.stButton > button:first-child {
        background-color: #ff4b4b;
        color: white;
        font-size: 24px;
        font-weight: bold;
        border-radius: 12px;
        border: 2px solid #ff3333;
        padding: 15px 30px;
        transition: all 0.3s ease-in-out;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }

    /* Makes the 'Yes' button grow on hover */
    div.stButton > button:first-child:hover {
        transform: scale(1.15);
        background-color: #ff3333;
        box-shadow: 0 6px 8px rgba(0,0,0,0.15);
    }
    </style>
    """, unsafe_allow_html=True)

# --- Main App Content ---
st.title("Ayanfe mi... I have a very important question. 🌹")
st.write("") # Add a little spacing
st.header("Will you be my Valentine?")

# Create two columns for layout
col1, col2 = st.columns(2)

with col1:
    # The "Yes" button logic
    if st.button("YES! ❤️", key="yes_button"):
        st.balloons()
        st.success("Yay! You just made me the happiest person! Best. Day. Ever. 😍")
        # Display a celebratory GIF
        st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHpueXpueXpueXpueXpueXpueXpueXpueXpueXpueXpueXpueCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/lNy70qJtN6D2uXqV8C/giphy.gif", use_column_width=True)

with col2:
    # This is the "Moving No Button" logic using HTML & JavaScript
    no_button_html = """
    <div id="no-container" style="height: 150px; width: 100%; position: relative; display: flex; justify-content: center; align-items: center;">
        <button id="no-btn" style="position: absolute; background-color: #6c757d; color: white; border: none; padding: 10px 20px; font-size: 16px; border-radius: 5px; cursor: pointer; transition: 0.1s;">
            No
        </button>
    </div>

    <script>
        const btn = document.getElementById('no-btn');

        btn.addEventListener('mouseover', function() {
            // Calculate random positions for the button to jump to
            // We use 'fixed' position so it can jump anywhere on the screen
            const x = Math.random() * (window.innerWidth - btn.offsetWidth);
            const y = Math.random() * (window.innerHeight - btn.offsetHeight);
            
            btn.style.position = 'fixed';
            btn.style.left = x + 'px';
            btn.style.top = y + 'px';
        });
        
        // Just in case they are super fast and manage to click it
        btn.onclick = function() {
            alert("Nice try, but you can't escape love! 😉");
        }
    </script>
    """
    components.html(no_button_html, height=250)

st.write("---")

st.caption("Made with ❤️ and a little bit of Python code, just for you.")
