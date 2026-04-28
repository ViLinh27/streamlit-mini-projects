'''
9.11 Multiple topic (multi room) chat

builds upon 9.9 and 9.10,
exapnds chat example so that users can communicate with multiple chat threads,
all in the same interface ( a lot like a simple web forum):

'''
import streamlit as st, sqlite3, datetime #,os ; os.remove('forum.db)

con=sqlite3.connect('forum.db')
cur=con.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS db(topic TEXT, messages TEXT)')

#st.set_page_config(layout='wide',page_title="Forum")

for row in cur.execute ('SELECT rowid, topic, messages FROM db'):
    st.subheader(row[1])
    with st.expander(''):
        col1,col2 = st.columns([3,2])
        with col1:
            st.text_area('topic', row[2], height=350, label_visibility='collapsed')
            