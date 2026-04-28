'''
9.10 chat room with database 

Builds on basic structure of previous chat room but saves data to single field in databse table,
better suited to prdouction use.

for real production environemnts, apps that build on these simple models are best migrated from sqlite to any multi user databse system like :
PostgresQL
MySQL
MSSQL
etc.

most SQL commands here of chat app should be familiar from prev examples

notice commented end of first line.
uncomment that part and run app again: this will completely delete database and start fresh
::that will cause save messages to be permanently lost though
'''

import streamlit as st, sqlite3, datetime#, os ; os.remove('chats.db')

con=sqlite3.connect('chats.db')
cur=con.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS db(messages TEXT)')

col1, col2=st.columns([2,3])#you enter the message in col1 and col2 is where we see the chat
with col2:
  msg=cur.execute('SELECT messages FROM db').fetchone()#retrieves row from db
  if msg==None:
    cur.execute('INSERT INTO db(messages) VALUES ("")')
    con.commit()#save to database
  st.text_area('msg', msg[0], height=350, label_visibility='collapsed')#show messages from db

with col1:
  with st.form('New Message', clear_on_submit=True):
    name=st.text_input('Name')
    message=st.text_area('Message') 
    timestamp=datetime.datetime.now()

    if st.form_submit_button('Add Message'):
      newmsg=f'---  {name}   {timestamp}\n\n{message}\n\n{msg[0]}'
      print('debug: '+newmsg)#debug
      cur.execute(
        'UPDATE db SET messages=? WHERE rowid=?;', 
        (newmsg, 1)
      )
      con.commit()
      st.rerun()
