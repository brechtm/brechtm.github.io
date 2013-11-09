Introducing RinohType
#####################

:subtitle: the Python document processor
:tags: python
:category: RinohType

.. contents::

I originally planned to release RinohType into wild only after I had finished a full review, refactoring and documenting of the code. I also wanted to write some API documentation and a small tutorial, all in the spirit of making a good first impression. Turns out all this takes a huge amount of time! So I've decided to dump the code in its current state onto GitHub, write a blog article about it and await some valuable feedback while I resume my refactoring and documenting chore.

If you decide to play around with the code, please bear in mind that this is just a preview; your experience might not be as smooth as I intend it to be eventually.

Motivation
==========

Somewhere back in 2009, I was using `LaTeX <http://en.wikipedia.org/wiki/LaTeX>`_ to write a paper on some of my `PhD research <{filename}pages/thesis.rst>`_. I had used LaTeX before for a number of lab reports and two master's theses, so I was already experienced with it. While I find working with LaTeX is generally a smooth experience, I did encounter some annoyances over the years. The particular annoyance of the day was figure placement. Where LaTeX's automatic figure placement is pretty good in longer texts, I find it extremely frustrating when writing a short paper. For these papers, I basically want to place my figures manually, exactly where I want them (figure 2 goes in the top of the left column on page 2, for example). However, this doesn't seem to be an option with LaTeX, so I ended up moving my ``\includegraphics`` directive around in the LaTeX source document in a trial-and-error fashion to have the figure eventually appear where I wanted it to be. Basically, this meant moving all my ``\includegraphics`` directives to a location far from near the text where it would end up in the rendered document. After a good hour of messing around with this and `exploring <http://www.ntg.nl/pipermail/ntg-context/2008/037150.html>`_  two alternatives to LaTeX (`Lout <http://en.wikipedia.org/wiki/Lout_(software)>`_ and `ConTeXt <http://en.wikipedia.org/wiki/ConTeXt>`_), I said to myself, *Enough! I'm writing my own document processor!* And so I set out to build the definitive replacement for LaTeX.

It is worth pointing out the other gripes I have with (La)TeX at this point. I will probably regret this later (I have the impression TeXies can be quite fanatical), but here we go:

- TeX is not transparent. It is a huge, complex system. To make things worse, there are a number of different TeX distributions, each organizing things in a slightly different way. With hundreds of megabytes and seemingly millions of files for a typical TeX installation, I have no idea what is going on when TeX processes a document. `kpathsea <http://www.ctan.org/pkg/kpathsea>`_ is a testament to a part of this complexity.
- The arcane TeX macro language is not accessible to a broad audience. I believe this is why most LaTeX-generated documents you come across have exactly the same (retro) look; very few people are capable of creating new document styles.
- TeX is not very modern. Yes, even today it still is a very impressive piece of software. However, next to being built upon some weird macro language of old, it predates a lot of modern technologies (Unicode, standard font file formats, Postscript and PDF), so these things had to be hacked into it. While I understand you generally shouldn't rewrite software from scratch, maybe TeX should be one of the few exceptions to this rule?
- TeX's warnings/errors are often very cryptic. It can sometimes take a long time to figure out what's wrong.
- (La)TeX has an incredible amount of extension packages available. There's probably a package for pretty much `anything you might ever need <http://tex.stackexchange.com/questions/67656/are-there-other-fun-packages-like-the-coffee-stains-package>`_. But why do I even need to mess around with all these extension packages when all I'm doing is writing a simple article? Doesn't this mean that LaTeX should include at least some of the most commonly used packages by default?
- This might largely be a solved problem by now, but I remember often running into input and font encoding issues with LaTeX in the past.
- There is no strict separation of content and style. This is mostly an issue for publishers that want to ensure a consistent style across articles in a journal. With LaTeX, academic authors can always reduce the margins or change the interline spacing to be able to squeeze in more half-truths.

Wow, this all sounds very negative. I should mention that RinohType was in a large part also inspired by (La)TeX in a positive way; the latter gets a lot of things right indeed. However, I believe we can do better than TeX. Not so much in the typesetting quality, but in the ease-of-use.

