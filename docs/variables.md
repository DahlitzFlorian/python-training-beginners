# Variables

In this section you'll learn about variables in Python, how to assign values to them as well as assigning multiple values at once.


## Assignments

Defining a variable is as easy as:

```python
x = 5
```

Python doesn't care about the type of value you assign to a variable (at least not in these basic cases).
The following parts are executed in the Python REPL to get immediately the results of our commands.

```python
>>> x = 5
>>> x
5
>>> type(x)
<class 'int'>
>>> x = "Hello World"
>>> x
'Hello World'
>>> type(x)
<class 'str'>
```

Unlike other programming languages like C, we are not restricted to assign a number (an [integer][integer] = `int`) again to the variable `x`.
Instead we can assign a different type of value to our variable - in this case a string (= `str`).
Also note the usage of the built-in `type()` function.
With type you are able to get (as you might guess) the type of a variable or object.


## Multiple Assignments

Python allows you to assign multiple values to multiple variables at once:

```python
>>> x, y = 5, 6
>>> x
5
>>> y
6
```


[integer]: https://en.wikipedia.org/wiki/Integer
