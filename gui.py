import functions
import FreeSimpleGUI as sg

label = sg.Text("Enter a task")
input_box = sg.InputText(tooltip="Enter Task")
add_button = sg.Button("Add")

window = sg.Window('Planner App', layout=[[label], [input_box, add_button]], resizable=True)
window.read()
window.close()