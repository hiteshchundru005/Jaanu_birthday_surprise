import streamlit as st
import time
import base64
import os

# --- Page Configuration ---
st.set_page_config(
    page_title="For My Jaanu ❤️",
    page_icon="👑",
    layout="centered"
)

# --- Background Music Logic ---
MUSIC_FILE = "song.mp3" 

def get_audio_html(file_path):
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            data = f.read()
            b64 = base64.b64encode(data).decode()
            return f"""
                <audio autoplay loop id="bg-music">
                    <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
                </audio>
                <script>
                    var audio = document.getElementById("bg-music");
                    audio.volume = 0.2;
                    audio.play();
                </script>
            """
    return ""

# --- Advanced Custom Styling (Ethereal Romance Theme) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,700;1,700&family=Montserrat:wght@300;400;600&family=Dancing+Script:wght@600&display=swap');

    /* Custom Cursor */
    html, body, [data-testid="stAppViewContainer"] {
        cursor: url('https://cdn-icons-png.flaticon.com/32/1077/1077035.png'), auto;
    }

    /* Dynamic Bokeh Background */
    .stApp {
        background: radial-gradient(circle at 20% 30%, #fff5f5 0%, #fffaf0 100%);
        background-attachment: fixed;
        overflow: hidden;
    }

    .stApp::before {
        content: "";
        position: absolute;
        top: -50%; left: -50%; width: 200%; height: 200%;
        background: radial-gradient(circle at 50% 50%, rgba(255, 182, 193, 0.15), transparent 40%),
                    radial-gradient(circle at 80% 20%, rgba(255, 215, 0, 0.1), transparent 30%),
                    radial-gradient(circle at 10% 80%, rgba(255, 105, 180, 0.1), transparent 35%);
        animation: rotate 30s linear infinite;
        z-index: -1;
    }

    @keyframes rotate {
        from { transform: rotate(0deg); }
        to { transform: rotate(360deg); }
    }

    /* Glassmorphism Refined */
    .glass-card {
        background: rgba(255, 255, 255, 0.6);
        backdrop-filter: blur(15px);
        -webkit-backdrop-filter: blur(15px);
        border-radius: 40px;
        border: 1px solid rgba(255, 255, 255, 0.4);
        padding: 50px 40px;
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.05), inset 0 0 20px rgba(255,255,255,0.5);
        margin-bottom: 30px;
        text-align: center;
        animation: fadeIn 1.2s ease-out;
    }

    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }

    /* Premium Typography */
    h1 {
        font-family: 'Playfair Display', serif !important;
        font-size: 3.5rem !important;
        color: #5d4037 !important;
        letter-spacing: -1px;
        margin-bottom: 0.5rem !important;
    }
    
    .body-text {
        font-family: 'Montserrat', sans-serif !important;
        font-weight: 400;
        font-size: 1.15rem;
        color: #6d4c41;
        line-height: 1.9;
        letter-spacing: 0.3px;
    }

    .italic-signature {
        font-family: 'Dancing Script', cursive !important;
        font-size: 2.2rem;
        color: #d81b60;
        margin-top: 20px;
    }

    /* Luxury Buttons */
    .stButton>button {
        width: 100%;
        border-radius: 100px;
        padding: 18px 40px;
        background: #5d4037;
        color: #fffaf0 !important;
        font-family: 'Montserrat', sans-serif;
        font-weight: 600;
        font-size: 1rem;
        border: none;
        letter-spacing: 2px;
        text-transform: uppercase;
        box-shadow: 0 10px 30px rgba(93, 64, 55, 0.2);
        transition: all 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }

    .stButton>button:hover {
        transform: scale(1.02);
        background: #d81b60;
        box-shadow: 0 15px 40px rgba(216, 27, 96, 0.3);
    }

    /* Image Gallery Styling */
    .stImage img {
        border-radius: 30px;
        filter: sepia(10%) contrast(105%);
        transition: all 0.6s ease;
    }
    .stImage img:hover {
        filter: sepia(0%) contrast(110%);
        transform: translateY(-10px);
    }

    /* Hide Streamlit UI */
    footer {visibility: hidden;}
    header {visibility: hidden;}
    #MainMenu {visibility: hidden;}
    audio { display: none; }
    
    /* Scrollbar */
    ::-webkit-scrollbar { width: 6px; }
    ::-webkit-scrollbar-track { background: transparent; }
    ::-webkit-scrollbar-thumb { background: #d81b60; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- Session State ---
if 'step' not in st.session_state:
    st.session_state.step = 'start'
if 'candles_blown' not in st.session_state:
    st.session_state.candles_blown = False
if 'music_playing' not in st.session_state:
    st.session_state.music_playing = False

def go_to_step(step_name):
    st.session_state.step = step_name

# Play Music
if st.session_state.music_playing:
    st.markdown(get_audio_html(MUSIC_FILE), unsafe_allow_html=True)

# --- 1. Start Screen ---
if st.session_state.step == 'start':
    st.write("")
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.markdown("<h1>For My Jaanu 👑</h1>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image("https://cdn-icons-png.flaticon.com/512/3514/3514510.png", width=180) 
        st.markdown("<p class='body-text' style='font-style: italic; opacity: 0.8;'>\"In your quiet strength, I found my loudest joy.\"</p>", unsafe_allow_html=True)
        if st.button("Enter Her World"):
            st.session_state.music_playing = True 
            go_to_step('celebration')
            st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

# --- 2. Celebration Screen ---
elif st.session_state.step == 'celebration':
    st.balloons()
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.markdown("<h1>Happy Birthday!</h1>", unsafe_allow_html=True)
    st.markdown("""
        <p class='body-text'>
        Jaanu, even though I couldn’t be beside you, every heartbeat of mine was celebrating you today.<br>
        This digital space is a small vessel for all the love my heart carries.
        </p>
    """, unsafe_allow_html=True)
    
    st.write("---")
    
    if not st.session_state.candles_blown:
        st.markdown("<div style='font-size: 60px; margin: 20px 0;'>🕯️🕯️🕯️</div>", unsafe_allow_html=True)
        st.write("The candles are lit for your soul. Make a wish...")
        if st.button("Blow Them Out"):
            st.session_state.candles_blown = True
            st.rerun()
    else:
        st.snow()
        st.markdown("<div style='font-size: 70px; margin: 20px 0;'>🎁✨</div>", unsafe_allow_html=True)
        st.success("May every prayer you whisper today be answered.")
        if st.button("See My Message ➡️"):
            go_to_step('meaning')
            st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

# --- 3. Meaning Section ---
elif st.session_state.step == 'meaning':
    st.markdown("<div class='glass-card' style='text-align: left;'>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; font-size: 2.8rem !important;'>The Essence of You</h1>", unsafe_allow_html=True)
    st.markdown("""
        <p class='body-text'>
        "Jaanu... On your special day, I just want to tell you how deeply grateful I am for you. 
        You’ve become such an important part of my life; your presence brings calm to my chaos and light to my darkest days. <br><br>
        Your smile heals more than you know, and your heart is truly rare. Every memory with you feels precious, 
        and every conversation feels special. I pray this year gives you everything you have ever wished for: 
        happiness, peace, success, and endless reasons to smile.<br><br>
        Always remember how loved and valued you are. Stay the beautiful soul you have always been. ❤️"
        </p>
    """, unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("Our Memories"):
        go_to_step('gallery')
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

# --- 4. Gallery Section ---
elif st.session_state.step == 'gallery':
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.markdown("<h1>Memory Lane</h1>", unsafe_allow_html=True)
    st.markdown("<p class='body-text' style='margin-bottom: 30px;'>Moments that time forgot, but I never will.</p>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.image("p1.jpg", caption="My Safe Place 🏠")
        st.image("p2.jpg", caption="Pure Happiness ✨")
    with col2:
        st.image("p3.jpeg", caption="Calm in the Chaos 🌅")
        st.image("p4.png", caption="Simply Perfect 🌸")

    st.write("")
    if st.button("The Final Note"):
        go_to_step('final')
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

# --- 5. Final Message ---
elif st.session_state.step == 'final':
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.markdown("<h1>Always & Forever 💛</h1>", unsafe_allow_html=True)
    st.markdown("""
        <p class='body-text'>
        No matter where life takes me, <b>jaanu</b> will always be the most precious rhythm in my world.<br><br>
        Happy Birthday to the magic I am lucky to call mine.<br>
        </p>
    """, unsafe_allow_html=True)
    st.markdown("<div class='italic-signature'>— Yours, always.</div>", unsafe_allow_html=True)
    
    st.write("<br>", unsafe_allow_html=True)
    if st.button("Relive the Magic"):
        st.session_state.step = 'start'
        st.session_state.candles_blown = False
        st.session_state.music_playing = False
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("<p style='font-family:Montserrat; font-weight:600;'>Settings</p>", unsafe_allow_html=True)
    st.session_state.music_playing = st.checkbox("Music Enabled", value=st.session_state.music_playing)
    st.write("---")
    st.caption("Ethereal Edition 1.0")