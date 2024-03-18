.. _input_configuration:

========
输入配置
========

可配置的输入功能列表
====================

- 0 = 无功能；
- 1 = 手动倒缝；
- 2 = 正向补针；
- 3 = 反向补针；  
- 4 = 停车时正向补针，运转时手动倒缝；
- 5 = 停车时反向补针，运转时手动倒缝；
- 6 = 切换大小交互量；
- 7 = 快捷取消/打开前后加固；
- 8 = 切换针距；
- 9 = 切换面线张力；
- 10 = 进入/退出暂停模式 [#]_；
- 11 = 进入/退出穿线模式 [#]_；
- 12 = 切换缝线中心导向压脚抬起/落下；
- 13 = 机头倾倒状态传感器；
- 14 = 面线状态传感器；
- 15 = 护眼板状态传感器；
- 16 = 旋梭盖板状态传感器；
- 17 = 切换压脚抬起/落下 [#]_；
- 18 = 按键控制压脚；
- 19 = 润滑油量提醒传感器； 
- 20 = 切换送料滚轮抬起/落下；
- 21 = 重置底线计数器；
- 22 = 模拟电子手轮转动(向前)；
- 23 = 模拟电子手轮转动(向后)；
- 24 = 切换缝制方向 [#]_；
- 100 = 交互量限速挡位传感器；
- 101 = 压脚高度传感器；
- 102 = 电子手轮CHA；
- 103 = 电子手轮CHB。

.. [#] 暂停模式下，前踩调速器机器不运转。

.. [#] 穿线模式下，前踩调速器机器不运转，并且面线张力打开，以方便穿线。

.. [#] 代码17功能为按键按下抬起压脚，此时松开按键，压脚仍然抬起，再次按下按键则放下压脚；
       
       代码18功能为按键按下抬起压脚，此时按键松开则压脚放下。

.. [#] 代码1功能为按下按键由正缝切换为倒缝，此时松开按键则恢复为正缝；
       
       代码24功能为按下按键由正缝切换为倒缝，此时松开按键，仍然倒缝，再次按下按键则由倒缝切换为正缝。

.. important::
   超过100的功能需要配置在特殊的输入端口上，比如模拟输入。

**怎样设置一个输入端口的功能？**

按照以下步骤：

1. 确认你需要修改那一路端口，比如时输入端口1还是输入端口2，这部分需要参考具体产品的接线图，
   之后参考本章节 `参数列表`_ 部分，查找控制此端口功能的参数序号。
2. 参考本章节开头 `可配置的输入功能列表`_ 部分，得到你需要的功能代码。
3. 将步骤1得到的参数修改为步骤2得到的功能代码，之后重启控制器。
   
举例说明：

Step1：想把热键盒第六个按键的功能修改为拖布滚轮；

Step2：查询参数列表，可知控制热键盒第六个按键的功能的为 *A41*；

   A41: 热键盒按键6功能

Step3：查询可配置的输入功能列表，拖布滚轮的功能代码为 *20*；

   20 = 切换送料滚轮抬起/落下；

那么将A41修改为20即可。

参数列表
==============

A 04
----

.. dropdown:: 输入01功能 <...> 
   :animate: fade-in-slide-down
   
   -Max  199
   -Min  0
   -Unit  --
   -Description  定义输入01的功能。

A 05
----

.. dropdown:: 输入02功能 <...>
   :animate: fade-in-slide-down
   
   -Max  199
   -Min  0
   -Unit  --
   -Description  定义输入02的功能。

A 36
----

.. dropdown:: 热键盒按键1功能 <...> 
   :animate: fade-in-slide-down
   
   -Max  199
   -Min  0
   -Unit  --
   -Description  定义热键盒按键1的功能。

A 37
----

.. dropdown:: 热键盒按键2功能 <...>
   :animate: fade-in-slide-down
   
   -Max  199
   -Min  0
   -Unit  --
   -Description  定义热键盒按键2的功能。

A 38
----

.. dropdown:: 热键盒按键3功能 <...>
   :animate: fade-in-slide-down
   
   -Max  199
   -Min  0
   -Unit  --
   -Description  定义热键盒按键3的功能。

A 39
----

.. dropdown:: 热键盒按键4功能 <...>
   :animate: fade-in-slide-down
   
   -Max  199
   -Min  0
   -Unit  --
   -Description  定义热键盒按键4的功能。

A 40
----

.. dropdown:: 热键盒按键5功能 <...>
   :animate: fade-in-slide-down
   
   -Max  199
   -Min  0
   -Unit  --
   -Description  定义热键盒按键5的功能。

A 41
----

.. dropdown:: 热键盒按键6功能 <...>
   :animate: fade-in-slide-down
   
   -Max  199
   -Min  0
   -Unit  --
   -Description  定义热键盒按键6的功能。

A 68
----

.. dropdown:: 热键盒按键7功能 <...>
   :animate: fade-in-slide-down
   
   -Max  199
   -Min  0
   -Unit  --
   -Description  定义热键盒按键7的功能。

A 81
----

.. dropdown:: 输入03功能 <...>
   :animate: fade-in-slide-down
   
   -Max  199
   -Min  0
   -Unit  --
   -Description  定义输入03的功能。

A 82
----

.. dropdown:: 输入04功能 <...>
   :animate: fade-in-slide-down
   
   -Max  199
   -Min  0
   -Unit  --
   -Description  定义输入04的功能。

A 83
----

.. dropdown:: 输入05功能 <...>
   :animate: fade-in-slide-down
   
   -Max  199
   -Min  0
   -Unit  --
   -Description  定义输入05的功能。

A 84
----

.. dropdown:: 输入06功能 <...>
   :animate: fade-in-slide-down
   
   -Max  199
   -Min  0
   -Unit  --
   -Description  定义输入06的功能。

A 85
----

.. dropdown:: 输入07功能 <...> 
   :animate: fade-in-slide-down
   
   -Max  199
   -Min  0
   -Unit  --
   -Description  定义输入07的功能。

A 86
----

.. dropdown:: 输入08功能 <...>
   :animate: fade-in-slide-down
   
   -Max  199
   -Min  0
   -Unit  --
   -Description  定义输入08的功能。

A 87
----

.. dropdown:: 输入09功能 <...>
   :animate: fade-in-slide-down
   
   -Max  199
   -Min  0
   -Unit  --
   -Description  定义输入09的功能。

A 88
----

.. dropdown:: 输入10功能 <...>
   :animate: fade-in-slide-down
   
   -Max  199
   -Min  0
   -Unit  --
   -Description  定义输入10的功能。
