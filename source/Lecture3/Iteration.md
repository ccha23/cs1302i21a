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

# Iteration

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
from ipywidgets import interact
```

+++ {"slideshow": {"slide_type": "slide"}}

## Motivation

+++ {"slideshow": {"slide_type": "fragment"}}

Many tasks are repetitive:
- To print from 1 up to a user-specified number, which can be arbitrarily large.
- To compute the maximum of a sequence of numbers, which can be arbitrarily long.
- To repeatedly ask users for input until the input is within the right range.

+++ {"slideshow": {"slide_type": "subslide"}}

**How to write code to perform repetitive tasks?**

+++ {"slideshow": {"slide_type": "fragment"}}

E.g., can you complete the following code to print from 1 up to a user-specified number?

```{code-cell}
---
slideshow:
  slide_type: '-'
---
%%mytutor -h 300
num = int(input('>'))
if 1 < num: print(1)
if 2 < num: print(2)
if 3 < num: print(3)
# YOUR CODE HERE 
```

+++ {"slideshow": {"slide_type": "subslide"}}

*code duplication* is not good because:
- Duplicate code is hard to read/write/maintain.  
    Imagine there is a small change needed to every duplicate code.
- The number of repetitions may not be known before runtime.

+++ {"slideshow": {"slide_type": "fragment"}}

Instead, programmers write a *loop* which specifies a piece of code to be executed iteratively.

+++ {"slideshow": {"slide_type": "slide"}}

## For Loop

+++ {"slideshow": {"slide_type": "subslide"}}

### Iterate over a sequence

+++ {"slideshow": {"slide_type": "fragment"}}

**How to print from 1 up to 4?**

+++ {"slideshow": {"slide_type": "fragment"}}

We can use a [`for` statement](https://docs.python.org/3.3/tutorial/controlflow.html#for-statements) as follows:

```{code-cell}
---
slideshow:
  slide_type: '-'
---
%%mytutor -h 300
for i in 1, 2, 3, 4:
    print(i)
```

+++ {"slideshow": {"slide_type": "fragment"}}

- `i` is automatically assigned to each element in the sequence `1, 2, 3, 4` one-by-one from left to right.
- After each assignment, the body `print(i)` is executed. 

N.b., if `i` is defined before the for loop, its value will be overwritten.  

+++ {"slideshow": {"slide_type": "subslide"}}

The assignment is not restricted to integers and can also be a tuple assignment.

```{code-cell}
---
slideshow:
  slide_type: '-'
---
tuples = (0,'l'), (1,'o'), (2,'o'), (3,'p')
for i,c in tuples: print(i,c)  # one-liner
```

+++ {"slideshow": {"slide_type": "fragment"}}

An even shorter code...

```{code-cell}
---
slideshow:
  slide_type: '-'
---
for i,c in enumerate('loop'): print(i,c)
```

+++ {"slideshow": {"slide_type": "subslide"}}

### Iterate over a range

+++ {"slideshow": {"slide_type": "fragment"}}

**How to print up to a user-specified number?**

+++ {"slideshow": {"slide_type": "fragment"}}

We can use [`range`](https://docs.python.org/3/library/stdtypes.html#range):

```{code-cell}
---
slideshow:
  slide_type: '-'
tags: [remove-output]
---
stop = int(input('>')) + 1
for i in range(stop):
    print(i)
```

+++ {"slideshow": {"slide_type": "fragment"}}

**Why add 1 to the user input number?**

+++ {"slideshow": {"slide_type": "fragment"}}

`range(stop)` generates a sequence of integers from `0` up to *but excluding* `stop`.

+++ {"slideshow": {"slide_type": "fragment"}}

**How to start from a number different from `0`?**

```{code-cell}
---
slideshow:
  slide_type: fragment
---
for i in range(1,5): print(i)
```

+++ {"slideshow": {"slide_type": "fragment"}}

**What about a step size different from `1`?**

```{code-cell}
---
slideshow:
  slide_type: fragment
