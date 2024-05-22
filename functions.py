def get_todos(filepath='todos.txt'):
    """ Read a text file and return a list of to-do items """
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local


def write_todos(todos_local, filepath='todos.txt'):
    """ Write a to-do to a text file"""
    with open(filepath, 'w') as file:
        file.writelines(todos_local)


if __name__ == "__main__":
    print(get_todos())
