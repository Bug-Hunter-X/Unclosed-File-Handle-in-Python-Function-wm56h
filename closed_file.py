import os
def function_with_closed_file(filename):
    try:
        f = open(filename, 'w')
        # ... some code that might raise an exception ...
        f.write('This is some sample text.')
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if 'f' in locals() and f != None:
            f.close()

#Example call
function_with_closed_file('my_file.txt')

#Alternative using with statement for better resource management
def function_with_with_statement(filename):
    try:
        with open(filename, 'w') as f:
            f.write('This is some sample text.')
    except Exception as e:
        print(f"An error occurred: {e}")

# Example call
function_with_with_statement('my_file_2.txt')
