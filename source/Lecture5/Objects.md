---
jupytext:
  formats: ipynb,md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.12
    jupytext_version: 1.9.1
kernelspec:
  display_name: Python 3.7
  language: python
  name: python3
---

+++ {"cell_style": "center", "slideshow": {"slide_type": "slide"}}

# Objects

+++ {"slideshow": {"slide_type": "-"}, "tags": ["remove-cell"]}

**CS1302 Introduction to Computer Programming**
___

```{code-cell} ipython3
---
slideshow:
  slide_type: fragment
tags: [remove-cell]
---
%reload_ext mytutor
```

+++ {"slideshow": {"slide_type": "slide"}}

## Object-Oriented Programming

+++ {"slideshow": {"slide_type": "fragment"}}

**Why object-oriented programming?**

```{code-cell} ipython3
---
slideshow:
  slide_type: fragment
---
import jupyter_manim
from manimlib.imports import *
```

```{code-cell} ipython3
---
slideshow:
  slide_type: '-'
---
%%manim HelloWorld -l
class HelloWorld(Scene):
    def construct(self):
        self.play(Write(TextMobject('Hello, World!')))
```

+++ {"slideshow": {"slide_type": "fragment"}}

 - `HelloWorld` is a specific `Scene` that is
 - `construct`ed by `play`ing an animation that `Write`
 - the `TextMobject` of the message `'Hello, World!'`. 

+++ {"slideshow": {"slide_type": "fragment"}}

**Exercise** Try changing
- Mobjects: `TextMobject('Hello, World!')` to `TexMobject(r'E=mc^2')` or `Circle()` or `Square()`.
- Animation objects: `Write` to `FadeIn` or `GrowFromCenter`.

