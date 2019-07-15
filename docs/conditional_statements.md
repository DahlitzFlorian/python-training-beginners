# Conditional Statements

A conditional statement, symbolized by p &rarr; q, is an if-then statement in which p is a hypothesis and q is a conclusion.
Let's have a look at some examples to illustrate it.


## if Statement

The most basic conditional statement is the `if`-statement with an `if`-clause only.
If the condition after the `if` keyword is true, the statements belonging to the `if`-block are executed.
Otherwise they are ignored.

```python
if 5 < 3:
    # The following statements are NOT executed
    x = 5
    print(x + 3)

print("Hello World")

if True:
    print("True is True, of course!")

print("End.")
```

If you execute the above example, you'll get:

```shell
Hello World
True is True, of course!
End.
```

`if`-statements can be arbitrarily nested as shown in the following example.

```python
x, y = 5, 3

if x == 5:
    if y == 3:
        print("x = 5 and y = 3")
    else:
        print("x = 5 but y != 3")
else:
    print("x != 5 and y != 3")
```

Keep in mind, that this decreases readability, so if you have many levels of nested `if`-statements, you may want to refactor you code.
With the above example in mind, let's assume you only care about the fact, that `x` is equal to `5` and `y` is equal to `3`.
You could combine it using the logical operator `and`.

```python
if x == 5 and y == 3:
    print("x = 5 and y = 3")
else:
    print("x != 5 and y != 3")
```

## else Clause

Optionally, you can append an `else`-clause to the `if`-clause, which is only executed if the condition belonging to the `if` is not `True`.

```python
if False:
    print("The condition is True!")
else:
    print("Sadly, the condition is False.")
```

Output:

```shell
Sadly, the condition is False.
```

> **Note:** There can only be one `else`-clause per `if`-statement.


## elif Statement

Sometimes it's helpful to check against another condition before you execute a default (`else`) case.
Luckily, Python provides us the `elif`-clause.
The statement belonging to `elif` is only evaluated if the initial `if` condition is `False`.

> **Note:** There can be an arbitrary number of `elif`-clauses per `if`-statement.
> They are evaluated from top-down until the first matches.

```python
x = 5

if x > 2 and x < 7:
    print("x is between 2 and 7 exclusively")
elif x > 2:
    print("x is greater than 6")  # The first condition is already evaluated as False, so if x is greater than 2 it has to be greater than 6 (>= 7)
else:
    print("x is smaller than 3")  # The first two conditions are already evaluated as False, so x has to be smaller than 3 (<= 2)
```

> **Note:** You can rewrite the first condition to:
> ```python
> if 2 < x < 7:
>     print("x is between 2 and 7 exclusively")
> ``
> That's the beauty of Python!


## Conditional Expression

A conditional expression is comparable to the ternary-operator, which you can find in other languages.
In it's simples form, the Python conditional expression (or conditional operator or ternary operator) looks like this:

```python
<expr1> if <conditional_expr> else <expr2>
```

`conditional_expr` is evaluated first.
If it evaluates to `True`, then `expr1` is evaluated and the program flow continues.
However, if it evaluates to `False`, then `expr2` is evaluated.

```python
>>> 5 if 5 < 3 else 3
3
>>> "Hello World" if True else False
'Hello World'
```

You can find more information about Python's conditional expression in the resources listed below.


## Further Resources

- [Conditional Statements in Python](https://realpython.com/python-conditional-statements/)
