# Unclosed File Handle Bug in Python

This repository demonstrates a common, yet subtle, bug in Python: forgetting to close a file handle after opening it.  This can lead to resource leaks and potential data corruption.

The `unclosed_file.py` file shows the problematic code. The `closed_file.py` file shows the corrected code with proper error handling and resource management.  The bug is that the file opened within `function_with_unclosed_file` is not explicitly closed, leading to a resource leak if an exception occurs.