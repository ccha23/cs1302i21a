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

# Using Functions

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

## Motivation

+++ {"slideshow": {"slide_type": "fragment"}}

**How to reuse code so we can write less?**

+++ {"slideshow": {"slide_type": "fragment"}}

When we write a loop, the code is executed multiple times, once for each iteration.

+++ {"slideshow": {"slide_type": "fragment"}}

This is a simple form of *code reuse* that 
- gives your code an elegant *structure* that
- can be executed efficiently by a computer, and
- *interpreted* easily by a programmer.

+++ {"slideshow": {"slide_type": "fragment"}}

**How to repeat execution at different times, in different programs, and in slightly different ways?**

+++ {"slideshow": {"slide_type": "slide"}}

## Functions

+++ {"slideshow": {"slide_type": "fragment"}}

**How to calculate the logarithm?**

+++ {"slideshow": {"slide_type": "fragment"}}

There is no arithmetic operator for logarithm.  
Do we have to implement it ourselves?

+++ {"slideshow": {"slide_type": "subslide"}}

We can use the function `log` from the [`math` *module*](https://docs.python.org/3/library/math.html):

```{code-cell}
---
slideshow:
  slide_type: '-'
---
from math import log
log(256, 2)  # log base 2 of 256
```

+++ {"slideshow": {"slide_type": "fragment"}}

The above computes the base-$2$ logarithm, $\log_2(256)$. Like functions in mathematics, a computer function `log` 
- is *called/invoked* with some input *arguments* `(256, 2)` following the function, and
- *returns* an output value computed from the input arguments.

```{code-cell}
---
slideshow:
  slide_type: fragment
---
# A function is callable while an integer is not
callable(log), callable(1)
```

+++ {"slideshow": {"slide_type": "subslide"}}

Unlike mathematical functions:
- A computer function may require no arguments, but we still need to call it with `()`. 

```{code-cell}
---
slideshow:
  slide_type: '-'
tags: [remove-output]
---
input()
```

+++ {"slideshow": {"slide_type": "fragment"}}

- A computer function may have side effects and return `None`.

```{code-cell}
---
slideshow:
  slide_type: '-'
---
x = print()
print(x, 'of type', type(x))
```

+++ {"slideshow": {"slide_type": "fragment"}}

An argument of a function call can be any expression.

```{code-cell}
---
slideshow:
  slide_type: '-'
tags: [remove-output]
---
print('1st input:', input(), '2nd input', input())
```

+++ {"slideshow": {"slide_type": "fragment"}}

Note also that
- the argument can also be a function call like function composition in mathematics. 
- Before a function call is executed, its arguments are evaluated first from left to right.

+++ {"slideshow": {"slide_type": "subslide"}}

**Why not implement logarithm yourself?**

+++ {"slideshow": {"slide_type": "fragment"}}

- The function from standard library is efficiently implemented and thoroughly tested/documented.
- Knowing what a function does is often insufficient for an efficient implementation.  
    (See [how to calculate logarithm](https://en.wikipedia.org/wiki/Logarithm#Calculation) as an example.)

+++ {"slideshow": {"slide_type": "fragment"}}

Indeed, the `math` library does not implement `log` itself:
> **CPython implementation detail:** The `math` module consists mostly of thin *wrappers* around the platform C math library functions. - [pydoc last paragraph](https://docs.python.org/3/library/math.html)

(See the [source code wrapper for `log`](https://github.com/python/cpython/blob/457d4e97de0369bc786e363cb53c7ef3276fdfcd/Modules/mathmodule.c#L731).) 

+++ {"slideshow": {"slide_type": "subslide"}}

**Exercise** What is a function in programming?

+++ {"nbgrader": {"grade": true, "grade_id": "what-is-a-function", "locked": false, "points": 0, "schema_version": 3, "solution": true, "task": false}, "slideshow": {"slide_type": "-"}}

- A function is a structure that allows a piece of code to be reused in a program.  
- A function can adapt its computations to different situations using input arguments.  

+++ {"slideshow": {"slide_type": "slide"}}

## Import Functions from Modules

+++ {"slideshow": {"slide_type": "fragment"}}

**How to import functions?**

+++ {"slideshow": {"slide_type": "fragment"}}

We can use the [`import` statement](https://docs.python.org/3/reference/simple_stmts.html#import) to import multiple functions into the program *global frame*.

```{code-cell}
---
slideshow:
  slide_type: '-'
---
%%mytutor -h 300
from math import log10, ceil
x = 1234
print('Number of digits of x:', ceil(log10(x)))
```

+++ {"slideshow": {"slide_type": "fragment"}}

The above import both the functions `log10` and `ceil` from `math` to compute the number $\lceil \log_{10}(x)\rceil$ of digits of a *strictly positive* integer $x$.

+++ {"slideshow": {"slide_type": "subslide"}}

**How to import all functions from a library?**

```{code-cell}
---
slideshow:
  slide_type: fragment
---
%%mytutor -h 300
from math import *  # import all except names starting with an underscore
print('{:.2f}, {:.2f}, {:.2f}'.format(sin(pi / 6), cos(pi / 3), tan(pi / 4)))
```

+++ {"slideshow": {"slide_type": "fragment"}}

The above uses the wildcard `*` to import ([nearly](https://docs.python.org/3/tutorial/modules.html#more-on-modules)) all the functions/variables provided in `math`.

+++ {"slideshow": {"slide_type": "slide"}}

**What if different packages define the same function?**

```{code-cell}
---
slideshow:
  slide_type: fragment
---
%%mytutor -h 300
print('{}'.format(pow(-1, 2)))
print('{:.2f}'.format(pow(-1, 1 / 2)))
from math import *
print('{}'.format(pow(-1, 2)))
print('{:.2f}'.format(pow(-1, 1 / 2)))
```

+++ {"slideshow": {"slide_type": "fragment"}}

- The function `pow` imported from `math` overwrites the built-in function `pow`.  
- Unlike the built-in function, `pow` from `math` returns only floats but not integers nor complex numbers. 
- We say that the import statement *polluted the namespace of the global frame* and caused a *name collision*. 

+++ {"slideshow": {"slide_type": "subslide"}}

**How to avoid name collisions?**

```{code-cell}
---
slideshow:
  slide_type: '-'
---
%%mytutor -h 250
import math
print('{:.2f}, {:.2f}'.format(math.pow(-1, 2), pow(-1, 1 / 2)))
```

+++ {"slideshow": {"slide_type": "fragment"}}

We can use the full name (*fully-qualified name*) `math.pow` prefixed with the module name (and possibly package names containing the module).

+++ {"slideshow": {"slide_type": "subslide"}}

**Can we shorten a name?**

+++ {"slideshow": {"slide_type": "fragment"}}

The name of a library can be very long and there can be a hierarchical structure as well.  
E.g., to plot a sequence using `pyplot` module from `matplotlib` package:

```{code-cell}
---
slideshow:
  slide_type: '-'
---
%matplotlib inline
import matplotlib.pyplot
matplotlib.pyplot.stem([4, 3, 2, 1])
matplotlib.pyplot.ylabel(r'$x_n$')
matplotlib.pyplot.xlabel(r'$n$')
matplotlib.pyplot.title('A sequence of numbers')
matplotlib.pyplot.show()
```

+++ {"slideshow": {"slide_type": "fragment"}}

It is common to rename `matplotlib.pyplot` as `plt`:

```{code-cell}
---
slideshow:
  slide_type: '-'
---
%matplotlib inline
import matplotlib.pyplot as plt
plt.stem([4, 3, 2, 1])
plt.ylabel(r'$x_n$')
plt.xlabel(r'$n$')
plt.title('A sequence of numbers')
plt.show()
```

+++ {"slideshow": {"slide_type": "subslide"}}

We can also rename a function as we import it to avoid name collision:

```{code-cell}
---
slideshow:
  slide_type: fragment
---
from math import pow as fpow
fpow(2, 2), pow(2, 2)
```

+++ {"slideshow": {"slide_type": "subslide"}}

**Exercise** What is wrong with the following code?

```{code-cell}
---
slideshow:
  slide_type: fragment
---
import math as m
for m in range(5): m.pow(m, 2)
```

+++ {"nbgrader": {"grade": true, "grade_id": "name-conflict", "locked": false, "points": 0, "schema_version": 3, "solution": true, "task": false}, "slideshow": {"slide_type": "-"}}

There is a name collision: `m` is assigned to an integer in the for loop and so it is no longer the module `math` when calling `m.pow`.

+++

**Exercise** Use the `randint` function from `random` to simulate the rolling of a die, by printing a random integer from 1 to 6. 

```{code-cell}
---
nbgrader:
  grade: true
  grade_id: random
  locked: false
  points: 0
  schema_version: 3
  solution: true
  task: false
---
import random
print(random.randint(1, 6))
```

+++ {"slideshow": {"slide_type": "slide"}}

## Built-in Functions

+++ {"slideshow": {"slide_type": "fragment"}}

**How to learn more about a function such as `randint`?**

+++ {"slideshow": {"slide_type": "fragment"}}

There is a built-in function `help` for showing the *docstring* (documentation string). 

```{code-cell}
---
slideshow:
  slide_type: '-'
---
import random
help(random.randint)  # random must be imported before
```

```{code-cell}
---
slideshow:
  slide_type: '-'
tags: [output_scroll, remove-output]
---
help(random)  # can also show the docstring of a module
```

```{code-cell}
:tags: [output_scroll, remove-output]

help(help)
```

+++ {"slideshow": {"slide_type": "subslide"}}

**Does built-in functions belong to a module?**

+++ {"slideshow": {"slide_type": "fragment"}}

Indeed, every function must come from a module.

```{code-cell}
---
slideshow:
  slide_type: '-'
---
__builtin__.print('I am from the __builtin__ module.')
```

+++ {"slideshow": {"slide_type": "fragment"}}

`__builtin__` module is automatically loaded because it provides functions that are commonly use for all programs.

+++ {"slideshow": {"slide_type": "subslide"}}

**How to list everything in a module?** 

+++ {"slideshow": {"slide_type": "fragment"}}

We can use the built-in function `dir` (*directory*).

```{code-cell}
---
slideshow:
  slide_type: '-'
tags: [output_scroll, remove-output]
---
dir(__builtin__)
```

+++ {"slideshow": {"slide_type": "subslide"}}

We can also call `dir` without arguments.  
What does it print?

```{code-cell}
---
slideshow:
  slide_type: '-'
tags: [output_scroll, remove-output]
---
dir()
```
