# Data Types

This section covers Python's basic data types such as numeric (`int` and `float`), string (`str`) and boolean (`bool`) types as well as a few more complex data structures, which are essential for programming in Python: Lists (`list`), Tuples (`tuple`), Dictionaries (`dict`), and Sets (`set`).


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


## More Complex Data Structures


### Lists

A list is a set of elements.
It doesn't matter of which type the elements inside the list are (integer, string, boolean).
Another important note is, that lists remember the order of the elements they contain.
So if I have a list of the numbers from 1 to 9 as shown in the following example, the number 1 remains at the first position, the number 2 at the second and so on.

```python
>>> x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> x
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> x
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> x
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```

You can add a new element to the list by using the `append` method, and remove the last element by using `pop`.

```python
>>> x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> x.append("dog")
>>> x
[1, 2, 3, 4, 5, 6, 7, 8, 9, "dog"]
>>> x.pop()
'dog'
>>> x
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```

> **Note:** `pop` does not only remove the last element of the list, but returns it, too.

If you want to learn more about lists and operations you can perform on them, have a look at the resources provided below.


### Tuples

Tuples are similar to lists, except that they are *immutable*.
That means, that after they've been created, you are not able to modify them anymore.
To illustrate that further: After creating a list, which are *mutable*, you can append another element to the list or remove an element.
If you have created a tuple, you cannot modify it.

```python
>>> x = (1, 2, "Hello World", 6)
>>> x
(1, 2, 'Hello World', 6)
>>> x.append(5)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'tuple' object has no attribute 'append'
>>> x[1] = 4
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
```

As you can see, if we try to modify a tuple, we get an error.
First I tried to use the `append` method (as with lists) and got an `AttributeError`, which tells me, that this method is not implemented for tuples.
So I've tried to modify the element at index 1 (in this case the number 2 as Python starts counting at index 0) using the index operator `[]`, I've got a `TypeError`, which tells me, that item assignments are not supported.

In the [Further Resources](#further-resources) section you'll find a pretty good article giving a full introduction into Python lists and tuples, and comparing both data structures.


### Dictionaries

Python's dictionaries are comparable with Hash Maps in other programming languages (like Java).
The idea is to save elements together with their corresponding keys in an unordered data structure.
You can now access the elements inside the map/dictionary by using the corresponding key.

> **Analogy:** You can think of a Python's dictionary as a normal dictionary, where you look up translations of definitions.
> Using a normal dictionary you access the translations or definitions by specifying/searching for a key.

```python
>>> x = {"Poland": "Polen", "Germany": "Deutschland", "France": "Frankreich"}
>>> x
{'Poland': 'Polen', 'Germany': 'Deutschland', 'France': 'Frankreich'}
>>> x.get("France")
'Frankreich'
>>> x["Germany"]
'Deutschland'
>>> x.get("Sweden")
>>> x["Sweden"]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'Sweden'
>>> x.get("Sweden", "No translation found")
'No translation found'
```

In the example above we specify a new dictionary containing three country names and their german translation.
We try to access the german translation for the country *France* and get back *Frankreich*, which is indeed the german translation for *France*.
We used to `get` method, which is implemented for dictionaries.
After that, we tried to access the german translation for the country *Germany* by using the index operator `[]`.
This also worked.

If we try to access a countries translation, which is not part of the dictionary (in this case *Sweden*), nothing is returned and no exception is raised.
However, if we try to access the very same country using the index operator, a `KeyError` exception is raised.
The `get` method not only prevents us from catching an exception, but let's us also specify a default value, which is returned if the specified key has no corresponding value in the dictionary.

> **Note:** Dictionary keys can be of any type.
> The only limitation is, that they need to be *immutable*.
> So a tuple can be used as a dictionary key as well as an integer, a string or a boolean.
> However, a list cannot be used as a dictionary key.


### Sets

There are three main things you need to know about sets:

- Sets are unordered.
- Set elements are unique. Duplicate elements are not allowed.
- A set itself may be modified, but the elements contained in the set must be of an immutable type.

The first to statements are quite straightforward.
However, the third might not be.
It indicates, that only elements can be part of a set, which you are not able to modify - which are *immutable*.
Integers, booleans, strings and tuples are such candidates.
However, a list is not allowed to be part of a set as shown in the following examples block.

> **Note:** You might notice, that Python uses curly braces `{}` for defining sets as well.
> Be careful not to confuse them with dictionaries: Elements in a set do not have keys!

```python
>>> x = {1, 2, 3, "abc", (5, 6)}
>>> x
{1, 2, 3, 'abc', (5, 6)}
>>> x.add(9)
>>> x
{1, 2, 3, 'abc', (5, 6), 9}
>>> x.add([0, 4])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'
```

> **Note:** Don't get irritated by the fact, that the printed set in the REPL is ordered.
> Internally, sets are not ordered, however the REPL is able to print them in an ordered format.
> This is out of scope for this training.


## Further Resources

- [Real Python: Basic Data Types in Python][realpythondatatypes]
- [Python 3 Escape Sequences](https://www.quackit.com/python/reference/python_3_escape_sequences.cfm)
- [Lists and Tuples in Python](https://realpython.com/python-lists-tuples/)
- [Dictionaries in Python](https://realpython.com/python-dicts/)
- [Sets in Python](https://realpython.com/python-sets/)


[pep8]: https://www.python.org/dev/peps/pep-0008/
[realpythondatatypes]: https://realpython.com/python-data-types
