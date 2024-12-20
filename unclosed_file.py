def function_with_unclosed_file(filename):
    f = open(filename, 'w')
    # ... some code that might raise an exception ...
    # Forgot to close the file
    # ... more code ...

#Example call
function_with_unclosed_file('my_file.txt')