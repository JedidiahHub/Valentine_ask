import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="A Special Question", page_icon="❤️")

# Custom CSS for the "Yes" button inflation and styling
st.markdown("""
    <style>
    .stButton > button {
        transition: all 0.3s ease-in-out;
        background-color: #ff4b4b;
        color: white;
        font-size: 20px;
        border-radius: 10px;
    }
    /* This makes the Yes button grow when the user interacts */
    .yes-btn:hover {
        transform: scale(1.5);
    }
    </style>
    """, unsafe_allow_html=True)

st.title("Hey you... I have a question. 🌹")
st.header("Will you be my Valentine?")

# Create two columns
col1, col2 = st.columns(2)

with col1:
    if st.button("YES! ❤️", key="yes_button"):
        st.balloons()
        st.success("Yay! I knew you'd say yes! Best. Day. Ever. 😍")
        st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHpueXpueXpueXpueXpueXpueXpueXpueXpueXpueXpueXpueCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/lNy70qJtN6D2uXqV8C/giphy.gif")

with col2:
    # This is the "Moving No Button" logic using JavaScript
    no_button_html = """
    <div id="no-container" style="height: 100px; width: 100%; position: relative;">
        <button id="no-btn" style="position: absolute; background-color: #6c757d; color: white; border: none; padding: 10px 20px; border-radius: 5px; cursor: pointer; transition: 0.1s;">
            No
        </button>
    </div>

    <script>
        const btn = document.getElementById('no-btn');
        const container = document.getElementById('no-container');

        btn.addEventListener('mouseover', function() {
            // Calculate random positions within the container
            const x = Math.random() * (window.innerWidth - 100);
            const y = Math.random() * (window.innerHeight - 100);
            
            // Move the button to a fixed/absolute position on the screen
            btn.style.position = 'fixed';
            btn.style.left = x + 'px';
            btn.style.top = y + 'px';
        });
        
        btn.onclick = function() {
            alert("Nice try, but you can't click it!");
        }
    </script>
    """
    components.html(no_button_html, height=200)

st.write("---")
st.write("Made with ❤️ and a little bit of Python code.")