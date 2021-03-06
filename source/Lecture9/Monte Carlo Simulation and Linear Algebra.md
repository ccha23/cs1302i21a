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

# Monte Carlo Simulation and Linear Algebra

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

+++ {"slideshow": {"slide_type": "subslide"}}

## Monte Carlo simulation

+++ {"slideshow": {"slide_type": "subslide"}}

**What is Monte Carlo simulation?**

+++ {"slideshow": {"slide_type": "fragment"}}

 > The name Monte Carlo refers to the [Monte Carlo Casino in Monaco](https://en.wikipedia.org/wiki/Monte_Carlo_Casino) where Ulam's uncle would borrow money from relatives to gamble.

+++ {"slideshow": {"slide_type": "fragment"}}

It would be nice to simulate the casino, so Ulam's uncle did not need to borrow money to go.  
Actually...,
- Monte Carlo is the code name of the secret project for creating the [hydrogen bomb](https://en.wikipedia.org/wiki/Monte_Carlo_method). 
- [Ulam](https://en.wikipedia.org/wiki/Stanislaw_Ulam) worked with [John von Neumann](https://en.wikipedia.org/wiki/John_von_Neumann) to program the first electronic computer ENIAC to simulate a computational model of a thermonuclear reaction.

(See also [The Beginning of the Monte Carlo Method](https://permalink.lanl.gov/object/tr?what=info:lanl-repo/lareport/LA-UR-88-9067) for a more detailed account.)

+++ {"slideshow": {"slide_type": "subslide"}}

**How to compute the value of $\pi$**?

+++ {"slideshow": {"slide_type": "fragment"}}

An application of Monte Carlo simulation is in approximating $\pi$ using 
the [Buffon's needle](https://en.wikipedia.org/wiki/Buffon%27s_needle_problem).  
There is [a program](https://www.khanacademy.org/computer-programming/pi-by-buffons-needle/6695500989890560) written in javascript to do this.

+++ {"slideshow": {"slide_type": "fragment"}}

The javascript program a bit long to digest, so we will use an alternative simulation that is easier to understand/program.

+++ {"slideshow": {"slide_type": "subslide"}}

If we uniformly randomly pick a point in a square. What is the chance it is in the inscribed circle, i.e., the biggest circle inside the square?

+++ {"slideshow": {"slide_type": "-"}}

The chance is the area of the circle divided by the area of the square. Suppose the square has length $\ell$, then the chance is

$$ \frac{\pi (\ell /2)^2}{ (\ell)^2 } = \frac{\pi}4 $$
independent of the length $\ell$.

+++ {"slideshow": {"slide_type": "subslide"}}

**Exercise** Complete the following function to return an approximation of $\pi$ as follows:
1. Simulate the random process of picking a point from a square repeatedly `n` times by  
  generating the $x$ and $y$ coordinates uniformly randomly from a unit interval $[0,1)$.
2. Compute the fraction of times the point is in the first quadrant of the inscribed circle as shown in the figure below.
3. Return $4$ times the fraction as the approximation.
<p><a href="https://commons.wikimedia.org/wiki/File:Pi_30K.gif#/media/File:Pi_30K.gif"><img src="https://upload.wikimedia.org/wikipedia/commons/8/84/Pi_30K.gif" alt="Pi 30K.gif"></a></p>

```{code-cell}
---
nbgrader:
  grade: false
  grade_id: approximate_pi
  locked: false
  schema_version: 3
  solution: true
  task: false
slideshow:
  slide_type: '-'
---
import random, math

def approximate_pi(n):
    ### BEGIN SOLUTION
     return 4*len([True for i in range(n) 
                   if random.random()**2 + random.random()**2 < 1])/n
    ### END SOLUTION
print(f'Approximate: {approximate_pi(int(1e7))}\nGround truth: {math.pi}')
```

+++ {"slideshow": {"slide_type": "subslide"}}

**How accurate is the approximation?**

+++ {"slideshow": {"slide_type": "fragment"}}

The following uses a powerful library `numpy` for computing to return a [$95\%$-confidence interval](http://onlinestatbook.com/2/estimation/mean.html#:~:text=To%20compute%20the%2095%25%20confidence,be%20between%20the%20cutoff%20points.).

```{code-cell}
---
slideshow:
  slide_type: '-'
---
import numpy as np

def np_approximate_pi(n):
    in_circle = (np.random.random((n,2))**2).sum(axis=-1) < 1
    mean = 4 * in_circle.mean()
    std = 4 * in_circle.std() / n**0.5
    return np.array([mean - 2*std, mean + 2*std])

interval = np_approximate_pi(int(1e7))
print(f'''95%-confidence interval: {interval}
Estimate: {interval.mean():.4f} ?? {(interval[1]-interval[0])/2:.4f}
Ground truth: {math.pi}''')
```

+++ {"slideshow": {"slide_type": "fragment"}}

Note that the computation done using `numpy` is over $5$ times faster despite the additional computation of the standard deviation.

+++ {"slideshow": {"slide_type": "subslide"}}

There are faster methods to approximate $\pi$ such as the [Chudnovsky_algorithm](https://en.wikipedia.org/wiki/Chudnovsky_algorithm), but Monte-Carlo method is still useful in more complicated situations.   
E.g., see the Monte Carlo simulation of a [real-life situation](https://www.youtube.com/watch?v=-fCVxTTAtFQ) in playing basketball:
> "When down by three and left with only 30 seconds is it better to attempt a hard 3-point shot or an easy 2-point shot and get another possession?"   --LeBron James

+++ {"slideshow": {"slide_type": "slide"}}

## Linear Algebra

+++ {"slideshow": {"slide_type": "subslide"}}

**How to solve a linear equation?**

+++ {"slideshow": {"slide_type": "fragment"}}

Given the following linear equation in variable $x$ with real-valued coefficient $a$ and $b$,

$$ a x = b,$$
what is the value of $x$ that satisfies the equation?

+++ {"slideshow": {"slide_type": "subslide"}}

**Exercise** Complete the following function to return either the unique solution of $x$ or `None` if a unique solution does not exist.

```{code-cell}
---
nbgrader:
  grade: false
  grade_id: solve_linear_equation
  locked: false
  schema_version: 3
  solution: true
  task: false
slideshow:
  slide_type: '-'
---
def solve_linear_equation(a,b):
    ### BEGIN SOLUTION
    return b/a if a != 0 else None
    ### END SOLUTION

import ipywidgets as widgets
@widgets.interact(a=(0,5,1),b=(0,5,1))
def linear_equation_solver(a=2, b=3):
    print(f'''linear equation: {a}x = {b}
       solution: x = {solve_linear_equation(a,b)}''')
```

+++ {"slideshow": {"slide_type": "subslide"}}

**How to solve multiple linear equations?**

+++ {"slideshow": {"slide_type": "fragment"}}

In the general case, we have a system of $m$ linear equations and $n$ variables:

$$ \begin{aligned}
a_{00} x_0 + a_{01} x_1 + \dots + a_{0(n-1)} x_{n-1} &= b_0\\
a_{10} x_0 + a_{11} x_1 + \dots + a_{1(n-1)} x_{n-1} &= b_1\\
\vdots\kern2em &= \vdots\\
a_{(m-1)0} x_0 + a_{(m-1)1} x_1 + \dots + a_{(m-1)(n-1)} x_{n-1} &= b_{m-1}\\
\end{aligned}
$$
where
- $x_j$ for $j\in \{0,\dots,n-1\}$ are the variables, and
- $a_{ij}$ and $b_j$ for $i\in \{0,\dots,m-1\}$ and $j\in \{0,\dots,n-1\}$ are the coefficients.

A fundamental problem in linear algebra is to compute the unique solution to the system if it exists.

+++ {"slideshow": {"slide_type": "fragment"}}

We will consider the simpler 2-by-2 system with 2 variables and 2 equations:

$$ \begin{aligned}
a_{00} x_0 + a_{01} x_1 &= b_0\\
a_{10} x_0 + a_{11} x_1 &= b_1.
\end{aligned}
$$

+++ {"slideshow": {"slide_type": "subslide"}}

To get an idea of the solution, suppose 

$$a_{00}=a_{11}=1, a_{01} = a_{10} = 0.$$
The system of equations become

$$ \begin{aligned}
x_0 \hphantom{+ x_1} &= b_0\\
\hphantom{x_0 +}  x_1 &= b_1,
\end{aligned}
$$
which gives the solution directly.

+++ {"slideshow": {"slide_type": "fragment"}}

What about $a_{00}=a_{11}=2$ instead?

$$ \begin{aligned}
2x_0 \hphantom{+ x_1} &= b_0\\
\hphantom{2x_0 +}  2x_1 &= b_1,
\end{aligned}$$

+++ {"slideshow": {"slide_type": "fragment"}}

To obtain the solution, we simply divide both equations by 2:

$$ \begin{aligned}
x_0 \hphantom{+ x_1} &= \frac{b_0}2\\
\hphantom{x_0 +}  x_1 &= \frac{b_1}2.
\end{aligned}
$$

+++ {"slideshow": {"slide_type": "fragment"}}

What if $a_{01}=2$ instead?

$$ \begin{aligned}
2x_0 + 2x_1 &= b_0\\
\hphantom{2x_0 +}  2x_1 &= b_1\\
\end{aligned}
$$

+++ {"slideshow": {"slide_type": "fragment"}}

The second equation gives the solution of $x_1$, and we can use the solution in the first equation to solve for $x_0$. More precisely:
- Subtract the second equation from the first one:

$$ \begin{aligned}
2x_0 \hphantom{+2x_1} &= b_0 - b_1\\
\hphantom{2x_0 +}  2x_1 &= b_1\\
\end{aligned}
$$
- Divide both equation by 2:

$$ \begin{aligned}
x_0 \hphantom{+ x_1} &= \frac{b_0 - b_1}2\\
\hphantom{x_0 +}  x_1 &= \frac{b_1}2\\
\end{aligned}
$$

+++ {"slideshow": {"slide_type": "subslide"}}

The above operations are called *row operations* in linear algebra: each row is an equation.  
A system of linear equations can be solved by the linear operations of 
1. multiplying an equation by a constant, and
2. subtracting one equation from another.

+++ {"slideshow": {"slide_type": "fragment"}}

How to write a program to solve a general 2-by-2 system? We will use the `numpy` library.

+++ {"slideshow": {"slide_type": "subslide"}}

### Creating `numpy` arrays

+++ {"slideshow": {"slide_type": "subslide"}}

**How to store the coefficients?**

+++ {"slideshow": {"slide_type": "fragment"}}

In linear algebra, a system of equations such as

$$ \begin{aligned}
a_{00} x_0 + a_{01} x_1 &= b_0\\
a_{10} x_0 + a_{11} x_1 &= b_1
\end{aligned}
$$
is written concisely in *matrix* form as $ \mathbf{A} \mathbf{x} = \mathbf{b} $:

$$\overbrace{\begin{bmatrix}
a_{00} & a_{01}\\
a_{10} & a_{11}
\end{bmatrix}}^{\mathbf{A}}
\overbrace{
\begin{bmatrix}
x_0\\
x_1
\end{bmatrix}}
^{\mathbf{x}}
= \overbrace{\begin{bmatrix}
b_0\\
b_1
\end{bmatrix}}^{\mathbf{b}},
$$
where
$ \mathbf{A} \mathbf{x}$ is the *matrix multiplication*

$$ \mathbf{A} \mathbf{x} = \begin{bmatrix}
a_{00} x_0 + a_{01} x_1\\
a_{10} x_0 + a_{11} x_1
\end{bmatrix}.
$$

+++ {"slideshow": {"slide_type": "fragment"}}

We say that $\mathbf{A}$ is a [*matrix*](https://en.wikipedia.org/wiki/Matrix_(mathematics)) and its dimension/shape is $2$-by-$2$:
- The first dimension/axis has size $2$. We also say that the matrix has $2$ rows.
- The second dimension/axis has size $2$. We also say that the matrix has $2$ columns.
$\mathbf{x}$ and $\mathbf{b}$ are called column vectors, which are matrices with one column.

+++ {"slideshow": {"slide_type": "subslide"}}

Consider the example
$$ \begin{aligned}
2x_0 + 2x_1 &= 1\\
\hphantom{2x_0 +}  2x_1 &= 1,
\end{aligned}$$
or in matrix form with
$$ \begin{aligned}
\mathbf{A}&=\begin{bmatrix}
a_{00} & a_{01} \\
a_{10} & a_{11} 
\end{bmatrix} 
= \begin{bmatrix}
2 & 2 \\
0 & 2 
\end{bmatrix}\\
\mathbf{b}&=\begin{bmatrix}
b_0\\
b_1
\end{bmatrix} = \begin{bmatrix}
1\\
1
\end{bmatrix}\end{aligned}$$

+++ {"slideshow": {"slide_type": "fragment"}}

Instead of using `list` to store the matrix, we will use a `numpy` array.

```{code-cell}
---
slideshow:
  slide_type: '-'
---
A = np.array([[2.,2],[0,2]])
b = np.array([1.,1])
A, b
```

+++ {"slideshow": {"slide_type": "subslide"}}

Compared to `list`, `numpy` array is often more efficient and has more useful attributes.

```{code-cell}
---
slideshow:
  slide_type: '-'
---
array_attributes = set(attr for attr in dir(np.array([])) if attr[0]!='_')
list_attributes = set(attr for attr in dir(list) if attr[0]!='_')
print('\nCommon attributes:\n',*(array_attributes & list_attributes))
print('\nArray-specific attributes:\n', *(array_attributes - list_attributes))
print('\nList-specific attributes:\n',*(list_attributes - array_attributes))
```

+++ {"slideshow": {"slide_type": "subslide"}}

The following attributes give the dimension/shape, number of dimensions, size, and datatype.

```{code-cell}
---
slideshow:
  slide_type: '-'
---
for array in A, b:
    print(f'''{array}
    shape: {array.shape}
    ndim: {array.ndim}
    size: {array.size}
    dtype: {array.dtype}
    ''')
```

+++ {"slideshow": {"slide_type": "fragment"}}

Note that the function `len` only returns the size of the first dimension:

```{code-cell}
---
slideshow:
  slide_type: '-'
---
assert A.shape[0] == len(A)
len(A)
```

+++ {"slideshow": {"slide_type": "subslide"}}

Unlike `list`, every `numpy` array has a data type. For efficient computation/storage, numpy implements different data types with different storage sizes:
* integer: `int8`, `int16`, `int32`, `int64`, `uint8`, ...
* float: `float16`, `float32`, `float64`, ...
* complex: `complex64`, `complex128`, ...
* boolean: `bool8`
* Unicode: `string`
* Object: `object`

+++ {"slideshow": {"slide_type": "fragment"}}

E.g., `int64` is the 64-bit integer. Unlike `int`, `int64` has a range.

```{code-cell}
---
slideshow:
  slide_type: '-'
---
np.int64?
print(f'range: {np.int64(-2**63)} to {np.int64(2**63-1)}')
np.int64(2**63)   # overflow error
```

+++ {"slideshow": {"slide_type": "subslide"}}

We can use the `astype` method to convert the data type:

```{code-cell}
---
slideshow:
  slide_type: '-'
---
A_int64 = A.astype(int)       # converts to int64 by default
A_float32 = A.astype(np.float32)  # converts to float32
for array in A_int64, A_float32:
    print(array, array.dtype)
```

+++ {"slideshow": {"slide_type": "fragment"}}

We have to be careful about assigning items of different types to an array.

```{code-cell}
---
slideshow:
  slide_type: '-'
---
A_int64[0,0] = 1
print(A_int64)
A_int64[0,0] = 0.5
print(A_int64)                # intended assignment fails
np.array([int(1), float(1)])  # will be all floating point numbers
```

+++ {"slideshow": {"slide_type": "subslide"}}

**Exercise** Create a heterogeneous numpy array to store both integer and strings:
```Python
[0, 1, 2, 'a', 'b', 'c']
```
*Hint:* There is an numpy data type called `object`.

```{code-cell}
---
nbgrader:
  grade: false
  grade_id: hetero
  locked: false
  schema_version: 3
  solution: true
  task: false
slideshow:
  slide_type: '-'
---
np.object?
### BEGIN SOLUTION
heterogeneous_np_array = np.array([*range(3),*'abc'],dtype=object)
### END SOLUTION
heterogeneous_np_array
```

+++ {"slideshow": {"slide_type": "fragment"}}

Be careful when creating arrays of `tuple`/`list`:

```{code-cell}
---
slideshow:
  slide_type: '-'
---
for array in (np.array([(1,2),[3,4,5]],dtype=object),
              np.array([(1,2),[3,4]],dtype=object)):
    print(array, '\nshape:', array.shape, 'length:', len(array), 'size:', array.size)
```

+++ {"slideshow": {"slide_type": "subslide"}}

`numpy` provides many functions to create an array:

```{code-cell}
---
slideshow:
  slide_type: '-'
---
np.zeros?
np.zeros(0), np.zeros(1), np.zeros((2,3,4))  # Dimension can be higher than 2
```

```{code-cell}
---
slideshow:
  slide_type: '-'
---
np.ones?
np.ones(0, dtype=int), np.ones((2,3,4), dtype=int)  # initialize values to int 1
```

```{code-cell}
np.eye?
np.eye(0), np.eye(1), np.eye(2), np.eye(3)  # identity matrices
```

```{code-cell}
np.diag?
np.diag(range(1)), np.diag(range(2)), np.diag(np.ones(3),k=1)  # diagonal matrices
```

```{code-cell}
---
slideshow:
  slide_type: '-'
---
np.empty?
np.empty(0), np.empty((2,3,4), dtype=int)  # create array faster without initialization
```

+++ {"slideshow": {"slide_type": "subslide"}}

`numpy` also provides functions to build an array using rules.

```{code-cell}
---
slideshow:
  slide_type: '-'
---
np.arange?
np.arange(5), np.arange(4,5), np.arange(4.5,5.5,0.5)  # like range but allow non-integer parameters
```

```{code-cell}
---
slideshow:
  slide_type: '-'
---
np.linspace?
np.linspace(4,5), np.linspace(4,5,11), np.linspace(4,5,11)  # can specify number of points instead of step
```

```{code-cell}
---
slideshow:
  slide_type: '-'
---
np.fromfunction?
np.fromfunction(lambda i, j: i * j, (3,4))  # can initialize using a function
```

+++ {"slideshow": {"slide_type": "subslide"}}

We can also reshape an array using the `reshape` method/function:

```{code-cell}
---
slideshow:
  slide_type: '-'
---
array = np.arange(2*3*4)
array.reshape?
(array, 
 array.reshape(2,3,4),      # last axis index changes fastest
 array.reshape(2,3,-1),     # size of last axis calculated automatically
 array.reshape((2,3,4), order='F')) # first axis index changes fastest
```

+++ {"slideshow": {"slide_type": "fragment"}}

`flatten` is a special case of reshaping an array to one dimension.  
(Indeed, `flatten` returns a copy of the array but `reshape` returns a dynamic view whenever possible.)

```{code-cell}
---
slideshow:
  slide_type: '-'
---
array = np.arange(2*3*4).reshape(2,3,4)
array, array.flatten(), array.reshape(-1), array.flatten(order='F')
```

+++ {"slideshow": {"slide_type": "subslide"}}

**Exercise** Correct the following function to print every element of an array line-by-line.
```Python
def print_array_entries_line_by_line(array):
    for i in array:
        print(i)
```

```{code-cell}
---
nbgrader:
  grade: false
  grade_id: flatten
  locked: false
  schema_version: 3
  solution: true
  task: false
slideshow:
  slide_type: '-'
tags: [remove-output]
---
def print_array_entries_line_by_line(array):
    ### BEGIN SOLUTION
    for i in array.flatten():
        print(i)
    ### END SOLUTION
    
print_array_entries_line_by_line(np.arange(2*3*4).reshape(2,3,4))
```

+++ {"slideshow": {"slide_type": "slide"}}

### Operating on `numpy` arrays

+++ {"slideshow": {"slide_type": "subslide"}}

**How to verify the solution of a system of linear equations?**

+++ {"slideshow": {"slide_type": "fragment"}}

Before solving the system of linear equations, let us try to verify a solution to the equations:

$$ \begin{aligned}
2x_0 + 2x_1 &= 1\\
\hphantom{2x_0 +}  2x_1 &= 1
\end{aligned}
$$

+++ {"slideshow": {"slide_type": "fragment"}}

`numpy` provides the function `matmul` and the operator `@` for matrix multiplication.

```{code-cell}
---
slideshow:
  slide_type: '-'
---
print(np.matmul(A,np.array([0,0])) == b)
print(A @ np.array([0,0.5]) == b)
```

+++ {"slideshow": {"slide_type": "subslide"}}

Note that the comparison on `numpy` arrays returns a boolean array instead of a boolean value, unlike the comparison operations on lists.

+++ {"slideshow": {"slide_type": "fragment"}}

To check whether all items are true, we use the `all` method.

```{code-cell}
---
slideshow:
  slide_type: '-'
---
print((np.matmul(A,np.array([0,0])) == b).all())
print((A @ np.array([0,0.5]) == b).all())
```

+++ {"slideshow": {"slide_type": "subslide"}}

**How to concatenate arrays?**

+++ {"slideshow": {"slide_type": "-"}}

We will operate on an augmented matrix of the coefficients:

$$ \begin{aligned} \mathbf{C} &= \begin{bmatrix}
\mathbf{A} & \mathbf{b}
\end{bmatrix}\\
&= \begin{bmatrix}
a_{00} & a_{01} & b_0 \\
a_{10} & a_{11} & b_1
\end{bmatrix} 
\end{aligned}
$$

+++ {"slideshow": {"slide_type": "fragment"}}

`numpy` provides functions to create block matrices:

```{code-cell}
---
slideshow:
  slide_type: '-'
---
np.block?
C = np.block([A,b.reshape(-1,1)])  # reshape to ensure same ndim
C
```

+++ {"slideshow": {"slide_type": "fragment"}}

To stack an array along different axes:

```{code-cell}
---
slideshow:
  slide_type: '-'
---
array = np.arange(1*2*3).reshape(1,2,3)
for concat_array in [array,
                     np.hstack((array,array)),   # stack along the first axis
                     np.vstack((array,array)),                  # second axis
                     np.concatenate((array,array), axis=-1),    # last axis
                     np.stack((array,array), axis=0)]:          # new axis
    print(concat_array, '\nshape:', concat_array.shape)
```

+++ {"slideshow": {"slide_type": "subslide"}}

**How to perform arithmetic operations on a `numpy` array?**

+++ {"slideshow": {"slide_type": "fragment"}}

To divide all the coefficients by $2$, we can simply write:

```{code-cell}
---
slideshow:
  slide_type: '-'
---
D = C / 2
D
```

+++ {"slideshow": {"slide_type": "fragment"}}

Note that the above does not work for `list`.

```{code-cell}
---
slideshow:
  slide_type: '-'
---
C.tolist() / 2 # deep convert to list
```

+++ {"slideshow": {"slide_type": "subslide"}}

Arithmetic operations on `numpy` arrays apply if the arrays have compatible dimensions. Two dimensions are compatible when
- they are equal, except for
- components equal to 1.

+++ {"slideshow": {"slide_type": "fragment"}}

`numpy` uses [broadcasting rules](https://numpy.org/doc/stable/user/basics.broadcasting.html#general-broadcasting-rules) to stretch the axis of size 1 up to match the corresponding axis in other arrays.  
`C / 2` is a example where the second operand $2$ is broadcasted to a $2$-by-$2$ matrix before the elementwise division. Another example is as follows. 

```{code-cell}
---
slideshow:
  slide_type: '-'
---
three_by_one = np.arange(3).reshape(3,1)
one_by_four = np.arange(4).reshape(1,4)
print(f'''
{three_by_one}
*
{one_by_four}
==
{three_by_one * one_by_four}
''')
```

+++ {"slideshow": {"slide_type": "subslide"}}

Next, to subtract the second row of the coefficients from the first row:

```{code-cell}
---
slideshow:
  slide_type: '-'
---
D[0,:] = D[0,:] - D[1,:]
D
```

+++ {"slideshow": {"slide_type": "fragment"}}

Notice the use of commas to index different dimensions instead of using multiple brackets:

```{code-cell}
---
slideshow:
  slide_type: '-'
---
assert (D[0][:] == D[0,:]).all()
```

+++ {"slideshow": {"slide_type": "subslide"}}

Using this indexing technique, it is easy extract the last column as the solution to the system of linear equations:

```{code-cell}
---
slideshow:
  slide_type: '-'
---
x = D[:,-1]
x
```

+++ {"slideshow": {"slide_type": "fragment"}}

This gives the desired solution $x_0=0$ and $x_1=0.5$ for

$$ \begin{aligned}
2x_0 + 2x_1 &= 1\\
\hphantom{2x_0 +}  2x_1 &= 1\\
\end{aligned}$$

+++ {"slideshow": {"slide_type": "subslide"}}

`numpy` provides many [convenient ways](https://numpy.org/doc/stable/reference/arrays.indexing.html#advanced-indexing) to index an array.

```{code-cell}
---
slideshow:
  slide_type: '-'
---
B = np.arange(2*3).reshape(2,3)
B, B[(0,1),(2,0)]  # selecting the corners using integer array
```

```{code-cell}
---
slideshow:
  slide_type: '-'
---
B = np.arange(2*3*4).reshape(2,3,4)
B, B[0], B[0,(1,2)], B[0,(1,2),(2,3)], B[:,(1,2),(2,3)]  # pay attention to the last two cases
```

```{code-cell}
---
slideshow:
  slide_type: '-'
---
assert (B[...,-1] == B[:,:,-1]).all()
B[...,-1]  # ... expands to selecting all elements of all previous dimensions
```

```{code-cell}
---
slideshow:
  slide_type: '-'
---
B[B>5]  # indexing using boolean array
```

+++ {"slideshow": {"slide_type": "subslide"}}

Finally, the following function solves a system of 2 linear equations with 2 variables.

```{code-cell}
---
slideshow:
  slide_type: '-'
---
def solve_2_by_2_system(A,b):
    '''Returns the unique solution of the linear system, if exists, 
    else returns None.'''
    C = np.hstack((A,b.reshape(-1,1)))
    if C[0,0] == 0: C = C[(1,0),:]
    if C[0,0] == 0: return None
    C[0,:] = C[0,:] / C[0,0]
    C[1,:] = C[1,:] - C[0,:] * C[1,0]
    if C[1,1] == 0: return None
    C[1,:] = C[1,:] / C[1,1]
    C[0,:] = C[0,:] - C[1,:] * C[0,1]
    return C[:,-1]
```

```{code-cell}
---
slideshow:
  slide_type: '-'
---
# tests
for A in (np.eye(2),
          np.ones((2,2)),
          np.stack((np.ones(2),np.zeros(2))),
          np.stack((np.ones(2),np.zeros(2)),axis=1)):
    print(f'A={A}\nb={b}\nx={solve_2_by_2_system(A,b)}\n')
```

### Universal functions

+++ {"slideshow": {"slide_type": "subslide"}}

Why does the first line of code below return two arrays but the second code return only one array? Shouldn't the first line of code return the following?
```Python
array([[(0,1), (0,2), (0,3)],
       [(1,1), (1,2), (1,3)]])
```

```{code-cell}
---
slideshow:
  slide_type: '-'
---
print(np.fromfunction(lambda i,j:(i,j), (2,3), dtype=int))
print(np.fromfunction(lambda i,j:(i*j), (2,3), dtype=int))
```

+++ {"slideshow": {"slide_type": "-"}}

From the documentation, `fromfunction` applies the given function to the two arrays as arguments.
- The first line of code returns a tuple of the arrays.
- The second line of code multiplies the two arrays to give one array, according to how multiplication works for numpy arrays.

+++ {"slideshow": {"slide_type": "subslide"}}

Indeed, `numpy` implements [universal/vectorized functions/operators](https://numpy.org/doc/stable/reference/ufuncs.html) that take arrays as arguments and perform operations with appropriate broadcasting rules. The following is an example that uses the universal function `np.sin`:

```{code-cell}
---
slideshow:
  slide_type: '-'
---
import matplotlib.pyplot as plt

@widgets.interact(a=(0,5,1),b=(-1,1,0.1))
def plot_sin(a=1,b=0):
    x = np.linspace(0,2*math.pi)
    plt.plot(x,np.sin(a*x+b*math.pi))  # np.sin, *, + are universal functions
    plt.title(r'$\sin(ax+b\pi)$')
    plt.xlabel(r'$x$ (radian)')
```

+++ {"slideshow": {"slide_type": "subslide"}}

In addition to making the code shorter, universal functions are both efficient and flexible. (Recall the Monte Carlo simulation to approximate $\pi$.)

+++ {"slideshow": {"slide_type": "fragment"}}

**Exercise** Explain how the Monte Carlo simulation work using universal functions:
```Python
def np_approximate_pi(n):
    in_circle = (np.random.random((n,2))**2).sum(axis=-1) < 1
    mean = 4 * in_circle.mean()
    std = 4 * in_circle.std() / n**0.5
    return np.array([mean - 2*std, mean + 2*std])
```

+++ {"nbgrader": {"grade": true, "grade_id": "universal", "locked": false, "points": 0, "schema_version": 3, "solution": true, "task": false}}

- `random.random` generates a numpy array for $n$ points in the unit square randomly.
- `sum` sums up the element along the last axis to give the squared distance.
- `<` returns the boolean array indicating whether each point is in the first quadrant of the inscribed circle.
- `mean` and `std` returns the mean and standard deviation of the boolean array with True and False interpreted as 1 and 0 respectively.
