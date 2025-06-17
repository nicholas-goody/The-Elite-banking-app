import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Bank App - Home",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded",
)

users = {
    "Nikola": {
        "password": "password123",
        "balance": 5000,
        "transactions": [
            {"date": "2025-06-01", "type": "Deposit", "amount": 1000},
            {"date": "2025-06-05", "type": "Withdrawal", "amount": 500},
        ],
    },
    "Samuel": {
        "password": "securepass",
        "balance": 3000,
        "transactions": [
            {"date": "2025-06-02", "type": "Deposit", "amount": 2000},
            {"date": "2025-06-06", "type": "Withdrawal", "amount": 1000},
        ],
    },
}


users = {
    "Nikola": {"password": "password123", "balance": 5000},
    "Samuel": {"password": "securepass", "balance": 3000},
}

# Login feature
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False
    st.session_state["current_user"] = None

if not st.session_state["logged_in"]:
    st.title("Bank App - Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username in users and users[username]["password"] == password:
            st.session_state["logged_in"] = True
            st.session_state["current_user"] = username
            st.success(f"Welcome, {username}!")
        else:
            st.error("Invalid username or password.")
else:
    # Logged-in view
    current_user = st.session_state["current_user"]
    user_data = users[current_user]

    components.html(
        """
        <div style="position: relative; width: 100%; height: 300px;">
            <canvas id="fireworksCanvas" style="width: 100%; height: 100%;"></canvas>
        </div>
        <script>
            const canvas = document.getElementById('fireworksCanvas');
            const ctx = canvas.getContext('2d');
            canvas.width = window.innerWidth;
            canvas.height = 300;

            const particles = [];
            const colors = ['#ff0000', '#00ff00', '#0000ff', '#ffff00', '#ff00ff'];

            function createParticle(x, y) {
                const color = colors[Math.floor(Math.random() * colors.length)];
                const size = Math.random() * 5 + 2;
                const speedX = Math.random() * 4 - 2;
                const speedY = Math.random() * 4 - 2;
                particles.push({ x, y, size, color, speedX, speedY });
            }

            function updateParticles() {
                for (let i = particles.length - 1; i >= 0; i--) {
                    const p = particles[i];
                    p.x += p.speedX;
                    p.y += p.speedY;
                    p.size *= 0.95;
                    if (p.size < 0.5) {
                        particles.splice(i, 1);
                    }
                }
            }

            function drawParticles() {
                ctx.clearRect(0, 0, canvas.width, canvas.height);
                for (const p of particles) {
                    ctx.beginPath();
                    ctx.arc(p.x, p.y, p.size, 0, Math.PI * 2);
                    ctx.fillStyle = p.color;
                    ctx.fill();
                }
            }

            function loop() {
                updateParticles();
                drawParticles();
                requestAnimationFrame(loop);
            }

            canvas.addEventListener('click', (e) => {
                for (let i = 0; i < 50; i++) {
                    createParticle(e.clientX, e.clientY);
                }
            });

            loop();
        </script>
        """,
        height=300,
    )

    # Header
    st.markdown('<div class="header">Welcome to The Elite Bank</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="subheader">Hello, {current_user}! Your balance is ${user_data["balance"]}</div>', unsafe_allow_html=True)

    # Adds columns for a clean layout
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.image("https://via.placeholder.com/400x200", use_container_width=True)

    # Quick Actions
    st.markdown("### Quick Actions")
    col1, col2 = st.columns(2)

    with col1:
        if st.button("View Savings"):
            st.write(f"Savings details for {current_user} will be displayed here.")

    with col2:
        if st.button("Transfer Funds"):
            st.write(f"Transfer funds functionality for {current_user} will be implemented here.")

    # Logout button
    if st.button("Logout"):
        st.session_state["logged_in"] = False
        st.session_state["current_user"] = None
        st.experimental_rerun()

# adds a stylish header
st.markdown(
    """
    <style>
    .header {
        font-size: 40px;
        font-weight: bold;
        color: #4CAF50;
        text-align: center;
        margin-bottom: 20px;
    }
    .subheader {
        font-size: 20px;
        color: #555;
        text-align: center;
        margin-bottom: 40px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="header">Welcome to The Elite Bank</div>', unsafe_allow_html=True)
st.markdown('<div class="subheader">Your trusted partner in financial management</div>', unsafe_allow_html=True)

# Adds a footer
st.markdown(
    """
    <style>
    .footer {
        font-size: 14px;
        color: #aaa;
        text-align: center;
        margin-top: 50px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="footer">© 2025 Bank App. All rights reserved.</div>', unsafe_allow_html=True)
