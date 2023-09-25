.. _second_stitch_length:

========
第二针距
========

**长针距自动限速**

如果参数 `O 33`_ 设置为1，当切换到长针距时缝纫速度将被限制在参数 `S 17`_ 所设置的值。

参数列表
========

S 17
----

.. dropdown:: 大针距限速值 <...>
   :animate: fade-in-slide-down
   
   -Max  4500
   -Min  100
   -Unit  spm
   -Description  当使用大针距时的限速值。

A 25
----

.. dropdown:: 大小针距状态 <...>
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description  大小针距状态（只读）。

A 46
----

.. dropdown:: 大小针距 <...>
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | 大小针距功能：
     | 0 = 关闭；
     | 1 = 打开。

A 50
----

.. dropdown:: 加固缝针距 <...>
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | 选择是否在前后加固时自动切换到小针距：
     | 0 = 关闭；
     | 1 = 打开。

O 33
----

.. dropdown:: 针距限速 <...>
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | 当切换为大针距时进行限速：
     | 0 = 关闭；
     | 1 = 打开。

O 78
----

.. dropdown:: 时间（t1） <...>
   :animate: fade-in-slide-down
   
   -Max  999
   -Min  1
   -Unit  毫秒
   -Description  第二针距：全力100%占空比出力的持续 :term:`时间t1` 。

O 79
----

.. dropdown:: 维持出力（t2） <...>
   :animate: fade-in-slide-down
   
   -Max  100
   -Min  1
   -Unit  %
   -Description  第二针距：维持出力 :term:`时间t2` 内的占空比。
