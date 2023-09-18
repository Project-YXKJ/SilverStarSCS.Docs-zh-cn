.. _seam:

====
线迹
====

**线缝段和程序**

*线缝段* 是组成程序的基本概念，通常来讲一个线缝段被分为三个部分：前加固、中间段、以及
后加固和剪线。

一个线缝段由首次踩踏调速器 :term:`POSITION 1` 位置开始，踩踏 :term:`POSITION -2` 
位置结束，也就是剪线作为结束标志。

*缝制程序* 是至少包含一个线缝段的线迹组合，我们可以称之线缝段-01，线缝段-02 ... 线缝段-n，
程序控制他们自动顺序执行，当最后一段线缝段-n执行后，程序结束，之后再次循环。


**定针缝**

定针缝是允许用户自由编程的缝纫程序，最多可以编制25段线缝段，每段最多99针。

缝纫程序的功能分为两个区域：作用于缝纫程序的全局功能以及作用于线缝段的局部功能。

*全局功能：*

- 软启动

*局部功能：*

- 线缝段针数
- 前后加固
- 夹线器
- 剪线
- 线缝段中途停止时机针位置
- 线缝段中途停止后自动抬压脚
- 线缝段结束后自动抬压脚

线缝段针数为0的线缝段被视为一个定针缝程序的结束标识，如果下一段针数为0则程序将重新返回第一段。

任意线缝段结束后，踩踏调速器 :term:`POSITION -2` 都将结束整个程序，如果此时没有执行过剪线则执行剪线
并返回第一段，已经执行过剪线则直接返回第一段。

**补针(针杆位置切换)**

If **A03** is equal to 0:

When press the key, the needle moves form the current position to the position 
set by parameter **D15** or **D16**, which one is the closest, the target position
is that one. E.g, current position is 40 degrees, **D15** is 70, **D16** is 200, 
when you press the button, the motion trace is "40->70->200->70->200...".

If **A03** is equal to 1:

when you press the button, two cases: if you set stop at upper position, 
the needle moves form the current position to the position set by parameter **D01**. 
if you set stop at lower position, the needle moves form the current position to the 
position set by parameter **D02**:


参数列表
========

S 05
----

.. dropdown:: 折返缝速度
   :animate: fade-in-slide-down
   
   -Max  4500
   -Min  100
   -Unit  spm
   -Description  折返缝模式下的最高速度。

S 06
----

.. dropdown:: 定针缝速度
   :animate: fade-in-slide-down
   
   -Max  4500
   -Min  100
   -Unit  spm
   -Description  定针缝中间段自动缝制速度。

A 01
----

.. dropdown:: 停针位
   :animate: fade-in-slide-down

   -Max  1
   -Min  0
   -Unit  --
   -Description
     | 当缝制途中停车时机针的位置：   
     | 0 = 下针位，机针在缝料之下；
     | 1 = 上针位，机针在缝料之上。

A 02
----

.. dropdown:: 定针缝自动缝制使能
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | 只对定针缝有效：
     | 0 = 定针缝中间段速度受调速器控制；
     | 1 = 中间段自动缝制。

A 03
----

.. dropdown:: 补针停车模式
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | 0 = 补半针；
     | 1 = 补整针。

A 16
----

.. dropdown:: 定针缝前加固结束自动缝制使能
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | 定针缝程序中，前加固结束后是否自动开始中间段的缝制：
     | 0 = 前加固结束后停车，直到调速器再次前踩时才继续缝纫；
     | 1 = 自动缝制中间段。

A 17
----

.. dropdown:: 定针缝中间段结束后自动后加固
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description  
     | 定针缝程序中，当中间段缝制完成后是否自动执行后加固及剪线：
     | 0 = 停车，再次踩踏调速器才执行终止回缝及剪线动作；
     | 1 = 自动执行。

A 30
----

.. dropdown:: 补针模式
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | 0 = 单次补针；
     | 1 = 连续补针。

A 31
----

.. dropdown:: 手动倒缝模式
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | 0 = 正常模式；
     | 1 = 停车拉倒缝。

D 11
----

.. dropdown:: 按键倒缝生效区间下限
   :animate: fade-in-slide-down
   
   -Max  359
   -Min  0
   -Unit  1°
   -Description  如果针杆位置大于此角度，手动倒缝按键不起作用。

D 12
----

.. dropdown:: 按键倒缝生效区间上限
   :animate: fade-in-slide-down
   
   -Max  359
   -Min  0
   -Unit  1°
   -Description  如果针杆位置大于此角度，手动倒缝按键不起作用。

D 15
----

.. dropdown:: 补针上角度
   :animate: fade-in-slide-down
   
   -Max  359
   -Min  0
   -Unit  1°
   -Description  补针模式下的上针位角度。

D 16
----

.. dropdown:: 补针下角度
   :animate: fade-in-slide-down
   
   -Max  359
   -Min  0
   -Unit  1°
   -Description  补针模式下的下针位角度。

O 18
----

.. dropdown:: 缝型标志
   :animate: fade-in-slide-down
   
   -Max  3
   -Min  1
   -Unit  --
   -Description  缝型标志（只读）。

O 69
----

.. dropdown:: 补针时机
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description  
     | 决定何时可以进行补针操作：
     | 0 = 剪线后禁止补针；
     | 1 = 停车后就可以补针。
