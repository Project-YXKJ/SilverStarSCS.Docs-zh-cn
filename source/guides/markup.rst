.. _markup:

=======================
reStructuredText markup
=======================

.. highlight::  rest

This document describes the custom reStructuredText markup introduced by Sphinx
to support SilverStar SCS Documentation and how it should be used.

.. seealso::

   The authoritative https://docutils.sourceforge.io/rst.html

   https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html


reStructuredText primer
=======================

This section is a brief introduction to reStructuredText (reST) concepts and
syntax, intended to provide authors with enough information to author documents
productively.  Since reST was designed to be a simple, unobtrusive markup
language, this will not take too long.

Use of whitespace
-----------------

All reST files use an indentation of 3 spaces; no tabs are allowed.  The
maximum line length is 80 characters for normal text, but tables, deeply
indented code samples and long links may extend beyond that.  Code example
bodies should use normal Python 4-space indentation.

Make use of multiple blank lines where applicable to clarify the structure of
the reST file.  Extra blank lines help group sections together to make the
organization of the file clearer.

A sentence-ending period may be followed by one or two spaces. While reST
ignores the second space, it is customarily put in by some users, for example
to aid Emacs' auto-fill mode.

Paragraphs
----------

The paragraph is the most basic block in a reST document.  Paragraphs are simply
chunks of text separated by one or more blank lines.  As in Python, indentation
is significant in reST, so all lines of the same paragraph must be left-aligned
to the same level of indentation.

.. _inline-markup:

Inline markup
-------------

The standard reST inline markup is quite simple: use

* one asterisk: ``*text*`` for emphasis (italics),
* two asterisks: ``**text**`` for strong emphasis (boldface), and
* backquotes: ````text```` for code samples, variables, and literals.

If asterisks or backquotes appear in running text and could be confused with
inline markup delimiters, they have to be escaped with a backslash.

Be aware of some restrictions of this markup:

* it may not be nested,
* content may not start or end with whitespace: ``* text*`` is wrong,
* it must be separated from surrounding text by non-word characters.  Use a
  backslash escaped space to work around that: ``thisis\ *one*\ word``.

.. tab:: reStructuredText

   .. code-block:: restructuredtext

      *text emphasis*
      **text strong emphasis**
      ``Hello World`` 
      thisis\ *one*\ word

.. tab:: Rendered 

   | *text emphasis*
   | **text strong emphasis**
   | ``Hello World`` 
   | thisis\ *one*\ word

reST also allows for custom "interpreted text roles", which signify that the
enclosed text should be interpreted in a specific way.  Sphinx uses this to
provide semantic markup and cross-referencing of identifiers, as described in
the appropriate section.  The general syntax is ``:rolename:`content```.

Lists and Quote-like blocks
---------------------------

List markup is natural: just place an asterisk at the start of a paragraph and
indent properly. The same goes for numbered lists; they can also be
automatically numbered using a ``#`` sign.

.. tab:: reStructuredText

   .. code-block:: reST

      * This is a bulleted list.
      * It has two items, the second

        item uses two lines.

      1. This is a numbered list.
      2. It has two items too.

      #. This is a numbered list.
      #. It has two items too.

.. tab:: Rendered

   * This is a bulleted list.
   * It has two items, the second

     item uses two lines.

   1. This is a numbered list.
   2. It has two items too.

   #. This is a numbered list.
   #. It has two items too.

Nested lists are possible, but be aware that they must be separated from the parent 
list items by blank lines:

.. tab:: reStructuredText

   .. code-block:: restructuredtext
      
      * this is
      * a list

         * with a nested list
         * and some subitems

      * and here the parent list continues

.. tab:: Rendered

   * this is
   * a list

      * with a nested list
      * and some subitems

   * and here the parent list continues

Definition lists are created as follows, Note that the term cannot have more 
than one line of text:

.. tab:: reStructuredText

   .. code-block:: restructuredtext

      term (up to a line of text)
         Definition of the term, which must be indented

         and can even consist of multiple paragraphs

      next term
         Description.

.. tab:: Rendered

   term (up to a line of text)
      Definition of the term, which must be indented

      and can even consist of multiple paragraphs

   next term
      Description.

Paragraphs are quoted by just indenting them more than the surrounding paragraphs:

Line blocks are a way of preserving line breaks. Line blocks are useful for 
address blocks, verse (poetry, song lyrics):

