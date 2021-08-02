Chapter 0
=========

Braces define a set (in Python as in Mathematics)

♡  ∈ { ♢, ♡, ♠, ♣ } read "Heart belongs to the set of suits."

R denotes all real numbers, C denotes all complex numbers.

|S| denotes the cardinality of the finite set S. Cardinality is the number of
elements. The set of suits has cardinality 4.

The Cartesian Product of A, B is the set of all pairs (a,b) where a ∈ A and b ∈
B.

The cardinality of |A * B| = |A| * |B|.

> Formally, a function is a set of pairs no two of which share the same first
> entry.

How quaint.

More jargon: the output of a function is said to be the image of the input under
the function and the input is the pre-image of the output.

The set D of possible inputs is the <term>domain</term> of the function.

If r = f(q) we say that "q maps to r under f" denoted as q ⇒ r.

The "co-domain" is a set from which the function's output values are chosen.

f : D ⇒ F means that f is a function whose domain is the set D and whose
co-domain is the set F.

The image of a function f is the set of images of all domain elements.

In this book they refer to Python 'functions' as 'procedures' to avoid
confusion.

A computational problem is an input-output specification that a procedure might
satisfy.

For sets D & F we use the notation F^D to denote all functions from D to F. The
set of functions from the set W of words to the set R of real numbers is denoted
R^W.

For any finite sets D & F, `|D^F| = |D|^|F|`.

For any domain D, there is a function `id<sub>D</sub> : D → D` called the identity
function for D, defined by

`id<sub>D</sub>(d) = d` for every d ∈ D.

Composition of functions `( g ○ f )(x) = g(f(x))`

