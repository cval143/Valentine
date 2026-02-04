import streamlit as st

yay_photo_id = "12-clOZKGXgFvJI-GwI7R_nTxRQHyYJ70" 
yay_url = f"https://drive.google.com/uc?export=view&id={yay_photo_id}"

st.set_page_config(page_title="Special Delivery 💌", page_icon="💖")

# Initialize the stages 
if 'stage' not in st.session_state:
    st.session_state.stage = 'question'

#STAGE 1
if st.session_state.stage == 'question':
    st.markdown("<h1 style='text-align: center; color: #ff4b6b;'>I have a very important question...</h1>", unsafe_allow_html=True)
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHpueGZ3Ym9qZzR4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4JnBzYz0x/MDJ9uLGiTLBRC/giphy.gif")
    st.markdown("<h2 style='text-align: center;'>Will you be my Valentine? 🌹</h2>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("YES! 😍"):
            # Setting the stage name exactly how you wanted it
            st.session_state.stage = 'YAYYY GOOD CHOICE' 
            st.rerun()
    with col2:
        if st.button("No 🤥"):
            st.error("Wrong Answer, TRY AGAIN🙄")

# STAGE 2
elif st.session_state.stage == 'YAYYY GOOD CHOICE':
    st.balloons()
    st.markdown("<h1 style='text-align: center; color: #ff4b6b;'>YAYYY GOOD CHOICE!!</h1>", unsafe_allow_html=True)
    
    # This pulls your specific Google Drive photo
    st.image(yay_url, caption="Current Mood: Pure Joy! ✨", use_container_width=True)
    
    st.write("---") 
    st.markdown("<p style='text-align: center; font-size: 14px; color: #ff4b6b;'><b>Click below to continue...</b></p>", unsafe_allow_html=True)
    
    if st.button("See what's next? ✨"):
        st.session_state.stage = 'gift'
        st.rerun()

# STAGE 3
elif st.session_state.stage == 'gift':
    st.markdown("<h3 style='text-align: center;'>Since you said yes, here is your reward...</h3>", unsafe_allow_html=True)
    
    if st.button("🎁 OPEN YOUR GIFT 🎁"):
        st.snow()
        
        st.markdown("<h1 style='text-align: center; color: #ff4b6b;'>🎉 CONGRATULATIONS! 🎉</h1>", unsafe_allow_html=True)
        st.markdown("<h2 style='text-align: center;'>You have won a Million Kisses! 💋😘</h2>", unsafe_allow_html=True)
        st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHpueGZ3Ym9qZzR4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4JnBzYz0x/KztT2c4u8mYYUiMKdJ/giphy.gif")