.. tab:: reStructuredText

   .. code-block:: restructuredtext

      | Do not go gentle into that good night,
      | Old age should burn and rave at close of day;
      | Rage, rage against the dying of the light.

.. tab:: Rendered

   | Do not go gentle into that good night,
   | Old age should burn and rave at close of day;
   | Rage, rage against the dying of the light.

Literal blocks
--------------

Literal code blocks are introduced by ending a paragraph with the special marker ``::``.
The literal block must be indented (and, like all paragraphs, separated from 
the surrounding ones by blank lines):

.. tab:: reStructuredText

   .. code-block:: restructuredtext

      This is a normal text paragraph. The next paragraph is a code sample::

         It is not processed in any way, except
         that the indentation is removed.

         It can span multiple lines.

      This is a normal text paragraph again.  

.. tab:: Rendered

   This is a normal text paragraph. The next paragraph is a code sample::

      It is not processed in any way, except
      that the indentation is removed.

      It can span multiple lines.

   This is a normal text paragraph again.  

The handling of the ``::`` marker is smart:

* If it occurs as a paragraph of its own, that paragraph is completely 
  left out of the document.
* If it is preceded by whitespace, the marker is removed.
* If it is preceded by non-whitespace, the marker is replaced by a single colon.

That way, the second sentence in the above example’s first paragraph would be 
rendered as "The next paragraph is a code sample:".

Tables
------
For grid tables, you have to “paint” the cell grid yourself. They look like this::

   +------------------------+------------+----------+----------+
   | Header row, column 1   | Header 2   | Header 3 | Header 4 |
   | (header rows optional) |            |          |          |
   +========================+============+==========+==========+
   | body row 1, column 1   | column 2   | column 3 | column 4 |
   +------------------------+------------+----------+----------+
   | body row 2             | ...        | ...      |          |
   +------------------------+------------+----------+----------+

Simple tables are easier to write, but limited: they must contain more than one row, 
and the first column cells cannot contain multiple lines. They look like this::

   =====  =====  =======
   A      B      A and B
   =====  =====  =======
   False  False  False
   True   False  False
   False  True   False
   True   True   True
   =====  =====  =======

Two more syntaxes are supported: CSV tables and List tables. They use an explicit
markup block. Refer to `Tables`_ for more information.

.. _Tables: https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#table-directives

Hyperlinks
----------

External links
^^^^^^^^^^^^^^

Use ```Link text <http://target>`_`` for inline web links.  If the link text
should be the web address, you don't need special markup at all, the parser
finds links and mail addresses in ordinary text.

.. Important::

   There must be a space between the link text and the opening < for the URL.

You can also separate the link and the target definition, like this:

.. tab:: reStructuredText

   .. code-block:: restructuredtext

      This is a paragraph that contains `a link`_.

      .. _a link: https://domain.invalid/

.. tab:: Rendered

   This is a paragraph that contains `a link`_.

   .. _a link: https://domain.invalid/


Internal links
^^^^^^^^^^^^^^

Internal linking is done via a special reST role, see the section on specific
markup, :ref:`doc-ref-role`.

Sections
--------

Section headers are created by underlining (and optionally overlining) the
section title with a punctuation character, at least as long as the text::

   =================
   This is a heading
   =================

Normally, there are no heading levels assigned to certain characters as the
structure is determined from the succession of headings.  However, for the
Python documentation, here is a suggested convention:

* ``#`` with overline, for parts
* ``*`` with overline, for chapters
* ``=``, for sections
* ``-``, for subsections
* ``^``, for subsubsections
* ``"``, for paragraphs

Field Lists
-----------

Roles
-----

A role or "custom interpreted text role" (:ref:`ref <roles>`) is an inline
piece of explicit markup. It signifies that the enclosed text should be
interpreted in a specific way.  Sphinx uses this to provide semantic markup and
cross-referencing of identifiers, as described in the appropriate section.  The
general syntax is ``:rolename:`content```.

Docutils supports the following roles:

* ``emphasis`` -- equivalent of ``*emphasis*``
* ``strong`` -- equivalent of ``**strong**``
* ``literal`` -- equivalent of ````literal````
* ``subscript`` -- subscript text
* ``superscript`` -- superscript text
* ``title-reference`` -- for titles of books, periodicals, and other
  materials

Refer to :ref:`roles` for roles added by Sphinx.

Explicit markup
---------------

