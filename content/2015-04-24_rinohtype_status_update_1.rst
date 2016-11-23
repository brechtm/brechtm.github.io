RinohType update: reStructuredText and style sheets
###################################################

:tags: python
:category: rinohtype

.. contents::


Almost 18 months have passed since I `announced RinohType`_, so it's about time for a little status update. Inspired by some of the comments on the last blog article, I decided to focus on `reStructuredText`_ support, as this would make RinohType much more useful to many people. The changes required to fully support reStructuredText also led to may other improvements in RinohType. Additionally, the style sheet system has received some important updates. The changes are summarized below.

Last year, I submitted a talk proposal to EuroPython which was unfortunately rejected. From the reviewers' comments I understood that the proposal could not be accepted without the availability of a RinohType release. For EuroPython 2015, I submitted a new proposal, now accompanied with a `first RinohType release`_. This release includes a command-line to tool to render reStructuredText files and a Sphinx builder. You are welcome to give it a spin and send me feedback. Expect to encounter many bugs, however. Please find more details in the description on PyPI.

.. _announced RinohType: {filename}2013-11-03_introducing-rinohtype.rst
.. _first RinohType release: https://pypi.python.org/pypi/RinohType/0.1.1


reStructuredText and Sphinx
===========================

RinohType now has fairly complete support for `reStructuredText`_. Armed with `demo.txt`_, I set out to interpret and render all remaining reStructuredText doctree elements: field/option lists, hyperlinks, problematic nodes (text color), compound paragraphs, sidebar, inline images, figures, citations and tables. While all reStructured directives  should now be supported, the various options that can be passed to the them might be not be.

reStructuredText's ability to nest document elements uncovered the fact that many of my document building blocks were built under much simpler assumptions. For example, a table cell can now contain any other element such as a list or even another table, where before it could only contain text. The document building blocks in general are now much more capable and should be able to handle whatever reStructuredText supports at the least. The RinohType building blocks (so-called *flowables*) now also form a proper nested document tree, which is very useful when styling the document.

Table rendering code was rewritten completely to:

- accept any flowable as cell content instead of only text,
- better fit the styling mechanism, and
- be able to automatically size columns based on their content.

A wonderful corollary of reStructuredText support is that it was fairly easy to create a Sphinx builder. I have already used it to render a small technical report for my freelance work. It does not yet support all custom reStructuredText directives added by Sphinx however, so it cannot yet render Sphinx's documentation. Locally, I have it parsing the complete document tree, but it still fails rendering at some point, so you can expect this to work very soon. The builder is included in the release mentioned above. Instructions on how to use it can be found in the release's package description on PyPI.

.. _demo.txt: http://docutils.sourceforge.net/docs/user/rst/demo.txt


PDF Backend
===========

