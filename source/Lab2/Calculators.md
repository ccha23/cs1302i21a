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

# Calculators

+++ {"slideshow": {"slide_type": "-"}, "tags": ["remove-cell"]}

**CS1302 Introduction to Computer Programming**
___

+++ {"slideshow": {"slide_type": "subslide"}}

Run the following to load additional tools required for this lab.  
In particular, the `math` library provides many useful mathematical functions and constants.

```{code-cell}
---
hide_input: false
init_cell: true
slideshow:
  slide_type: '-'
---
%reset -f
from ipywidgets import interact
import matplotlib.pyplot as plt
import numpy as np
import math
from math import log, exp, sin, cos, tan, pi
```

+++ {"slideshow": {"slide_type": "subslide"}}

The following code is a Python one-liner that creates a calculator.  
Evaluate the cell with `Ctrl+Enter`:

```{code-cell}
---
slideshow:
  slide_type: '-'
---
print(eval(input()))
```

+++ {"slideshow": {"slide_type": "fragment"}}

Try some calculations below using this calculator:
1. $2^3$ by entering `2**3`;
1. $\frac23$ by entering `2/3`;
1. $\left\lceil\frac32\right\rceil$ by entering `3//2`;
1. $3\mod 2$ by entering `3%2`;
1. $\sqrt{2}$ by entering `2**0.5`; and
1. $\sin(\pi/6)$ by entering `sin(pi/6)`;

+++ {"slideshow": {"slide_type": "fragment"}}

For this lab, you will create more powerful and dedicated calculators.   
We will first show you a demo. Then, it will be your turn to create the calculators.

+++ {"slideshow": {"slide_type": "slide"}}

## Hypotenuse Calculator (Demo)

+++ {"slideshow": {"slide_type": "-"}}