"Explicit markup" is used in reST for most constructs that need special
handling, such as footnotes, specially-highlighted paragraphs, comments, and
generic directives.

An explicit markup block begins with a line starting with ``..`` followed by
whitespace and is terminated by the next paragraph at the same level of
indentation.  (There needs to be a blank line between explicit markup and normal
paragraphs.  This may all sound a bit complicated, but it is intuitive enough
when you write it.)

.. _primer-directives:

Directives
----------

Docutils supports the following directives:

* Admonitions: attention, caution, danger, error, hint, important, note,
  tip, warning and the generic admonition.
* Images: image, figure.
* Special tables: table, csv-table, list-table.

Admonitions:

.. tab:: reStructuredText
   
   .. code-block:: restructuredtext

      .. attention::
         attention

      .. caution::
         caution

      .. danger::
         danger

      .. error::
         error

      .. Hint::
         Hint

      .. important::
         important

      .. note::
         note

      .. seealso::
         seealso

      .. tip::
         tip
         
      .. todo::
         todo

      .. warning::
         warning

.. tab:: Rendered

   .. attention::
      attention

   .. caution::
      caution

   .. danger::
      danger

   .. error::
      error

   .. Hint::
      Hint

   .. important::
      important

   .. note::
      note

   .. seealso::
      seealso

   .. tip::
      tip
      
   .. todo::
      todo

   .. warning::
      warning
      
Directives added by Sphinx are described in :ref:`Directives <directives>`.

A directive is a generic block of explicit markup. Along with roles, it is one of
the extension mechanisms of reST, and Sphinx makes heavy use of it.

Basically, a directive consists of a name, arguments, options and content. (Keep
this terminology in mind, it is used in the next chapter describing custom
directives.)  

::

   .. name:: argument
      :options name: options value
      
      content

Looking at this example::

   .. function:: foo(x)
                 foo(y, z)
      :module: some.module.name

      Return a line of text input from the user.  
 

``function`` is the directive name.  It is given two arguments here, the
remainder of the first line and the second line, as well as one option ``module``
(as you can see, options are given in the lines immediately following the
arguments and indicated by the colons).

The directive content follows after a blank line and is indented relative to the
directive start or if options are present, by the same amount as the options.

Be careful as the indent is not a fixed number of whitespace, e.g. three, 
but any number whitespace. 

Images
------

reST supports an image directive, used like so::

   .. image:: gnu.png
      (options)

When used within Sphinx, the file name given (here gnu.png) must either be relative 
to the source file, or absolute which means that they are relative to the top source 
directory. For example, the file sketch/spam.rst could refer to the image``images/spam.png``
as ``../images/spam.png`` or ``/images/spam.png``。

Footnotes
---------

