'''Write a function that performs the following tasks:
Accepts a list and an index as input.
Attempts to access the element at the given index in the list.
Handles both IndexError
Uses a finally block to print "Task completed" regardless of whether an exception
occurred or not.'''


def list_element(list_1, index):
    try:
        element = list_1[index]
        print(element)
    except IndexError as e:
        print(f"Error: {e}")
    finally:
        print("Task completed")
