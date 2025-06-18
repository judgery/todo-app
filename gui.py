import functions
import FreeSimpleGUI as sg

label = sg.Text("Enter a task")
input_box = sg.InputText(tooltip="Enter Task", key="todo")
add_button = sg.Button("Add")

window = sg.Window('Planner App',
                   layout=[[label], [input_box, add_button]],
                   font=('Arial', 12),
                   resizable=True)

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            tasks = functions.get_todolist()
            new_task = values['todo'] + "\n"
            tasks.append(new_task)
            functions.write_tolist(tasks)
        case sg.WIN_CLOSED:
            break

window.close()