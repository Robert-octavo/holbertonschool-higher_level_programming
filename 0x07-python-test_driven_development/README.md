# **Python :snake: - Test-driven development**
## **Background Context**
Important notice on intranet checks for Python projects

Starting from today:

* Based on the requirements of each task, **you should always write the documentation (module(s) + function(s)) and tests first**, before you actually code anything
* The intranet checks for Python projects won’t be released before their first deadline, in order for you to focus more on TDD and think about all possible cases
* We strongly encourage you to work together on test cases, so that you don’t miss any edge case. **But not in the implementation of them!**
* **Don’t trust the user**, always think about all possible edge cases

# **Resources**
### **Read or Watch:**
* [Doctest -- Test interactive Python example (until “26.2.3.7. Warnings” included))](https://intranet.hbtn.io/rltoken/N5NE4DNMS6P9Pnky7Q9ijw)
* [Doctest -- Testing through documentation](https://intranet.hbtn.io/rltoken/cpEYbv_Z55QrSVRiuG5tUw)
* [Unit Test Python ](https://intranet.hbtn.io/rltoken/CELicn3K8hODQsWZak_h0g)

# **Learning Objectives**

At the end of this project, you are expected to be able to explain to anyone, **without the help of Google**:

# **General**

* Why Python programming is awesome
* What’s an interactive test
* Why tests are important
* How to write Docstrings to create tests
* How to write documentation for each module and function
* What are the basic option flags to create tests
* How to find edge cases

# **Requirements**
## **Python Scripts**

* Allowed editors: vi, vim, emacs
* All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.9)
* All your files should end with a new line
* The first line of all your files should be exactly #!/usr/bin/python3
* A README.md file, at the root of the folder of the project, is mandatory
* Your code should use the pycodestyle (version 2.8.*)
* All your files must be executable
* The length of your files will be tested using wc

## **Python Test Cases**

* Allowed editors: vi, vim, emacs
* All your files should end with a new line
* All your test files should be inside a folder tests
* All your test files should be text files (extension: .txt)
* All your tests should be executed by using this command: **python3 -m doctest ./tests/**
* All your modules should have a documentation *(python3 -c 'print(__import__("my_module").__doc__)')*
* All your functions should have a documentation *(python3 -c 'print(__import__("my_module").my_function.__doc__)')*
* A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
* We strongly encourage you to work together on test cases, so that you don’t miss any edge case – The Checker is checking for tests!

## **Example of Test**
*python3 -m doctest -v ./tests/5-text_indentation.txt*

for the unitest use:

*python3 -m unittest tests.6-max_integer_test 2>&1 | tail -1*
