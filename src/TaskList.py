#Reference: https://stackoverflow.com/questions/15599639/what-is-the-perfect-counterpart-in-python-for-while-not-eof
def display_priority_list():
  print("\n----------------------")
  with open('urgent_list.txt') as file_reader:
    for line in file_reader:
        print(line)


def add_priority_task():
  file_writer = open("urgent_list.txt", mode="a")
  user_input = input("Enter your task. Press 'enter' to complete task\n")
  file_writer.write(user_input + "\n")
  file_writer.close()
  print("Task added")

def is_sure():
  user_input = input("Are you sure? Y/N\n")
  if (user_input.lower()) == 'y':
    return True
  else:
    return False 


#TODO: cleared items should go to completed list so user can view/recover them
      #or have a seperate option to complete all vs clear all

def clear_urgent_list():
  if (not is_sure()):
    return
  file_writer = open("urgent_list.txt", mode="w")
  file_writer.write("")
  file_writer.close()
  print("List cleared")

def clear_normal_list():
  if (not is_sure()):
    return
  file_writer = open("normal_list.txt", mode="w")
  file_writer.write("")
  file_writer.close()
  print("List cleared")

def list_options():
  print("Options: ")
  print("  1. Add urgent task")
  print("  2. Add normal task")
  print("  3. List all tasks")
  print("  4. List urgent tasks only")
  print("  5. List non-urgent tasks only")
  print("  6. Change an incomplete task to complete")
  print("  7. Change a normal task to urgent")
  print("  8. Change an urgent task to normal")
  print("  9. View completed tasks")
  print("  10. Add completed task to normal task list")
  print("  11. Clear normal list")
  print("  12. Clear urgent list")
  print("  13. Clear all lists")
  print("  Press e to exit")

  user_input = input()
#def take_user_input(user_input):
  match user_input:
    case '1':
      add_priority_task()
      return 0
    case '2':
      return 0
    case '3':
      return 0
    case '4':
      display_priority_list()
      return 0
    case '5':
      return 0
    case '6':
      return 0
    case '7':
      return 0
    case '8':
      return 0
    case '9':
      return 0
    case '10':
      return 0
    case '11':
      clear_normal_list()
      return 0
    case '12':
      clear_urgent_list()
      return 0
    case '13':
      if (not is_sure()):
        return 0
      clear_normal_list()
      clear_urgent_list()
      return 0
    case 'e':
      return 1
    case 'E':
      return 1
    case '_':
      return 0


print("\nHello!")
print("List of urgent tasks: ")
print("----------------------\n")
display_priority_list()

while(True):
  print("\n----------------------")
  user_input = list_options()
  if (user_input == 1):
    break
  else:
    continue




  







