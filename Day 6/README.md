# Iterators, Generators, Decorators & Context Managers

## Introduction

This program demonstrates four useful Python concepts:Iterators, Generators, Decorators, and Context Managers. The examples are kept simple to understand how each concept works and where it can be useful.

## Topics Covered

- Iterators
- Generators
- Decorators
- Function execution timing
- Context Managers
- Custom Context Managers
- Exception Handling
- Timer using `@contextmanager`

## 1. Iterators

An iterator is used to access elements one at a time. Python provides `iter()` and `next()` functions to work with iterators.

Custom iterators can also be created using `__iter__()` and `__next__()` methods.

- `__iter__()` returns the iterator object.
- `__next__()` gives the next element.
- `StopIteration` is raised when there are no more elements.
- Iterators are useful when we want to process data one item at a time.

## 2. Generators

Generators are a simple way to create iterators. They use the `yield` keyword to produce values one at a time.

When `yield` is executed, the function pauses and continues from the same position when the next value is requested.

- Generators use `yield`.
- Values are produced one at a time.
- They use less memory.
- They are useful for handling large amounts of data.
- They support lazy evaluation.

## 3. Decorators

A decorator is used to add extra functionality to an existing function without changing its original code.

Python provides the `@` syntax to apply a decorator to a function.

- Decorators modify or extend function behavior.
- They commonly use a wrapper function.
- The original function does not need to be changed.

## 4. Context Managers

Context managers are used to manage resources properly. They are commonly used while working with files.

The `with` statement automatically handles the resource and makes sure it is properly closed after the work is completed.

- Context managers help manage resources safely.
- They are commonly used for file handling.
- The `with` statement automatically performs cleanup.
- They reduce the need to manually close resources.

## 5. Custom Context Manager

Python also allows us to create our own context managers using `__enter__()` and `__exit__()`.

### `__enter__()`

- It runs when the `with` block starts.
- It can be used to prepare a resource or perform setup.

### `__exit__()`

- It runs when the `with` block ends.
- It can be used for cleanup.
- It also receives information about exceptions that occur inside the block.
### Execution Flow
- The context manager is created.
- `__enter__()` is called.
- The code inside the `with` block is executed.
- `__exit__()` is called.
- The context is closed.

## 6. Exception Handling

The `__exit__()` method can receive information about an exception that occurs inside the `with` block.

It receives three values:

- `exc_type` stores the type of exception.
- `exc_value` stores information about the exception.
- `tb` stores traceback information.

If there is no exception, these values are `None`.

The `__exit__()` method can also decide whether an exception should be suppressed.

## 7. Timer Using `@contextmanager`

A timer context manager is created using the `@contextmanager` decorator from Python's `contextlib` module.

It is used to measure how much time a particular block of code takes to execute.

### Timer Working

- The starting time is recorded.
- The context manager reaches `yield`.
- The code inside the `with` block runs.
- The context manager continues after the block finishes.
- The ending time is recorded.
- The total execution time is calculated and displayed.

The output depends on how long the code inside the `with` block takes to execute. For example:

`Time: 5.0002s`

The exact time may be slightly different on different systems.

## Summary

This program gives understanding of following concepts:

- Iterators produces values all at once.
- Generators produce values one at a time and everytime we use next method it starts from the beginning
- Decorators add extra features to functions.
- Context managers handle resources safely.
- Timers helps us to measure execution time of the program.