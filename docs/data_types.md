# Data Types

This section covers Python's basic data types such as numeric (`int` and `float`), string (`str`) and boolean (`bool`) types as well as a few more complex data types, which are essential for programming in Python: Lists (`list`), Tuples (`tuple`), Dictionaries (`dict`), and Sets (`set`).


## Basic Data Types


### Integers

Whenever you want to represent integers in Python, the built-in `int` data type is used.
It's worth to note, that Python's `int` data type has effectively no limit - though it's limited by the amount of available memory.

Examples of integers: `1`, `2`, `9999999`, `-5000`.


### Floating-Point Numbers

Unlike other programming languages, Python has only one built-in data type to represent floating-point numbers: `float`.
You can create a floating-point number by using a decimal point or the scientific notation.

Examples: `4.3`, `4.3e-5` (= `0.000043`), `.5` (= `0.5`), `3.` (= `3.0`).


### Complex Number

Complex Numbers are beyond the scope of this training.
However, here is an example of a complex number representation in Python: `2+3j`.


### Strings

Everything surrounded by quotation marks is considered a string.
Python does't distiguish between single characters or a number of characters: They are all strings (type: `str`).
Please note, that it's not important whether you use single quotes `'` or double quotes `"` to mark something as a string.
Be sure to check out the examples below to get a sense of how both types of quotes behave if used together.

> **Note:** The official style guide for Python code is defined in [PEP 8][pep8].
> Although it doesn't make any recommondation, which type of quotes to use, it's common practise to use double quotes whenever possible.

The following examples are executed in the Python REPL.

```python
>>> "Hello World"
'Hello World'
>>> 'Hello World'
'Hello World'
>>> "Something with 'single quotes' in it."
"Something with 'single quotes' in it."
>>> 'Double quotes "surrounded" by single quotes'
'Double quotes "surrounded" by single quotes'
```

If you want to use double quotes inside a string surrounded by double quotes, you need to escape the inner double quotes as shown in the following example.

```python
>>> "I want to name my own Cafe \"Berlin Cafe\"."
'I want to name my own Cafe "Berlin Cafe".'
```

A list of escape sequences can be found in the [Further Resources](#further-resources) part of this section.

There exist a third way to define a string.
In this case you use triple quotes to surround a set of characters: `'''` or `"""`.
Strings created with triple quotes allow you to use quotes and the newline-character without escaping them.
To learn more about them, check out [this article][realpythondatatypes].


### Booleans

Booleans are quite easy to understand: The value is either `True` or `False`.
They are mostly used in conditional statements or to show, whether something exists or not.

```python
>>> x = True
>>> type(x)
<class 'bool'>
>>> x = False
>>> x
False
```


## More Complex Data Types


### Lists


### Tuples


### Dictionaries


### Sets


## Further Resources

- [Real Python: Basic Data Types in Python][realpythondatatypes]
- [Python 3 Escape Sequences](https://www.quackit.com/python/reference/python_3_escape_sequences.cfm)


[pep8]: https://www.python.org/dev/peps/pep-0008/
[realpythondatatypes]: https://realpython.com/python-data-types
