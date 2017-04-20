# File

* [Adding\_two\_Scalars.py](#scalar)
* [Adding\_two\_Matrices.py](#matrix)

* * *

### Detail

<h4 id = "scalar">Adding\_two\_Scalars.py</h4>

1. ***Define Variables***
    
    `x`, `y`, and `z` are all Variable objects.
    The output of the function `f` is a `numpy.ndarray` with **zero** dimensions. 

    From the official tutorial website, it says you may have noticed that there was a slight delay in executing the function instruction. 
    Behind the scene, `f` was being compiled into **C code**.

    In Theano, **all symbols must be typed**. `T.dscalar` is the type we assign to "0-dimensional arrays fo doubles"
    It is a Theano [Type][1].

    `x` and `y` are instances of `TensorVariable`. 
    However, they are assigned the theano Type `dscalar` in their `type` field.

        >>> type(x)
        <class 'theano.tensor.var.TensorVariable'>
        >>> x.type
        TensorType(float64, scalar)
        >>> T.dscalar
        TensorType(float64, scalar)
        >>> x.type is T.dscalar
        True

    By calling `T.dscalar` with a `string` argument, you create a Variable representing a floating-point scalar quantity with the given name. 
    If you provide no argument, the symbol will be unnamed. **Names are not required, but they can help debugging.**

2. ***Define pre-function***

    The next step is to combine x and y into their sum z:

        >>> z = x + y

    z is *yet* another Variable which represents the addition of x and y. You can use the `pp` function to pretty-print out the computation associated to z.

        >>> from theano import pp
        >>> print(pp(z))
        (x + y)

3. ***Define function***

    The last step is to create a function taking x and y as inputs and giving z as output:

        >>> f = function([x, y], z)

    The first argument to function is a `list` of Variables that will be provided as inputs to the function. 
The second argument is **a single Variable or a list of Variables**.
    For either case, the second argument is what we want to see as output when we apply the function. `f` may then be used like a normal Python function.

[1]: http://deeplearning.net/software/theano_versions/dev/extending/graphstructures.html#type

<h4 id = "matrix">Adding\_two\_Matrices.py</h4>
