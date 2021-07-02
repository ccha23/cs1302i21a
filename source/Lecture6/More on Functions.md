---
jupytext:
  formats: ipynb,md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.12
    jupytext_version: 1.9.1
kernelspec:
  display_name: Python 3.7 (XPython)
  language: python
  name: xpython
---

+++ {"cell_style": "center", "slideshow": {"slide_type": "slide"}}

# More on Functions

+++ {"slideshow": {"slide_type": "-"}, "tags": ["remove-cell"]}

**CS1302 Introduction to Computer Programming**
___

```{code-cell}
---
slideshow:
  slide_type: fragment
tags: [remove-cell]
---
%reload_ext mytutor
```

+++ {"hide_input": true, "slideshow": {"slide_type": "slide"}}

## Recursion

+++ {"slideshow": {"slide_type": "fragment"}}

Consider computing the [Fibonacci number](https://en.wikipedia.org/wiki/Fibonacci_number) of order $n$:

$$
F_n := 
\begin{cases}
F_{n-1}+F_{n-2} & n>1 \kern1em \text{(recurrence)}\\
1 & n=1 \kern1em \text{(base case)}\\
0 & n=0 \kern1em \text{(base case)}.
\end{cases}$$
Fibonacci numbers have practical applications in generating [pseudorandom numbers](https://en.wikipedia.org/wiki/Lagged_Fibonacci_generator).

+++ {"slideshow": {"slide_type": "subslide"}}

**Can we define the function by calling the function itself?**

```{code-cell}
---
code_folding: []
jupyter:
  outputs_hidden: true
slideshow:
  slide_type: fragment
---
%%mytutor -r -h 450
def fibonacci(n):
    if n > 1:
        return fibonacci(n - 1) + fibonacci(n - 2)  # recursion
    elif n == 1:
        return 1
    else:
        return 0

fibonacci(2)
```

+++ {"slideshow": {"slide_type": "fragment"}}

[*Recursion*](https://en.wikipedia.org/wiki/Recursion_(computer_science)) is a function that calls itself (*recurs*).

+++ {"slideshow": {"slide_type": "subslide"}}

**Exercise** Write a function `gcd` that implements the [Euclidean algorithm for the greatest common divisor](https://en.wikipedia.org/wiki/Euclidean_algorithm): 

$$\operatorname{gcd}(a,b)=\begin{cases}a & b=0\\ \operatorname{gcd}(b, a\operatorname{mod}b) & \text{otherwise} \end{cases}$$

```{code-cell}
---
nbgrader:
  grade: false
  grade_id: gcd
  locked: false
  schema_version: 3
  solution: true
  task: false
slideshow:
  slide_type: '-'
---
%%mytutor -r -h 550
def gcd(a, b):
    ### BEGIN SOLUTION
    return gcd(b, a % b) if b else a
    ### END SOLUTION


gcd(3 * 5, 5 * 7)
```

+++ {"slideshow": {"slide_type": "subslide"}}

**Is recursion strictly necessary?**  

+++ {"slideshow": {"slide_type": "fragment"}}

No. We can always convert a recursion to an iteration.  
E.g., the following computes the Fibonnacci number of order using a while loop instead.

```{code-cell}
---
slideshow:
  slide_type: '-'
---
%%mytutor -r -h 550
def fibonacci_iteration(n):
    if n > 1:
        _, F = 0, 1  # next two Fibonacci numbers
        while n > 1:
            _, F, n = F, F + _, n - 1
        return F
    elif n == 1:
        return 1
    else:
        return 0
    
fibonacci_iteration(3)
```

```{code-cell}
# more tests
for n in range(5):
    assert fibonacci(n) == fibonacci_iteration(n)
```

+++ {"slideshow": {"slide_type": "fragment"}}

**Exercise** Implement `gcd_iteration` using a while loop instead of a recursion.

```{code-cell}
---
code_folding: []
nbgrader:
  grade: false
  grade_id: gcd_iteration
  locked: false
  schema_version: 3
  solution: true
  task: false
slideshow:
  slide_type: '-'
---
%%mytutor -r -h 550
def gcd_iteration(a, b):
    ### BEGIN SOLUTION
    while b:
        a, b = b, a % b
    return a
    ### END SOLUTION


gcd_iteration(3 * 5, 5 * 7)
```

```{code-cell}
---
jupyter:
  outputs_hidden: true
slideshow:
  slide_type: fragment
---
# test
for n in range(5):
    assert fibonacci(n) == fibonacci_iteration(n)
```

+++ {"slideshow": {"slide_type": "subslide"}}

**What is the benefit of recursion?**

+++ {"slideshow": {"slide_type": "fragment"}}

- Recursion is often shorter and easier to understand.
- It is also easier to write code by *wishful thinking* or *[declarative programming](https://en.wikipedia.org/wiki/Declarative_programming)*.

+++ {"slideshow": {"slide_type": "slide"}}

**Is recusion more efficient than iteration?**

+++ {"slideshow": {"slide_type": "fragment"}}

**Exercise** Find the smallest values of `n` for`fibonacci(n)` and `fibonacci_iteration(n)` respectively to run for more than a second.

```{code-cell}
---
jupyter:
  outputs_hidden: true
nbgrader:
  grade: false
  grade_id: fib_recursion
  locked: false
  schema_version: 3
  solution: true
  task: false
slideshow:
  slide_type: fragment
---
# Assign n
### BEGIN SOLUTION
n = 33
### END SOLUTION
fib_recursion = fibonacci(n)
```

```{code-cell}
---
jupyter:
  outputs_hidden: true
nbgrader:
  grade: false
  grade_id: fib_iteration
  locked: false
  schema_version: 3
  solution: true
  task: false
slideshow:
  slide_type: fragment
---
# Assign n
### BEGIN SOLUTION
n = 300000
### END SOLUTION
fib_iteration = fibonacci_iteration(n)
```

+++ {"slideshow": {"slide_type": "subslide"}}

To see why recursion is slow, we will modify `fibonacci` to print each function call as follows.

```{code-cell}
---
jupyter:
  outputs_hidden: true
slideshow:
  slide_type: '-'
---
def fibonacci(n):
    '''Returns the Fibonacci number of order n.'''
    print('fibonacci({!r})'.format(n))
    return fibonacci(n - 1) + fibonacci(n - 2) if n > 1 else 1 if n == 1 else 0


fibonacci(5)
```

+++ {"slideshow": {"slide_type": "fragment"}}

`fibonacci(5)` calls `fibonacci(3)` and `fibonacci(4)`, which in turn call `fibonacci(2)` and `fibonacci(3)`. `fibonacci(3)` is called twice.

+++ {"slideshow": {"slide_type": "slide"}}

## Global Variables

+++ {"slideshow": {"slide_type": "fragment"}}

Consider the problem of generating a sequence of Fibonacci numbers.

```{code-cell}
---
slideshow:
  slide_type: '-'
---
for n in range(5):
    print(fibonacci_iteration(n))
```

+++ {"slideshow": {"slide_type": "fragment"}}

**Is the above loop efficient?**

+++ {"slideshow": {"slide_type": "fragment"}}

No. Each call to `fibonacci_iteration(n)` recomputes the last two Fibonacci numbers $F_{n-1}$ and $F_{n-2}$ for $n\geq 2$.

+++ {"slideshow": {"slide_type": "fragment"}}

**How to avoid redundant computations?**

+++ {"slideshow": {"slide_type": "fragment"}}

One way is to store the last two computed Fibonacci numbers.

```{code-cell}
---
code_folding: []
jupyter:
  outputs_hidden: true
slideshow:
  slide_type: '-'
---
%%mytutor -h 600
def next_fibonacci():
    '''Returns the next Fibonacci number.'''
    global _Fn, _Fn1, _n  # global declaration
    value = _Fn
    _Fn, _Fn1, _n = _Fn1, _Fn + _Fn1, _n + 1
    return value

def print_fibonacci_state():
    print('''States:
    _Fn  : Next Fibonacci number      = {}
    _Fn1 : Next next Fibonacci number = {}
    _n   : Next order                 = {}'''.format(_Fn,_Fn1,_n))

# global variables for next_fibonacci and print_fibonacci_state
_Fn, _Fn1, _n = 0, 1, 0

for n in range(5):
    print(next_fibonacci())
print_fibonacci_state()
```

+++ {"slideshow": {"slide_type": "fragment"}}

Rules for [*global/local variables*](https://docs.python.org/3/faq/programming.html#what-are-the-rules-for-local-and-global-variables-in-python):
1. A local variable must be defined within a function.
1. An assignment defines a local variable except in a [`global` statement](https://docs.python.org/3/reference/simple_stmts.html#the-global-statement).

+++ {"slideshow": {"slide_type": "fragment"}}

**Why `global` is NOT needed in `print_fibonacci_state`?**

+++ {"slideshow": {"slide_type": "fragment"}}

Without ambiguity, `_Fn, _Fn1, _n` in `print_fibonacci_state` are not local variables by Rule 1 because they are not defined within the function.

+++ {"slideshow": {"slide_type": "fragment"}}

**Why `global` is needed in `next_fibonacci`?**

+++ {"slideshow": {"slide_type": "fragment"}}

What happens otherwise:

```{code-cell}
---
jupyter:
  outputs_hidden: true
slideshow:
  slide_type: '-'
---
def next_fibonacci():
    '''Returns the next Fibonacci number.'''
    # global _Fn, _Fn1, _n
    value = _Fn
    _Fn, _Fn1, _n = _Fn1, _Fn + _Fn1, _n + 1
    return value

next_fibonacci()
```

+++ {"slideshow": {"slide_type": "fragment"}}

Why is there an `UnboundLocalError`?

+++ {"slideshow": {"slide_type": "fragment"}}

- The assignment defines `_Fn` as a local variable by Rule 2.  
- However, the assignment requires first evaluating `_Fn`, which is not yet defined.

+++ {"slideshow": {"slide_type": "subslide"}}

**Are global variables preferred over local ones?**

+++

Suppose for aesthetic reasons we remove the underscores in global variable names?

```{code-cell}
---
code_folding: []
jupyter:
  outputs_hidden: true
---
%%mytutor -h 600
def next_fibonacci():
    '''Returns the next Fibonacci number.'''
    global Fn, Fn1, n
    value = Fn
    Fn, Fn1, n = Fn1, Fn + Fn1, n + 1
    return value

def print_fibonacci_state():
    print('''States:
    Fn  : Next Fibonacci number      = {}
    Fn1 : Next next Fibonacci number = {}
    n   : Next order                 = {}'''.format(Fn,Fn1,n))

# global variables renamed without underscores
Fn, Fn1, n = 0, 1, 0

n = 0
while n < 5:
    print(next_fibonacci())
    n += 1
print_fibonacci_state()
```

+++ {"slideshow": {"slide_type": "fragment"}}

**Exercise** Why does the while loop prints only 3 instead of 5 Fibonacci numbers?

+++ {"nbgrader": {"grade": true, "grade_id": "global_bug", "locked": false, "points": 0, "schema_version": 3, "solution": true, "task": false}, "slideshow": {"slide_type": "-"}}

There is a name collision. `n` is also incremented by `next_fibonacci()`, and so the while loop is only executed 3 times in total. 

+++ {"slideshow": {"slide_type": "fragment"}}

With global variables
- codes are less predictable, more difficult to reuse/extend, and
- tests cannot be isolated, making debugging difficult.

+++ {"slideshow": {"slide_type": "subslide"}}

**Is it possible to store the function states without using global variables?**

+++ {"slideshow": {"slide_type": "fragment"}}

Yes. We can use nested functions and [`nonlocal` variables](https://docs.python.org/3/reference/simple_stmts.html#grammar-token-nonlocal-stmt).

```{code-cell}
---
code_folding: []
jupyter:
  outputs_hidden: true
slideshow:
  slide_type: '-'
---
def fibonacci_closure(Fn, Fn1):
    def next_fibonacci():
        '''Returns the next (generalized) Fibonacci number starting with 
        Fn and Fn1 as the first two numbers.'''
        nonlocal Fn, Fn1, n  # declare nonlocal variables
        value = Fn
        Fn, Fn1, n = Fn1, Fn + Fn1, n + 1
        return value

    def print_fibonacci_state():
        print('''States:
        Next Fibonacci number      = {}
        Next next Fibonacci number = {}
        Next order                 = {}'''.format(Fn, Fn1, n))

    n = 0  # Fn and Fn1 specified in the function arguments
    return next_fibonacci, print_fibonacci_state


next_fibonacci, print_fibonacci_state = fibonacci_closure(0, 1)
n = 0
while n < 5:
    print(next_fibonacci())
    n += 1
print_fibonacci_state()
```

+++ {"slideshow": {"slide_type": "fragment"}}

The state variables `Fn, Fn1, n` are now *encapsulated*, and so    
the functions returned by `fibonacci_closure` no longer depends on any global variables.

+++ {"slideshow": {"slide_type": "subslide"}}

Another benefit of using nested functions is that we can also create different Fibonacci sequence with different base cases.

```{code-cell}
---
jupyter:
  outputs_hidden: true
slideshow:
  slide_type: '-'
---
my_next_fibonacci, my_print_fibonacci_state = fibonacci_closure('cs', '1302')
for n in range(5):
    print(my_next_fibonacci())
my_print_fibonacci_state()
```

+++ {"slideshow": {"slide_type": "fragment"}}

`next_fibonacci` and `print_fibonacci_state` are *local functions* of `fibonacci_closure`.  
- They can access (*capture*) the other local variables of `fibonacci_closure` by forming the so-called *closures*.
- Similar to the use of `global` statement, a [`non-local` statement](https://docs.python.org/3/reference/simple_stmts.html#the-nonlocal-statement) is needed for assigning nonlocal variables.

+++ {"slideshow": {"slide_type": "fragment"}}

Each local function has an attribute named `__closure__` that stores the captured local variables.

```{code-cell}
---
jupyter:
  outputs_hidden: true
slideshow:
  slide_type: '-'
---
def print_closure(f):
    '''Print the closure of a function.'''
    print('closure of ', f.__name__)
    for cell in f.__closure__:
        print('    {} content: {!r}'.format(cell, cell.cell_contents))


print_closure(next_fibonacci)
print_closure(print_fibonacci_state)
```

+++ {"slideshow": {"slide_type": "slide"}}

## Generator

+++ {"slideshow": {"slide_type": "fragment"}}

Another way to generate a sequence of objects one-by-one is to write a *generator*.

```{code-cell}
---
code_folding: []
jupyter:
  outputs_hidden: true
slideshow:
  slide_type: '-'
---
fibonacci_generator = (fibonacci_iteration(n) for n in range(3))
fibonacci_generator
```

+++ {"slideshow": {"slide_type": "fragment"}}

The above uses a [*generator expression*](https://docs.python.org/3/reference/expressions.html#grammar-token-generator-expression) to define `fibonacci_generator`.

+++ {"slideshow": {"slide_type": "subslide"}}

**How to obtain items from a generator?**

+++ {"slideshow": {"slide_type": "fragment"}}

We can use the [`next` function](https://docs.python.org/3/library/functions.html#next).

```{code-cell}
---
slideshow:
  slide_type: '-'
---
while True: 
    print(next(fibonacci_generator)) # raises StopIterationException eventually
```

+++ {"slideshow": {"slide_type": "fragment"}}

A generator object is [*iterable*](https://www.programiz.com/python-programming/iterator), i.e., it implements both `__iter__` and `__next__` methods that are automatically called in a `for` loop as well as the `next` function.

```{code-cell}
---
slideshow:
  slide_type: '-'
---
fibonacci_generator = (fibonacci_iteration(n) for n in range(5))
for fib in fibonacci_generator:  # StopIterationException handled by for loop
    print(fib)
```

+++ {"slideshow": {"slide_type": "subslide"}}

**Is `fibonacci_generator` efficient?**

+++ {"slideshow": {"slide_type": "subslide"}}

No again due to redundant computations.  
A better way to define the generator is to use the keyword [`yield`](https://docs.python.org/3/reference/expressions.html?highlight=yield#yield-expressions):

```{code-cell}
---
jupyter:
  outputs_hidden: true
---
%%mytutor -h 450
def fibonacci_sequence(Fn, Fn1, stop):
    '''Return a generator that generates Fibonacci numbers
    starting from Fn and Fn1 until stop (exclusive).'''
    while Fn < stop:
        yield Fn  # return Fn and pause execution
        Fn, Fn1 = Fn1, Fn1 + Fn


for fib in fibonacci_sequence(0, 1, 5):
    print(fib)
```

+++ {"slideshow": {"slide_type": "fragment"}}

1. `yield` causes the function to return a *generator* without executing the function body.
1. Calling `__next__` resumes the execution, which 
    - pauses at the next `yield` expression, or
    - raises the `StopIterationException` at the end.

+++ {"slideshow": {"slide_type": "fragment"}}

**Exercise** The yield expression `yield ...` is mistaken in [Halterman17] to be a statement. It is actually an expression because 
- The value of a `yield` expression is `None` by default, but 
- it can be set by the `generator.send` method.

Add the document string to the following function. In particular, explain the effect of calling the method `send` on the returned generator.

```{code-cell}
---
code_folding: []
jupyter:
  outputs_hidden: true
nbgrader:
  grade: false
  grade_id: send
  locked: false
  schema_version: 3
  solution: true
  task: false
slideshow:
  slide_type: '-'
---
%%mytutor -r -h 500
def fibonacci_sequence(Fn, Fn1, stop):
    ### BEGIN SOLUTION
    '''Return a generator that generates Fibonacci numbers
    starting from Fn and Fn1 to stop (exclusive). 
    generator.send(value) sets next number to value.'''
    ### END SOLUTION
    while Fn < stop:
        value = yield Fn
        if value is not None: 
            Fn1 = value  # set next number to the value of yield expression
        Fn, Fn1 = Fn1, Fn1 + Fn 
```

+++ {"slideshow": {"slide_type": "slide"}}

## Optional Arguments

+++

**How to make function arguments optional?**

```{code-cell}
def fibonacci_sequence(Fn=0, Fn1=1, stop=None):
    while stop is None or Fn < stop:
        value = yield Fn
        Fn, Fn1 = Fn1, Fn1 + Fn
```

```{code-cell}
for fib in fibonacci_sequence(0,1,5):
    print(fib)  # with all arguments specified
```

```{code-cell}
for fib in fibonacci_sequence(stop=5):
    print(fib)  # with default Fn=0, Fn1=1
```

+++ {"slideshow": {"slide_type": "fragment"}}

`stop=5` is called a [keyword argument](https://docs.python.org/3/glossary.html#term-keyword-argument). Unlike `positional arguments`, it specifies the name of the argument explicitly.

+++ {"slideshow": {"slide_type": "fragment"}}

**Exercise** `stop` is an [optional argument](https://docs.python.org/3/tutorial/controlflow.html#default-argument-values) with the *default value* `None`. What is the behavior of the following code?

```{code-cell}
---
slideshow:
  slide_type: '-'
---
for fib in fibonacci_sequence(5):
    print(fib)
    if fib > 10:  
        break  # Will this be executed?
```

+++ {"nbgrader": {"grade": true, "grade_id": "stop", "locked": false, "points": 0, "schema_version": 3, "solution": true, "task": false}, "slideshow": {"slide_type": "-"}}

With the default value of `None`, the while loop becomes an infinite loop. The generator will keep generating the next Fibonacci number without any bound on the order. In particular, `fibonacci_sequence(5)` creates an unstoppable (default) generator with base case `Fn=5` (specified) and `Fn1=1` (default).

+++ {"slideshow": {"slide_type": "subslide"}}

Rules for specifying arguments:
1. Keyword arguments must be after all positional arguments.
1. Duplicate assignments to an argument are not allowed.

+++ {"slideshow": {"slide_type": "fragment"}}

E.g., the following results in error:

```{code-cell}
---
slideshow:
  slide_type: '-'
---
fibonacci_sequence(stop=10, 1)
```

```{code-cell}
---
slideshow:
  slide_type: '-'
---
fibonacci_sequence(1, Fn=1)
```

+++ {"slideshow": {"slide_type": "subslide"}}

The following shows that the behavior of `range` is different.

```{code-cell}
---
slideshow:
  slide_type: fragment
---
for count in range(1, 10, 2):
    print(count, end=' ')  # counts from 1 to 10 in steps of 2
print()
for count in range(1, 10):
    print(count, end=' ')  # default step=1
print()
for count in range(10):
    print(count, end=' ')  # default start=0, step=1
range(stop=10)  # fails
```

+++ {"slideshow": {"slide_type": "fragment"}}

`range` takes only positional arguments.  
However, the first positional argument has different intepretations (`start` or `stop`) depending on the number of arguments (2 or 1).

+++ {"slideshow": {"slide_type": "fragment"}}

`range` is indeed NOT a generator.

```{code-cell}
---
jupyter:
  outputs_hidden: true
slideshow:
  slide_type: fragment
---
print(type(range),type(range(10)))
```

+++ {"slideshow": {"slide_type": "subslide"}}

## Variable number of arguments

+++ {"slideshow": {"slide_type": "fragment"}}

We can simulate the behavior of range by having a [variable number of arguments](https://docs.python.org/3.4/tutorial/controlflow.html#arbitrary-argument-lists).

```{code-cell}
---
slideshow:
  slide_type: fragment
---
def print_arguments(*args, **kwargs):
    '''Take any number of arguments and prints them'''
    print('args ({}): {}'.format(type(args),args))
    print('kwargs ({}): {}'.format(type(kwargs),kwargs))

print_arguments(0, 10, 2, start=1, stop=2)
print("{k}".format(greeting="Hello",k=8),"*"  )
```

+++ {"slideshow": {"slide_type": "fragment"}}

- `args` is a tuple of positional arguments.
- `kwargs` is a dictionary of keyword arguments.

+++ {"slideshow": {"slide_type": "fragment"}}

`*` and `**` are *unpacking operators* for tuple/list and dictionary respectively:

```{code-cell}
---
slideshow:
  slide_type: fragment
---
args = (0, 10, 2)
kwargs = {'start': 1, 'stop': 2}
print_arguments(*args, **kwargs)
```

The following function converts all the arguments to a string.  
It will be useful later on.

```{code-cell}
---
slideshow:
  slide_type: fragment
---
def argument_string(*args, **kwargs):
    '''Return the string representation of the list of arguments.'''
    return '({})'.format(', '.join([
        *['{!r}'.format(v) for v in args],  # arguments
        *['{}={!r}'.format(k, v)
          for k, v in kwargs.items()]  # keyword arguments
    ]))

argument_string(0, 10, 2, start=1, stop=2)
```

+++ {"slideshow": {"slide_type": "subslide"}}

**Exercise** Redefine `fibonacci_sequence` so that the positional arguments depend on the number of arguments:

```{code-cell}
---
code_folding: [19]
nbgrader:
  grade: false
  grade_id: optional
  locked: false
  schema_version: 3
  solution: true
  task: false
slideshow:
  slide_type: '-'
---
def fibonacci_sequence(*args):
    '''Return a generator that generates Fibonacci numbers
    starting from Fn and Fn1 to stop (exclusive). 
    generator.send(value) sets next number to value.
    
    fibonacci_sequence(stop)
    fibonacci_sequence(Fn,Fn1)
    fibonacci_sequence(Fn,Fn1,stop)
    '''
    Fn, Fn1, stop = 0, 1, None  # default values

    # handle different number of arguments
    if len(args) is 1:
        ### BEGIN SOLUTION
        stop = args[0]
        ### END SOLUTION
    elif len(args) is 2:
        Fn, Fn1 = args[0], args[1]
    elif len(args) > 2:
        Fn, Fn1, stop = args[0], args[1], args[2]
    
    while stop is None or Fn < stop:
        value = yield Fn
        if value is not None: 
            Fn1 = value  # set next number to the value of yield expression
        Fn, Fn1 = Fn1, Fn1 + Fn
```

```{code-cell}
---
slideshow:
  slide_type: fragment
---
for fib in fibonacci_sequence(5): # default Fn=0, Fn=1
    print(fib)
```

```{code-cell}
---
slideshow:
  slide_type: fragment
---
for fib in fibonacci_sequence(1, 2): # default stop=None
    print(fib)  
    if fib>5:
        break
```

```{code-cell}
---
slideshow:
  slide_type: fragment
---
args = (1, 2, 5)
for fib in fibonacci_sequence(*args): # default stop=None
    print(fib) 
```

+++ {"slideshow": {"slide_type": "slide"}}

## Decorator

+++ {"slideshow": {"slide_type": "subslide"}}

**What is function decoration?**  
**Why decorate a function?**

```{code-cell}
---
jupyter:
  outputs_hidden: true
slideshow:
  slide_type: '-'
---
def fibonacci(n):
    '''Returns the Fibonacci number of order n.'''
    global count, depth
    count += 1
    depth += 1
    print('{:>3}: {}fibonacci({!r})'.format(count, '|' * depth, n))
    
    value = fibonacci(n - 1) + fibonacci(n - 2) if n > 1 else 1 if n == 1 else 0
    
    depth -= 1
    if depth is -1:  # recursion done
        print('Done')
        count = 0  # reset count for subsequent recursions
    return value


count, depth = 0, -1
for n in range(6):
    print(fibonacci(n))
```

+++ {"slideshow": {"slide_type": "fragment"}}

The code decorates the `fibonacci` function by printing each recursive call and the depth of the call stack.  
The decoration is useful in showing the efficiency of the function, but it rewrites the function definition.

+++ {"slideshow": {"slide_type": "subslide"}}

**How to decorate a function without changing its code?**

+++ {"slideshow": {"slide_type": "fragment"}}

- What if the decorations are temporary and should be removed later?  
- Go through the source codes of all decorated functions to remove the decorations?  
- When updating a piece of code, switch back and forth between original and decorated codes?

+++ {"slideshow": {"slide_type": "subslide"}}

What about defining a new function that calls and decorates the original function?

```{code-cell}
---
code_folding: [0]
slideshow:
  slide_type: fragment
---
def fibonacci(n):
    '''Returns the Fibonacci number of order n.'''
    return fibonacci(n - 1) + fibonacci(n - 2) if n > 1 else 1 if n is 1 else 0

def fibonacci_decorated(n):
    '''Returns the Fibonacci number of order n.'''
    global count, depth
    count += 1
    depth += 1
    print('{:>3}: {}fibonacci({!r})'.format(count, '|' * depth, n))
    
    value = fibonacci(n)
    
    depth -= 1
    if depth is -1:  # recursion done
        print('Done')
        count = 0  # reset count for subsequent recursions
    return value


count, depth = 0, -1
for n in range(6):
    print(fibonacci_decorated(n))    
```

+++ {"slideshow": {"slide_type": "fragment"}}

We want `fibonacci` to call `fibonacci_decorated` instead.  
What about renaming `fibonacci_decorated` to `fibonacci`?

```Python
fibonacci = fibonacci_decorated
count, depth = 0, -1
fibonacci_decorated(10)
```

(If you are faint-hearted, don't run the above code.)

+++ {"slideshow": {"slide_type": "fragment"}}

We want `fibonacci_decorated` to call the original `fibonacci`.

+++ {"slideshow": {"slide_type": "subslide"}}

The solution is to capture the original `fibonacci` in a closure:

```{code-cell}
---
code_folding: []
jupyter:
  outputs_hidden: true
slideshow:
  slide_type: fragment
---
import functools


def print_function_call(f):
    '''Return a decorator that prints function calls.'''
    @functools.wraps(f)  # give wrapper the identity of f and more
    def wrapper(*args, **kwargs):
        nonlocal count, depth
        count += 1
        depth += 1
        call = '{}{}'.format(f.__name__, argument_string(*args, **kwargs))
        print('{:>3}:{}{}'.format(count, '|' * depth, call))

        value = f(*args, **kwargs)  # wrapper calls f

        depth -= 1
        if depth is -1:
            print('Done')
            count = 0
        return value

    count, depth = 0, -1
    return wrapper  # return the decorated function
```

+++ {"slideshow": {"slide_type": "fragment"}}

`print_function_call` takes in `f` and returns `wrapper`, which captures and decorates `f`:
- `wrapper` expects the same set of arguments for `f`,  
- returns the same value returned by `f` on the arguments, but
- can execute additional codes before and after calling `f` to print the function call.

+++ {"slideshow": {"slide_type": "fragment"}}

By redefining `fibonacci` as the returned `wrapper`, the original `fibonacci` captured by `wrapper` calls `wrapper` as desired.

```{code-cell}
:code_folding: [0]

def fibonacci(n):
    return fibonacci(n - 1) + fibonacci(n - 2) if n > 1 else 1 if n is 1 else 0


fibonacci = print_function_call(
    fibonacci)  # so original fibonnacci calls wrapper
fibonacci(5)
```

+++ {"slideshow": {"slide_type": "fragment"}}

The redefinition does not change the original `fibonacci` captured by `wrapper`.

```{code-cell}
---
slideshow:
  slide_type: fragment
---
import inspect
for cell in fibonacci.__closure__:
    if callable(cell.cell_contents):
        print(inspect.getsource(cell.cell_contents))
```

+++ {"slideshow": {"slide_type": "subslide"}}

Python provides the syntatic sugar below to simplify the redefinition.

```{code-cell}
---
code_folding: [1]
jupyter:
  outputs_hidden: true
slideshow:
  slide_type: '-'
---
@print_function_call
def fibonacci(n):
    return fibonacci(n - 1) + fibonacci(n - 2) if n > 1 else 1 if n is 1 else 0


fibonacci(5)
```

+++ {"slideshow": {"slide_type": "subslide"}}

There are many techniques used in the above decorator.

+++ {"slideshow": {"slide_type": "fragment"}}

**Why use a variable number of arguments in `wrapper`**

+++ {"slideshow": {"slide_type": "fragment"}}

To decorate any function with possibly different number of arguments.

+++ {"slideshow": {"slide_type": "subslide"}}

**Why decorate the wrapper with `@functools.wraps(f)`?**

+++ {"slideshow": {"slide_type": "fragment"}}

- Ensures some attributes (such as `__name__`) of the wrapper function is the same as those of `f`.
- Add useful attributes. E.g., `__wrapped__` stores the original function so we can undo the decoration.

```{code-cell}
---
slideshow:
  slide_type: fragment
---
fibonacci, fibonacci_decorated = fibonacci.__wrapped__, fibonacci  # recover
print('original fibonacci:')
print(fibonacci(5))

fibonacci = fibonacci_decorated  # decorate
print('decorated fibonacci:')
print(fibonacci(5))
```

+++ {"slideshow": {"slide_type": "subslide"}}

**How to use decorator to improve recursion?**

+++ {"slideshow": {"slide_type": "fragment"}}

We can also use a decorator to make recursion more efficient by caching the return values.  
`cache` is a dictionary where `cache[n]` stores the computed value of $F_n$ to avoid redundant computations.

```{code-cell}
---
jupyter:
  outputs_hidden: true
slideshow:
  slide_type: fragment
---
def caching(f):
    '''Return a decorator that caches a function with a single argument.'''
    @functools.wraps(f)
    def wrapper(n):
        if n not in cache:
            cache[n] = f(n)
        else:
            print('read from cache')
        return cache[n]

    cache = {}
    wrapper.clear_cache = lambda : cache.clear()  # add method to clear cache
    return wrapper


@print_function_call
@caching
def fibonacci(n):
    return fibonacci(n - 1) + fibonacci(n - 2) if n > 1 else 1 if n == 1 else 0
```

```{code-cell}
---
jupyter:
  outputs_hidden: true
slideshow:
  slide_type: fragment
---
fibonacci(5)
fibonacci(5)
fibonacci.clear_cache()
fibonacci(5)
```

+++ {"slideshow": {"slide_type": "fragment"}}

A method `clear_cache` is added to the wrapper to clear the cache.   
`lambda <argument list> : <expression>`is called a [*lambda* expression](https://docs.python.org/3/reference/expressions.html#lambda), which conveniently defines an *anonymous function*.

```{code-cell}
---
slideshow:
  slide_type: fragment
---
type(fibonacci.clear_cache), fibonacci.clear_cache.__name__
```

+++ {"slideshow": {"slide_type": "slide"}}

## Module

+++ {"slideshow": {"slide_type": "subslide"}}

**How to create a module?**

+++ {"slideshow": {"slide_type": "fragment"}}

To create a module, simply put the code in a python source file `<module name>.py` in
- the current directory, or
- a python *site-packages* directory in system path.

```{code-cell}
---
slideshow:
  slide_type: '-'
---
import sys
print(sys.path)
```

+++ {"slideshow": {"slide_type": "subslide"}}

For example, to create a module for generating Fibonacci numbers:

```{code-cell}
---
slideshow:
  slide_type: '-'
---
%more fibonacci.py
```

```{code-cell}
---
slideshow:
  slide_type: '-'
---
import fibonacci as fib # as statement shortens name
help(fib)
```

```{code-cell}
---
slideshow:
  slide_type: '-'
---
print(fib.fibonacci(5))
print(fib.fibonacci_iteration(5))
```