---
for i in range(0,5,2): print(i)  # starting number must also be specified. Why?
```

+++ {"slideshow": {"slide_type": "subslide"}}

**Exercise** How to count down from 4 to 0? Do it without addition or subtraction.

```{code-cell}
---
nbgrader:
  grade: false
  grade_id: count-down
  locked: false
  schema_version: 3
  solution: true
  task: false
slideshow:
  slide_type: '-'
---
### BEGIN SOLUTION
for i in range(4,-1,-1): print(i)
### END SOLUTION
```

+++ {"slideshow": {"slide_type": "subslide"}}

**Exercise** Print from `0` to a user-specified number but in steps of `0.5`.  
E.g., if the user inputs `2`, the program should print:
```
0.0
0.5
1.0
1.5
2.0
```

*Note:* `range` only accepts integer arguments.

```{code-cell}
---
nbgrader:
  grade: false
  grade_id: fractional-step
  locked: false
  schema_version: 3
  solution: true
  task: false
slideshow:
  slide_type: '-'
tags: [remove-output]
---
num = int(input('>'))
### BEGIN SOLUTION
for i in range(0, 2 * num + 1, 1):
    print(i / 2)
### END SOLUTION
```

+++ {"slideshow": {"slide_type": "subslide"}}

**Exercise** How to print the character `'*'` repeatedly for `m` rows and `n` columns?  
*Hint:* Use a *nested for loop*, i.e., write a for loop (called *inner loop*) inside the body of another for loop (*outer loop*).

```{code-cell}
---
nbgrader:
  grade: false
  grade_id: nested-loop
  locked: false
  schema_version: 3
  solution: true
  task: false
slideshow:
  slide_type: '-'
---
@interact(m=(0, 10), n=(0, 10))
def draw_rectangle(m=5, n=5):
    ### BEGIN SOLUTION
    for i in range(m):
        for j in range(n):
            print('*', end='')
        print()
    ### END SOLUTION
```

+++ {"slideshow": {"slide_type": "slide"}}

### Iterate over a string

+++ {"slideshow": {"slide_type": "subslide"}}

**What does the following do?**

```{code-cell}
---
slideshow:
  slide_type: '-'
---
%%mytutor -h 300
for character in 'loop': print(character)
```

+++ {"slideshow": {"slide_type": "fragment"}}

A string is *iterable* because it can be regarded as a sequence of characters.
- The function [`len`](https://docs.python.org/3/library/functions.html#len) can return the length of a string.
- The indexing operator `[]` can return the character of a string at a specified location.

```{code-cell}
---
slideshow:
  slide_type: '-'
---
message = "loop"
print('length:', len(message))
print('characters:', message[0], message[1], message[2], message[3])
```

+++ {"slideshow": {"slide_type": "fragment"}}

We can also iterate over a string as follows although it is less elegant:

```{code-cell}
---
slideshow:
  slide_type: '-'
---
for i in range(len('loop')): print('loop'[i])
```

+++ {"slideshow": {"slide_type": "subslide"}}

**Exercise** Print a string assigned to `message` in reverse.  
E.g., `'loop'` should be printed as `'pool'`.

```{code-cell}
---
nbgrader:
  grade: false
  grade_id: cell-90113e8af18be3c4
  locked: false
  schema_version: 3
  solution: true
  task: false
slideshow:
  slide_type: '-'
---
@interact(message='loop')
def reverse_print(message):
    ### BEGIN SOLUTION
    for i in range(len(message)):
        print(message[-i - 1], end='')
    ### END SOLUTION
```

+++ {"slideshow": {"slide_type": "slide"}}

## While Loop

+++ {"slideshow": {"slide_type": "subslide"}}

**How to repeatedly ask the user to enter an input until the user input is not empty?**

+++ {"slideshow": {"slide_type": "fragment"}}

Python provides the [`while` statement](https://docs.python.org/3/reference/compound_stmts.html#while) to loop until a specified condition is false.

```{code-cell}
---
slideshow:
  slide_type: '-'
