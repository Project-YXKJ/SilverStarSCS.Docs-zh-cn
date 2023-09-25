.. _puller:

========
送料滚轮
========

**自动模式如何工作？**:

- 当压脚抬起时，拖布轮随之自动抬起；
- 当缝制前后加固时，拖布轮自动抬起；
- 当倒缝时，拖布轮自动抬起；
- 可以将输入按键功能配置为切换拖布轮抬起/落下，当按键抬起拖布轮时，拖布轮将始终
  抬起直到再次通过按键落下。

参数列表
========

A 64
----

.. dropdown:: 延迟针数 <...>
   :animate: fade-in-slide-down

   -Max  255
   -Min  0
   -Unit  stitch
   -Description  新的线迹开始后拖布轮延迟放下的针数。

A 89
----

.. dropdown:: 送料滚轮 <...>
   :animate: fade-in-slide-down

   -Max  1
   -Min  0
   -Unit  --
   -Description
     | 送料滚轮功能开关：
     | 0 = 关闭；
     | 1 = 打开。

A 90
----

.. dropdown:: 拖布轮状态 <...>
   :animate: fade-in-slide-down

   -Max  1
   -Min  0
   -Unit  --
   -Description  拖布轮状态（只读）。

O 97
----

.. dropdown:: 时间（t1） <...>
   :animate: fade-in-slide-down

   -Max  999
   -Min  1
   -Unit  毫秒
   -Description  拖布轮：全力100%占空比出力的持续 :term:`时间t1` 。

O 98
----

.. dropdown:: 维持出力（t2） <...>
   :animate: fade-in-slide-down

   -Max  100
   -Min  1
   -Unit  --
   -Description  拖布轮：维持出力 :term:`时间t2` 内的占空比。
