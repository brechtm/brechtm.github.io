Python and the need for speed
#############################

:tags: python
:category: rinohtype

.. contents::

Python is doing very well in the world of programming languages. The popularity
of Python has been growing steadily over the past decades as shown by the
`TIOBE <https://www.tiobe.com/tiobe-index/>`_ and `PYPL
<http://pypl.github.io>`_ indexes. This doesn't have to be surprising, since
Python has a lot going for it: it's easy to learn, it has a beautiful syntax,
an excellent standard library, a great package ecosystem covering many domains
and a friendly community. However, one thing that Python is not, is fast.

Python is **Not** Fast Enough
=============================

While it is true that many applications can benefit from `NumPy
<http://www.numpy.org>`_, `Numba <http://numba.pydata.org>`_ and `Cython
<http://cython.org>`_ to speed them up massively, there is a class of
applications that cannot take this route. One example is my own project,
`rinohtype. <http://www.mos6581.org/rinohtype>`_ There is no single, obvious
bottleneck such as a tight number-crunching loop that can be sped up using
these tools. *But haven't you heard about PyPy?*, you say. I have, and alas, it
runs rinohtype `slower than CPython!
<https://bitbucket.org/pypy/pypy/issues/2365/rinohtype-much-slower-on-pypy3>`_
PyPy neither is able to speed up all classes of applications. And especially
for batch-type applications such as rinohtype, the significant `JIT warmup time
<https://lincolnloop.com/blog/speed-comparison-cpython-pypy-pyston/>`_ might
even negate any speedups.

I am not alone to believe that Python's speed is an issue. Countless efforts
have been made at running Python applications at a faster pace: `PyPy
<http://pypy.org>`_, `Pyston <https://github.com/dropbox/pyston>`_,
`Pyjion <https://github.com/Microsoft/Pyjion>`_, `Nuitka <http://nuitka.net>`_
, `Pythran <http://pythonhosted.org/pythran/>`_, `FAT Python,
<https://github.com/haypo/fatoptimizer>`_ `RegisterVM
<https://hg.python.org/sandbox/registervm/file/tip/REGISTERVM.txt>`_, `wpython,
<https://code.google.com/archive/p/wpython/>`_ `HotPy
<http://code.google.com/p/hotpy/>`_, `unladen-swallow
<https://code.google.com/archive/p/unladen-swallow/>`_, `Psyco,
<http://psyco.sf.net/>`_ `Shed Skin <http://code.google.com/p/shedskin/>`_, and
`more <https://wiki.python.org/moin/PythonImplementations>`_. Pyston is a
JIT-based Python implementation originally supported by DropBox. Unfortunately,
`DropBox have stopped sponsoring its development
<https://blog.pyston.org/2017/01/31/pyston-0-6-1-released-and-future-plans>`_
and has been moving its performance-critical code over to Go. Google similarly
seems to be `moving away from Python
<https://opensource.googleblog.com/2017/01/grumpy-go-running-python.html>`_.
These are clear indications that Python is losing ground to new programming
languages that offer a similar features to Python but better performance in
addition. There's no more denying that Python isn't fast enough.

A Different Approach
====================

We should face the facts and admit we are fighting a losing battle. Yet another
Python compiler or JIT engine will not bring the hoped-for performance boost.
As demonstrated by the many failed attempts, speedy execution of (all) Python
code is a near-impossible challenge. It's time to look at more drastic, but
technically much simpler ways to solve Python's performance problem.

JavaScript (`V8 <https://developers.google.com/v8/>`_, `SpiderMonkey
<https://developer.mozilla.org/en-US/docs/Mozilla/Projects/SpiderMonkey>`_) and
Lua (`LuaJIT <http://luajit.org>`_) are often cited as examples of dynamic
languages with very fast JIT implementations. These languages are arguably much
simpler than Python, which undoubtedly influences the complexity and
performance of a JIT compiler. Therefore, the reason for Python's limited
performance perhaps lies in the `nature of the language
<http://faster-cpython.readthedocs.io/misc.html#why-python-is-slow>`_ itself;
some of its features simply make it ill-suited for fast execution using a JIT.
One example of such a feature is the fact that `everything in Python is
mutable, <http://faster-cpython.readthedocs.io/mutable.html>`_ killing many
opportunities for optimization.

It should be possible to define a subset of the Python language, uninspiredly
dubbed "TurboPython", that excludes those features that stand in the way of
high-performance JIT execution (or compilation). Not using some of these
features coincides with good design practices, so it doesn't necessarily have
to be all bad. While the fact that everything is mutable in Python is useful
for mocking purposes during testing, it is generally considered extremely bad
style to override builtin functions, constants or class methods in production
code. Other candidates for banishment from TurboPython include ``eval`` and
``exec``.

Since type annotations are now an official Python feature, I would go far as to
say that these should be required in TurboPython code, since the presence of
type information allows for the JIT compiler to be much simpler and more
performant (and reduces warmup time as well). In fact, even without a JIT, a
simple TurboPython interpreter might even be many times faster than CPython.

TurboPython should of course not replace Python as we know it. It needs to
exist alongside Python, to be used when the extra performance is required.
Since TurboPython is a subset of Python, it will also run on Python
interpreters, albeit slower. Ideally, a single class, module or package used
could be written in TurboPython and benefit from the extra speed while the rest
of the application runs at its usual pace. `Python 3.6 introduced an API that
allows plugging a JIT into CPython,
<https://docs.python.org/3.6/whatsnew/3.6.html#pep-523-adding-a-frame-evaluation-api-to-cpython>`_
which might be used to implement something like this.

I lack the experience with interpreter/JIT/compiler design to assess whether
the suggestions made above are in fact feasible and capable of resulting in a
significant speed boost. I'll leave that to others. I do however know that the
current approaches are not cutting it and alternatives need to be explored.

Comments on `comp.lang.python`_, `Lobste.rs`_ and Reddit_.

.. _comp.lang.python: https://groups.google.com/forum/#!topic/comp.lang.python/8grCQrkSLb8
.. _Lobste.rs: https://lobste.rs/s/gsi5xy/python_need_for_speed
.. _Reddit: https://www.reddit.com/r/Python/comments/640imt/python_and_the_need_for_speed/