![interact](https://www.cs.cityu.edu.hk/~ccha23/cs1302/Lab2/hypotenuse-calculator.gif)

+++ {"slideshow": {"slide_type": "fragment"}}

Using the Pythagoras theorem below, we can define the following function `length_of_hypotenus` to calculate the length `c` of the hypotenuse given the lengths `a` and `b` of the other sides of a right-angled triangle:
$$c = \sqrt{a^2 + b^2}$$

```{code-cell}
---
slideshow:
  slide_type: fragment
---
def length_of_hypotenuse(a, b):
    c = (a**2 + b**2)**(0.5)  # Pythagoras
    return c
```

+++ {"slideshow": {"slide_type": "fragment"}}

- You need not understand how a function is defined, but
- you should know how to *write the formula as a Python expression*, and
- *assign to the variable* `c` the value of the expression (Line 2).

+++ {"slideshow": {"slide_type": "subslide"}}

For example, you may be asked to write Line 2, while Line 1 and 3 are given to you:

+++ {"slideshow": {"slide_type": "fragment"}}

**Exercise** Complete the function below to return the length `c` of the hypotenuse given the lengths `a` and `b`.

```{code-cell}
---
nbgrader:
  grade: false
  grade_id: length_of_hypotenus
  locked: false
  schema_version: 3
  solution: true
  task: false
slideshow:
  slide_type: '-'
---
def length_of_hypotenuse(a, b):
    ### BEGIN SOLUTION
    c = (a**2 + b**2)**(0.5)  # Pythagoras
    ### END SOLUTION
    return c
```

+++ {"slideshow": {"slide_type": "fragment"}}

Note that indentation affects the execution of Python code. The assignment statement must be indented to indicate that it is part of the *body* of the function.  
(Try removing the indentation and see what happens.)

+++ {"slideshow": {"slide_type": "subslide"}}

We will use widgets (`ipywidgets`) to let user interact with the calculator more easily: 

```{code-cell}
---
code_folding: []
slideshow:
  slide_type: '-'
---
# hypotenuse calculator
@interact(a=(0, 10, 1), b=(0, 10, 1))
def calculate_hypotenuse(a=3, b=4):
    print('c: {:.2f}'.format(length_of_hypotenuse(a, b)))
```

+++ {"slideshow": {"slide_type": "fragment"}}

After running the above cell, you can move the sliders to change the values of `a` and `b`. The value of `c` will be updated immediately.

+++ {"slideshow": {"slide_type": "fragment"}}

- For this lab, you need not know how write widgets, but
- you should know how to *format a floating point number* (Line 3). 

+++ {"slideshow": {"slide_type": "subslide"}}

You can check your code with a few cases listed in the test cell below.

```{code-cell}
---
code_folding: []
nbgrader:
  grade: true
  grade_id: test-length_of_hypotenus
  locked: true
  points: 1
  schema_version: 3
  solution: false
  task: false
slideshow:
  slide_type: '-'
---
# tests
def test_length_of_hypotenuse(a, b, c):
    c_ = length_of_hypotenuse(a, b)
    correct = math.isclose(c, c_)
    if not correct:
        print(f'For a={a} and b={b}, c should be {c}, not {c_}.')
    assert correct


test_length_of_hypotenuse(3, 4, 5)
test_length_of_hypotenuse(0, 0, 0)
test_length_of_hypotenuse(4, 7, 8.06225774829855)
```

+++ {"slideshow": {"slide_type": "slide"}}

## Quadratic Equation

+++ {"slideshow": {"slide_type": "subslide"}}

### Graphical Calculator for Parabola

+++ {"slideshow": {"slide_type": "-"}}

![plot parabola](https://www.cs.cityu.edu.hk/~ccha23/cs1302/Lab2/plot_parabola.gif)

+++ {"slideshow": {"slide_type": "subslide"}}

In mathematics, the collection of points $(x,y)$ satisfying the following equation forms a *parabola*:

$$
y=ax^2+bx+c
$$
where $a$, $b$, and $c$ are real numbers called the *coefficients*.

+++ {"slideshow": {"slide_type": "fragment"}}

**Exercise** Given the variables `x`, `a`, `b`, and `c` store the $x$-coordinate and the coefficients $a$, $b$, and $c$ respectively, assign to `y` the corresponding $y$-coordinate for the parabola.

```{code-cell}
---
nbgrader:
  grade: false
  grade_id: get_y
  locked: false
  schema_version: 3
  solution: true
  task: false
slideshow:
  slide_type: '-'
---
def get_y(x, a, b, c):
    ### BEGIN SOLUTION
    y = a * x**2 + b * x + c
    ### END SOLUTION
    return y
```

```{code-cell}
---
code_folding: []
nbgrader:
  grade: true
  grade_id: test-get_y
  locked: true
  points: 1
  schema_version: 3
  solution: false
  task: false
slideshow:
  slide_type: fragment
---
# tests
def test_get_y(y,x,a,b,c):
    y_ = get_y(x,a,b,c)
    correct = math.isclose(y,y_)
    if not correct:
        print(f'With (x, a, b, c)={x,a,b,c}, y should be {y} not {y_}.')
    assert correct

test_get_y(0,0,0,0,0)
test_get_y(1,0,1,2,1)
test_get_y(2,0,2,1,2)
### BEGIN HIDDEN TESTS
# print(*[f'test_get_y{(get_y(*args),*args)}' for args in [(1.2,2,3,4),(2,3.3,4,5),(3,4.4,5,6)]],sep='\n')
test_get_y(10.48, 1.2, 2, 3, 4)
test_get_y(26.2, 2, 3.3, 4, 5)
test_get_y(60.6, 3, 4.4, 5, 6)
### END HIDDEN TESTS
```

```{code-cell}
---
code_folding: []
slideshow:
  slide_type: subslide
---
# graphical calculator for parabola
@interact(a=(-10, 10, 1), b=(-10, 10, 1), c=(-10, 10, 1))
def plot_parabola(a, b, c):
    xmin, xmax, ymin, ymax, resolution = -10, 10, -10, 10, 50
    ax = plt.gca()
    ax.set_title(r'$y=ax^2+bx+c$')
    ax.set_xlabel(r'$x$')
    ax.set_ylabel(r'$y$')
    ax.set_xlim([xmin, xmax])
    ax.set_ylim([ymin, ymax])
    ax.grid()

    x = np.linspace(xmin, xmax, resolution)
    ax.plot(x, get_y(x, a, b, c))
```

+++ {"slideshow": {"slide_type": "slide"}}

### Quadratic Equation Solver

+++ {"slideshow": {"slide_type": "-"}}

![quadratic equtaion soler](https://www.cs.cityu.edu.hk/~ccha23/cs1302/Lab2/quadratic-equation-solver.gif)

+++ {"slideshow": {"slide_type": "subslide"}}

For the quadratic equation

$$
ax^2+bx+c=0,
$$
the *roots* (solutions for $x$) are give by

$$
\frac{-b-\sqrt{b^2-4ac}}{2a},\frac{-b+\sqrt{b^2-4ac}}{2a}.
$$

+++ {"slideshow": {"slide_type": "fragment"}}

**Exercise** Assign to `root1` and `root2` the values of the first and second roots above respectively.

```{code-cell}
---
nbgrader:
  grade: false
  grade_id: get_roots
  locked: false
  schema_version: 3
  solution: true
  task: false
slideshow:
  slide_type: fragment
---
def get_roots(a, b, c):
    ### BEGIN SOLUTION
    d = (b * b - 4 * a * c)**0.5
    root1, root2 = (-b - d) / 2 / a,  (-b + d) / 2 / a
    ### END SOLUTION
    return root1, root2
```

```{code-cell}
---
code_folding: []
nbgrader:
  grade: true
  grade_id: test-get_roots
  locked: true
  points: 1
  schema_version: 3
  solution: false
  task: false
slideshow:
  slide_type: fragment
---
# tests
def test_get_roots(roots, a, b, c):
    roots_ = get_roots(a, b, c)
    correct = all([math.isclose(roots[i], roots_[i]) for i in range(2)])
    if not correct:
        print(f'With (a, b, c)={a,b,c}, roots should be {roots} not {roots_}.')
    assert correct


test_get_roots((-1.0, 0.0), 1, 1, 0)
test_get_roots((-1.0, -1.0), 1, 2, 1)
test_get_roots((-2.0, -1.0), 1, 3, 2)
### BEGIN HIDDEN TESTS
test_get_roots((-1.0, -0.5), 2, 3, 1)
test_get_roots((-3.0, -1.0), 1, 4, 3)
test_get_roots((-2.0, -0.5), 2, 5, 2)


def generate_test_get_roots():
    for args in [(1, 1, 0), (1, 2, 1), (1, 3, 2), (2, 3, 1), (1, 4, 3),
                 (2, 5, 2)]:
        print(f'test_get_roots{(get_roots(*args),*args)}', sep='\n')


# generate_test_get_roots()
### END HIDDEN TESTS
```

```{code-cell}
---
code_folding: [0]
slideshow:
  slide_type: fragment
---
# quadratic equations solver
@interact(a=(-10,10,1),b=(-10,10,1),c=(-10,10,1))
def quadratic_equation_solver(a=1,b=2,c=1):
    print('Roots: {}, {}'.format(*get_roots(a,b,c)))
```

+++ {"slideshow": {"slide_type": "slide"}}

## Number Conversion

+++ {"slideshow": {"slide_type": "subslide"}}

### Byte-to-Decimal Calculator

+++ {"slideshow": {"slide_type": "-"}}

![byte-to-decimal](https://www.cs.cityu.edu.hk/~ccha23/cs1302/Lab2/byte-to-decimal.gif)

+++ {"slideshow": {"slide_type": "subslide"}}

Denote a binary number stored as a byte ($8$-bit) as

$$ 
b_7\circ b_6\circ b_5\circ b_4\circ b_3\circ b_2\circ b_1\circ b_0, 
$$
where $\circ$ concatenates $b_i$'s together into a binary string.

+++ {"slideshow": {"slide_type": "fragment"}}

The binary string can be converted to a decimal number by the formula

$$ 
b_7\cdot 2^7 + b_6\cdot 2^6 + b_5\cdot 2^5 + b_4\cdot 2^4 + b_3\cdot 2^3 + b_2\cdot 2^2 + b_1\cdot 2^1 + b_0\cdot 2^0. 
$$

+++ {"slideshow": {"slide_type": "fragment"}}

E.g., the binary string `'11111111'` is the largest integer represented by a byte:

$$
2^7+2^6+2^5+2^4+2^3+2^2+2^1+2^0=255=2^8-1.
$$

+++ {"slideshow": {"slide_type": "fragment"}}

**Exercise** Assign to `decimal` the *integer* value represented by a byte.  
The byte is a sequence of bits assigned to the variables `b7,b6,b5,b4,b3,b2,b1,b0` as *characters*, either `'0'` or `'1'`.

```{code-cell}
---
nbgrader:
  grade: false
  grade_id: byte_to_decimal
  locked: false
  schema_version: 3
  solution: true
  task: false
slideshow:
  slide_type: fragment
---
def byte_to_decimal(b7, b6, b5, b4, b3, b2, b1, b0):
    ### BEGIN SOLUTION
    decimal = int(b7) * 2**7 + int(b6) * 2**6 + int(b5) * 2**5 + \
              int(b4) * 2**4 + int(b3) * 2**3 + int(b2) * 2**2 + \
              int(b1) * 2**1 + int(b0) * 2**0
    ### END SOLUTION
    return decimal
```

```{code-cell}
---
code_folding: [0]
nbgrader:
  grade: true
  grade_id: test-byte_to_decimal
  locked: true
  points: 1
  schema_version: 3
  solution: false
  task: false
slideshow:
  slide_type: fragment
---
# tests
def test_byte_to_decimal(decimal, b7, b6, b5, b4, b3, b2, b1, b0):
    decimal_ = byte_to_decimal(b7, b6, b5, b4, b3, b2, b1, b0)
    correct = decimal == decimal_ and isinstance(decimal_, int)
    if not correct:
        print(
            f'{b7}{b6}{b5}{b4}{b3}{b2}{b1}{b0} should give {decimal} not {decimal_}.'
        )
    assert correct


test_byte_to_decimal(38, '0', '0', '1', '0', '0', '1', '1', '0')
test_byte_to_decimal(20, '0', '0', '0', '1', '0', '1', '0', '0')
test_byte_to_decimal(22, '0', '0', '0', '1', '0', '1', '1', '0')
### BEGIN HIDDEN TESTS
test_byte_to_decimal(146, '1', '0', '0', '1', '0', '0', '1', '0')
test_byte_to_decimal(128, '1', '0', '0', '0', '0', '0', '0', '0')
test_byte_to_decimal(71, '0', '1', '0', '0', '0', '1', '1', '1')


def generate_test_byte_to_decimal(n):
    for args in [tuple(np.random.choice(['0', '1'], 8)) for i in range(n)]:
        print(f'test_byte_to_decimal{(byte_to_decimal(*args),*args)}')


# generate_test_byte_to_decimal(6)
### END HIDDEN TESTS
```

```{code-cell}
:code_folding: [0]

# byte-to-decimal calculator
bit = ['0', '1']


@interact(b7=bit, b6=bit, b5=bit, b4=bit, b3=bit, b2=bit, b1=bit, b0=bit)
def convert_byte_to_decimal(b7, b6, b5, b4, b3, b2, b1, b0):
    print('decimal:', byte_to_decimal(b7, b6, b5, b4, b3, b2, b1, b0))
```

+++ {"slideshow": {"slide_type": "subslide"}}

### Decimal-to-Byte Calculator

+++ {"slideshow": {"slide_type": "-"}}

![decimal-to-byte](https://www.cs.cityu.edu.hk/~ccha23/cs1302/Lab2/decimal-to-byte.gif)

+++ {"slideshow": {"slide_type": "subslide"}}

**Exercise** Assign to `byte` a *string of 8 bits* that represents the value of `decimal`, a non-negative decimal integer from $0$ to $2^8-1=255$.  
*Hint: Use `//` and `%`.*

```{code-cell}
---
nbgrader:
  grade: false
  grade_id: decimal_to_byte
  locked: false
  schema_version: 3
  solution: true
  task: false
slideshow:
  slide_type: '-'
---
def decimal_to_byte(decimal):
    ### BEGIN SOLUTION
    byte = '{}{}{}{}{}{}{}{}'.format(
        decimal // 2**7 % 2, 
        decimal // 2**6 % 2, 
        decimal // 2**5 % 2,
        decimal // 2**4 % 2, 
        decimal // 2**3 % 2, 
        decimal // 2**2 % 2,
        decimal // 2 % 2, 
        decimal % 2)
    ### END SOLUTION
    return byte
```

```{code-cell}
---
code_folding: [0]
nbgrader:
  grade: true
  grade_id: test-decimal_to_byte
  locked: true
  points: 1
  schema_version: 3
  solution: false
  task: false
slideshow:
  slide_type: fragment
---
# tests
def test_decimal_to_byte(byte,decimal):
    byte_ = decimal_to_byte(decimal)
    correct = byte == byte_ and isinstance(byte, str) and len(byte) == 8
    if not correct:
        print(
            f'{decimal} should be represented as the byte {byte}, not {byte_}.'
        )
    assert correct


test_decimal_to_byte('01100111', 103)
test_decimal_to_byte('00000011', 3)
test_decimal_to_byte('00011100', 28)
### BEGIN HIDDEN TESTS
test_decimal_to_byte('11011111', 223)
test_decimal_to_byte('00000100', 4)
test_decimal_to_byte('10011001', 153)


def generate_test_decimal_to_byte(n):
    for arg in [np.random.randint(0, 2**8) for i in range(n)]:
        print(f'test_decimal_to_byte{(decimal_to_byte(arg),arg)}')


# generate_test_decimal_to_byte(6)
### END HIDDEN TESTS
```

```{code-cell}
---
code_folding: [0]
slideshow:
  slide_type: fragment
---
# decimal-to-byte calculator
@interact(decimal=(0,255,1))
def convert_decimal_to_byte(decimal=0):
    print('byte:', decimal_to_byte(decimal))
```
