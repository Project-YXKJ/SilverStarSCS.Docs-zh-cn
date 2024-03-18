.. _thread_cutter:

====
剪线
====

**剪线执行流程**

在达到 `D 03`_ 设置的位置后，剪线电磁铁接通，之后达到 `D 04`_ 的位置后，关断。

如果在剪线过程发生机械堵转，那么剪线电磁铁会在500毫秒之后自动关断，以防止烧毁电磁铁。

参数列表
========

S 07
----

.. dropdown:: 剪线速度 <...>
   :animate: fade-in-slide-down
   
   -Max  300
   -Min  150
   -Unit  spm
   -Description  剪线动作的速度。

A 06
----

.. dropdown:: 剪线功能 <...>
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | 剪线功能开关：
     | 0 = 关闭；
     | 1 = 打开。

A 42
----

.. dropdown:: 短线头功能 <...>
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | 可选功能, 只针对特定型号：
     | 0 = 关闭；
     | 1 = 打开。     

A 67
----

.. dropdown:: 短线头针数 <...>
   :animate: fade-in-slide-down
   
   -Max  10
   -Min  0
   -Unit  针
   -Description  短线头功能打开时，剪线前的小针距针数。

D 03
----

.. dropdown:: 剪线开始角度 <...>
   :animate: fade-in-slide-down
   
   -Max  359
   -Min  0
   -Unit  1°
   -Description  剪线电磁铁动作角度。


D 04
----

.. dropdown:: 剪线结束角度 <...>
   :animate: fade-in-slide-down
   
   -Max  359
   -Min  0
   -Unit  1°
   -Description  剪线电磁铁释放角度。

D 17
----

.. dropdown:: Start Movable Knife Position(STC) <...>
   :animate: fade-in-slide-down
   
   -Max  359
   -Min  0
   -Unit  1°
   -Description  短线头机型剪线时动刀电磁铁动作角度。

D 18
----

.. dropdown:: 动刀结束角度(STC) <...>
   :animate: fade-in-slide-down
   
   -Max  359
   -Min  0
   -Unit  1°
   -Description  短线头机型剪线时动刀电磁铁释放角度。

D 19
----

.. dropdown:: 倒缝开始角度(STC) <...>
   :animate: fade-in-slide-down
   
   -Max  359
   -Min  0
   -Unit  1°
   -Description  短线头机型剪线时倒缝电磁体动作角度。

D 20
----

.. dropdown:: 倒缝结束角度(STC) <...>
   :animate: fade-in-slide-down
   
   -Max  359
   -Min  0
   -Unit  1°
   -Description  短线头机型剪线时倒缝电磁体释放角度。

D 21
----

.. dropdown:: 零针距开始角度(STC) <...>
   :animate: fade-in-slide-down
   
   -Max  359
   -Min  0
   -Unit  1°
   -Description  短线头机型剪线时零针距电磁体动作角度。

D 22
----

.. dropdown:: 零针距结束角度(STC) <...>
   :animate: fade-in-slide-down
   
   -Max  359
   -Min  0
   -Unit  1°
   -Description  短线头机型剪线时零针距电磁体释放角度。
   
O 38
----

.. dropdown:: 剪线后检查调速器位置 <...>
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | 剪线后开始一段新线迹之前，调速器是否需要回到位置0：
     | 0 = 关闭；
     | 1 = 打开。

O 95
----

.. dropdown:: 时间（t1） <...>
   :animate: fade-in-slide-down
   
   -Max  999
   -Min  1
   -Unit  毫秒
   -Description  短线头零针距：全力100%占空比出力的持续 :term:`时间t1` 。

O 96
----

.. dropdown:: 维持出力（t2） <...>
   :animate: fade-in-slide-down
   
   -Max  100
   -Min  1
   -Unit  %
   -Description  短线头零针距：维持出力 :term:`时间t2` 内的占空比。