tags: [remove-output]
---
while not input('Input something please:'): pass
```

+++ {"slideshow": {"slide_type": "fragment"}}

As long as the condition after `while` is true, the body gets executed repeatedly. In the above example,
- if user press enter without inputting anything, 
- `input` returns an empty string `''`, which is [regarded as `False`](https://docs.python.org/3/reference/expressions.html#booleans), and so
- the looping condition `not input('...')` is `True`.

+++ {"slideshow": {"slide_type": "subslide"}}

**Is it possible to use a for loop instead of a while loop?**

+++ {"slideshow": {"slide_type": "fragment"}}

- Not without hacks because the for loop is a *definite loop* which has a definite number of iterations before the execution of the loop.
- `while` statement is useful for an *indefinite loop* where the number of iterations is unknown before the execution of the loop.

+++ {"slideshow": {"slide_type": "fragment"}}

It is possible, however, to replace a for loop by a while loop.  
E.g., the following code prints from `0` to `4` using a while loop instead of a for loop.

```{code-cell}
---
slideshow:
  slide_type: fragment
---
i = 0
while i <= 4:
    print(i)
    i += 1
```

+++ {"slideshow": {"slide_type": "fragment"}}

- A while loop may not be as elegant (short), c.f., `for i in range(5): print(i)`, but
- it can always be as efficient.

+++ {"slideshow": {"slide_type": "subslide"}}

**Should we just use while loop?**

+++ {"slideshow": {"slide_type": "fragment"}}

Consider using the following while loop to print from `0` to a user-specified value.

```{code-cell}
---
slideshow:
  slide_type: '-'
tags: [remove-output]
---
num = int(input('>'))
i = 0
while i!=num+1: 
    print(i)
    i += 1
```

+++ {"slideshow": {"slide_type": "fragment"}}

**Exercise** Is the above while loop doing the same thing as the for loop below?

```{code-cell}
---
slideshow:
  slide_type: '-'
tags: [remove-output]
---
for i in range(int(input('>')) + 1): print(i)
```

+++ {"nbgrader": {"grade": true, "grade_id": "infinite-loop", "locked": false, "points": 0, "schema_version": 3, "solution": true, "task": false}, "slideshow": {"slide_type": "-"}}

When user input negative integers smaller than or equal to -2,
- the while loop becomes an infinite loop, but
- the for loop terminates without printing any number.

+++ {"slideshow": {"slide_type": "fragment"}}

We have to be careful not to create unintended *infinite loops*.  
The computer can't always detect whether there is an infinite loop. ([Why not?](https://en.wikipedia.org/wiki/Halting_problem))

+++ {"slideshow": {"slide_type": "slide"}}

## Break/Continue/Else Constructs of a Loop

+++ {"slideshow": {"slide_type": "subslide"}}

### Breaking out of a loop

+++ {"slideshow": {"slide_type": "fragment"}}

**Is the following an infinite loop?**

```{code-cell}
---
slideshow:
  slide_type: '-'
---
%%mytutor -h 300
while True:
    message = input('Input something please:')
    if message: break
print('You entered:', message)
```

+++ {"slideshow": {"slide_type": "fragment"}}

The loop is terminated by the [`break` statement](https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops) when user input is non-empty.

+++ {"slideshow": {"slide_type": "subslide"}}

**Why is the `break` statement useful?**

+++ {"slideshow": {"slide_type": "fragment"}}

 Recall the earlier `while` loop:

```{code-cell}
---
slideshow:
  slide_type: '-'
---
%%mytutor -h 300
while not input('Input something please:'): pass 
```

+++ {"slideshow": {"slide_type": "fragment"}}

This while loop is not useful because it does not store the user input.

+++ {"slideshow": {"slide_type": "subslide"}}

**Is the `break` statement strictly necessary?** 

+++ {"slideshow": {"slide_type": "fragment"}}

We can avoid `break` statement by using *flags*, which are boolean variables for flow control:

```{code-cell}
---
slideshow:
  slide_type: fragment
