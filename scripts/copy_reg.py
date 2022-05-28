from bcdebug import debug
# Helper to provide extensibility for pickle/cPickle.

dispatch_table = {}
safe_constructors = {}

def pickle(ob_type, pickle_function, constructor_ob = None):
    debug(__name__ + ", pickle")
    dispatch_table[ob_type] = pickle_function

    if constructor_ob is not None:
        constructor(constructor_ob)

def constructor(object):
    debug(__name__ + ", constructor")
    safe_constructors[object] = 1

# Example: provide pickling support for complex numbers.

def pickle_complex(c):
    debug(__name__ + ", pickle_complex")
    return complex, (c.real, c.imag)

pickle(type(1j), pickle_complex, complex)
