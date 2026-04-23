'''
9.8 Markdown editor

simple editor that allows user to enter text with markdown tags
into st.text_area() widget and displays visual result using
st.markdown() widget.

'''

import streamlit as st, sqlite3

con= sqlite3.connect('markdown.db')
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS db(name TEXT, code TEXT)")

### From the earlier project
code = st.text_area('Enter text to turn into markdown here please')

st.write("Make sure to add the appropriate tags to your text so the editor knows how to style the markdown.")
st.write("Click outside the text are to see your markdown. ")
if code:
    st.markdown(code)
### From the earlier project

if st.button('Add new Row'):
    cur. execute('INSERT INTO db (name, code) VALUES(?,?)', ('',''))
    con.commit()

for row in cur.execute('SELECT rowid, name, code FROM db ORDER BY name '):
    with st.form(f'ID-{row[0]}'):
        name=st.text_input('Name', row[1])
        code = st.text_area('Code', row[2])
        if st.form_submit_button('Save and View'):
            cur.execute(
                'UPDATE db SET name=?, code=? WHERE rowid=?;',
                (name, code, str(row[0]))
            )
            con.commit(); st.rerun()#st.experimental_rerun() got deprecated, st.rerun() is the new way to do it. It will rerun the script from the top, so any changes will be reflected immediately.
        if st.form_submit_button("Delete"):
            cur.execute(f'DELETE FROM db WHERE rowid="{row[0]}"')
            con.commit() ; st.rerun()
        st.markdown(code)
