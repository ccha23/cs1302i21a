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

+++ {"slideshow": {"slide_type": "slide"}}

# Writing Function

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

+++ {"slideshow": {"slide_type": "slide"}}

## Function Definition

+++ {"slideshow": {"slide_type": "fragment"}}

**How to write a function?**

+++ {"slideshow": {"slide_type": "fragment"}}

A function is defined using the [`def` keyword](https://docs.python.org/3/reference/compound_stmts.html#def):

+++ {"slideshow": {"slide_type": "fragment"}}

The following is a simple function that prints "Hello, World!".

```{code-cell}
---
slideshow:
  slide_type: fragment
---
# Function definition
def say_hello():
    print('Hello, World!')
```

```{code-cell}
---
slideshow:
  slide_type: '-'
---
# Function invocation
say_hello()
```

+++ {"slideshow": {"slide_type": "subslide"}}

To make a function more powerful and solve different problems,  
we can 
- use a [return statement](https://docs.python.org/3/reference/simple_stmts.html#the-return-statement) to return a value that
- depends on some input arguments.

```{code-cell}
---
slideshow:
  slide_type: fragment
---
def increment(x):
    return x + 1


increment(3)
```

+++ {"slideshow": {"slide_type": "subslide"}}

We can also have multiple input arguments.

```{code-cell}
---
slideshow:
  slide_type: fragment
---
def length_of_hypotenuse(a, b):
    if a >= 0 and b >= 0:
        return (a**2 + b**2)**0.5
    else:
        print('Input arguments must be non-negative.')
```

```{code-cell}
---
slideshow:
  slide_type: '-'
---
length_of_hypotenuse(3, 4)
```

```{code-cell}
---
slideshow:
  slide_type: '-'
---
length_of_hypotenuse(-3, 4)
```

+++ {"slideshow": {"slide_type": "slide"}}

## Documentation

+++ {"slideshow": {"slide_type": "subslide"}}

**How to document a function?**

```{code-cell}
---
slideshow:
  slide_type: fragment
---
# Author: John Doe
# Last modified: 2020-09-14
def increment(x):
    '''The function takes in a value x and returns the increment x + 1.
    
    It is a simple example that demonstrates the idea of
    - parameter passing, 
    - return statement, and 
    - function documentation.'''
    return x + 1  # + operation is used and may fail for 'str'
```

+++ {"slideshow": {"slide_type": "fragment"}}

The `help` command shows the docstring we write 
- at beginning of the function body
- delimited using triple single/double quotes. 

```{code-cell}
---
slideshow:
  slide_type: '-'
---
help(increment)
```

+++ {"slideshow": {"slide_type": "fragment"}}

The docstring should contain the *usage guide*, i.e., information for new users to call the function properly.  
There is a Python style guide (PEP 257) for
- [one-line docstrings](https://www.python.org/dev/peps/pep-0257/#one-line-docstrings) and
- [multi-line docstrings](https://www.python.org/dev/peps/pep-0257/#multi-line-docstrings).

+++ {"slideshow": {"slide_type": "subslide"}}

**Why doesn't `help` show the comments that start with `#`?**

+++ {"slideshow": {"slide_type": "-"}}

```Python
# Author: John Doe
# Last modified: 2020-09-14
def increment(x):
    ...
    return x + 1  # + operation is used and may fail for 'str'
```

+++ {"slideshow": {"slide_type": "fragment"}}

Those comments are not usage guide. They are intended for programmers who need to maintain/extend the function definition.

+++ {"slideshow": {"slide_type": "fragment"}}

- Information about the author and modification date facilitate communications among programmers.
- Comments within the code help explain important and not-so-obvious implementation details.

+++ {"slideshow": {"slide_type": "subslide"}}

**How to let user know the data types of input arguments and return value?**

+++ {"slideshow": {"slide_type": "subslide"}}

We can [annotate](https://docs.python.org/3/library/typing.html) the function with *hints* of the types of the arguments and return value.

```{code-cell}
---
slideshow:
  slide_type: '-'
---
# Author: John Doe
# Last modified: 2020-09-14
def increment(x: float) -> float:
    '''The function takes in a value x and returns the increment x + 1.
    
    It is a simple example that demonstrates the idea of
    - parameter passing, 
    - return statement, and 
    - function documentation.'''
    return x + 1  # + operation is used and may fail for 'str'


help(increment)
```

+++ {"slideshow": {"slide_type": "fragment"}}

The above annotations is not enforced by the Python interpreter.  
Nevertheless, such annotations make the code easier to understand and can be used by editor with type-checking tools.

```{code-cell}
---
slideshow:
  slide_type: '-'
---
def increment_user_input():
    return increment(input())  # does not raise error even though input returns str
```

```{code-cell}
---
slideshow:
  slide_type: '-'
tags: [remove-output]
---
increment_user_input()  # still lead to runtime error
```

+++ {"slideshow": {"slide_type": "slide"}}

## Parameter Passing

+++ {"slideshow": {"slide_type": "fragment"}}

**Can we increment a variable instead of returning its increment?**

```{code-cell}
---
slideshow:
  slide_type: '-'
---
def increment(x):
    x += 1
```

```{code-cell}
---
slideshow:
  slide_type: fragment
---
x = 3
increment(x)
print(x)  # 4?
```

+++ {"slideshow": {"slide_type": "-"}}

Does the above code increment `x`?

```{code-cell}
---
slideshow:
  slide_type: subslide
---
%%mytutor -h 350
def increment(x):
    x += 1


x = 3
increment(x)
print(x)
```

+++ {"slideshow": {"slide_type": "fragment"}}

- Step 3: The function `increment` is invoked with the argument evaluated to the value of `x`.
- Step 3-4: A local frame is created for variables local to `increment` during its execution.    
    - The *formal parameter* `x` in `def increment(x):` becomes a local variable and
    - it is assigned the value `3` of the *actual parameter* given by the global variable `x`.
- Step 5-6: The local (but not the global) variable `x` is incremented.
- Step 6-7: The function call completes and the local frame is removed.
