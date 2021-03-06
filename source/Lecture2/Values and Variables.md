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

# Values and Variables

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

## Integers

+++ {"slideshow": {"slide_type": "subslide"}}

**How to enter an [integer](https://docs.python.org/3/reference/lexical_analysis.html#integer-literals) in a program?**

```{code-cell}
---
slideshow:
  slide_type: fragment
---
15  # an integer in decimal
```

```{code-cell}
---
slideshow:
  slide_type: '-'
---
0b1111  # a binary number
```

```{code-cell}
---
slideshow:
  slide_type: '-'
---
0xF  # hexadecimal (base 16) with possible digits 0, 1,2,3,4,5,6,7,8,9,A,B,C,D,E,F
```

+++ {"slideshow": {"slide_type": "subslide"}}

**Why all outputs are the same?**

+++ {"slideshow": {"slide_type": "fragment"}}

- What you have entered are *integer literals*, which are integers written out literally. 
- All the literals have the same integer value in decimal.
- By default, if the last line of a code cell has a value, the jupyter notebook (*IPython*) will store and display the value as an output. 

```{code-cell}
---
slideshow:
  slide_type: fragment
---
3  # not the output of this cell
4 + 5 + 6
```

+++ {"slideshow": {"slide_type": "fragment"}}

- The last line above also has the same value, `15`.
- It is an *expression* (but not a literal) that *evaluates* to the integer value.

+++ {"slideshow": {"slide_type": "subslide"}}

**Exercise** Enter an expression that evaluates to an integer value, as big as possible.  
(You may need to interrupt the kernel if the expression takes too long to evaluate.)

```{code-cell}
---
nbgrader:
  grade: true
  grade_id: big-int
  locked: false
  points: 0
  schema_version: 3
  solution: true
  task: false
slideshow:
  slide_type: '-'
tags: [remove-output]
---
# There is no maximum for an integer for Python3. 
# See https://docs.python.org/3.1/whatsnew/3.0.html#integers
11 ** 100000
```

+++ {"slideshow": {"slide_type": "slide"}}

## Strings

+++ {"slideshow": {"slide_type": "subslide"}}

**How to enter a [string](https://docs.python.org/3/reference/lexical_analysis.html#string-and-bytes-literals) in a program?**

```{code-cell}
---
slideshow:
  slide_type: fragment
---
'\U0001f600: I am a string.'  # a sequence of characters delimited by single quotes.
```

```{code-cell}
---
slideshow:
  slide_type: fragment
---
"\N{grinning face}: I am a string."  # delimited by double quotes.
```

```{code-cell}
---
slideshow:
  slide_type: fragment
---
"""\N{grinning face}: I am a string."""  # delimited by triple single/double quotes.
```

+++ {"slideshow": {"slide_type": "fragment"}}

- `\` is called the *escape symbol*.  
- `\U0001f600` and `\N{grinning face}` are *escape sequences*.  
- These sequences represent the same grinning face emoji by its Unicode in hexadecimal and its name.

+++ {"slideshow": {"slide_type": "subslide"}}

**Why use different quotes?**

```{code-cell}
---
slideshow:
  slide_type: fragment
---
print('I\'m line #1.\nI\'m line #2.')  # \n is a control code for line feed
print("I'm line #3.\nI'm line #4.")  # no need to escape single quote.
print('''I'm line #5.
I'm line #6.''')  # multi-line string
```

+++ {"slideshow": {"slide_type": "fragment"}}

Note that:
- The escape sequence `\n` does not represent any symbol.  
- It is a *control code* that creates a new line when printing the string.  
- Another common control code is `\t` for tab.

+++ {"slideshow": {"slide_type": "fragment"}}

Using double quotes, we need not escape the single quote in `I'm`.  

+++ {"slideshow": {"slide_type": "fragment"}}

Triple quotes delimit a multi-line string, so there is no need to use `\n`.  
(You can copy and paste a multi-line string from elsewhere.)

+++ {"slideshow": {"slide_type": "subslide"}}

In programming, there are often many ways to do the same thing.  
The following is a one-line code ([one-liner](https://en.wikipedia.org/wiki/One-liner_program)) that prints multiple lines of strings without using `\n`:

```{code-cell}
---
slideshow:
  slide_type: fragment
---
print("I'm line #1", "I'm line #2", "I'm line #3", sep='\n')  # one liner
```

+++ {"slideshow": {"slide_type": "fragment"}}

- `sep='\n'` is a *keyword argument* that specifies the separator of the list of strings.
- By default, `sep=' '`, a single space character.

+++ {"slideshow": {"slide_type": "subslide"}}

In IPython, we can get the *docstring* (documentation) of a function conveniently using the symbol `?`.

```{code-cell}
---
slideshow:
  slide_type: '-'
---
?print
```

```{code-cell}
---
slideshow:
  slide_type: '-'
---
print?
```

+++ {"slideshow": {"slide_type": "subslide"}}

**Exercise** Print a cool multi-line string below.

```{code-cell}
---
nbgrader:
  grade: true
  grade_id: multi-line
  locked: false
  points: 0
  schema_version: 3
  solution: true
  task: false
slideshow:
  slide_type: '-'
---
print('''
 (??? ?????_?????)??? 
 ???(???????????????)??? 
 (..?????_?????..)
 (?????? 3???)???
''')
# See also https://github.com/glamp/bashplotlib
# Star Wars via Telnet http://asciimation.co.nz/
```

+++ {"slideshow": {"slide_type": "slide"}}

## Variables and Assignment

+++ {"slideshow": {"slide_type": "subslide"}}

It is useful to store a value and retrieve it later.  
To do so, we assign the value to a variable:

```{code-cell}
---
slideshow:
  slide_type: fragment
---
x = 15
x  # output the value of x
```

+++ {"slideshow": {"slide_type": "subslide"}}

**Is assignment the same as equality?**

+++ {"slideshow": {"slide_type": "fragment"}}

No because:
- you cannot write `15 = x`, but
- you can write `x = x + 1`, which increases the value of `x` by `1`.

+++ {"slideshow": {"slide_type": "fragment"}}

**Exercise** Try out the above code yourself.

```{code-cell}
---
nbgrader:
  grade: true
  grade_id: assign-vs-eq
  locked: false
  points: 0
  schema_version: 3
  solution: true
  task: false
slideshow:
  slide_type: '-'
---
x = x + 1
x
```

+++ {"slideshow": {"slide_type": "subslide"}}

Let's see the effect of assignment step-by-step:
1. Run the following cell.
1. Click `Next >` to see the next step of the execution.

```{code-cell}
---
slideshow:
  slide_type: '-'
---
%%mytutor -h 200
x = 15
x = x + 1
```

+++ {"slideshow": {"slide_type": "subslide"}}

The following *tuple assignment* syntax can assign multiple variables in one line.

```{code-cell}
---
slideshow:
  slide_type: '-'
---
%%mytutor -h 200
x, y, z = '15', '30', 15
```

+++ {"slideshow": {"slide_type": "fragment"}}

One can also use *chained assignment* to set different variables to the same value.

```{code-cell}
---
slideshow:
  slide_type: '-'
---
%%mytutor -h 250
x = y = z = 0
```

+++ {"slideshow": {"slide_type": "subslide"}}

Variables can be deleted using `del`. Accessing a variable before assignment raises a Name error.

```{code-cell}
---
slideshow:
  slide_type: '-'
---
del x, y
x, y
```

+++ {"slideshow": {"slide_type": "slide"}}

## Identifiers

+++ {"slideshow": {"slide_type": "fragment"}}

*Identifiers* such as variable names are case sensitive and follow certain rules.

+++ {"slideshow": {"slide_type": "subslide"}}

**What is the syntax for variable names?**

+++ {"slideshow": {"slide_type": "fragment"}}

1. Must start with a letter or `_` (an underscore) followed by letters, digits, or `_`.
1. Must not be a [keyword](https://docs.python.org/3.7/reference/lexical_analysis.html#keywords) (identifier reserved by Python):

+++ {"slideshow": {"slide_type": "-"}}

<pre>False      await      else       import     pass
None       break      except     in         raise
True       class      finally    is         return
and        continue   for        lambda     try
as         def        from       nonlocal   while
assert     del        global     not        with
async      elif       if         or         yield</pre>

+++ {"slideshow": {"slide_type": "fragment"}}

**Exercise** Evaluate the following cell and check if any of the rules above is violated.

```{code-cell}
---
code_folding: []
slideshow:
  slide_type: '-'
---
from ipywidgets import interact
@interact
def identifier_syntax(assignment=['a-number = 15',
                     'a_number = 15',
                     '15 = 15',
                     '_15 = 15',
                     'del = 15',
                     'Del = 15',
                     'type = print',
                     'print = type',
                     'input = print']):
    exec(assignment)
    print('Ok.')
```

+++ {"nbgrader": {"grade": true, "grade_id": "invalid-identifiers", "locked": false, "points": 0, "schema_version": 3, "solution": true, "task": false}, "slideshow": {"slide_type": "-"}}

1. `a-number = 15` violates Rule 1 because `-` is not allowed. `-` is interpreted as an operator.
1. `15 = 15` violates Rule 1 because `15` starts with a digit instead of letter or _.
1. `del = 15` violates Rule 2 because `del` is a keyword.

+++ {"slideshow": {"slide_type": "fragment"}}

What can we learn from the above examples?

+++ {"slideshow": {"slide_type": "fragment"}}

- `del` is a keyword and `Del` is not because identifiers are case sensitive.
- Function/method/type names `print`/`input`/`type` are not keywords and can be reassigned.  
  This can useful if you want to modify the default implementations without changing their source code.

+++ {"slideshow": {"slide_type": "fragment"}}

To help make code more readable, additional style guides such as [PEP 8](https://www.python.org/dev/peps/pep-0008/#function-and-variable-names) are available:

+++ {"slideshow": {"slide_type": "-"}}

- Function names should be lowercase, with words separated by underscores as necessary to improve readability.  
- Variable names follow the same convention as function names.

+++ {"slideshow": {"slide_type": "subslide"}}

## User Input

+++ {"slideshow": {"slide_type": "fragment"}}

**How to let the user input a value at *runtime*,  
i.e., as the program executes?**

+++ {"slideshow": {"slide_type": "fragment"}}

We can use the method `input`:
- There is no need to delimit the input string by quotation marks.
- Simply press `enter` after typing a string.

```{code-cell}
---
slideshow:
  slide_type: '-'
tags: [remove-output]
---
print('Your name is', input('Please input your name: '))
```

+++ {"slideshow": {"slide_type": "fragment"}}

- The `input` method prints its argument, if any, as a [prompt](https://en.wikipedia.org/wiki/Command-line_interface#Command_prompt).  
- It takes user's input and *return* it as its value. `print` takes in that value and prints it.

+++ {"slideshow": {"slide_type": "fragment"}}

**Exercise** Explain whether the following code prints `'My name is Python'`. Does `print` return a value? 

```{code-cell}
---
slideshow:
  slide_type: '-'
---
print('My name is', print('Python'))
```

+++ {"nbgrader": {"grade": true, "grade_id": "print-returns-none", "locked": false, "points": 0, "schema_version": 3, "solution": true, "task": false}, "slideshow": {"slide_type": "-"}}

- Unlike `input`, the function `print` does not return the string it is trying to print. Printing a string is, therefore, different from returning a string.
- `print` actually returns a `None` object that gets printed as `None`.

+++ {"slideshow": {"slide_type": "slide"}}

## Type Conversion

+++ {"slideshow": {"slide_type": "subslide"}}

The following program tries to compute the sum of two numbers from user inputs:

```{code-cell}
---
slideshow:
  slide_type: '-'
tags: [remove-output]
---
num1 = input('Please input an integer: ')
num2 = input('Please input another integer: ')
print(num1, '+', num2, 'is equal to', num1 + num2)
```

+++ {"slideshow": {"slide_type": "fragment"}}

**Exercise** There is a [bug](https://en.wikipedia.org/wiki/Software_bug) in the above code. Can you locate the error?

+++ {"nbgrader": {"grade": true, "grade_id": "cell-d1d22bc89eb9f7b6", "locked": false, "points": 0, "schema_version": 3, "solution": true, "task": false}, "slideshow": {"slide_type": "-"}}

The two numbers are concatenated instead of added together.

+++ {"slideshow": {"slide_type": "subslide"}}

`input` *returns* user input as a string.  
E.g., if the user enters `12`, the input is
- not treated as the integer twelve, but rather
- treated as a string containing two characters, one followed by two.

+++ {"slideshow": {"slide_type": "fragment"}}

To see this, we can use `type` to return the data type of an expression.

```{code-cell}
---
slideshow:
  slide_type: '-'
tags: [remove-output]
---
num1 = input('Please input an integer: ')
print('Your input is', num1, 'with type', type(num1))
```

+++ {"slideshow": {"slide_type": "fragment"}}

**Exercise** `type` applies to any expressions. Try it out below on `15`, `print`, `print()`, `input`, and even `type` itself and `type(type)`.

```{code-cell}
---
nbgrader:
  grade: true
  grade_id: type
  locked: false
  points: 0
  schema_version: 3
  solution: true
  task: false
slideshow:
  slide_type: '-'
---
type(15), type(print), type(print()), type(input), type(type), type(type(type))
```

+++ {"slideshow": {"slide_type": "fragment"}}

**So what happens when we add strings together?**

```{code-cell}
---
slideshow:
  slide_type: '-'
---
'4' + '5' + '6'
```

+++ {"slideshow": {"slide_type": "fragment"}}

**How to fix the bug then?**

+++ {"slideshow": {"slide_type": "fragment"}}

We can convert a string to an integer using `int`.

```{code-cell}
---
slideshow:
  slide_type: '-'
---
int('4') + int('5') + int('6')
```

+++ {"slideshow": {"slide_type": "fragment"}}

We can also convert an integer to a string using `str`.

```{code-cell}
---
slideshow:
  slide_type: '-'
---
str(4) + str(5) + str(6)
```

+++ {"slideshow": {"slide_type": "fragment"}}

**Exercise** Fix the bug in the following cell.

```{code-cell}
---
nbgrader:
  grade: false
  grade_id: string-concat-bug
  locked: false
  schema_version: 3
  solution: true
  task: false
slideshow:
  slide_type: '-'
tags: [remove-output]
---
num1 = input('Please input an integer: ')
num2 = input('Please input another integer: ')
# print(num1, '+', num2, 'is equal to', num1 + num2)  # fix this line below
### BEGIN SOLUTION
print(num1, '+', num2, 'is equal to', int(num1) + int(num2))
### END SOLUTION
```

+++ {"slideshow": {"slide_type": "slide"}}

## Error

+++ {"slideshow": {"slide_type": "fragment"}}

In addition to writing code, a programmer spends significant time in *debugging* code that contains errors.

+++ {"slideshow": {"slide_type": "fragment"}}

**Can an error be automatically detected by the computer?**

+++ {"slideshow": {"slide_type": "fragment"}}

- You have just seen an example of *logical error*, which is due to an error in the logic.  
- The ability to debug or even detect such error is, unfortunately, beyond Python's intelligence.

+++ {"slideshow": {"slide_type": "fragment"}}

Other kinds of error may be detected automatically.  
As an example, note that we can omit `+` for string concatenation, but we cannot omit it for integer summation:

```{code-cell}
---
slideshow:
  slide_type: fragment
---
print('Skipping + for string concatenation')
'4' '5' '6'
```

```{code-cell}
---
slideshow:
  slide_type: '-'
---
print('Skipping + for integer summation')
4 5 6
```

+++ {"slideshow": {"slide_type": "fragment"}}

Python interpreter detects the bug and raises a *syntax* error.

+++ {"slideshow": {"slide_type": "subslide"}}

**Why Syntax error can be detected automatically?  
Why is the print statement before the error not executed?**

+++ {"slideshow": {"slide_type": "fragment"}}

- The Python interpreter can easily detect syntax error even before executing the code simply because
- the interpreter fails to interpret the code, i.e., translates the code to lower-level executable code.

+++ {"slideshow": {"slide_type": "subslide"}}

The following code raises a different kind of error.

```{code-cell}
---
slideshow:
  slide_type: '-'
---
print("Evaluating '4' + '5' + 6")
'4' + '5' + 6  # summing string with integer
```

+++ {"slideshow": {"slide_type": "fragment"}}

**Why Python throws a TypeError when evaluating `'4' + '5' + 6`?**

+++ {"slideshow": {"slide_type": "fragment"}}

There is no default implementation of `+` operation on a value of type `str` and a value of type `int`. 

+++ {"slideshow": {"slide_type": "fragment"}}

- Unlike syntax error, the Python interpreter can only detect type error at runtime (when executing the code.) 
- Hence, such error is called a *runtime error*.

+++ {"slideshow": {"slide_type": "subslide"}}

**Why is TypeError a runtime error?**

+++ {"slideshow": {"slide_type": "fragment"}}

 The short answer is that Python is a [strongly-and-dynamically-typed](https://en.wikipedia.org/wiki/Strong_and_weak_typing) language:
- Strongly-typed: Python does not force a type conversion to avoid a type error.
- Dynamically-typed: Python allow data type to change at runtime.

+++ {"slideshow": {"slide_type": "fragment"}}

The underlying details are more complicated than required for this course. It helps if you already know the following languages:
- JavaScript, which is a *weakly-typed* language that forces a type conversion to avoid a type error.
- C, which is a *statically-typed* language that does not allow data type to change at runtime.

```{code-cell}
---
slideshow:
  slide_type: '-'
---
%%javascript
alert('4' + '5' + 6)  // no error because 6 is converted to a str automatically
```

+++ {"slideshow": {"slide_type": "fragment"}}

A weakly-typed language may seem more robust, but it can lead to [more logical errors](https://www.oreilly.com/library/view/fluent-conference-javascript/9781449339203/oreillyvideos1220106.html).  
To improve readability, [typescript](https://www.typescriptlang.org/) is a strongly-typed replacement of javascript.

+++ {"slideshow": {"slide_type": "fragment"}}

**Exercise** Not all the strings can be converted into integers. Try breaking the following code by providing invalid inputs and record them in the subsequent cell. Explain whether the errors are runtime errors.

```{code-cell}
---
slideshow:
  slide_type: '-'
tags: [remove-output]
---
num1 = input('Please input an integer: ')
num2 = input('Please input another integer: ')
print(num1, '+', num2, 'is equal to', int(num1) + int(num2))
```

+++ {"nbgrader": {"grade": true, "grade_id": "invalid-input", "locked": false, "points": 0, "schema_version": 3, "solution": true, "task": false}, "slideshow": {"slide_type": "-"}}

The possible invalid inputs are:
> `4 + 5 + 6`, `15.0`, `fifteen`

It raises a value error, which is a runtime error detected during execution.  

Note that the followings are okay
> int('-1'), eval('4 + 5 + 6')

+++ {"slideshow": {"slide_type": "slide"}}

## Floating Point Numbers

+++ {"slideshow": {"slide_type": "fragment"}}

Not all numbers are integers. In Enginnering, we often need to use fractions.

+++ {"slideshow": {"slide_type": "subslide"}}

**How to enter fractions in a program?**

```{code-cell}
---
slideshow:
  slide_type: fragment
---
x = -0.1 # decimal number
y = -1.0e-1 # scientific notation
z = -1/10 # fraction
x, y, z, type(x), type(y), type(z)
```

+++ {"slideshow": {"slide_type": "subslide"}}

**What is the type `float`?**

+++ {"slideshow": {"slide_type": "fragment"}}

- `float` corresponds to the [*floating point* representation](https://en.wikipedia.org/wiki/Floating-point_arithmetic#Floating-point_numbers).  
- A `float` in stored exactly the way we write it in scientific notation: 

$$
\overbrace{-}^{\text{sign}} \underbrace{1.0}_{\text{mantissa}\kern-1em}e\overbrace{-1}^{\text{exponent}\kern-1em}=-1\times 10^{-1}
$$
- The [truth](https://www.h-schmidt.net/FloatConverter/IEEE754.html) is more complicated than required for the course.

+++ {"slideshow": {"slide_type": "fragment"}}

Integers in mathematics may be regarded as a `float` instead of `int`:

```{code-cell}
---
slideshow:
  slide_type: '-'
---
type(1.0), type(1e2)
```

+++ {"slideshow": {"slide_type": "fragment"}}

You can also convert an `int` or a `str` to a `float`.

```{code-cell}
---
slideshow:
  slide_type: '-'
---
float(1), float('1')
```

+++ {"slideshow": {"slide_type": "subslide"}}

**Is it better to store an integer as `float`?**

+++ {"slideshow": {"slide_type": "fragment"}}

Python stores a [floating point](https://docs.python.org/3/library/sys.html#sys.float_info) with finite precision (usually as a 64bit binary fraction):

```{code-cell}
---
slideshow:
  slide_type: fragment
---
import sys
sys.float_info
```

+++ {"slideshow": {"slide_type": "fragment"}}

It cannot represent a number larger than the `max`:

```{code-cell}
---
slideshow:
  slide_type: '-'
---
sys.float_info.max * 2
```

+++ {"slideshow": {"slide_type": "fragment"}}

The precision also affects the check for equality.

```{code-cell}
---
slideshow:
  slide_type: '-'
---
(1.0 == 1.0 + sys.float_info.epsilon * 0.5, # returns true if equal
 1.0 == 1.0 + sys.float_info.epsilon * 0.6, sys.float_info.max + 1 == sys.float_info.max)
```

+++ {"slideshow": {"slide_type": "fragment"}}

Another issue with float is that it may keep more decimal places than desired.

```{code-cell}
---
slideshow:
  slide_type: '-'
---
1/3
```

+++ {"slideshow": {"slide_type": "subslide"}}

**How to [round](https://docs.python.org/3/library/functions.html#round) a floating point number to the desired number of decimal places?**

```{code-cell}
---
slideshow:
  slide_type: fragment
---
round(2.665,2), round(2.675,2)
```

+++ {"slideshow": {"slide_type": "fragment"}}

**Why 2.675 rounds to 2.67 instead of 2.68?**

+++ {"slideshow": {"slide_type": "fragment"}}

- A `float` is actually represented in binary.  
- A decimal fraction [may not be represented exactly in binary](https://docs.python.org/3/tutorial/floatingpoint.html#tut-fp-issues).

+++ {"slideshow": {"slide_type": "subslide"}}

The `round` function can also be applied to an integer.

```{code-cell}
---
slideshow:
  slide_type: fragment
---
round(150,-2), round(250,-2)
```

+++ {"slideshow": {"slide_type": "fragment"}}

**Why 250 rounds to 200 instead of 300?**

+++ {"slideshow": {"slide_type": "fragment"}}

- Python 3 implements the default rounding method in [IEEE 754](https://en.wikipedia.org/w/index.php?title=IEEE_754#Rounding_rules).

+++ {"slideshow": {"slide_type": "slide"}}

## String Formatting

+++ {"slideshow": {"slide_type": "subslide"}}

**Can we round a `float` or `int` for printing but not calculation?**

+++ {"slideshow": {"slide_type": "fragment"}}

This is possible with [*format specifications*](https://docs.python.org/3/library/string.html#format-specification-mini-language).

```{code-cell}
---
slideshow:
  slide_type: '-'
---
x = 10000/3
print('x ??? {:.2f} (rounded to 2 decimal places)'.format(x))
x
```

+++ {"slideshow": {"slide_type": "subslide"}}

- `{:.2f}` is a *format specification* 
- that gets replaced by a string 
- that represents the argument `x` of `format` 
- as a decimal floating point number rounded to 2 decimal places.

+++ {"slideshow": {"slide_type": "fragment"}}

**Exercise** Play with the following widget to learn the effect of different format specifications. In particular, print `10000/3` as `3,333.33`.

```{code-cell}
---
code_folding: [7]
slideshow:
  slide_type: '-'
---
from ipywidgets import interact
@interact(x='10000/3',
          align={'None':'','<':'<','>':'>','=':'=','^':'^'},
          sign={'None':'','+':'+','-':'-','SPACE':' '},
          width=(0,20),
          grouping={'None':'','_':'_',',':','},
          precision=(0,20))
def print_float(x,sign,align,grouping,width=0,precision=2):
    format_spec = f"{{:{align}{sign}{'' if width==0 else width}{grouping}.{precision}f}}"
    print("Format spec:",format_spec)
    print("x ???",format_spec.format(eval(x)))
```

```{code-cell}
---
nbgrader:
  grade: true
  grade_id: format-spec
  locked: false
  points: 0
  schema_version: 3
  solution: true
  task: false
---
print('{:,.2f}'.format(10000/3))
```

+++ {"slideshow": {"slide_type": "subslide"}}

String formatting is useful for different data types other than `float`.  
E.g., consider the following program that prints a time specified by some variables.

```{code-cell}
---
slideshow:
  slide_type: '-'
---
# Some specified time
hour = 12
minute = 34
second = 56

print("The time is " + str(hour) + ":" + str(minute) + ":" + str(second)+".")
```

+++ {"slideshow": {"slide_type": "fragment"}}

Imagine you have to show also the date in different formats.  
The code can become very hard to read/write because 
- the message is a concatenation of multiple strings and
- the integer variables need to be converted to strings.

+++ {"slideshow": {"slide_type": "fragment"}}

Omitting `+` leads to syntax error. Removing `str` as follows also does not give the desired format.

```{code-cell}
---
slideshow:
  slide_type: '-'
---
print("The time is ", hour, ":", minute, ":", second, ".")  # note the extra spaces
```

+++ {"slideshow": {"slide_type": "subslide"}}

To make the code more readable, we can use the `format` function as follows.

```{code-cell}
---
slideshow:
  slide_type: '-'
---
message = "The time is {}:{}:{}."
print(message.format(hour,minute,second))
```

+++ {"slideshow": {"slide_type": "fragment"}}

- We can have multiple *place-holders* `{}` inside a string.
- We can then provide the contents (any type: numbers, strings..) using the `format` function, which
- substitutes the place-holders by the function arguments from left to right.

+++ {"slideshow": {"slide_type": "subslide"}}

According to the [string formatting syntax](https://docs.python.org/3/library/string.html#format-string-syntax), we can change the order of substitution using 
- indices *(0 is the first item)* or 
- names inside the placeholder `{}`:

```{code-cell}
---
slideshow:
  slide_type: fragment
---
print("You should {0} {1} what I say instead of what I {0}.".format("do", "only"))
print("The surname of {first} {last} is {last}.".format(first="John", last="Doe"))
```

+++ {"slideshow": {"slide_type": "subslide"}}

You can even put variables inside the format specification directly and have a nested string formatting.

```{code-cell}
---
slideshow:
  slide_type: '-'
---
align, width = "^", 5
print(f"{{:*{align}{width}}}".format(x))  # note the syntax f"..."
```

+++ {"slideshow": {"slide_type": "subslide"}}

**Exercise** Play with the following widget to learn more about the formating specification.  
1. What happens when `align` is none but `fill` is `*`?
1. What happens when the `expression` is a multi-line string?

```{code-cell}
---
code_folding: []
slideshow:
  slide_type: '-'
---
from ipywidgets import interact
@interact(expression=r"'ABC'",
          fill='*',
          align={'None':'','<':'<','>':'>','=':'=','^':'^'},
          width=(0,20))
def print_objectt(expression,fill,align='^',width=10):
    format_spec = f"{{:{fill}{align}{'' if width==0 else width}}}"
    print("Format spec:",format_spec)
    print("Print:",format_spec.format(eval(expression)))
```

+++ {"nbgrader": {"grade": true, "grade_id": "string-formatting", "locked": false, "points": 0, "schema_version": 3, "solution": true, "task": false}}

1. It returns a ValueError because align must be specified when fill is.
1. The newline character is simply regarded a character. The formatting is not applied line-by-line. E.g., try 'ABC\nDEF'.
