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

# Expressions and Arithmetic

+++ {"slideshow": {"slide_type": "-"}, "tags": ["remove-cell"]}

**CS1302 Introduction to Computer Programming**
___

+++ {"slideshow": {"slide_type": "slide"}}

## Operators

+++ {"slideshow": {"slide_type": "fragment"}}

The followings are common operators you can use to form an expression in Python:

+++ {"slideshow": {"slide_type": "-"}}

| Operator  |   Operation    | Example |
| --------: | :------------- | :-----: |
| unary `-` | Negation       |  `-y`   |
|       `+` | Addition       | `x + y` |
|       `-` | Subtraction    | `x - y` |
|       `*` | Multiplication |  `x*y`  |
|       `/` | Division       |  `x/y`  |

+++ {"slideshow": {"slide_type": "fragment"}}

- `x` and `y` in the examples are called the *left and right operands* respectively.
- The first operator is a *unary operator*, which operates on just one operand.   
    (`+` can also be used as a unary operator, but that is not useful.)
- All other operators are *binary operators*, which operate on two operands.

+++ {"slideshow": {"slide_type": "fragment"}}

Python also supports some more operators such as the followings:

+++ {"slideshow": {"slide_type": "-"}}

| Operator |    Operation     | Example |
| -------: | :--------------- | :-----: |
|     `//` | Integer division | `x//y`  |
|      `%` | Modulo           |  `x%y`  |
|     `**` | Exponentiation   | `x**y`  |

```{code-cell}
---
code_folding: [0]
slideshow:
  slide_type: fragment
---
# ipywidgets to demonstrate the operations of binary operators
from ipywidgets import interact
binary_operators = {'+':' + ','-':' - ','*':'*','/':'/','//':'//','%':'%','**':'**'}
@interact(operand1=r'10',
          operator=binary_operators,
          operand2=r'3')
def binary_operation(operand1,operator,operand2):
    expression = f"{operand1}{operator}{operand2}"
    value = eval(expression)
    print(f"""{'Expression:':>11} {expression}\n{'Value:':>11} {value}\n{'Type:':>11} {type(value)}""")
```

+++ {"slideshow": {"slide_type": "fragment"}}

**Exercise** What is the difference between `/` and `//`?

+++ {"nbgrader": {"grade": true, "grade_id": "integer-division", "locked": false, "points": 0, "schema_version": 3, "solution": true, "task": false}, "slideshow": {"slide_type": "-"}}

- `/` is the usual division, and so `10/3` returns the floating-point number $3.\dot{3}$.
- `//` is integer division, and so `10//3` gives the integer quotient 3.

+++ {"slideshow": {"slide_type": "fragment"}}

**What does the modulo operator `%` do?**

+++ {"slideshow": {"slide_type": "-"}}

