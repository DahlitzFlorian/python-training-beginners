# Exception Handling

Once in a while you may come across *Exception*.
Per definition an exception is an event, which occurs during the execution of a program, that disrupts the normal flow of the program's instructions.
For instance if you try to read data from a file, which does not exist, a `FileNotFoundError` occurs.
However, you don't want your program to crash and provide an alternative if the file does not exist.

There exist two approaches to accomplish that.
First of all you could check, whether the file exists, and if so, open it.
This is the recommended way.
However, you could also catch the `FileNotFoundError` exception if it occurs and handle it properly using a `try-except`-statement.


## try-except

Python tries to execute the statements contained in the `try`-block.
If the execution fails/is interrupted by an exception, the `try`-block is left and the following `except`-block (if existent) is entered.

```python
try:
    f = open("some_non-existent_file.txt")
except FileNotFoundError:
    print("A FileNotFoundError occured!")
    # do something to handle it properly
```

If you don't specify an exception name like `FileNotFoundError` and leave it empty, all types of exceptions will be catched.
However, this is **not** recommended as it silences all exceptions!


## else-Clause

You can add an `else`-clause to a `try`-statement as well.
Note, that this is optional.
The `else`-clause will be executed if no exception occured.


## finally-Clause

Last but not least a `finally`-clause can be added to the `try`-statement.
Again, this is optional.
The `finally`-clause is always executed at the end of a `try`-statement (so after the `try`-, `except`-, and `else`-clause).
You can use it to ensure, that a certain value is always present or an opened file is always closed afterwards.


## Further Resources

- [Python Exceptions: An Introduction](https://realpython.com/python-exceptions/)
- [Python Exception Handling - Try, Except and Finally](https://www.programiz.com/python-programming/exception-handling)
