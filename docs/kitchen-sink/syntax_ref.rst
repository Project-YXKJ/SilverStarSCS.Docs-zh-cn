.. _syntax_ref:


================
Syntax Reference
================

reStructuredText
================

Explicit Markup
---------------


Hyperlink Targets
*****************

超链接目标可以是命名的或匿名的. 命名超链接目标由显式标记开始(".. "), 下划线, 
引用名称(无尾部下划线), 冒号, 空格和链接块组成:

.. code-block:: restructuredtext

  .. _hyperlink-name: link-block

匿名超链接目标由显式标记开始(".. "), 两个下划线, 一个冒号, 空格和一个链接块组成,
没有参考名称.

.. code-block:: restructuredtext

  .. __: anonymous-hyperlink-target-link-block

匿名超链接的替代语法由两个下划线, 一个空格和一个链接块组成：

.. code-block:: restructuredtext

  __ anonymous-hyperlink-target-link-block

超链接目标分为三种类型：内部、外部和间接。

1.内部

Clicking on this internal hyperlink will take us to the target_
below.

.. _target:

The hyperlink target above points to this paragraph.

2.外部

.. code-block:: restructuredtext

  See the Python_ home page for info.

  `Write to me`_ with your questions.

  .. _Python: https://www.python.org
  .. _Write to me: jdoe@example.com



2.间接

.. code-block:: restructuredtext

  .. _one: two_
  .. _two: three_
  .. _three:

List Table
----------

.. list-table:: Parameter list
  :widths: 4 5 5 10 70

  * - No.
    - Max
    - Min
    - Unit
    - Description
  * - O56
    - 4095
    - 0  
    - --
    - The maximum pedal input when position 2, value > O57 

Sphinx Design
=============

Dropdown
--------

.. dropdown:: < > Detail 
   :animate: fade-in-slide-down
   
   -Max  maximum
   -Min  minimum
   -Unit  unit
   -Description
     | The description can also start on the next line.
     | value1: text;
     | value2: text.


Grid
----
.. grid:: 1 2 3 4
  :margin: 4 4 0 0
  :gutter: 1

  .. grid-item-card:: 标题1
    :link: www.baidu.com
    :link-type: url
    
    内容1
  
  .. grid-item-card:: 标题2

    内容1
