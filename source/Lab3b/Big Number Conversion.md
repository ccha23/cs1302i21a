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

# Big Number Conversion

+++ {"slideshow": {"slide_type": "-"}, "tags": ["remove-cell"]}

**CS1302 Introduction to Computer Programming**
___

+++ {"slideshow": {"slide_type": "slide"}}

## Conversion to Decimal

+++ {"slideshow": {"slide_type": "subslide"}}

In this notebook, we will use iterations to convert numbers with arbitrary size.

+++ {"slideshow": {"slide_type": "subslide"}}

### Binary-to-Decimal

+++ {"slideshow": {"slide_type": "fragment"}}

In a previous lab, we considered converting a byte string to decimal.  
What about converting a binary string of arbitrary length to decimal?

+++ {"slideshow": {"slide_type": "subslide"}}

Given a binary string of an arbitrarily length $k$,

$$ 
b_{k-1}\circ \dots \circ b_1\circ b_0,
$$
the decimal number can be computed by the formula

$$
2^0 \cdot b_0 + 2^1 \cdot b_1 + \dots + 2^{k-1} \cdot b_{k-1}.
$$

+++ {"slideshow": {"slide_type": "fragment"}}

In mathematics, we use the summation notation to write the above formula:

$$ 
\sum_{i=0}^{k-1} 2^i \cdot b_{i}.
$$

+++ {"slideshow": {"slide_type": "subslide"}}

In a program, the formula can be implemented as a for loop:

+++ {"code_folding": [], "slideshow": {"slide_type": "-"}}

```Python
def binary_to_decimal(binary_str):
    k = len(binary_str)
    decimal = 0                                     # initialization
    for i in range(k):
        decimal += 2**i * int(binary_str[(k-1)-i])  # iteration
    return decimal
```

+++ {"slideshow": {"slide_type": "fragment"}}

Note that $b_i$ is given by `binary_str[(k-1)-i]`:

$$
\begin{array}{c|c:c:c:c|}\texttt{binary_str} & b_{k-1} & b_{k-2} & \dots & b_0\\ \text{indexing} & [0] & [1] & \dots & [k-1] \end{array}
$$

+++ {"slideshow": {"slide_type": "subslide"}}

The following is another way to write the for loop.

+++ {"slideshow": {"slide_type": "fragment"}}

```Python
def binary_to_decimal(binary_str):
    decimal = 0                                # initialization
    for bit in binary_str:
        decimal = decimal * 2 + int(bit)       # iteration
    return decimal
```

+++ {"slideshow": {"slide_type": "fragment"}}

The algorithm implements the same formula factorized as follows:

$$
\begin{aligned} \sum_{i=0}^{k-1} 2^i \cdot b_{i} 
&=  \left(\sum_{i=1}^{k-1} 2^i \cdot b_{i}\right) + b_0\\
&=  \left(\sum_{i=1}^{k-1} 2^{i-1} \cdot b_{i}\right)\times 2 + b_0 \\
&=  \left(\sum_{j=0}^{k-2} 2^{j} \cdot b_{j+1}\right)\times 2 + b_0 && \text{with $j=i-1$} \\
&= \underbrace{(\dots (\underbrace{(\underbrace{\overbrace{0}^{\text{initialization}\kern-2em}\times 2 + b_{k-1}}_{\text{first iteration} }) \times 2 + b_{k-2}}_{\text{second iteration} }) \dots )\times 2 + b_0}_{\text{last iteration} }.\end{aligned}
$$ 

+++ {"slideshow": {"slide_type": "subslide"}}

**Exercise** Complete the code for `binary_to_decimal` with the most efficient implementation you can think of.  
(You can choose one of the two implementations above but take the time to type in the code instead of copy-and-paste.)

