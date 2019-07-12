# General

This section covers all general things about Python and things, which do not belong to any of the other categories.


## Installation

I generally recommend installing Python via binary from [python.org](https://www.python.org/).
However, since Microsoft allows you to [install Python via the Windows Store](https://devblogs.microsoft.com/python/python-in-the-windows-10-may-2019-update/), it's highly recommended for Windows users to install Python this way.
There are a lot advantages of this approach.

> **Note:** As a Mac or Linux user, you may want to add the following alias to your `.bashrc` or `.zshrc` as most systems come with Python 2 installed by default and `python` points to the Python 2 installation:
>
> ```python
> alias python='python3'


## Read-Eval-Print Loop (REPL)

The Read-Eval-Print Loop (REPL) ships with your Python installation.
In fact, if you enter `python` in your console, the REPL should start.
The idea behind the REPL is, that you get immediate feedback about the commands you've entered.

Whenever you see `>>>` in the code examples, you can be sure, that the code is executed in the REPL.
Otherwise the code will be part of a script.

Example:

```python
>>> 5
5
```


## Execution

If you want to run a Python file via command-line, simply run:

```shell
$ python <filename>
```

E.g.:

```shell
$ python my_file.py
```


## Naming Conventions

[PEP 8](https://www.python.org/dev/peps/pep-0008/) is the *Style Guide for Python Code*.
It not only specifies code formatting and programming recommondations, but also [naming conventions](https://www.python.org/dev/peps/pep-0008/#naming-conventions).
You should definitely check it out.

> **Note:** As described in the previous paragraph, PEP 8 does also specify code formatting guidelines.
> However, if you want to use a code formatter, I can highly recommend [Black](https://github.com/python/black).


## Comments

To write a comment, just put a `#` symbol in front of it.
Everything after the `#` will be ignored (until the end of the line).
To write a multi-line comment, you can use Python's triple-quoted strings: `"""`.

```python
# Here's a single line comment
x = 5  # A single line comment after code

"""
This is
a multi-line comment
x = 3
"""
b = 9
```