For me, the obvious programming language to choose for this little project was Python, as it is probably the most accessible programming language and generally fun to program in (ok, that's subjective). I imagined Python's powerful OO could be employed to define document styles that could easily be inherited from. Initially, I also planned on the source document being Python source files. While technically possible, I am now convinced that Python's syntax is not suited for this purpose.

My goals in developing RinohType are mostly inspired by (La)TeX's shortcomings and common sense:

- RinohType should have a simple, transparent design and depend on as few external libraries as possible. This helps to keep installation and usage simple.
- It should be easy to define custom document layouts and visual styles.
- RinohType should accept Unicode input (only!).
- There should be built-in support for images and floats.
- It should be able to perform high-quality typesetting, supporting kerning, ligatures and hyphenation at the least.
- It should be able to typeset complex mathematical formulae.
- It should support modern font technologies (OpenType) and output to PDF.
- Naturally, it should support obvious features such as cross-references, page numbering, footnotes, table of contents and index generation.

Current Status
==============

Because of the Unicode requirement, I opted to skip Python 2 and go with Python 3 which uses Unicode for all text strings. This avoids all problems associated with input encoding and simplifies text handling internally.

At the time of writing, RinohType implements:

- A simple, but powerful page layout engine, allowing for page headers/footers, columns and floats.
- Typesetting is already quite capable, supporting hyphenation, sub/superscripts, kerning, ligatures, text justification (left, right, justified) and alignment to tab stops.
- A hierarchical styles system, for both paragraphs and other objects such as figures and tables.
- Nestable inline text styling.
- Support for Type1, TrueType and OpenType (both the TrueType and CFF/Postscript/Type1 variants) fonts.
- A simple PDF backend. Other backends can be easily added.
- Numbered, unnumbered and definition lists.
- Figures (input as PDF files) and basic tables (with row/column spanning), with automatically numbered captions.
- Cross-references, automatic page numbering and footnotes.
- Automatically generated table of contents.
- With the help of `citeproc-py`_, support for citing references from a BibTeX database and generating a bibliography.

The one major omission from this list is formula rendering. I did try using the TeX formula renderer from matplotlib (the ``mathtext`` module) and `SVGMath <http://sourceforge.net/projects/svgmath/>`_, but with unsatisfactory results. I've decided to write math rendering from scratch once the core of RinohType (everything listed above) is working properly.

Example Documents and Input Formats
===================================

After abandoning the idea to use Python source files as the input format, I opted to go with XML, since it's a very common format and, more importantly, allows for validation using XML schemas. The `RFIC example <https://github.com/brechtm/rinohtype/tree/master/examples/rfic2009>`_ in the RinohType repository makes use of a custom XML input format, as defined in ``rfic.rnc`` (`RELAX NG Compact <http://relaxng.org/compact-tutorial-20030326.html>`_). This example shows off most of RinoType's capabilities. Download the `generated PDF </files/intro_template.pdf>`_ to see the output.

Guided by the RFIC example, it should be fairly straightforward (but still a lot of work) to write a DocBook frontend for RinohType. XML is also a great intermediate format, useful when to-XML converters for other input formats are available.

XML is unfortunately not the best format for hand editing. One of the advantages of TeX source files is that they are easy to write and read (the content parts anyway). Luckily, Python's "native"
`reStructuredText <http://docutils.sourceforge.net/rst.html>`_ is a great markup syntax that is easy to write and read. Additionally, it is extensible, which makes it pretty much the perfect input format for RinohType (I haven't thought about how to verify rST input yet, though). The `rST example <https://github.com/brechtm/rinohtype/tree/master/examples/restructuredtext>`_ attempts to typeset the `ReStructuredText Primer <http://docutils.sourceforge.net/docs/user/rst/quickstart.html>`_. Here is the `output </files/intro_rst.pdf>`_. The rST parser contained in ``rst.py`` will eventually be moved into the core of RinohType as a frontend.


Evaluation
==========

Unsurprisingly, even after four years into its development, RinohType still does not provide an option for absolute figure placement, the missing LaTeX feature that started this journey. Of course, a lot of other things needed to be put in place before this could be addressed. While I could implement this feature at this point, there are more pressing things to address.

I'm pretty happy with the result so far and I'm especially proud of the simplicity and compactness of the code. The ``rinoh`` Python package counts less than 6500 lines of code (excluding comments/docstrings and empty lines). This includes both the PDF backend (1700 lines) and the font parsers (1750 lines), so the core of RinohType comprises only about 3000 lines of code! I think this is in a large part made possible due to the expressive power of Python. Though the fact that I was constantly refactoring must have also been an important factor.

One aspect that I'm not so enthusiastic about is RinohType's performance. On my modest `Celeron T3000 1.8 GHz <http://ark.intel.com/products/40738/Intel-Celeron-Processor-T3000-1M-Cache-1_80-GHz-800-MHz-FSB>`_ laptop, the average rendering time for a page in the RFIC example is a disappointing 0.8 seconds. For small documents, this is unlikely to be a problem, but for books it's problematic. RinohType should become *at least* a factor of ten faster. I've already introduced some optimizations such as `memoization <http://stackoverflow.com/questions/1988804/what-is-memoization-and-how-can-i-use-it-in-python>`_ and using generators instead of lists, but it is clearly not cutting it. Looking for an easy solution, I've done some quick tests with PyPy3k (rendering the RFIC example over and over in a loop), but these were rather disappointing; rendering speed was about five times *slower* compared to CPython. With Cython, I'm not sure what part of the code to enhance with type declarations, as there is no obvious number crunching going on.


Planned Work
============

I first want to finish refactoring and documenting the remaining parts of the code. When this is done, performance tweaking will probably be near the top of my to-do list. Once the current functionality is more or less stable, I'd like to tackle maths typesetting. I'm secretly hoping Microsoft's mathematical OpenType layout extensions can help me get good results for at least a `small number of fonts <http://en.wikipedia.org/wiki/Category:Mathematical_OpenType_typefaces>`_ with minimal effort.

Some other features that I have been thinking of, in order of likeliness to actually make it into RinohType in the foreseeable future:

- Manual figure placement!
- Provide a number of standard document/page/font styles
- Fake small capitals for fonts that do not provide any
- Enhance the PDF backend with support for colors, hyperlinks, bookmarks, etc.
- Provide a RinohType output backend for `Sphinx <http://sphinx-doc.org>`_
- Include font definitions for freely available fonts (automatically downloaded when referenced)
- Advanced typesetting features such as Knuth-Plass line breaking and `microtypography <http://en.wikipedia.org/wiki/Microtypography>`_ as in PDFTeX (once performance is up to standards)
- DocBook frontend
- Support for non-Western languages; support RTL text and related OpenType extensions
- Non-rectangular paragraphs


For the Brave / Dependencies
============================

You can try out RinohType by cloning `the repository <https://github.com/brechtm/rinohtype>`_, adding the top-level directory to your ``PYTHON_PATH`` and running the examples.

For the RFIC example, you will need `citeproc-py <https://pypi.python.org/pypi/citeproc-py>`_. If you want to validate the XML input, you will also need `lxml <http://lxml.de>`_. For the reStructuredText example, you need `docutils <https://pypi.python.org/pypi/docutils>`_.

While it should be obvious how to adjust the text styles in the examples, it is not equally obvious how page layout is defined in the RFIC example. Also, an introduction on how the parsed input data (XML or rST) is processed might be useful if you want to define another XML input schema or extend the reStructuredText frontend. For this reason, I plan on following up on this article with a short tutorial covering these topics before I start writing official documentation.


The License
===========

While this originally started out as just another one of my programming projects, I am investigating the possibility to sell licenses for commercial use, as this could ensure that RinohType is actively developed in the future. I have therefor released RinohType under the Affero GPL.

The Affero GPL ensures that RinohType is free for use in open source projects. I am aware that the viral nature of the GPL makes it impossible for non-GPL projects to depend on RinohType, though. Unfortunately, it is this same viral nature that makes it possible to sell commercial-use licenses (a non-intentional side-effect of the copyleft?). Perhaps it is possible to employ a BSD-like license customized to prohibit commercial use? I have not yet found any examples of such a setup, but I will look into this.


Discussion
==========

See comments on `Hacker News <https://news.ycombinator.com/item?id=6668551>`_ and `Reddit <http://www.reddit.com/r/Python/comments/1pw20k/introducing_rinohtype_the_python_document/>`_.