---
%%mytutor -h 350
has_no_input = True
while has_no_input:
    message = input('Input something please:')
    if message: has_no_input = False
print('You entered:', message)
```

+++ {"slideshow": {"slide_type": "fragment"}}

Using flags makes the program more readable, and we can use multiple flags for more complicated behavior.  
The variable names for flags are often `is_...`, `has_...`, etc.

+++ {"slideshow": {"slide_type": "slide"}}

### Continue to Next Iteration

+++ {"slideshow": {"slide_type": "subslide"}}

**What does the following program do?  
Is it an infinite loop?**

```{code-cell}
---
slideshow:
  slide_type: '-'
---
%%mytutor -h 300
while True:
    message = input('Input something please:')
    if not message: continue
    print('You entered:', message)
```

+++ {"slideshow": {"slide_type": "fragment"}}

- The program repeatedly ask the user for input.
- If the input is empty, the `continue` statement will skip to the next iteration.
- The loop can only be terminated by interrupting the kernel.
- Such an infinite loop can be useful. E.g., your computer clock continuously updates the current time.

+++ {"slideshow": {"slide_type": "fragment"}}

**Exercise** Is the `continue` statement strictly necessary? Can you rewrite the above program without the `continue` statement? 

```{code-cell}
---
nbgrader:
  grade: false
  grade_id: avoid-continue
  locked: false
  schema_version: 3
  solution: true
  task: false
slideshow:
  slide_type: '-'
---
%%mytutor -h 350
while True:
    message = input('Input something please:')
    ### BEGIN SOLUTION
    if message:
        print('You entered:', message)
    ### END SOLUTION
```

+++ {"slideshow": {"slide_type": "subslide"}}

### Else construct for a loop

+++ {"slideshow": {"slide_type": "fragment"}}

The following program 
- checks whether the user input is a positive integer using `isdigit`, and if so,
- check if the positive integer is a composite number, i.e., a product of two smaller positive integers.

```{code-cell}
---
slideshow:
  slide_type: '-'
---
@interact(num='1')
def check_composite(num):
    if num.isdigit():
        num = int(num)
        for divisor in range(2,num):
            if num % divisor:
                continue
            else:
                print('It is composite.')
                break
        else:
            print('It is not composite.')
    else:
        print('Not a positive integer.')
```

```{code-cell}
---
slideshow:
  slide_type: fragment
---
%%mytutor -h 500 
def check_composite(num):
    if num.isdigit():
        num = int(num)
        for divisor in range(2,num):
            if num % divisor:
                continue
            else:
                print('It is composite.')
                break
        else:
            print('It is not composite.')
    else:
        print('Not a positive integer.')
        
check_composite('1')
check_composite('2')
check_composite('3')
check_composite('4')
```

+++ {"slideshow": {"slide_type": "fragment"}}

In addition to using `continue` and `break` in an elegant way,  
the code also uses an else clause that is executed only when the loop terminates *normally* not by `break`.

+++ {"slideshow": {"slide_type": "fragment"}}

**Exercise** There are three else claues in the earlier code. Which one is for the loop?

+++ {"slideshow": {"slide_type": "-"}}

- The second else clause that `print('It is not composite.')`.
- The clause is called when there is no divisor found in the range from `2` to `num`.

+++ {"slideshow": {"slide_type": "subslide"}}

**Exercise** Convert the for loop to a while loop.  
Can you improve the code to use fewer iterations?

```{code-cell}
---
nbgrader:
  grade: false
  grade_id: for-to-while
  locked: false
  schema_version: 3
  solution: true
  task: false
slideshow:
  slide_type: '-'
---
@interact(num='1')
def check_composite(num):
    if num.isdigit():
        num = int(num)
        # for divisor in range(2,num):    # use while instead
        divisor = 2
        while divisor <= num**0.5: 
            if num % divisor:
                divisor += 1
            else:
                print('It is composite.')
                break
        else:
            print('It is not composite.')
    else:
        print('Not a positive integer.')
```