For footnotes, use ``[#]_`` to mark the footnote location, and add the footnote
body at the bottom of the document after a "Footnotes" rubric heading, like so:

.. tab:: reStructuredText

   .. code-block:: restructuredtext

      Lorem ipsum [#f1]_ dolor sit amet ... [#f2]_
  
      .. rubric:: Footnotes
  
      .. [#f1] Text of the first footnote.
      .. [#f2] Text of the second footnote.

.. tab:: Rendered 
   
   Lorem ipsum [#f1]_ dolor sit amet ... [#f2]_

   .. rubric:: Footnotes
   
   .. [#f1] Text of the first footnote.
   .. [#f2] Text of the second footnote.


Citations
---------

Standard reST citations are supported, with the additional feature that they are “global”,
i.e. all citations can be referenced from all files. Use them like so::

   Lorem ipsum [Ref]_ dolor sit amet.
   
   .. [Ref] Book or article reference, URL or whatever.

Citation usage is similar to footnote usage, but with a label that is not numeric or begins with ``#``.

Substitutions
-------------

reST supports "substitutions", which are pieces of text and/or markup referred to
in the text by ``|name|``. They are defined like footnotes with explicit markup blocks,
like this:

.. tab:: reStructuredText

   .. code-block:: reST

      .. |name| replace:: replacement *text*

      Substitutions: |name|    
  
.. tab:: Rendered 
   
   .. |name| replace:: replacement *text*

   Substitutions: |name|

If you want to use some substitutions for all documents, put them into `rst_prolog`_ or 
`rst_epilog`_ or put them into a separate file and include it into all documents you
want to use them in, using the include directive. (Be sure to give the include file
a file name extension differing from that of other source files, to avoid Sphinx 
finding it as a standalone document.)

.. _rst_prolog: https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-rst_prolog
.. _rst_epilog: https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-rst_epilog
.. _include: https://docutils.sourceforge.io/docs/ref/rst/directives.html#include

Comments
--------

Every explicit markup block (starting with :literal:`.. \ `) which isn't a
:ref:`valid markup construct <directives>` is regarded as a comment::

   .. This is a comment.

You can indent text after a comment start to form multiline comments::

   ..
      This whole indented block
      is a comment.

      Still in the comment.

Gotchas
-------

There are some problems one commonly runs into while authoring reST documents:

* **Separation of inline markup:** As said above, inline markup spans must be
  separated from the surrounding text by non-word characters, you have to use
  an escaped space to get around that.
* **No nested inline markup**: Something like ``*see :func:`foo`*`` is not possible.  

.. _roles:

Roles
=====

As :ref:`previously mentioned <inline-markup>`, Sphinx uses interpreted text 
roles to insert semantic markup into documents. 
They are written as ``:rolename:`content```.


Cross-referencing syntax
------------------------

Cross-references are generated by many semantic interpreted text roles.
Basically, you only need to write ``:role:`target```, and a link will be
created to the item named *target* of the type indicated by *role*.  The link's
text will be the same as *target*.

* You may supply an explicit title and reference target, like in reST direct
  hyperlinks: ``:role:`title <target>``` will refer to *target*, but the link
  text will be *title*.

* If you prefix the content with ``!``, no reference/hyperlink will be created.

* If you prefix the content with ``~``, the link text will only be the last
  component of the target.  For example, ``:py:meth:`~Queue.Queue.get``` will
  refer to ``Queue.Queue.get`` but only display ``get`` as the link text.  This
  does not work with all cross-reference roles, but is domain specific.

  In HTML output, the link's ``title`` attribute (that is e.g. shown as a
  tool-tip on mouse-hover) will always be the full target name.

.. _doc-ref-role:

Cross-referencing arbitrary locations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. describe:: ref

   To support cross-referencing to arbitrary sections in the documentation, the
   standard reST labels are "abused" a bit: Every label must precede a section
   title; and every label name must be unique throughout the entire documentation
   source.

   You can then reference to these sections using the ``:ref:`label-name``` role.

   Example::

      .. _my-reference-label:

      Section to cross-reference
      --------------------------

      This is the text of the section.

      It refers to the section itself, see :ref:`my-reference-label`.

   The ``:ref:`` invocation is replaced with the section title.

   Alternatively, you can reference any label (not just section titles)
   if you provide the link text ``:ref:`link text <reference-label>```.



Cross-referencing documents
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. describe:: doc

   Link to the specified document; the document name can be specified in
   absolute or relative fashion.  For example, if the reference
   ``:doc:`parrot``` occurs in the document ``sketches/index``, then the link
   refers to ``sketches/parrot``.  If the reference is ``:doc:`/people``` or
   ``:doc:`../people```, the link refers to ``people``.

   If no explicit link text is given (like usual: ``:doc:`Monty Python members
   </people>```), the link caption will be the title of the given document.

Referencing downloadable files
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. describe:: download

   This role lets you link to files within your source tree that are not reST 
   documents that can be viewed, but files that can be downloaded.

   When you use this role, the referenced file is automatically marked for 
   inclusion in the output when building (obviously, for HTML output only). 
   All downloadable files are put into a ``_downloads/<unique hash>/`` 
   subdirectory of the output directory; duplicate filenames are handled.

   An example::

      See :download:`this example script <../example.py>`.

   The given filename is usually relative to the directory the current source
   file is contained in, but if it absolute (starting with /), it is taken as 
   relative to the top source directory.

   The ``example.py`` file will be copied to the output directory, and a suitable
   link generated to it.

   Not to show unavailable download links, you should wrap whole paragraphs that 
   have this role::

      .. only:: builder_html

         See :download:`this example script <../example.py>`.

Cross-referencing figures by figure number
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. describe:: numref

   Link to the specified figures, tables, code-blocks and sections; the standard
   reST labels are used.  When you use this role, it will insert a reference to
   the figure with link text by its figure number like "Fig. 1.1".

   If an explicit link text is given (as usual: ``:numref:`Image of Sphinx (Fig.
   %s) <my-figure>```), the link caption will serve as title of the reference.
   As placeholders, ```%s`` and ``{number}`` get replaced by the figure
   number and ``{name}`` by the figure caption.
   If no explicit link text is given, the ``numfig_format`` setting is
   used as fall-back default.

   If ``numfig`` is ``False``, figures are not numbered,
   so this role inserts not a reference but the label or the link text.

Cross-referencing other items of interest
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following roles do possibly create a cross-reference, but do not refer to objects:

.. describe:: envvar

   An environment variable. Index entries are generated. Also generates a link to
   the matching ``envvar`` directive, if it exists.

.. describe:: keyword

   The name of a Python keyword.  Using this role will generate a link to the
   documentation of the keyword.  ``True``, ``False`` and ``None`` do not use
   this role, but simple code markup (````True````), given that they're
   fundamental to the language and should be known to any programmer.

.. describe:: option

   A command-line option to an executable program. This generates a link to a 
   ``option`` directive, if it exists.

.. describe:: token
   
   The name of a grammar token (used in the reference manual to create links
   between production displays).

The following role creates a cross-reference to the term in the glossary:

.. describe:: term

   Reference to a term in the glossary.  The glossary is created using the
   ``glossary`` directive containing a definition list with terms and
   definitions.  It does not have to be in the same file as the ``term``
   markup, in fact, by default the Python docs have one global glossary
   in the ``glossary.rst`` file.

   If you use a term that's not explained in a glossary, you'll get a warning
   during build.


Inline code highlighting
------------------------

.. describe:: code

   An inline code example. When used directly, this role just displays the text 
   without syntax highlighting, as a literal.

   .. tab:: reStructuredText

      .. code-block:: restructuredtext

         By default, inline code such as :code:`1 + 2` just displays without highlighting.

   .. tab:: Rendered 
   
      By default, inline code such as :code:`1 + 2` just displays without highlighting.

   Unlike the code-block directive, this role does not respect the default language set
   by the highlight directive.
   
   To enable syntax highlighting, you must first use the Docutils role directive to define
   a custom role associated with a specific language:

   .. tab:: reStructuredText

      .. code-block:: restructuredtext

         .. role:: python(code)
            :language: python
         
         In Python, :python:`1 + 2` is equal to :python:`3`.

   .. tab:: Rendered
      
      .. role:: python(code)
         :language: python
      
      In Python, :python:`1 + 2` is equal to :python:`3`. 

   To display a multi-line code example, use the code-block directive instead.


Math
----

.. describe:: math

   Role for inline math. Use like this:

   .. tab:: reStructuredText

      .. code-block:: restructuredtext

         Since Pythagoras, we know that: :math:`a^2 + b^2 = c^2`

   .. tab:: Rendered

      Since Pythagoras, we know that: :math:`a^2 + b^2 = c^2`

Other semantic markup
---------------------

The following roles don't do anything special except formatting the text
in a different style:

.. describe:: abbr

   An abbreviation. If the role content contains a parenthesized explanation,
   it will be treated specially: it will be shown in a tool-tip in HTML, 
   and output only once in LaTeX.

   .. tab:: reStructuredText

      .. code-block:: restructuredtext

         For example: :abbr:`LIFO (last-in, first-out)`

   .. tab:: Rendered

      For example: :abbr:`LIFO (last-in, first-out)`

.. describe:: command

   The name of an OS-level command, such as ``rm``.

   .. tab:: reStructuredText

      .. code-block:: restructuredtext

         For example: :command:`rm`

   .. tab:: Rendered

      For example: :command:`rm`

.. describe:: dfn

   Mark the defining instance of a term in the text.  (No index entries are
   generated.)

   .. tab:: reStructuredText

      .. code-block:: restructuredtext

         For example: :dfn:`binary mode`

   .. tab:: Rendered

      For example: :dfn:`binary mode`

.. describe:: file

   The name of a file or directory.  Within the contents, you can use curly
   braces to indicate a "variable" part:

   .. tab:: reStructuredText

      .. code-block:: restructuredtext

         for example: ... is installed in :file:`/usr/lib/python3.{x}/site-packages`

   .. tab:: Rendered

      for example: ... is installed in :file:`/usr/lib/python3.{x}/site-packages`
   
   In the built documentation, the ``x`` will be displayed differently to
   indicate that it is to be replaced by the Python minor version.

.. describe:: makevar

   The name of a :command:`make` variable.

   .. tab:: reStructuredText

      .. code-block:: restructuredtext

         For example: :makevar:`help`

   .. tab:: Rendered

      For example: :makevar:`help`

.. describe:: menuselection

   Menu selections should be marked using the ``menuselection`` role.  This is
   used to mark a complete sequence of menu selections, including selecting
   submenus and choosing a specific operation, or any subsequence of such a
   sequence.  The names of individual selections should be separated by
   ``-->``.

   .. tab:: reStructuredText

      .. code-block:: restructuredtext

         For example: :menuselection:`Start --> Programs`

   .. tab:: Display

      For example: :menuselection:`Start --> Programs`

.. describe:: regexp

   A regular expression. Quotes should not be included.

   .. tab:: reStructuredText

      .. code-block:: restructuredtext

         For example: :regexp:`([abc])+`

   .. tab:: Display

      For example: :regexp:`([abc])+`

Index-generating markup
-----------------------

Sphinx automatically creates index entries from all information units (like
functions, classes or attributes) like discussed before.

However, there is also an explicit directive available, to make the index more
comprehensive and enable index entries in documents where information is not
mainly contained in information units, such as the language reference.

The directive is ``index`` and contains one or more index entries.  Each entry
consists of a type and a value, separated by a colon.

For example::

   .. index::
      single: execution; context
      module: __main__
      module: sys
      triple: module; search; path

This directive contains five entries, which will be converted to entries in the
generated index which link to the exact location of the index statement (or, in
case of offline media, the corresponding page number).

The possible entry types are:

single
   Creates a single index entry.  Can be made a subentry by separating the
   subentry text with a semicolon (this notation is also used below to describe
   what entries are created).
pair
   ``pair: loop; statement`` is a shortcut that creates two index entries,
   namely ``loop; statement`` and ``statement; loop``.
triple
   Likewise, ``triple: module; search; path`` is a shortcut that creates three
   index entries, which are ``module; search path``, ``search; path, module``
   and ``path; module search``.
module, keyword, operator, object, exception, statement, builtin
   These all create two index entries.  For example, ``module: hashlib``
   creates the entries ``module; hashlib`` and ``hashlib; module``.  The
   builtin entry type is slightly different in that "built-in function" is used
   in place of "builtin" when creating the two entries.

For index directives containing only "single" entries, there is a shorthand
notation::

   .. index:: BNF, grammar, syntax, notation

This creates four index entries.

Substitutions
-------------

The documentation system provides three substitutions that are defined by
default. They are set in the build configuration file :file:`conf.py`.

.. describe:: |release|

   Replaced by the Python release the documentation refers to.  This is the full
   version string including alpha/beta/release candidate tags, e.g. ``2.5.2b3``.

.. describe:: |version|

   Replaced by the Python version the documentation refers to. This consists
   only of the major and minor version parts, e.g. ``2.5``, even for version
   2.5.1.

.. describe:: |today|

   Replaced by either today's date, or the date set in the build configuration
   file.  Normally has the format ``April 14, 2007``.

.. _directives:

Directives
==========

:ref:`As previously discussed <primer-directives>`, a directive is a generic block
of explicit markup. While Docutils provides a number of directives, Sphinx
provides many more and uses directives as one of the primary extension
mechanisms.

See `Domains`_ for roles added by domains.

.. _Domains: https://www.sphinx-doc.org/en/master/usage/domains/index.html

Table-of-contents markup
------------------------

Since reST does not have facilities to interconnect several documents, or split
documents into multiple output files, Sphinx uses a custom directive to add
relations between the single files the documentation is made of, as well as
tables of contents.  The ``toctree`` directive is the central element.

.. describe:: toctree

   This directive inserts a "TOC tree" at the current location, using the
   individual TOCs (including "sub-TOC trees") of the files given in the
   directive body.  A numeric ``maxdepth`` option may be given to indicate the
   depth of the tree; by default, all levels are included.

   Consider this example (taken from the library reference index)::

      .. toctree::
         :maxdepth: 2

         intro
         strings
         datatypes
         numeric
         (many more files listed here)

   This accomplishes two things:

   * Tables of contents from all those files are inserted, with a maximum depth
     of two, that means one nested heading.  ``toctree`` directives in those
     files are also taken into account.
   * Sphinx knows that the relative order of the files ``intro``,
     ``strings`` and so forth, and it knows that they are children of the
     shown file, the library index.  From this information it generates "next
     chapter", "previous chapter" and "parent chapter" links.

   In the end, all files included in the build process must occur in one
   ``toctree`` directive; Sphinx will emit a warning if it finds a file that is
   not included, because that means that this file will not be reachable through
   standard navigation.

   The special file ``contents.rst`` at the root of the source directory is the
   "root" of the TOC tree hierarchy; from it the "Contents" page is generated.

Paragraph-level markup
----------------------

These directives create short paragraphs and can be used inside information
units as well as normal text:

.. describe:: note

   An especially important bit of information about an API that a user should be
   aware of when using whatever bit of API the note pertains to.  The content of
   the directive should be written in complete sentences and include all
   appropriate punctuation.

   Example::

      .. note::

         This function is not suitable for sending spam e-mails.

.. describe:: warning

   An important bit of information about an API that a user should be aware of
   when using whatever bit of API the warning pertains to.  The content of the
   directive should be written in complete sentences and include all appropriate
   punctuation.  In the interest of not scaring users away from pages filled
   with warnings, this directive should only be chosen over ``note`` for
   information regarding the possibility of crashes, data loss, or security
   implications.

.. describe:: versionadded

   This directive documents the version of the project which added the described
   feature to the library or C API. When this applies to an entire module, it
   should be placed at the top of the module section before any prose.

   The first argument must be given and is the version in question; you can add
   a second argument consisting of a *brief* explanation of the change.

   Example::

      .. function:: func()

         Return foo and bar.

         .. versionadded:: 3.5
   
   Note that there must be no blank line between the directive head and the
   explanation; this is to make these blocks visually continuous in the markup.

.. describe:: versionchanged

   Similar to ``versionadded``, but describes when and what changed in the named
   feature in some way (new parameters, changed side effects, platform support,
   etc.).  This one *must* have the second argument (explanation of the change).

   Example::

      .. function:: func(spam=False)

         Return foo and bar, optionally with *spam* applied.

         .. versionchanged:: 3.6
            Added the *spam* parameter.

   Note that there should be no blank line between the directive head and the
   explanation; this is to make these blocks visually continuous in the markup.

.. describe:: deprecated

   Indicates the version from which the described feature is deprecated.

   There is one required argument: the version from which the feature is
   deprecated.

   Example::

      .. deprecated:: 3.8

.. describe:: deprecated-removed

   Like ``deprecated``, but it also indicates in which version the feature is
   removed.

   There are two required arguments: the version from which the feature is
   deprecated, and the version in which the feature is removed.

   Example::

      .. deprecated-removed:: 3.8 4.0

.. describe:: impl-detail

   This directive is used to mark CPython-specific information.  Use either with
   a block content or a single sentence as an argument, i.e. either ::

      .. impl-detail::

         This describes some implementation detail.

         More explanation.

   or ::

      .. impl-detail:: This shortly mentions an implementation detail.

   "\ **CPython implementation detail:**\ " is automatically prepended to the
   content.

.. describe:: seealso

   Many sections include a list of references to module documentation or
   external documents.  These lists are created using the ``seealso`` directive.

   The ``seealso`` directive is typically placed in a section just before any
   sub-sections.  For the HTML output, it is shown boxed off from the main flow
   of the text.

   The content of the ``seealso`` directive should be a reST definition list.
   Example::

      .. seealso::

         Module :mod:`zipfile`
            Documentation of the :mod:`zipfile` standard module.

         `GNU tar manual, Basic Tar Format <http://link>`_
            Documentation for tar archive files, including GNU tar extensions.

.. describe:: rubric

   This directive creates a paragraph heading that is not used to create a
   table of contents node.  It is currently used for the "Footnotes" caption.

.. describe:: centered

   This directive creates a centered boldfaced paragraph.  Use it as follows::

      .. centered::

         Paragraph contents.

Showing code examples
---------------------

Examples of Python source code or interactive sessions are represented using
standard reST literal blocks.  They are started by a ``::`` at the end of the
preceding paragraph and delimited by indentation.

Representing an interactive session requires including the prompts and output
along with the Python code.  No special markup is required for interactive
sessions. After the last line of input or output is presented, there should
be no trailing prompt. An example of correct usage is:


.. code-block:: python

   >>> 1 + 1
   2

Syntax highlighting is handled in a smart way:

* There is a "highlighting language" for each source file.  By default,
  this is ``'python'`` as the majority of files will have to highlight Python
  snippets.

* Within Python highlighting mode, interactive sessions are recognized
  automatically and highlighted appropriately.

* The highlighting language can be changed using the ``highlight``
  directive, used as follows::

     .. highlight:: c

  This language is used until the next ``highlight`` directive is
  encountered.

* The ``code-block`` directive can be used to specify the highlight language
  of a single code block, e.g.::

     .. code-block:: c

        #include <stdio.h>

        void main() {
            printf("Hello world!\n");
        }

* The values normally used for the highlighting language are:

  * ``python`` (the default)
  * ``c``
  * ``rest``
  * ``none`` (no highlighting)

* If highlighting with the current language fails, the block is not highlighted
  in any way.

Longer displays of verbatim text may be included by storing the example text in
an external file containing only plain text.  The file may be included using the
``literalinclude`` directive. For example, to include the Python source
file :file:`example.py`, use::
   
   .. literalinclude:: example.py

The file name is relative to the current file's path.  Documentation-specific
include files should be placed in the ``Doc/includes`` subdirectory.

Glossary
--------

.. describe:: glossary

   This directive must contain a reST definition-list-like markup with terms and
   definitions.  The definitions will then be referenceable with the``term`` role.
   Example::
      
      .. glossary::

         environment
            A structure where information about all documents under the root is
            saved, and used for cross-referencing.  The environment is pickled
            after the parsing stage, so that successive runs only need to read
            and parse new and changed documents.

         source directory
            The directory which, including its subdirectories, contains all
            source files for one Sphinx project.


Meta-information markup
-----------------------

.. describe:: sectionauthor

   Identifies the author of the current section.  The argument should include
   the author's name such that it can be used for presentation (though it isn't)
   and email address.  The domain name portion of the address should be lower
   case.  Example::

      .. sectionauthor:: Guido van Rossum <guido@python.org>

   Currently, this markup isn't reflected in the output in any way, but it helps
   keep track of contributions.

Math
----

The input language for mathematics is LaTeX markup.  This is the de-facto
standard for plain-text math notation and has the added advantage that no
further translation is necessary when building LaTeX output.

.. describe:: math

   Directive for displayed math (math that takes the whole line for itself).

   The directive supports multiple equations, which should be separated by a
   blank line:

   .. tab:: reStructuredText
      
      .. code-block:: restructuredtext

         .. math::

            (a + b)^2 = a^2 + 2ab + b^2

            (a - b)^2 = a^2 - 2ab + b^2

   .. tab:: Rendered

      .. math::

         (a + b)^2 = a^2 + 2ab + b^2

         (a - b)^2 = a^2 - 2ab + b^2

   In addition, each single equation is set within a ``split`` environment,
   which means that you can have multiple aligned lines in an equation,
   aligned at ``&`` and separated by ``\\``:
   
   .. tab:: reStructuredText
      
      .. code-block:: restructuredtext
   
         .. math::

            (a + b)^2  &=  (a + b)(a + b) \\
                       &=  a^2 + 2ab + b^2
   
   .. tab:: Rendered

      .. math::

         (a + b)^2  &=  (a + b)(a + b) \\
                     &=  a^2 + 2ab + b^2

   For more details, look into the documentation of the `AmSMath LaTeX
   package`_.

   When the math is only one line of text, it can also be given as a directive
   argument::

      .. math:: (a + b)^2 = a^2 + 2ab + b^2

   Normally, equations are not numbered.  If you want your equation to get a
   number, use the ``label`` option.  When given, it selects an internal label
   for the equation, by which it can be cross-referenced, and causes an equation
   number to be issued.  See role ``eq`` for an example.  The numbering
   style depends on the output format.

   There is also an option ``nowrap`` that prevents any wrapping of the given
   math in a math environment.  When you give this option, you must make sure
   yourself that the math is properly set up.  For example:
   
   .. tab:: reStructuredText
      
      .. code-block:: restructuredtext
         
         .. math::
            :nowrap:

            \begin{eqnarray}
               y    & = & ax^2 + bx + c \\
               f(x) & = & x^2 + 2xy + y^2
            \end{eqnarray}
   
   .. tab:: Rendered

      .. math::
         :nowrap:

         \begin{eqnarray}
            y    & = & ax^2 + bx + c \\
            f(x) & = & x^2 + 2xy + y^2
         \end{eqnarray}

.. _AmSMath LaTeX package: https://www.ams.org/publications/authors/tex/amslatex
