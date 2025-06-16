def get_todolist(filepath='todolist.txt'):
    """
    Read a text file and return the list
    of items to do.
    """
    with open(filepath, 'r') as file_local:
        todo_list_local = file_local.readlines()
    return todo_list_local


def write_tolist(todo_list_local, filepath="todolist.txt" ):
    """
    Write the item in the text file.
    """
    with open(filepath, 'w') as file_local:
        file_local.writelines(todo_list_local)
