FH = "todo-lists.txt"

def get_todos(filepath=FH):
    """" read a text file and return the list of to-do items"""
    with open(filepath,'r') as file_local:
        todo_local = file_local.readlines()
    return todo_local 

def write_todos(todos_arg, filepath=FH):
    """"" write the to-do items in the text file"""
    with open(filepath,'w') as file:
        file.writelines(todos_arg)
if __name__ == "__main__":
    print("Hello World")
    print(get_todos)
    