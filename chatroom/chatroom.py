'''
9.9 chat room
Message data saved to text file

Bare bones chat room app. 
Users can type their name and a message, and info is posted to be read and responded to by any
other users running the app. There's a timestamp on each post.

Consider:
Message posts written to single file=> any users trying to write to file at same time, could mean corrupted file
This app is meant to demo simple streamlit interface patterns. Not for porduction use.

Examples after follow patterns similar to this one but write to a databse, so better for production use.

label_visibility in the st.text_area() method, this hides the default label above text widget.

st.column(), 
st.text_input(), 
st.form(), 
st.form_submit_button(), and 
st.rerun() 
methods are all the streamlit code needed to make this app work
'''

import streamlit as st, datetime
# import os; os.remove('chat.txt')
# Uncomment line above to delete file containing all messages, and start over with fresh chat room

col1, col2=st.columns([2,3])
with col2:
    with open('chat.txt', 'a+') as file: pass
    with open('chat.txt', 'r+') as file:
        mag = file.read()
        st.text_area('mag', mag, height=350, label_visibility='collapsed')

with col1:
    with st.form('New Message', clear_on_submit=True):
        name=st.text_input('Name')
        message = st.text_area('Message')
        timestamp = datetime.datetime.now()
        if st.form_submit_button('Add Message'):
            newmessage = f'--- {name} {timestamp}\n\n{message}\n\n{mag}'
            with open('chat.txt', 'w') as file:
                file.write(newmessage)
            st.rerun()