The PDF backend was extended to support some of the reStructuredText features; it can now output colored text and display interactive hyperlinks (but for some reason, they don't all work in Apple Preview). Next to PDF images, bitmap images are now also supported when `Pillow`_ is installed.

It is now also possible to copy selected text from the resulting PDF and not end up with gibberish when pasting. The problem with certain PDF readers (Firefox's pdf.js and Evince) has not yet been resolved, however. I am fairly certain this is due a bug in the readers, but I might try to work around it.

.. _Pillow: https://python-pillow.github.io


Style System
============

I also took some time to make fundamental improvements to the styling system. The new system is heavily inspired by `CSS`_, but adds some extra functionality that CSS lacks. The style sheets are currently specified in Python code (see examples below). I might provide a plain text alternative (YAML, INI or perhaps even CSS) in the future. The following illustrates the most important features of the style system without going into details.

.. _CSS: https://en.wikipedia.org/wiki/Cascading_Style_Sheets


Selectors
---------

Very similar to `CSS selectors`_, elements can be matched based on their context. For example, the following matches any paragraph that is a child of a list item.

.. code-block:: python

    ListItem / Paragraph
    
``ListItem`` and ``Paragraph`` are both RinohType classes (``Flowable`` subclasses) that make up the document tree.

Similar to HTML/CSS's 'class' attribute, a flowable can have a 'style' attribute which can be checked when constructing a selector. This selects all paragraphs of style 'title':

.. code-block:: python

    Paragraph.like('title')

The ``like`` method can also match arbitrary attributes of elements. This can be used to do more advanced things such as selecting the background objects on all odd rows of a table, limited to the cells not spanning multiple rows:

.. code-block:: python

    TableCell.like(row_index=slice(0, None, 2), rowspan=1) / TableCellBackground
    
`Python's ellipsis`_ can be used to match any number of levels in the document tree. For example, the following matches any paragraph element at any level inside a table cell.

.. code-block:: python

    TableCell / ... / Paragraph

RinohType borrows CSS's concept of `specificity`_ to determine the "winning" selector when multiple selectors match a given document element.

.. _CSS selectors: https://en.wikipedia.org/wiki/Cascading_Style_Sheets#Selector
.. _Python's ellipsis: https://docs.python.org/3.5/library/constants.html#Ellipsis
.. _specificity: https://en.wikipedia.org/wiki/Cascading_Style_Sheets#Specificity


Matchers and Style Sheets
-------------------------

In contrast to CSS, RinohType's style system has an extra layer of indirection so that the user does not have to redefine the selectors in each style sheet. A ``StyledMatcher`` is basically a dictionary that maps descriptions to selectors.

.. code-block:: python

    matcher = StyledMatcher()
    ...
    matcher('emphasis', StyledText.like('emphasis'))
    matcher('nested line block', GroupedFlowables.like('line block')
                                 / GroupedFlowables.like('line block'))
    ...

A single ``StyledMatcher`` can serve multiple ``StyleSheet``\ s:

.. code-block:: python

    styles = StyleSheet('IEEE', matcher=matcher)
    ...
    styles('emphasis', font_slant=ITALIC)
    styles('nested line block', margin_left=0.5*CM)
    ...

One feature sorely missing from CSS is variables. Here's an example of how variables can be specified and used in RinohType style sheets:

.. code-block:: python

    styles.variables['ieee_family'] = TypeFamily(serif=times,
                                                 sans=helvetica,
                                                 mono=courier)
    ...
    styles('monospaced',
           typeface=Var('ieee_family').mono,
           font_size=9*PT,
           hyphenate=False,
           ligatures=False)
    ...
    
Another stylesheet can inherit from this one and easily replace all fonts in the document by overriding the ``ieee_family`` variable.

I doubt there will be a need to have many different matchers. The end user will likely never have to deal with them as most documents can use the default matcher. When custom flowables are used in a document, the default base matcher can be easily extended to style these.


Inheritance
-----------

Similar to CSS's `inheritance`_, **text elements** inherit properties from their parent. So for the example style sheet above, text with style ``emphasis`` inherits the properties (such as ``typeface``, ``font_weight`` and ``font_size``) from the paragraph it is a child of, but overrides the ``font_slant`` property.

In addition, RinohType allows specifying a base style for each style. This avoids duplication of style information and the maintenance difficulties resulting from it.

.. code-block:: python

    styles('heading level 1',
           typeface=Var('ieee_family').serif,
           font_weight=REGULAR,
           font_size=10*PT,
           small_caps=True,
           justify=CENTER,
           line_spacing=FixedSpacing(12*PT),
           space_above=18*PT,
           space_below=6*PT,
           number_format=ROMAN_UC,
           label_suffix='.' + FixedWidthSpace())
    
    styles('unnumbered heading level 1',
           base='heading level 1',
           number_format=None)

.. _inheritance: https://en.wikipedia.org/wiki/Cascading_Style_Sheets#Inheritance


Performance
===========

Shortly after posting the first blog article on RinohType, I've focused on speeding up document processing. Appareantly I managed to `almost halve rendering time`_ by refactoring the code and adding more memoization.

The next step was to speed up the slowest code by compiling to a fast C module using **Cython** and static type declarations. Unfortunately, there was no single part of the code where most of the time was spent, as these were repeatedly removed during refactoring for speed earlier. And even when cythonizing some parts, they didn't result in a significant performance boost. I believe this is due to the fact that there's not much number crunching going on as in the typical applications benefitting from Cython. In RinohType, I suspect container (dict, list) access operations to be the most common.

Next stop: **PyPy**. Hoping for a no-effort instant speedup, instead both `PyPy3`_ and `PyPy2`_ were much **slower** than CPython! As for Cython, I suppose this could be attributed to the fact that RinohType is not the typical use case for PyPy.

But the situation isn't dramatic. RinohType is plenty fast on modern systems. The rendering time shouldn't be a problem unless you're rendering hundreds of pages. Once RinohType is more feature-complete and less buggy, I might revisit performance tuning.

.. _almost halve rendering time: https://twitter.com/brechtmachiels/status/401322293928161280
.. _PyPy3: https://mail.python.org/pipermail/pypy-dev/2014-February/012182.html
.. _PyPy2: https://mail.python.org/pipermail/pypy-dev/2014-March/012284.html


Feedback
========

For general discussions on RinohType, you are welcome to join the `mailing list`_ (`GMANE archive`_). Please report bugs using the `GitHub issue tracker`_.

.. _mailing list: https://www.freelists.org/list/rinohtype
.. _GMANE archive: http://dir.gmane.org/gmane.comp.type-setting.rinohtype
.. _GitHub issue tracker: https://github.com/brechtm/rinohtype/issues


Comments on `Hacker News`_ and `Reddit`_

.. _Hacker News: https://news.ycombinator.com/item?id=9433415
.. _Reddit: http://www.reddit.com/r/Python/comments/33potn/rinohtype_the_python_document_processor_status/

.. _reStructuredText: http://docutils.sourceforge.net/rst.html
