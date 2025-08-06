import functions
import FreeSimpleGUI as sg

text = sg.Text("Type your to-do:")
input_box = sg.InputText(tooltip= "Todo.", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key="todos",
                      enable_events=True, size=(45, 10))
edit_button = sg.Button("Edit")

window = sg.Window('My To-do App', layout=[[text], [input_box, add_button],
                                           [list_box, edit_button]])

while True:
    event, value = window.read()
    print(event)
    print(value)
    match event:
        case "Add":
            todos = functions.get_todos()
            todos.append(value['todo'].capitalize() + '\n')
            functions.write_todos(todos)
            window['todos'].update(todos)
        case "Edit":
            todos = functions.get_todos()
            index = todos.index(value['todos'][0])
            new_todo = value['todo'] + '\n'
            todos[index] = new_todo.capitalize()
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "todos":
            todos = functions.get_todos()
            index = todos.index(value['todos'][0])
            todo = todos[index].strip('\n')
            window['todo'].update(todo)
        case sg.WINDOW_CLOSED:
            break

window.close()

