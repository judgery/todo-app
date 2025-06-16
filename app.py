# Build to-do list
# Store list in text file
# Display list to user
import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add') or user_action.startswith('new'):
        todo = user_action[4:]
        todo_list = functions.get_todolist()
        todo_list.append(todo + '\n')
        functions.write_tolist(todo_list)

    elif user_action.startswith ('show') or user_action.startswith ('display'):
        todo_list = functions.get_todolist()
        for index, item in enumerate(todo_list):
            item = item.strip('\n')
            row = f"{index+1}. {item.capitalize()}"
            print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1
            todo_list = functions.get_todolist()
            new_todo = input("Enter new task to do: ")
            todo_list[number] = new_todo + '\n'
            functions.write_tolist(todo_list)

        except ValueError:
            print("Your command is balls. Should be a number ya spastic /Burnsy")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])
            todo_list = functions.get_todolist()
            index = number -1
            todo_to_remove = todo_list[index].strip('\n')
            todo_list.pop(index)
            (functions.
             write_tolist(todo_list))

            message = f"Task {todo_to_remove} was removed!"
            print(message)
        except IndexError:
            print("There is no item with that number.")

    elif 'exit' in user_action:
        break
    else:
        print("Command is not valid, dickhead")

print("Bye!")
