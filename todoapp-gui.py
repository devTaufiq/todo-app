import functions
import FreeSimpleGUI as sg

text = sg.Text("Type your to-do:")
input_box = sg.InputText(tooltip= "Todo.")
add_button = sg.Button("Add")

window = sg.Window('My TodoApp', layout=[[text], [input_box, add_button]])
window.read()
window.close()

