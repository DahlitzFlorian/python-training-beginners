# Functions

Reusing code is essential in programming.
That's why functions exist.
Functions are a convenient way to divide your code into useful blocks, allowing us to order our code, make it more readable, reuse it and save some time. Also functions are a key way to define interfaces so programmers can share their code.


## Defining a Function

Defining a function in Python is as easy as:

```python
def sample_function():
    print("Hello from a function!")
```

The function `sample_function` doesn't accept any parameters.
In fact, you can only call the function, which prints *Hello from a function!*
Calling the function is as easy as:

```python
sample_function()
```


## Positional Arguments

If you want your function to accept arguments, you can add them to the functions definition.

```python
def greet(name):
    print(f"Hello {name}!")
```

Calling the function with your name results in a simple greet to yourself:

```python
>>> greet("Florian")
Hello Florian!
```

> **Note:** Did you notice the little `f` in front of the string in the `print` function?
> This turns the string into an `f-string`.
> They exist since Python 3.6 and allow you to format strings in a pretty straightforward way.
> Before that, one made use of the built-in `format` method belonging to the `str` type.

This kind of arguments is called *positional arguments* as Python maps the values you provide to the accepting arguments by position.


## Keyword Arguments

Besides *positional arguments* Python has another type of arguments: *Keyword arguments*.
As the name suggests this means, that you specify a value for the argument using a keyword.
This allows you to specify default values if no value is provided for a certain argument as well as to provide values for the arguments independent from the position.

```python
>>> def greet(name="Sam", location="Hamburg"):
...     print(f"Hey {name}! You are from {location}, right?")
...
>>> greet()
Hey Sam! You are from Hamburg, right?
>>> greet(name="Florian")
Hey Sam! You are from Hamburg, right?
>>> greet(location="Berlin", name="Florian")
Hey Florian! You are from Berlin, right?
```


## Return Values

You can return any value/object from a function.
Simply use the `return` keyword:

```python
>>> def square(number):
...     return number ** 2
...
>>> square(4)
16
```


## Further Resources

- [How To Define Functions in Python 3](https://www.digitalocean.com/community/tutorials/how-to-define-functions-in-python-3)
