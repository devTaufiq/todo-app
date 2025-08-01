FILEPATH = r"data\todos.txt"


def get_todos(filepath=FILEPATH):
    """ Read a text file and return a list of todos """
    with open(filepath, 'r') as file:
        todos = file.readlines()
    return todos


def write_todos(todos_local, filepath=FILEPATH):
    """Write a list of todos to a text file"""
    with open(filepath, 'w') as file:
        file.writelines(todos_local)