```{code-cell}
---
nbgrader:
  grade: false
  grade_id: binary_to_decimal
  locked: false
  schema_version: 3
  solution: true
  task: false
slideshow:
  slide_type: '-'
---
def binary_to_decimal(binary_str):
    ### BEGIN SOLUTION
    decimal = 0                                # initialization
    for bit in binary_str:
        decimal = decimal * 2 + int(bit)       # iteration
    ### END SOLUTION
    return decimal
```

```{code-cell}
---
code_folding: [0]
nbgrader:
  grade: true
  grade_id: test-binary_to_decimal
  locked: true
  points: 1
  schema_version: 3
  solution: false
  task: false
slideshow:
  slide_type: '-'
---
# tests
import numpy as np
def test_binary_to_decimal(decimal, binary_str):
    decimal_ = binary_to_decimal(binary_str)
    correct = isinstance(decimal_, int) and decimal_ == decimal
    if not correct:
        print(f'{binary_str} should give {decimal} not {decimal_}.')
    assert correct

test_binary_to_decimal(0, '0')
test_binary_to_decimal(255, '11111111')
test_binary_to_decimal(52154, '1100101110111010')
test_binary_to_decimal(3430, '110101100110')
### BEGIN HIDDEN TESTS
test_binary_to_decimal(4064, '111111100000')
test_binary_to_decimal(2508, '0100111001100')
test_binary_to_decimal(1864, '11101001000')
test_binary_to_decimal(1774, '11011101110')

def generate_test_binary_to_decimal(n, k=None):
    for binary_str in [
            ''.join(
                np.random.choice(['0','1'],
                    np.random.randint(11, 21) if k is None else k))
            for i in range(n)
    ]:
        print(
            f'test_binary_to_decimal{(binary_to_decimal(binary_str),binary_str)}'
        )


# generate_test_binary_to_decimal(6)
### END HIDDEN TESTS
```

```{code-cell}
---
code_folding: [0]
slideshow:
  slide_type: '-'
---
# binary-to-decimal converter
from ipywidgets import interact
bits = ['0', '1']
@interact(binary_str='1011')
def convert_byte_to_decimal(binary_str):
    for bit in binary_str:
        if bit not in bits:
            print('Not a binary string.')
            break
    else:
        print('decimal:', binary_to_decimal(binary_str))
```

+++ {"slideshow": {"slide_type": "slide"}}

### Undecimal-to-Decimal

+++ {"slideshow": {"slide_type": "fragment"}}

