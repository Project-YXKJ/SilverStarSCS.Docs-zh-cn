.. _needle_cooling:

========
机针冷却
========

机针冷却可以辅助给机针降温，避免缝料损伤，面线断裂。

**如何运行？**:

当缝制速度超过 `S 18`_ ，机针冷却生效吹气。

当缝制速度低于 `S 18`_ ，机针冷却并立刻关闭，而是继续生效一定时间后关闭，此时间由参数 `T 16`_ 控制。

在延时关闭的时间内，如果缝制速度再次超过 `S 18`_ ，机针冷却会再次生效。


参数列表
========

S 18
----

.. dropdown:: 机针冷却开启速度 <...>
   :animate: fade-in-slide-down
   
   -Max  4500
   -Min  100
   -Unit  spm
   -Description  超过此速度，机针冷却打开。

T 16
----

.. dropdown:: 机针冷却延续时间 <...>
   :animate: fade-in-slide-down
   
   -Max  10
   -Min  0
   -Unit  s
   -Description  当缝速低于机针冷却开启速度，延迟一段时间后机针冷却才关闭。
   
A 48
----

.. dropdown:: 机针冷却 <...>
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | 机针冷却功能开关：
     | 0 = 关闭；
     | 1 = 打开。
     
O 93
----

.. dropdown:: 时间（t1） <...>
   :animate: fade-in-slide-down
   
   -Max  999
   -Min  1
   -Unit  毫秒
   -Description  机针冷却：全力100%占空比出力的持续 :term:`时间t1` 。

O 94
----

.. dropdown:: 维持出力（t2） <...>
   :animate: fade-in-slide-down
   
   -Max  100
   -Min  1
   -Unit  %
   -Description  机针冷却：维持出力 :term:`时间t2` 内的占空比。