You can think of it as computing the remainder, but the [truth](https://docs.python.org/3/reference/expressions.html#binary-arithmetic-operations) is more complicated than required for the course.

+++ {"slideshow": {"slide_type": "fragment"}}

**Exercise** What does `'abc' * 3` mean? What about `10 * 'a'`?

+++ {"nbgrader": {"grade": true, "grade_id": "concatenation", "locked": false, "points": 0, "schema_version": 3, "solution": true, "task": false}, "slideshow": {"slide_type": "-"}}

- The first expression means concatenating `'abc'` three times.
- The second means concatenating `'a'` ten times.

+++ {"slideshow": {"slide_type": "fragment"}}

**Exercise** How can you change the default operands (`10` and `3`) for different operators so that the overall expression has type `float`.  
Do you need to change all the operands to `float`?

+++ {"nbgrader": {"grade": true, "grade_id": "mixed-type", "locked": false, "points": 0, "schema_version": 3, "solution": true, "task": false}, "slideshow": {"slide_type": "-"}}

- `/` already returns a `float`.
- For all other operators, changing at least one of the operands to `float` will return a `float`.

+++ {"slideshow": {"slide_type": "slide"}}

## Operator Precedence and Associativity

+++ {"slideshow": {"slide_type": "fragment"}}

An expression can consist of a sequence of operations performed in a row such as `x + y*z`.

+++ {"slideshow": {"slide_type": "fragment"}}

**How to determine which operation should be performed first?**

+++ {"slideshow": {"slide_type": "fragment"}}

Like arithmetics, the order of operations is decided based on the following rules applied sequentially: 
1. *grouping* by parentheses: inner grouping first
1. operator *precedence/priority*: higher precedence first
1. operator *associativity*:
    - left associativity: left operand first
    - right associativity: right operand first

+++ {"slideshow": {"slide_type": "subslide"}}

**What are the operator precedence and associativity?**

+++ {"slideshow": {"slide_type": "fragment"}}

The following table gives a concise summary:

+++ {"slideshow": {"slide_type": "-"}}

|    Operators     | Associativity |
| :--------------- | :-----------: |
| `**`             |     right     |
| `-` (unary)      |     right     |
| `*`,`/`,`//`,`%` |     left      |
| `+`,`-`          |     left      |

+++ {"slideshow": {"slide_type": "fragment"}}

**Exercise** Play with the following widget to understand the precedence and associativity of different operators.  
In particular, explain whether the expression `-10 ** 2*3` gives $(-10)^{2\times 3}= 10^6 = 1000000$.

```{code-cell}
---
slideshow:
  slide_type: '-'
---
from ipywidgets import fixed
@interact(operator1={'None':'','unary -':'-'},
          operand1=fixed(r'10'),
          operator2=binary_operators,
          operand2=fixed(r'2'),
          operator3=binary_operators,
          operand3=fixed(r'3')
          )
def three_operators(operator1,operand1,operator2,operand2,operator3,operand3):
    expression = f"{operator1}{operand1}{operator2}{operand2}{operator3}{operand3}"
    value = eval(expression)
    print(f"""{'Expression:':>11} {expression}\n{'Value:':>11} {value}\n{'Type:':>11} {type(value)}""")
```

+++ {"nbgrader": {"grade": true, "grade_id": "precedence", "locked": false, "points": 0, "schema_version": 3, "solution": true, "task": false}, "slideshow": {"slide_type": "-"}}

The expression evaluates to $(-(10^2))\times 3=-300$ instead because the exponentiation operator `**` has higher precedence than both the multiplication `*` and the negation operators `-`.

+++ {"slideshow": {"slide_type": "fragment"}}

**Exercise** To avoid confusion in the order of operations, we should follow the [style guide](https://www.python.org/dev/peps/pep-0008/#other-recommendations) when writing expression.  
What is the proper way to write `-10 ** 2*3`? 

```{code-cell}
---
nbgrader:
  grade: true
  grade_id: pep8
  locked: false
  points: 0
  schema_version: 3
  solution: true
  task: false
slideshow:
  slide_type: '-'
---
print(-10**2 * 3)  # can use use code-prettify extension to fix incorrect styles
print((-10)**2 * 3)
```

+++ {"slideshow": {"slide_type": "slide"}}

## Augmented Assignment Operators

+++ {"slideshow": {"slide_type": "fragment"}}

- For convenience, Python defines the [augmented assignment operators](https://docs.python.org/3/reference/simple_stmts.html#grammar-token-augmented-assignment-stmt) such as `+=`, where  
- `x += 1` means `x = x + 1`.

+++ {"slideshow": {"slide_type": "fragment"}}

The following widgets demonstrate other augmented assignment operators.

```{code-cell}
---
slideshow:
  slide_type: '-'
---
from ipywidgets import interact, fixed
@interact(initial_value=fixed(r'10'),
          operator=['+=','-=','*=','/=','//=','%=','**='],
          operand=fixed(r'2'))
def binary_operation(initial_value,operator,operand):
    assignment = f"x = {initial_value}\nx {operator} {operand}"
    _locals = {}
    exec(assignment,None,_locals)
    print(f"""Assignments:\n{assignment:>10}\nx: {_locals['x']} ({type(_locals['x'])})""")
```

+++ {"slideshow": {"slide_type": "fragment"}}

**Exercise** Can we create an expression using (augmented) assignment operators? Try running the code to see the effect.

```{code-cell}
---
slideshow:
  slide_type: '-'
---
3*(x = 15)
```

+++ {"nbgrader": {"grade": true, "grade_id": "assignment-statement", "locked": false, "points": 0, "schema_version": 3, "solution": true, "task": false}, "slideshow": {"slide_type": "-"}}

Assignment operators are used in assignment statements, which are not expressions because they cannot be evaluated.
