.. _tension:

========
面线张力
========

**剪线时**

剪线时，面线张力的放松是随角度动作的，在达到 `D 13`_ 设置的角度时，面线放松，之后在达到
`D 14`_ 设置的角度时，面线再次收紧。

**抬压脚时**

在压脚抬起时，依据此时有没有进行剪线，分为缝制中和剪线后两个场景，缝线张力的自动模式可以有多
种选择。默认的为缝制中抬压脚时不松线，剪线之后抬压脚挺线器会打开。

模式选择可以参考 `A 27`_ 。

**切换到大交互量时**

系统可以设置，在切换大交互量时，额外面线张力可以自动生效，以收紧缝线得到更好的缝制效果，之后
如果交互量再次切换为正常状态，额外的面线张力也可以自动恢复。

此功能由 `A 28`_ 控制。

**驱动形式**

如果面线张力机构是由电磁铁驱动而不是电磁阀，则需要格外留意 `O 75`_ 的值。

因为电磁铁持续供电进而热量堆积可能会烧毁电磁铁，所以 `O 75`_ 必须设置一个合理值来避免这种情况。


参数列表
========

A 26
----

.. dropdown:: 第二夹线器状态 <...>
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description  第二夹线器状态（只读）。

A 27
----

.. dropdown:: 压脚抬起时面线张力的工作模式 <...>
   :animate: fade-in-slide-down
   
   -Max  3
   -Min  0
   -Unit  --
   -Description
     | 0 = 缝制中不松线，剪线后不松线；
     | 1 = 缝制中松线，剪线后不松线；
     | 2 = 缝制中不松线，剪线后松线；
     | 3 = 缝制中松线，剪线后松线。
     
A 28
----

.. dropdown:: 自动收紧面线张力 <...>
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | 当切换到大交互量时自动收紧额外的缝线张力：
     | 0 = 关闭；
     | 1 = 打开。    

D 13
----

.. dropdown:: 松线开始角度 <...>
   :animate: fade-in-slide-down
   
   -Max  359
   -Min  0
   -Unit  1°
   -Description  剪线时面线张力电磁铁动作角度。

D 14
----

.. dropdown:: 松线结束角度 <...>
   :animate: fade-in-slide-down
   
   -Max  359
   -Min  0
   -Unit  1°
   -Description  剪线时面线张力释放角度。

O 49
----

.. dropdown:: 时间（t1） <...>
   :animate: fade-in-slide-down
   
   -Max  999
   -Min  1
   -Unit  毫秒
   -Description  面线张力：全力100%占空比出力的持续 :term:`时间t1` 。

O 50
----

.. dropdown:: 维持出力（t2） <...>
   :animate: fade-in-slide-down
   
   -Max  100
   -Min  1
   -Unit  %
   -Description  面线张力：维持出力 :term:`时间t2` 内的占空比。

O 75
----

.. dropdown:: 挺线最大维持时间 <...>
   :animate: fade-in-slide-down
   
   -Max  9999
   -Min  0
   -Unit  毫秒
   -Description 
     | 0 = 挺线可以一直维持；
     | 不为 0 = 经过此时间后挺线自动释放。
     
O 86
----

.. dropdown:: 时间（t1） <...>
   :animate: fade-in-slide-down
   
   -Max  500
   -Min  1
   -Unit  毫秒
   -Description  第二面线张力：全力100%占空比出力的持续 :term:`时间t1`。

O 87
----

.. dropdown:: 维持出力（t2） <...>
   :animate: fade-in-slide-down
   
   -Max  100
   -Min  1
   -Unit  %
   -Description  第二面线张力：维持出力 :term:`时间t2` 内的占空比。

O 88
----

.. dropdown:: 额外面线张力电磁阀工作模式 <...>
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | 0 = 通电，通气，挺线打开；
     | 1 = 通电，不通气，挺线关闭。
