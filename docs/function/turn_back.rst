.. _turn_back:

========
剪线回拉
========

设置 `A 13`_ 为1，可以选择启用反转提针，此功能方便取出缝料以避免机针刮伤面料。

在剪线流程结束之后，延迟 `T 12`_ 设定的时间之后，
提针速度被限制在 `S 16`_ 之内，当位置达到 `O 35`_ 后，电机停止。

参数列表
========

S 16
----

.. dropdown:: 反拉速度
   :animate: fade-in-slide-down
   
   -Max  500
   -Min  50
   -Unit  spm
   -Description  剪线后提针反拉速度。

T 12
----

.. dropdown:: 反拉延迟时间
   :animate: fade-in-slide-down
   
   -Max  1000
   -Min  1
   -Unit  毫秒
   -Description  剪线完成后经过此延时时间机针开始反转。
   
A 13
----

.. dropdown:: 剪线回拉
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | 剪线后提针回拉：
     | 0 = 关闭；
     | 1 = 打开。

O 35
----

.. dropdown:: 剪线反转位置
   :animate: fade-in-slide-down
   
   -Max  359
   -Min  0
   -Unit  1°
   -Description  剪线反转后针杆到达的位置。
