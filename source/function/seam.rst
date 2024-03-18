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

如果 `A 03`_ 设置为0：

当按动补针按键，系统会计算当前位置与 `D 15`_ 和 `D 16`_ 的距离并进行比较，那个距离近，
那么针杆就移动至哪个位置。

比如：当前针杆位置为40度， `D 15`_ 的值为70， `D 16`_ 的值为200度，显然40度距离70度更
近一点，那么按动补针按键运动轨迹为 ``位置40 => 70 => 200 => 70 => 200 ...`` 。


如果 `A 03`_ 设置为1：

当按动补针按键，此时分两种情况：如果设置为停上针位，则针杆从当前位置移动至 `D 01`_ 位置；
如果设置为停下针位，则针杆从当前位置移动至 `D 02`_ 位置。

比如：当前针杆位置为40度, `D 01`_ 的值为70， `D 02`_ 的值为200度，如果 `A 01`_ 为0，则
每次按动补针按键运动轨迹为 ``位置40 => 200 => 200 => 200 ...`` ；如果 `A 01`_ 为1，
每次按动补针按键运动轨迹为 ``位置40 => 70 => 70 => 70 ...`` 。

参数列表
========

S 05
----

.. dropdown:: 折返缝速度 <...>
   :animate: fade-in-slide-down
   
   -Max  4500
   -Min  100
   -Unit  spm
   -Description  折返缝模式下的最高速度。

S 06
----

.. dropdown:: 定针缝速度 <...>
   :animate: fade-in-slide-down
   
   -Max  4500
   -Min  100
   -Unit  spm
   -Description  定针缝中间段自动缝制速度。

A 01
----

.. dropdown:: 停针位 <...>
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

.. dropdown:: 定针缝自动缝制使能 <...>
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

.. dropdown:: 补针停车模式 <...>
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | 0 = 补半针；
     | 1 = 补整针。

A 16
----

.. dropdown:: 定针缝前加固结束自动缝制使能 <...>
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

.. dropdown:: 定针缝中间段结束后自动后加固 <...>
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

.. dropdown:: 补针模式 <...>
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | 0 = 单次补针；
     | 1 = 连续补针。

A 31
----

.. dropdown:: 手动倒缝模式 <...>
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | 0 = 正常模式；
     | 1 = 停车拉倒缝。

D 01
----

.. dropdown:: 上针位角度 <...>
   :animate: fade-in-slide-down
  
   -Max  359
   -Min  0
   -Unit  1°
   -Description  剪线后的针杆位置，机针在缝料之上。

D 02
----

.. dropdown:: 下针位角度 <...>
   :animate: fade-in-slide-down
  
   -Max  359
   -Min  0
   -Unit  1°
   -Description  一般中途停车时针杆位置，机针在缝料之下。

D 11
----

.. dropdown:: 按键倒缝生效区间下限 <...>
   :animate: fade-in-slide-down
   
   -Max  359
   -Min  0
   -Unit  1°
   -Description  如果针杆位置大于此角度，手动倒缝按键不起作用。

D 12
----

.. dropdown:: 按键倒缝生效区间上限 <...>
   :animate: fade-in-slide-down
   
   -Max  359
   -Min  0
   -Unit  1°
   -Description  如果针杆位置大于此角度，手动倒缝按键不起作用。

D 15
----

.. dropdown:: 补针上角度 <...>
   :animate: fade-in-slide-down
   
   -Max  359
   -Min  0
   -Unit  1°
   -Description  补针模式下的上针位角度。

D 16
----

.. dropdown:: 补针下角度 <...>
   :animate: fade-in-slide-down
   
   -Max  359
   -Min  0
   -Unit  1°
   -Description  补针模式下的下针位角度。

O 18
----

.. dropdown:: 缝型标志 <...>
   :animate: fade-in-slide-down
   
   -Max  3
   -Min  1
   -Unit  --
   -Description  缝型标志（只读）。

O 69
----

.. dropdown:: 补针时机 <...>
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description  
     | 决定何时可以进行补针操作：
     | 0 = 剪线后禁止补针；
     | 1 = 停车后就可以补针。
