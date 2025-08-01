import functions
import time

date_time = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", date_time)
while True:
    user_input = input("Enter add, show, edit, complete or exit: ")
    user_input = user_input.lower()
    user_input = user_input.strip()

    todos = functions.get_todos()

    if user_input.startswith("add"):
        todo = user_input[4:]
        todos.append(todo.capitalize() + '\n')
    elif user_input.startswith("show"):
        for i, item in enumerate(todos):
            print(f"{i + 1}. {item.strip('\n')}")
    elif user_input.startswith("edit"):
        try:
            number = int(user_input[5:])
            if number - 1 <= len(todos):
                new_todo = input("Enter a new todo to edit: ")
                todos[number - 1] = new_todo.capitalize() + '\n'
        except ValueError:
            continue
        except IndexError:
            continue
    elif user_input.startswith("complete"):
        try:
            number = int(user_input[9:])
            print(f"'{todos[number - 1].strip('\n')}' has been removed from your list.")
            todos.pop(number - 1)
        except ValueError:
            continue
        except IndexError:
            continue
    elif user_input.startswith("exit"):
        break
    else:
        print("Please enter a valid input.")

    functions.write_todos(todos)

print("Thank you for using TodoApp.")