A base-11 number system is called an [undecimal system](https://en.wikipedia.org/wiki/Undecimal). The digits range from 0 to 10 with 10 denoted as X:

$$
0, 1, 2, 3, 4, 5, 6, 7, 8, 9, X.
$$

The [International Standard Book Number (ISBN)](https://en.wikipedia.org/wiki/International_Standard_Book_Number) uses an undecimal digit.

+++ {"slideshow": {"slide_type": "subslide"}}

**Exercise** In the following code, assign to `decimal` the integer represented by an undecimal string of arbitrary length.  

+++ {"slideshow": {"slide_type": "-"}}

*Hint:* Write a conditional to 
1. check if a digit is (capital) `'X'`, and if so, 
2. convert the digit to the integer value 10.

```{code-cell}
---
nbgrader:
  grade: false
  grade_id: undecimal_to_decimal
  locked: false
  schema_version: 3
  solution: true
  task: false
slideshow:
  slide_type: subslide
---
def undecimal_to_decimal(undecimal_str):
    ### BEGIN SOLUTION  
    decimal = 0
    for undecimal in undecimal_str:
        decimal = decimal * 11 + (10 if undecimal == 'X' else int(undecimal))
    ### END SOLUTION
    return decimal
```

```{code-cell}
---
code_folding: []
nbgrader:
  grade: true
  grade_id: test-undecimal_to_decimal
  locked: true
  points: 1
  schema_version: 3
  solution: false
  task: false
slideshow:
  slide_type: '-'
---
# tests
def test_undecimal_to_decimal(decimal, undecimal_str):
    decimal_ = undecimal_to_decimal(undecimal_str)
    correct = isinstance(decimal_, int) and decimal_ == decimal
    if not correct:
        print(f'{undecimal_str} should give {decimal} not {decimal_}.')
    assert correct


test_undecimal_to_decimal(27558279079916281, '6662X0X584839464')
test_undecimal_to_decimal(23022771839270, '73769X2556695')
test_undecimal_to_decimal(161804347284488, '476129248X2067')
### BEGIN HIDDEN TESTS
test_undecimal_to_decimal(7405157175828961, '185556958178490X')
test_undecimal_to_decimal(32939220798033088, '79814X6100858380')
test_undecimal_to_decimal(895746146892, '31597X391013')

def generate_test_undecimal_to_decimal(n, k=None):
    for undecimal_str in [
            ''.join(
                np.random.choice(
                    [str(i) for i in range(10)] + ['X'],
                    np.random.randint(11, 21) if k is None else k))
            for i in range(n)
    ]:
        print(
            f'test_undecimal_to_decimal{(undecimal_to_decimal(undecimal_str),undecimal_str)}'
        )


# generate_test_undecimal_to_decimal(6)
### END HIDDEN TESTS
```

```{code-cell}
---
code_folding: [0]
slideshow:
  slide_type: '-'
---
# undecimal-to-decimal calculator
from ipywidgets import interact
undecimal_digits = [str(i) for i in range(10)] + ['X']
@interact(undecimal_str='X')
def convert_undecimal_to_decimal(undecimal_str):
    for digit in undecimal_str:
        if digit not in undecimal_digits:
            print('Not an undecimal string.')
            break
    else:
        print('decimal:', undecimal_to_decimal(undecimal_str))
```

+++ {"slideshow": {"slide_type": "slide"}}

## Conversion from Decimal

+++ {"slideshow": {"slide_type": "fragment"}}

Consider the reverse process that converts a non-negative decimal number of arbitrary size to a string representation in another number system.

+++ {"slideshow": {"slide_type": "subslide"}}

### Decimal-to-Binary

+++ {"slideshow": {"slide_type": "subslide"}}

The following code converts a decimal number to a binary string.

+++ {"slideshow": {"slide_type": "-"}}

```Python
def decimal_to_binary(decimal):
    binary_str = str(decimal % 2)
    while decimal // 2:
        decimal //= 2
        binary_str = str(decimal % 2) + binary_str
    return binary_str
```

+++ {"slideshow": {"slide_type": "fragment"}}

To understand the while loop, consider the same formula before, where the braces indicate the value of `decimal` at different times:

$$
\begin{aligned} \sum_{i=0}^{k-1} 2^i \cdot b_{i} &=  \left(\sum_{i=0}^{k-2} 2^{i-2} \cdot b_{i-1}\right)\times 2 + b_0 \\
&= \underbrace{(\underbrace{ \dots (\underbrace{(0\times 2 + b_{k-1}) \times 2 + b_{k-2}}_{\text{right before the last iteration} }  )\times 2 \dots + b_1}_{\text{right before the second iteration} })\times 2 + b_0}_{\text{right before the first iteration} }.\end{aligned}
$$ 

+++ {"slideshow": {"slide_type": "fragment"}}

- $b_0$ is the remainder `decimal % 2` right before the first iteration,
- $b_1$ is the remainder `decimal // 2 % 2` right before the second iteration, and
- $b_{k-1}$ is the remainder `decimal // 2 % 2` right before the last iteration.

+++ {"slideshow": {"slide_type": "fragment"}}

We can also write a for loop instead of a while loop:

```{code-cell}
---
slideshow:
  slide_type: '-'
---
from math import floor, log2
def decimal_to_binary(decimal):
    binary_str = ''
    num_bits = 1 + (decimal and floor(log2(decimal)))
    for i in range(num_bits):
        binary_str = str(decimal % 2) + binary_str
        decimal //= 2
    return binary_str
```

```{code-cell}
---
code_folding: [0]
slideshow:
  slide_type: '-'
---
# decimal-to-binary calculator
@interact(decimal='11')
def convert_decimal_to_binary(decimal):
    if not decimal.isdigit():
        print('Not a non-negative integer.')
    else:
        print('binary:', decimal_to_binary(int(decimal)))
```

+++ {"slideshow": {"slide_type": "subslide"}}

**Exercise** Explain what the expression `1 + (decimal and floor(log2(decimal)))` calculates. In particular, explain the purpose of the logical `and` operation in the expression?

+++ {"nbgrader": {"grade": true, "grade_id": "number-of-bits", "locked": false, "points": 1, "schema_version": 3, "solution": true, "task": false}, "slideshow": {"slide_type": "-"}}

The expression calculates the number of bits for representing `decimal`. The logical `and` short-circuits the evaluation of `log2(decimal)` when `decimal` equals `0` because `log2(0)` is undefined.

+++ {"slideshow": {"slide_type": "slide"}}

### Decimal-to-Undecimal

+++ {"slideshow": {"slide_type": "subslide"}}

**Exercise** Assign to `undecimal_str` the undecimal string that represents a non-negative integer `decimal` of any size.

+++ {"slideshow": {"slide_type": "fragment"}}

*Hint:* For loop or while loop?

```{code-cell}
---
nbgrader:
  grade: false
  grade_id: decimal_to_undecimal
  locked: false
  schema_version: 3
  solution: true
  task: false
slideshow:
  slide_type: '-'
---
def decimal_to_undecimal(decimal):
    ### BEGIN SOLUTION
    undecimal_str = '' # last digit will be obtained in the loop as well
    while True:        # to avoid code duplication
        digit_value = decimal % 11
        undecimal_str = ('X' if digit_value == 10 else
                         str(digit_value)) + undecimal_str
        decimal //= 11
        if not decimal: break
    ### END SOLUTION
    return undecimal_str
```

```{code-cell}
---
code_folding: [0]
nbgrader:
  grade: true
  grade_id: test-decimal_to_undecimal
  locked: true
  points: 1
  schema_version: 3
  solution: false
  task: false
slideshow:
  slide_type: '-'
---
# tests
def test_decimal_to_undecimal(undecimal,decimal):
    undecimal_ = decimal_to_undecimal(decimal)
    correct = isinstance(undecimal, str) and undecimal == undecimal_
    if not correct:
        print(
            f'{decimal} should be represented as the undecimal string {undecimal}, not {undecimal_}.'
        )
    assert correct

test_decimal_to_undecimal('X', 10)
test_decimal_to_undecimal('0', 0)
test_decimal_to_undecimal('1752572309X478', 57983478668530)
### BEGIN HIDDEN TESTS
test_decimal_to_undecimal('2090', 2761)
test_decimal_to_undecimal('4', 4)
test_decimal_to_undecimal('196676965013', 534330914989)
test_decimal_to_undecimal('494550605', 1040785498)
test_decimal_to_undecimal('62534436X0X98123X', 286068981907634166)

def generate_test_decimal_to_undecimal(n):
    for arg in [np.random.randint(0, 2**np.random.randint(63)-1) for i in range(n)]:
        print(f'test_decimal_to_undecimal{(decimal_to_undecimal(arg),arg)}')


# generate_test_decimal_to_undecimal(6)
### END HIDDEN TESTS
```

```{code-cell}
---
code_folding: [0]
slideshow:
  slide_type: '-'
---
# undecimal-to-decimal calculator
from ipywidgets import interact
@interact(decimal='10')
def convert_decimal_to_undecimal(decimal):
    if not decimal.isdigit():
        print('Not a non-negative integer.')
    else:
        print('undecimal:', decimal_to_undecimal(int(decimal)))
```
