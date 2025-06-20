import functions
import FreeSimpleGUI as sg
import time

sg.theme("DarkBlue")

clock = sg.Text("", key="clock")
label = sg.Text("Enter a task")
input_box = sg.InputText(tooltip="Enter Task", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todolist(),
                      key='todos',
                      enable_events=True, size=[35, 15])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window('Planner App',
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('Arial', 12),
                   resizable=True)

while True:
    event, values = window.read(timeout=500)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case "Add":
            tasks = functions.get_todolist()
            new_task = values['todo'] + "\n"
            tasks.append(new_task)
            functions.write_tolist(tasks)
            window['todos'].update(values=tasks)
        case "Edit":
            try:
                task_to_edit = values['todos'][0]
                new_task = values['todo'] + "\n"
                tasks = functions.get_todolist()
                index = tasks.index(task_to_edit)
                tasks[index] = new_task
                functions.write_tolist(tasks)
                window['todos'].update(values=tasks)
            except IndexError:
                sg.popup("Please select an item", font=('Arial', 12))

        case "Complete":
            try:
                task_to_complete = values['todos'][0]
                tasks = functions.get_todolist()
                tasks.remove(task_to_complete)
                functions.write_tolist(tasks)
                window['todos'].update(values=tasks)
                window['todo'].update(value="")
            except IndexError:
                sg.popup("Please select an item", font=('Arial', 12))
        case "Exit":
            break
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break

window.close()