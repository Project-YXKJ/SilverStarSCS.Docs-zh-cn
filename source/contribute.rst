
.. |SS-SCS-Docs| replace:: 银星SCS文档

================
为本项目做出贡献
================

本项目 |SS-SCS-Docs| 欢迎贡献！有许多方法可以帮助改进，包括:

* 阅读并提供反馈
* 审查新贡献
* 修改现有内容
* 编写新内容
* 翻译

翻译
====

新增语言
--------

本地构建本项目
==============

虽然并不强制贡献，但在本地构建这本书可能会很有用，比如以测试您的更改。为了在本地构建这本书，
您将需要：

1. :doc:`Nox <nox:index>`. 您可以通过 ``pip`` 安装和更新nox:

   .. code-block:: bash

      python -m pip install --user nox

2. Python 3.11. 我们的构建脚本通常仅使用Python 3.11进行测试，从这里下载 `Python 3.11`_ 
   并将其安装在您的操作系统上。

.. _Python 3.11: https://www.python.org/downloads/

要构建本书，请在项目的根文件夹中运行以下 shell 命令：

.. code-block:: bash

   nox -s build

该过程完成后，您可以在 ``./build/html``找到HTML输出，之后您可以使用网络浏览器打开 ``index.html`` 浏览本书，
不过更建议部署在 HTTP 服务器。

您可以使用以下命令构建这本书并部署在 HTTP 服务器：

.. code-block:: bash

   nox -s preview

可通过地址浏览 http://localhost:8000.

Style guide
===========

Voice and tone
--------------

When writing this guide, strive to write with a voice that's approachable and
humble, even if you have all the answers.

Imagine you're working on a Python project with someone you know to be smart and
skilled. You like working with them and they like working with you. That person
has asked you a question and you know the answer. How do you respond? *That* is
how you should write this guide.

Here's a quick check: try reading aloud to get a sense for your writing's voice
and tone. Does it sound like something you would say or does it sound like
you're acting out a part or giving a speech? Feel free to use contractions and
don't worry about sticking to fussy grammar rules. You are hereby granted
permission to end a sentence in a preposition, if that's what you want to end it
with.

When writing the guide, adjust your tone for the seriousness and difficulty of
the topic. If you're writing an introductory tutorial, it's OK to make a joke,
but if you're covering a sensitive security recommendation, you might want to
avoid jokes altogether.

Conventions and mechanics
-------------------------

**Write to the reader**
  When giving recommendations or steps to take, address the reader as *you*
  or use the imperative mood.

  | Wrong: To install it, the user runs…
  | Right: You can install it by running…
  | Right: To install it, run…

**State assumptions**
  Avoid making unstated assumptions. Reading on the web means that any page of
  the book may be the first page of the book that the reader ever sees.
  If you're going to make assumptions, then say what assumptions that you're
  going to make.

**Cross-reference generously**
  The first time you mention a tool or practice, link to the part of the
  guide that covers it, or link to a relevant document elsewhere. Save the
  reader a search.

**Respect naming practices**
  When naming tools, sites, people, and other proper nouns, use their preferred
  capitalization.

  | Wrong: Pip uses…
  | Right: pip uses…
  |
  | Wrong: …hosted on github.
  | Right: …hosted on GitHub.

**Use a gender-neutral style**
  Often, you'll address the reader directly with *you*, *your* and *yours*.
  Otherwise, use gender-neutral pronouns *they*, *their*, and *theirs* or avoid
  pronouns entirely.

  | Wrong: A maintainer uploads the file. Then he…
  | Right: A maintainer uploads the file. Then they…
  | Right: A maintainer uploads the file. Then the maintainer…

**Headings**
  Write headings that use words the reader is searching for. A good way to
  do this is to have your heading complete an implied question. For example, a
  reader might want to know *How do I install MyLibrary?* so a good heading
  might be *Install MyLibrary*.

  In section headings, use sentence case. In other words, write headings as you
  would write a typical sentence.

  | Wrong: Things You Should Know About Python
  | Right: Things you should know about Python

**Numbers**
  In body text, write numbers one through nine as words. For other numbers or
  numbers in tables, use numerals.

.. _contributors:

致谢
====

感谢对此工作做出贡献的人们：

* Zhang XiaoLei `snowzxl <https://github.com/snowzxl>`_
* Xia Tian `xiatian-xjtu <https://github.com/xiatian-xjtu>`_
* Zhang YuPeng `yupeng-zhang <https://github.com/yupeng-zhang>`_
