import streamlit as st
import functions  # Your own module where `get_todos` and `write_todos` are defined

# Fetch existing todos from a file or storage
todos = functions.get_todos()

# Function to add a new todo
def add_todo():
    todo = st.session_state["new_todo"] + "\n"  # Get new todo from input field
    todos.append(todo)                          # Add it to the list
    functions.write_todos(todos)                # Save updated list to file

# Page Title and Description
st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")

# Display existing todos with checkboxes
for index, todo in enumerate(todos):
    # Show each todo with a checkbox
    checkbox = st.checkbox(todo, key=todo)

    if checkbox:
        # If checkbox is checked, remove the todo
        todos.pop(index)
        functions.write_todos(todos)           # Save updated list
        del st.session_state[todo]             # Remove it from Streamlit's state
        st.experimental_rerun()                # Rerun the app to update UI

# Input field to add a new todo
st.text_input(
    label="",                                 # No label text
    placeholder="Add new todo...",            # Placeholder shown inside input
    on_change=add_todo,                       # Function to run when user hits Enter
    key='new_todo'                            # Session key to track input
)
