.. _output_configuration:

========
输出配置
========

可配置的输出功能列表
====================

  - 0 = 无功能；
  - 1 = 剪线；
  - 2 = 面线张力；
  - 3 = 夹线器；
  - 4 = 倒缝；
  - 5 = 压脚；
  - 6 = 交互量；
  - 7 = 额外的面线张力；
  - 8 = 扫线器；
  - 9 = 第二针距；
  - 10 = 机针冷却；
  - 11 = 额外剪线定刀(短线头机型)；
  - 12 = 缝线中心导向；
  - 13 = 零针距(短线头机型)；
  - 14 = 自动复位(双针机型)；
  
  .. _15:

  - 15 = 送料滚轮。

**怎样设置一个输入端口的功能？**:

按照以下步骤：

1. 确认你需要修改那一路端口，比如时输出端口1还是输出端口2，这部分需要参考具体产品的接线图，
   之后参考本章节 `参数列表`_ 部分，查找控制此端口功能的参数序号。
2. 参考本章节开头 `可配置的输出功能列表`_ 部分，得到你需要的功能代码。
3. 将步骤1得到的参数修改为步骤2得到的功能代码，之后重启控制器。

举例说明：

想把输出 **端口01** 的功能修改为拖布滚轮，查询得到 `A 71`_ 控制01路输出端口的功能，而拖布论滚的功能
代码为 15_ ，那么将A71修改为20即可。

参数列表
========

A 71
----

.. dropdown:: 输出01功能
   :animate: fade-in-slide-down
   
   -Max  maximum
   -Min  minimum
   -Unit  unit
   -Description  定义输出01的功能。

A 72
----

.. dropdown:: 输出02功能
   :animate: fade-in-slide-down
   
   -Max  maximum
   -Min  minimum
   -Unit  unit
   -Description  定义输出02的功能。

A 73
----

.. dropdown:: 输出03功能
   :animate: fade-in-slide-down
   
   -Max  maximum
   -Min  minimum
   -Unit  unit
   -Description  定义输出03的功能。

A 74
----

.. dropdown:: 输出04功能
   :animate: fade-in-slide-down
   
   -Max  maximum
   -Min  minimum
   -Unit  unit
   -Description  定义输出04的功能。

A 75
----

.. dropdown:: 输出05功能
   :animate: fade-in-slide-down
   
   -Max  maximum
   -Min  minimum
   -Unit  unit
   -Description  定义输出05的功能。


A 76
----

.. dropdown:: 输出06功能
   :animate: fade-in-slide-down
   
   -Max  maximum
   -Min  minimum
   -Unit  unit
   -Description  定义输出06的功能。

A 77
----

.. dropdown:: 输出07功能 
   :animate: fade-in-slide-down
   
   -Max  maximum
   -Min  minimum
   -Unit  unit
   -Description  定义输出07的功能。

A 78
----

.. dropdown:: 输出08功能
   :animate: fade-in-slide-down
   
   -Max  maximum
   -Min  minimum
   -Unit  unit
   -Description  定义输出08的功能。

A 79
----

.. dropdown:: 输出09功能 
   :animate: fade-in-slide-down
   
   -Max  maximum
   -Min  minimum
   -Unit  unit
   -Description  定义输出09的功能。

A 80
----

.. dropdown:: 输出10功能 
   :animate: fade-in-slide-down
   
   -Max  maximum
   -Min  minimum
   -Unit  unit
   -Description  定义输出10的功能。
