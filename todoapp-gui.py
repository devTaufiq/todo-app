import functions
import FreeSimpleGUI as sg
import time

sg.theme('LightGray1')
clock = sg.Text('', key='clock')
text = sg.Text("Enter your to-do:")
input_box = sg.InputText(tooltip= "Todo.", key="todo")
add_button = sg.Button("Add", size=(10))
list_box = sg.Listbox(values=functions.get_todos(), key="todos",
                      enable_events=True, size=(45, 10))
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit", size=(10))

window = sg.Window('My To-do App', layout=[[clock],
                                                [text],
                                                [input_box, add_button],
                                                [list_box, edit_button, complete_button],
                                                [exit_button]],
                                        font= ("Serif", 12))

while True:
    event, value = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case "Add":
            todos = functions.get_todos()
            todos.append(value['todo'].capitalize() + '\n')
            functions.write_todos(todos)
            window['todos'].update(todos)
        case "Edit":
            try:
                todos = functions.get_todos()
                index = todos.index(value['todos'][0])
                new_todo = value['todo'] + '\n'
                todos[index] = new_todo.capitalize()
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select a todo.")
        case "Complete":
            try:
                todos = functions.get_todos()
                index = todos.index(value['todos'][0])
                todos.pop(index)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value="")
            except IndexError:
                sg.popup("Please select a todo.")
        case "todos":
            todos = functions.get_todos()
            index = todos.index(value['todos'][0])
            todo = todos[index].strip('\n')
            window['todo'].update(todo)
        case "Exit":
            break
        case sg.WIN_CLOSED:
            break

window.close()

