import streamlit as st
import function 

todos= function.get_todos()

st.title("My Todo App")
st.subheader("Another shitty day started")
st.write("Let me see how much work I have to do")

for index,i in enumerate(todos):
    checkbox=st.checkbox(i, key=i)
    if checkbox:
        todos.pop(index)
        function.write_todos(todos)
        del st.session_state[i]
        st.experimental_rerun()


def add_todo():
    todo=st.session_state["new_todo"]+ "\n"
    todos.append(todo)
    function.write_todos(todos)

st.text_input(label="Add to-do", placeholder="More? God damn. Good luck bro",
              on_change=add_todo, key="new_todo")

