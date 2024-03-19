.. |SS-SCS-Docs| replace:: 银星SCS文档

================
参与文档贡献
================

本项目 |SS-SCS-Docs| 欢迎贡献！有许多方法可以帮助改进，包括:

* 阅读并提供反馈
* 审查新贡献
* 修改现有内容
* 编写新内容
* 翻译

文档类型
===================

该项目由四种不同的文档类型组成，每个文档类型具有特定的目的。
该项目致力于遵循 `Diátaxis process`_ 用于创建高质量的文档。
当新建文档时，请选择适当的文档类型。

.. _Diátaxis process: https://diataxis.fr/

教程
---------

教程的重点是通过完成一个目标来向读者传授新概念目标。它们是一步接一步的指南。
它们不包括无关的警告或信息。

指南
------

指南专注于完成特定任务，或者承担一定程度的前提知识教学。这些与教程类似，
但是内容聚焦且明确重点，并可以提供大量注意事项和附加信息，如果这些是需要的。
指南也还可以讨论完成任务的多种方法。

说明
------------

说明专注于理解和提供信息，他们针对某一个特定话题讨论或者说明，无需事前预设一个阅读目标。

规格
--------------

规范是参考文档，专注于全面记录产品的接口。

翻译
============

*TODO*

我们使用 `Weblate`_ 来管理本项目的多语种翻译。
请访问Weblate上的项目地址来贡献 `packaging.python.org`_。

.. tip::

   项目的所有翻译必须遵循 `reStructuredText语法 <reStructuredText syntax_>`_.

.. _Weblate: https://weblate.org/
.. _packaging.python.org: https://hosted.weblate.org/projects/
.. _reStructuredText syntax: https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html

增加语言
-----------------

If your language is not listed on `packaging.python.org`_, click the button
:guilabel:`Start new translation` at the bottom of the language list and add
the language you want to translate.

遵循reStructuredText语法
---------------------------------

如果您不熟悉reStructuredText(RST)语法，请在翻译工作开始之前阅读 `this guide`_

**不要直接翻译引用中的文字**

  当翻译一个引用中的文本时，不要直接翻译。

  | Wrong: Translate the following text directly:

  .. code-block:: rst

      `some ref`_ -> `TRANSLATED TEXT HERE`_

  | Right: Translate the following text with your own language and add the original reference:

  .. code-block:: rst

      `some ref`_ -> `TRANSLATED TEXT HERE <some ref_>`_

.. _this guide: https://docutils.sourceforge.io/docs/user/rst/quickref.html

本地构建本项目
==============

虽然并不强制贡献，但在本地构建这本书可能会很有用，比如以测试您的更改。为了在本地构建这本书，
您将需要：

1. :doc:`Nox <nox:index>`. 您可以通过 ``pip`` 安装和更新nox:

   .. code-block:: bash

      python -m pip install nox

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

风格指南
===========

读者
----

本指南的读者是所有使用 SilverStar SCS 产品的人。

特别要记住，并非所有使用 SilverStar SCS 的人都视自己为开发人员。
本文档的受众包括操作人员、维护人员、以及专业人士。

写作语气
--------------

撰写本指南时，力求以平易近人且谦逊的语气进行写作谦虚，即使你知道所有的答案。

想象一下，您正在与一个您认识的聪明且技术精湛的人一起开展一个项目。
你喜欢和他们一起工作，他们也喜欢和你一起工作。那个人问了你一个问题，
而你知道答案。你如何回应？ *这* 就是您编写本指南的方式。

撰写文档时，根据话题的严肃性和难度调整语气。如果你正在写一个介绍性教程，
开个玩笑是可以的，但如果您要说明的是产品的敏感规格，您可能需要完全避免开玩笑。

惯例和机制
-------------------------

**写给读者**
  在提供建议或采取的步骤时，请称呼读者为*您*或使用请求语气。

  | 错误：要安装它，用户运行...
  | 正确：您可以通过运行...来安装它
  | 正确：要安装它，请运行...

**陈述假设**
  避免未说明的假设。在网络上阅读这个文档，意味着任何页面可能是读者读到的第一页。
  如果您要做出假设，请说明您的假设是什么。

**慷慨地交叉引用**
  第一次提到一个工具或概念时，请链接到该工具或概念在文档其他部分中的解释，或链接到其他相关文档。
  节省读者的再次搜索。

**尊重命名习惯**
  在命名工具、站点、人员和其他专有名词时，使用他们管用的大写。

  | 错误: Pip使用…
  | 正确: pip使用…
  |
  | 错误: …部署在github.
  | 正确: …部署在GitHub.

**标题**
  使用读者正在搜索的单词编写标题。一个好方法是让问题本身成为你的标题。
  例如，一个读者可能想知道*如何安装库文件*，那么*如何安装库文件*就是一个好标题。

  在章节标题中，使用大小写。换句话说，像写句子一样写标题。

  | 错误: Things You Should Know About Python
  | 正确: Things you should know about Python

**数字**
  在正文中，使用小写中文数字。对于其他数字或表中的数字，请使用阿拉伯数字。

.. _contributors:

致谢
====

感谢对此工作做出贡献的人们：

* Zhang XiaoLei `snowzxl <https://github.com/snowzxl>`_
* Xia Tian `xiatian-xjtu <https://github.com/xiatian-xjtu>`_
* Zhang YuPeng `yupeng-zhang <https://github.com/yupeng-zhang>`_
