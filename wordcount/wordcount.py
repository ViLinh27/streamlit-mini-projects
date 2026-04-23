'''
from streamlitpython.com
9.4 Word Count
example splits text entered into an st.text_area widget,
and displays count of values in list using st.write widget
'''

import streamlit as st

text = st.text_area("Type or paste some text here please")
st.write('Click outside the text area to see the word count')
if text: 
    words = text.split()
    st.write(f'Number of words in your text:\n\n{len(words)}')
    