# Python: A Big Picture

## What is Python?

Python is a programming language that is **dynamically-typed** and **interpreted**.

**Dynamically-typed**: we do not need to specify in advance what kind of data variables are going to kkhold. Type-checking happens at runtime instead of compile time.

**Interpreted**: we don't need to compile the code before running it. It is very easy to prototype and test code changes.

This is why Python is extensively used in Data Science and Machine Learning - to allow quick code changes and testing.

Being interpreted means that code runs slower. But libraries usually have code written in a low-level language (like C/C++) and bindings in Python.

Python is a **multi-paradigm** programming language. You can use it to write code that is object-oriented, structure-oriented, or even functional.

## Python Versions

You will hear about two versions of Python: 2.x and 3.x. Since January 1, 2020 the Python Software Foundation stopped supporting version 2.x.

## How to Run Python Programs

There are many different ways of running pieces of code written in Python with the technology available today. We will look at most of these ways later in the course. For now, to make our lives easy, we will run Python programs on our pesonal laptops with the Python interpreter.

## Libraries

One of the best things about Python is the amount of libraries available. For almost anything you'll ever need, there will be a library available.

We will use the pip package manager for Python to install any external libraries we'll need. Using pip is as simple as:

```
pip install <package_name>
```

## Reading Documentation

When you want to do something but can't figure out how, the best place to look is the documentation.

It could be [Python's documentation](https://docs.python.org/3/) or the documentation of a library you're using.

Learning how to read and navigate documentation is an invaluable skill! We will help you build this skill throughout this course.

## Using Google

When you have read the documentation and can't find what you need, it is time to Google it!

However, most of the times the answer you get from a Google search won't directly answer the question you might have. You will have to read and understand what you find and then apply it to your specific situation.

## Pulse Check - How Much Do You Already Know?

If you've already worked with any kind of programming language, you must have encountered some of these:

- Operators (arithmetic, assignment, conditional, etc.)
- Functions
- Comments (single and multiline)
- Branching (if/else if/else)
- Loops
- Data types (int, float, boolean)

## Installing Python on Windows

1. Install Visual Studio Code if there is no editor you are already using. That's our editor of choice.
1. Download the latest version of Python 3.x from https://www.python.org/downloads (Links to an external site.) and install it. Be sure to check the box that says to add Python 3.x to your path.
1. In your PowerShell (Terminal) program, run python. You run things in Terminal by just typing the name and pressing Enter. If you type python and it does not run, then you have to reinstall Python and make sure you check the box for “Add python to the PATH.” It’s very small so look carefully.
1. Type `quit()`, and press Enter to exit python.
1. You should be back at a prompt similar to what you had before you typed python.

## Get familiar with the Command Line interface

- Learn how to make a directory in the PowerShell (Terminal).
- Learn how to change into a directory in the PowerShell (Terminal).
- Use your editor to create a file in this directory. Make the file, Save or Save As..., and pick this directory.
- Go back to PowerShell (Terminal) using just the keyboard to switch windows.
- Back in PowerShell (Terminal), list the directory to see your newly created file.

## Simple Python programs to try out
- Display "Hello, World!"
- Check if a number is even
- Print the factorial of a number
- Count the number of vowels in a string

## Resources

- Python built-in functions: https://docs.python.org/3/library/functions.html
- [Learn Python 3 The Hard Way](https://shop.learncodethehardway.org/access/buy/9/)
