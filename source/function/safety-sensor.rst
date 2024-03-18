.. _safety-sensor:

==========
安全传感器
==========

机头倾倒开关
============

参数列表
--------

T 09
^^^^

.. dropdown:: 倾倒开关信号消抖时间 <...>
   :animate: fade-in-slide-down
   
   -Max  1000
   -Min  1
   -Unit  毫秒
   -Description  防止机头振动时倾倒开关误动作，倾倒开关信号必须持续有效一定时间才会被确认。

O 31
^^^^

.. dropdown:: 报警：倾倒开关 <...>
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | 机头被翻起时是否报警：
     | 0 = 关闭；
     | 1 = 打开。
     
O 32
^^^^

.. dropdown:: 倾倒开关信号极性 <...>
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | 0 = 常关断；
     | 1 = 常接通。

护眼挡板
========

参数列表
--------

O 28
^^^^

.. dropdown:: 报警：护眼板 <...>
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | 可选功能，护眼板被推开时是否报警：
     | 0 = 关闭；
     | 1 = 打开。

旋梭盖板
========

参数列表
--------

O 29
^^^^

.. dropdown:: 报警：旋梭盖板 <...> 
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | 可选功能，旋梭盖板被推开时是否报警：
     | 0 = 关闭；
     | 1 = 打开。
     

润滑油量
========

参数列表
--------

O 34
^^^^

.. dropdown:: 报警：油位检测 <...> 
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | 可选功能，检测润滑油位过低时是否报警：
     | 0 = 关闭；
     | 1 = 打开。


面线断线检测
============

参数列表
--------

T 13
^^^^

.. dropdown:: 面线检测信号消抖时间 <...> 
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description  面线检测报警确认时间，时间越短越灵敏。

O 92
^^^^

.. dropdown:: 信号极性(面线断线) <...> 
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | 0 = 常关断；
     | 1 = 常接通。
