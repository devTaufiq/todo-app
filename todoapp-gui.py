import functions
import FreeSimpleGUI as sg

text = sg.Text("Type your to-do:")
input_box = sg.InputText(tooltip= "Todo.", key="todo")
add_button = sg.Button("Add")

window = sg.Window('My To-do App', layout=[[text], [input_box, add_button]])

while True:
    event, value = window.read()
    match event:
        case "Add":
            todos = functions.get_todos()
            todos.append(value['todo'].capitalize() + '\n')
            functions.write_todos(todos)
        case sg.WINDOW_CLOSED:
            break

window.close()

