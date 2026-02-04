import streamlit as st

# # Stage 0: Config
yay_photo = "yay.png" 

st.set_page_config(page_title="Special Delivery 💌", page_icon="💖")

if 'stage' not in st.session_state:
    st.session_state.stage = 'question'

# # Stage 1
if st.session_state.stage == 'question':
    st.markdown("<h1 style='text-align: center; color: #ff4b6b;'>I have a very important question...</h1>", unsafe_allow_html=True)
    
    st.image("https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExaGRmNXIyNmQ5bTQzOHdheTk1M2w0aHRtZXdnemkzaDZyMjZqajZrdSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/n3KZaXLYLuyNSHEvbm/giphy.gif", use_container_width=True)
    
    st.markdown("<h2 style='text-align: center;'>Will you be my Valentine? 🌹</h2>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("YES! 😍"):
            st.session_state.stage = 'YAYYY GOOD CHOICE'
            st.rerun()
    with col2:
        if st.button("No 🤥"):
            st.error("Wrong Answer, TRY AGAIN🙄")

# # Stage 2
elif st.session_state.stage == 'YAYYY GOOD CHOICE':
    st.balloons()
    st.markdown("<h1 style='text-align: center; color: #ff4b6b;'>YAYYY GOOD CHOICE!!</h1>", unsafe_allow_html=True)
    
    st.image(yay_photo, use_container_width=True)
    
    st.write("---") 
    st.markdown("<p style='text-align: center; font-size: 14px; color: #ff4b6b;'><b>Click below to continue...</b></p>", unsafe_allow_html=True)
    
    if st.button("See what's next? ✨"):
        st.session_state.stage = 'gift'
        st.rerun()

# # Stage 3
elif st.session_state.stage == 'gift':
    if 'opened' not in st.session_state:
        st.session_state.opened = False

    if not st.session_state.opened:
        st.markdown("<h3 style='text-align: center;'>Since you said yes, here is your reward...</h3>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: #ff4b6b;'><b>Click the gift to open it! 🎁</b></p>", unsafe_allow_html=True)
        
        if st.button("🎁 CLICK TO OPEN YOUR GIFT 🎁", use_container_width=True):
             st.session_state.opened = True
             st.rerun()
        
        st.image("https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExeWhtZWVueTJ3bm90NmoyaW9zN3hnNTVuNnJybGNyMGxvcTJrNjM1aSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3oz8xLdUxP6SpHwfzW/giphy.gif", use_container_width=True)

    else:
        st.balloons() # Confetti effect!
        st.markdown("<h1 style='text-align: center; color: #ff4b6b;'>🎉 CONGRATULATIONS! 🎉</h1>", unsafe_allow_html=True)
        st.markdown("<h2 style='text-align: center;'>You have won a Million Kisses! 💋😘</h2>", unsafe_allow_html=True)
        
        st.image("https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExMGh5OXd6c3ZhbHlzaW1jcHEyM241aDBoODlnM3VkYTRscWg1d253aSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3o6gb0SwNZElo5JhDy/giphy.gif", use_container_width=True)
        
        if st.button("Start Over? 🔄"):
            st.session_state.stage = 'question'
            st.session_state.opened = False
            st.rerun()
