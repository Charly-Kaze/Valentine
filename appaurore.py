import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Valentine's Day", page_icon="❤️")

if 'answered' not in st.session_state:
    st.session_state.answered = False

if not st.session_state.answered:
    st.title("Will you be my Valentine? ❤️")
    
    st.image("Aurore.jpeg", width=200)

    # On crée une zone fixe pour les boutons
    col1, col2 = st.columns([1, 1])

    with col1:
        # Bouton OUI avec un style CSS pour forcer les dimensions
        st.markdown("""
            <style>
            div.stButton > button {
                width: 110px !important; height: 45px !important;
                background-color: #ff4d6d !important; color: white !important;
                font-size: 18px !important; font-weight: bold !important;
                border-radius: 8px !important; border: none !important;
            }
            </style>

        """, unsafe_allow_html=True)
        # Vrai bouton Streamlit (Infaillible)
        if st.button("Oui !", use_container_width=True):
            st.session_state.answered = True
            st.rerun()

    with col2:
        # Bouton Non en HTML avec des limites strictes
        no_button_html = """
        <div id="container" style="height: 100px; width: 100%; position: relative;">
            <button id="noBtn" style="
                position: absolute; 
                left: 10px; 
                top: 0px;
                padding: 10px 25px; 
                font-size: 16px; 
                background-color: #adb5bd; 
                color: white; 
                border: none; 
                border-radius: 8px; 
                cursor: pointer;
                font-weight: bold;
                transition: 0.1s;
            ">Non</button>
        </div>

        <script>
            const noBtn = document.getElementById('noBtn');
            const container = document.getElementById('container');

            noBtn.addEventListener('mouseover', () => {
                // On calcule des positions uniquement à l'intérieur du conteneur visible
                // pour qu'il ne disparaisse jamais de l'écran.
                const maxWidth = container.clientWidth - noBtn.clientWidth;
                const maxHeight = 250; // On lui donne une petite zone de saut

                const newX = Math.random() * maxWidth;
                const newY = (Math.random() * maxHeight) - 50;

                noBtn.style.left = newX + 'px';
                noBtn.style.top = newY + 'px';
            });
        </script>
        """
        components.html(no_button_html, height=1000)

else:
    # --- LA CÉLÉBRATION ---
    st.balloons()
    st.snow()
    st.balloons() # Double dose de ballons !
    st.title("YAY ! J'en étais sûre ! ❤️🎈")
    
    try:
        st.image("Aurore.jpeg", width=500)
    except:
        st.error("L'image 'Aurore.jpeg' est introuvable dans le dossier.")
    
    if st.button("Recommencer"):
        st.session_state.answered = False
        st.rerun()