See the [documentation](https://eulertour.com/docs/) for other choices.

+++ {"slideshow": {"slide_type": "fragment"}}

More complicated behavior can be achieved by using different objects.

```{code-cell} ipython3
---
slideshow:
  slide_type: '-'
---
%%html
<iframe width="912" height="513" src="https://www.youtube.com/embed/ENMyFGmq5OA" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
```

+++ {"slideshow": {"slide_type": "subslide"}}

**What is an object?**

+++ {"slideshow": {"slide_type": "fragment"}}

Almost everything is an [`object`](https://docs.python.org/3/library/functions.html?highlight=object#object) in Python.

```{code-cell} ipython3
---
slideshow:
  slide_type: '-'
---
isinstance?
isinstance(1, object), isinstance(1.0, object), isinstance('1', object)
```

+++ {"slideshow": {"slide_type": "fragment"}}

A function is also a [first-class](https://en.wikipedia.org/wiki/First-class_function) object object.

```{code-cell} ipython3
---
slideshow:
  slide_type: '-'
---
isinstance(print, object), isinstance(''.isdigit, object)
```

+++ {"slideshow": {"slide_type": "fragment"}}

A data type is also an object.

```{code-cell} ipython3
---
slideshow:
  slide_type: '-'
---
# chicken and egg relationship
isinstance(type, object), isinstance(object, type), isinstance(object, object)
```

+++ {"slideshow": {"slide_type": "subslide"}}

Python is a [*class-based* object-oriented programming](https://en.wikipedia.org/wiki/Object-oriented_programming#Class-based_vs_prototype-based) language:  
- Each object is an instance of a *class* (also called type in Python).
- An object is a collection of *members/attributes*, each of which is an object.

```{code-cell} ipython3
---
slideshow:
  slide_type: '-'
---
hasattr?
hasattr(str, 'isdigit')
```

+++ {"slideshow": {"slide_type": "fragment"}}

Different objects of a class
- have the same set of attributes as that of the class, but
- the attribute values can be different.

```{code-cell} ipython3
---
slideshow:
  slide_type: '-'
---
dir?
dir(1)==dir(int), complex(1, 2).imag != complex(1, 1).imag
```

+++ {"slideshow": {"slide_type": "subslide"}}

**How to operate on an object?**

+++ {"slideshow": {"slide_type": "fragment"}}

- A class can define a function as an attribute for all its instances.  
- Such a function is called a *method* or *member function*.

```{code-cell} ipython3
---
slideshow:
  slide_type: fragment
---
complex.conjugate(complex(1, 2)), type(complex.conjugate)
```

+++ {"slideshow": {"slide_type": "fragment"}}

A [method](https://docs.python.org/3/tutorial/classes.html#method-objects) can be accessed by objects of the class:

```{code-cell} ipython3
---
slideshow:
  slide_type: '-'
---
complex(1, 2).conjugate(), type(complex(1, 2).conjugate)
```

+++ {"slideshow": {"slide_type": "fragment"}}

`complex(1,2).conjugate` is a *callable* object:
- Its attribute `__self__` is assigned to `complex(1,2)`.
- When called, it passes `__self__` as the first argument to `complex.conjugate`.

```{code-cell} ipython3
---
slideshow:
  slide_type: '-'
---
callable(complex(1,2).conjugate), complex(1,2).conjugate.__self__
```

+++ {"slideshow": {"slide_type": "slide"}}

## File Objects

+++ {"slideshow": {"slide_type": "subslide"}}

**How to read a text file?**

+++ {"slideshow": {"slide_type": "fragment"}}

Consider reading a csv (comma separated value) file:

```{code-cell} ipython3
---
slideshow:
  slide_type: '-'
---
!more 'contact.csv'
```

+++ {"slideshow": {"slide_type": "fragment"}}

To read the file by a Python program:

```{code-cell} ipython3
---
slideshow:
  slide_type: '-'
---
f = open('contact.csv')  # create a file object for reading
print(f.read())   # return the entire content
f.close()         # close the file
```

+++ {"slideshow": {"slide_type": "fragment"}}

1. [`open`](https://docs.python.org/3/library/functions.html?highlight=open#open) is a function that creates a file object and assigns it to `f`.
1. Associated with the file object, 
 - [`read`](https://docs.python.org/3/library/io.html#io.TextIOBase.read) returns the entire content of the file as a string.
 - [`close`](https://docs.python.org/3/library/io.html#io.IOBase.close) flushes and closes the file.

+++ {"slideshow": {"slide_type": "subslide"}}

**Why close a file?**

+++ {"slideshow": {"slide_type": "fragment"}}

If not, depending on the operating system,
- other programs may not be able to access the file, and
- changes may not be written to the file.

+++ {"slideshow": {"slide_type": "subslide"}}

To ensure a file is closed properly, we can use the [`with` statement](https://docs.python.org/3/reference/compound_stmts.html#with):

```{code-cell} ipython3
---
slideshow:
  slide_type: fragment
---
with open('contact.csv') as f:
    print(f.read())
```

+++ {"slideshow": {"slide_type": "subslide"}}

The `with` statement applies to any [context manager](https://docs.python.org/3/reference/datamodel.html#context-managers) that provides the methods
- `__enter__` for initialization, and
- `__exit__` for finalization.

```{code-cell} ipython3
---
slideshow:
  slide_type: fragment
---
with open('contact.csv') as f:
    print(f, hasattr(f, '__enter__'), hasattr(f, '__exit__'), sep='\n')
```

+++ {"slideshow": {"slide_type": "fragment"}}

- `f.__enter__` is called after the file object is successfully created and assigned to `f`, and
- `f.__exit__` is called at the end, which closes the file.
- `f.closed` indicates whether the file is closed.

```{code-cell} ipython3
---
slideshow:
  slide_type: fragment
---
f.closed
```

+++ {"slideshow": {"slide_type": "fragment"}}

We can iterate a file object in a for loop,  
which implicitly call the method `__iter__` to read a file line by line.

```{code-cell} ipython3
---
slideshow:
  slide_type: fragment
---
with open('contact.csv') as f:
    for line in f:
        print(line, end='')

hasattr(f, '__iter__')
```

+++ {"slideshow": {"slide_type": "subslide"}}

**Exercise** Print only the first 5 lines of the file `contact.csv`.

```{code-cell} ipython3
---
nbgrader:
  grade: false
  grade_id: read-head
  locked: false
  schema_version: 3
  solution: true
  task: false
slideshow:
  slide_type: '-'
---
with open('contact.csv') as f:
    ### BEGIN SOLUTION
    for i, line in enumerate(f):
        print(line, end='')
        if i >= 5: break
    ### END SOLUTION
```

+++ {"slideshow": {"slide_type": "subslide"}}

**How to write to a text file?**

+++ {"slideshow": {"slide_type": "fragment"}}

Consider backing up `contact.csv` to a new file:

```{code-cell} ipython3
---
slideshow:
  slide_type: '-'
---
destination = 'private/new_contact.csv'
```

+++ {"slideshow": {"slide_type": "fragment"}}

The directory has to be created first if it does not exist:

```{code-cell} ipython3
---
slideshow:
  slide_type: '-'
---
import os
os.makedirs(os.path.dirname(destination), exist_ok=True)
```

```{code-cell} ipython3
---
slideshow:
  slide_type: '-'
---
os.makedirs?
!ls
```

+++ {"slideshow": {"slide_type": "fragment"}}

To write to the destination file:

```{code-cell} ipython3
---
code_folding: []
slideshow:
  slide_type: '-'
---
with open('contact.csv') as source_file:
    with open(destination, 'w') as destination_file:
        destination_file.write(source_file.read())
```

```{code-cell} ipython3
---
slideshow:
  slide_type: '-'
---
destination_file.write?
!more {destination}
```

+++ {"slideshow": {"slide_type": "fragment"}}

- The argument `'w'` to `open` sets the file object to write mode.
- The method `write` writes the input strings to the file.

+++ {"slideshow": {"slide_type": "subslide"}}

**Exercise** We can also use `a` mode to *append* new content to a file.   
Complete the following code to append `new_data` to the file `destination`.

```{code-cell} ipython3
---
nbgrader:
  grade: false
  grade_id: append
  locked: false
  schema_version: 3
  solution: true
  task: false
slideshow:
  slide_type: '-'
---
new_data = 'Effie, Douglas,galnec@naowdu.tc, (888) 311-9512'
with open(destination, 'a') as f:
    ### BEGIN SOLUTION
    f.write('\n')
    f.write(new_data)
    ### END SOLUTION
!more {destination}
```

+++ {"slideshow": {"slide_type": "subslide"}}

**How to delete a file?**

+++ {"slideshow": {"slide_type": "fragment"}}

Note that the file object does not provide any method to delete the file.  
Instead, we should use the function `remove` of the `os` module.

```{code-cell} ipython3
---
slideshow:
  slide_type: fragment
---
if os.path.exists(destination):
    os.remove(destination)
```

+++ {"slideshow": {"slide_type": "slide"}}

## String Objects

+++ {"slideshow": {"slide_type": "subslide"}}

**How to search for a substring in a string?**

+++ {"slideshow": {"slide_type": "fragment"}}

A string object has the method `find` to search for a substring.  
E.g., to find the contact information of Tai Ming:

```{code-cell} ipython3
---
slideshow:
  slide_type: fragment
---
str.find?
with open('contact.csv') as f:
    for line in f:
        if line.find('Tai Ming') != -1:
            record = line
            print(record)
            break
```

+++ {"slideshow": {"slide_type": "subslide"}}

**How to split and join strings?**

+++ {"slideshow": {"slide_type": "fragment"}}

A string can be split according to a delimiter using the `split` method.

```{code-cell} ipython3
---
slideshow:
  slide_type: '-'
---
record.split(',')
```

+++ {"slideshow": {"slide_type": "fragment"}}

The list of substrings can be joined back together using the `join` methods.

```{code-cell} ipython3
---
slideshow:
  slide_type: '-'
---
print('\n'.join(record.split(',')))
```

+++ {"slideshow": {"slide_type": "subslide"}}

**Exercise** Print only the phone number (last item) in `record`. Use the method `rstrip` or  `strip` to remove unnecessary white spaces at the end.

```{code-cell} ipython3
---
nbgrader:
  grade: false
  grade_id: strip
  locked: false
  schema_version: 3
  solution: true
  task: false
slideshow:
  slide_type: '-'
---
str.rstrip?
### BEGIN SOLUTION
print(record.split(',')[-1].rstrip())
### END SOLUTION
```

+++ {"slideshow": {"slide_type": "fragment"}}

**Exercise** Print only the name (first item) in `record` but with
- surname printed first with all letters in upper case 
- followed by a comma, a space, and
- the first name as it is in `record`.

E.g., `Tai Ming Chan` should be printed as `CHAN, Tai Ming`.  

*Hint*: Use the methods `upper` and `rsplit` (with the parameter `maxsplit=1`).

```{code-cell} ipython3
---
nbgrader:
  grade: false
  grade_id: process-name
  locked: false
  schema_version: 3
  solution: true
  task: false
slideshow:
  slide_type: '-'
---
str.rsplit?
### BEGIN SOLUTION
first, last = record.split(',')[0].rsplit(' ', maxsplit=1)
print('{}, {}'.format(last.upper(),first))
### END SOLUTION
```

+++ {"slideshow": {"slide_type": "slide"}}

## Operator Overloading

+++ {"slideshow": {"slide_type": "subslide"}}

### What is overloading?

+++ {"slideshow": {"slide_type": "fragment"}}

Recall that the addition operation `+` behaves differently for different types.

```{code-cell} ipython3
---
slideshow:
  slide_type: fragment
---
for x, y in (1, 1), ('1', '1'), (1, '1'):
    print(f'{x!r:^5} + {y!r:^5} = {x+y!r}')
```

- Having an operator perform differently based on its argument types is called [operator *overloading*](https://en.wikipedia.org/wiki/Operator_overloading).
- `+` is called a *generic* operator.
- We can also have function overloading to create generic functions.

+++ {"slideshow": {"slide_type": "subslide"}}

### How to dispatch on type?

+++ {"slideshow": {"slide_type": "fragment"}}

The strategy of checking the type for the appropriate implementation is called *dispatching on type*.

+++ {"slideshow": {"slide_type": "fragment"}}

A naive idea is to put all different implementations together with case-by-case checks of operand types.

```{code-cell} ipython3
---
slideshow:
  slide_type: '-'
---
def add_case_by_case(x, y):
    if isinstance(x, int) and isinstance(y, int):
        print('Do integer summation...')
    elif isinstance(x, str) and isinstance(y, str):
        print('Do string concatenation...')
    else:
        print('Return a TypeError...')
    return x + y  # replaced by internal implementations


for x, y in (1, 1), ('1', '1'), (1, '1'):
    print(f'{x!r:^10} + {y!r:^10} = {add_case_by_case(x,y)!r}')
```

+++ {"slideshow": {"slide_type": "subslide"}}

It can get quite messy with all possible types and combinations.

```{code-cell} ipython3
---
slideshow:
  slide_type: '-'
---
for x, y in ((1, 1.1), (1, complex(1, 2)), ((1, 2), (1, 2))):
    print(f'{x!r:^10} + {y!r:^10} = {x+y!r}')
```

+++ {"slideshow": {"slide_type": "subslide"}}

**What about new data types?**

```{code-cell} ipython3
---
slideshow:
  slide_type: '-'
---
from fractions import Fraction  # non-built-in type for fractions
for x, y in ((Fraction(1, 2), 1), (1, Fraction(1, 2))):
    print(f'{x} + {y} = {x+y}')
```

+++ {"slideshow": {"slide_type": "fragment"}}

Weaknesses of the naive approach:
1. New data types require rewriting the addition operation.
1. A programmer may not know all other types and combinations to rewrite the code properly.

+++ {"slideshow": {"slide_type": "subslide"}}

### How to have data-directed programming?

+++ {"slideshow": {"slide_type": "fragment"}}

The idea is to treat an implementation as a datum that can be returned by the operand types.

+++ {"slideshow": {"slide_type": "fragment"}}

- `x + y` is a [*syntactic sugar*](https://en.wikipedia.org/wiki/Syntactic_sugar) that
- invokes the method `type(x).__add__(x,y)` of `type(x)` to do the addition.

```{code-cell} ipython3
---
slideshow:
  slide_type: subslide
---
for x, y in (Fraction(1, 2), 1), (1, Fraction(1, 2)):
    print(f'{x} + {y} = {type(x).__add__(x,y)}')  # instead of x + y
```

+++ {"slideshow": {"slide_type": "fragment"}}

- The first case calls `Fraction.__add__`, which provides a way to add `int` to `Fraction`.
- The second case calls `int.__add__`, which cannot provide any way of adding `Fraction` to `int`. (Why not?)

+++ {"slideshow": {"slide_type": "fragment"}}

**Why return a [`NotImplemented` object](https://docs.python.org/3.6/library/constants.html#NotImplemented) instead of raising an error/exception?**

+++ {"slideshow": {"slide_type": "fragment"}}

- This allows `+` to continue to handle the addition by
- dispatching on `Fraction` to call its reverse addition method [`__radd__`](https://docs.python.org/3.6/library/numbers.html#implementing-the-arithmetic-operations).

```{code-cell} ipython3
---
code_folding: []
slideshow:
  slide_type: fragment
---
%%mytutor -h 500
from fractions import Fraction
def add(x, y):
    '''Simulate the + operator.'''
    sum = x.__add__(y)
    if sum is NotImplemented:
        sum = y.__radd__(x)
    return sum


for x, y in (Fraction(1, 2), 1), (1, Fraction(1, 2)):
    print(f'{x} + {y} = {add(x,y)}')
```

+++ {"slideshow": {"slide_type": "subslide"}}

The object-oriented programming techniques involved are formally called:
- [*Polymorphism*](https://en.wikipedia.org/wiki/Polymorphism_(computer_science)): Different types can have different implementations of the `__add__` method.  
- [*Single dispatch*](https://en.wikipedia.org/wiki/Dynamic_dispatch): The implementation is chosen based on one single type at a time. 

+++ {"slideshow": {"slide_type": "fragment"}}

Remarks:
- A method with starting and trailing double underscores in its name is called a [*dunder method*](https://dbader.org/blog/meaning-of-underscores-in-python).  
- Dunder methods are not intended to be called directly. E.g., we normally use `+` instead of `__add__`.
- [Other operators](https://docs.python.org/3/library/operator.html?highlight=operator) have their corresponding dunder methods that overloads the operator.

+++ {"slideshow": {"slide_type": "slide"}}

## Object Aliasing

+++ {"slideshow": {"slide_type": "subslide"}}

**When are two objects identical?**

+++ {"slideshow": {"slide_type": "fragment"}}

- Two objects are the same if they occupy the same memory.  
- The keyword `is` checks whether two objects are the same object.
- The function `id` returns a unique id number for each object.

```{code-cell} ipython3
---
slideshow:
  slide_type: fragment
---
%%mytutor -h 400
x, y = complex(1,2), complex(1,2)
z = x

for expr in 'id(x)', 'id(y)', 'id(z)', 'x == y == z', 'x is y', 'x is z':
    print(expr,eval(expr))
```

+++ {"slideshow": {"slide_type": "fragment"}}

As the box-pointer diagram shows:
- `x` is not `y` because they point to objects at different memory locations,  
  even though the objects have the same type and value.
- `x` is `z` because the assignment `z = x` binds `z` to the same memory location `x` points to.  
    `z` is said to be an *alias* (another name) of `x`. 

+++ {"slideshow": {"slide_type": "subslide"}}

**Should we use `is` or `==`?**

+++ {"slideshow": {"slide_type": "fragment"}}

`is` is faster but:

```{code-cell} ipython3
---
slideshow:
  slide_type: fragment
---
1 is 1, 1 is 1., 1 == 1.
```

+++ {"slideshow": {"slide_type": "fragment"}}

- `1 is 1.` returns false because `1` is `int` but `1.` is `float`.
- `==` calls the method `__eq__` of `float` which returns mathematical equivalence.

+++ {"slideshow": {"slide_type": "subslide"}}

*Can we use `is` for integer comparison?*

```{code-cell} ipython3
---
slideshow:
  slide_type: fragment
---
x, y = 1234, 1234
1234 is 1234, x is y
```

+++ {"slideshow": {"slide_type": "fragment"}}

No. The behavior of `is` is not entirely predictable. 

+++ {"slideshow": {"slide_type": "fragment"}}

**When should we use `is`?**

+++ {"slideshow": {"slide_type": "fragment"}}

`is` can be used for [built-in constants](https://docs.python.org/3/library/constants.html#built-in-constants) such as `None` and  `NotImplemented`  
because there can only be one instance of each of them.

```{code-cell} ipython3
!pip3 freeze > requirements.txt
```
