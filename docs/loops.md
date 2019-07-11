# Loops

This section covers Python's ability to loop/iterate over iterables.
An iterable can be anything, you can iterate over, e.g. lists, dicts, sets, ranges.


## for-Loop

Python's `for`-loop is used to perform *definite iterations*.
A definite iteration is an iteration, in which the number of repetitions is specified explicitly in advance.
Let's assume we have a list of names and we want to print each name on a different line.
We could do so, by using a `for`-loop.

```python
>>> names = ["Michael", "Florian", "Anna", "Sabrina"]
>>> for name in names:
...     print(name)
...
Michael
Florian
Anna
Sabrina
```

If you want to print all numbers in a certain range, you can make use of the built-in `range` function.

```python
>>> for i in range(3):
...     print(i)
...
0
1
2
```


## while-Loop

Sometimes you need to perform *indefinite iterations*.
In contrast to definite iterations the number of times the loop is executed isn’t specified explicitly in advance.
Rather, the designated block is executed repeatedly as long as some condition is met.

```python
>>> x = 5
>>> while x > 1:
...     print(x)
...     x -= 1
...
5
4
3
2
```

> **Note:** Loops can be nested as well!
> But as with conditional statements, keep in mind that this decreases code readability.


## Further Resource

- [Python "for" Loops (Definite Iteration)](https://realpython.com/python-for-loop/)
- [Python "while" Loops (Indefinite Iteration)](https://realpython.com/python-while-loop/)
- [How to Iterate Through a Dictionary in Python](https://realpython.com/iterate-through-dictionary-python/)
