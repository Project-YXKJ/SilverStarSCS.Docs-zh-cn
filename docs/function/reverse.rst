.. _reverse:

====
倒缝
====

参数列表
========

T 01
----

.. dropdown:: 倒缝电磁铁吸合到位所需时间
   :animate: fade-in-slide-down
   
   -Max  200
   -Min  1
   -Unit  毫秒
   -Description  倒缝电磁铁从开始动作到吸合到位需要的时间。

T 02
----

.. dropdown:: 倒缝电磁铁释放到位所需时间
   :animate: fade-in-slide-down
   
   -Max  200
   -Min  1
   -Unit  毫秒
   -Description  倒缝电磁铁从开始动作到释放到位需要的时间。

D 05
----

.. dropdown:: 倒缝开始角度
   :animate: fade-in-slide-down
   
   -Max  359
   -Min  0
   -Unit  1°
   -Description  倒缝电磁铁动作角度。
  
D 06
----

.. dropdown:: 倒缝结束角度
   :animate: fade-in-slide-down
   
   -Max  359
   -Min  0
   -Unit  1°
   -Description  倒缝电磁铁释放角度。

T 08
----

.. dropdown:: 时间（t1）
   :animate: fade-in-slide-down
   
   -Max  200
   -Min  1
   -Unit  毫秒
   -Description  倒缝:全力100%占空比出力的持续 :term:`时间t1` 。

O 09
----

.. dropdown:: 维持出力（t2）
   :animate: fade-in-slide-down
   
   -Max  100
   -Min  1
   -Unit  %
   -Description  倒缝:维持出力 :term:`时间t2` 内的占空比。

O 10
----

.. dropdown:: 倒缝自动释放使能
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description 
     | 经过一定时间后抬倒缝电磁铁是否自动释放：
     | 0 = 关闭；
     | 1 = 打开。


O 11
----

.. dropdown:: 倒缝最大维持时间
   :animate: fade-in-slide-down
   
   -Max  30
   -Min  5
   -Unit  s
   -Description  如果自动释放打开，倒缝释放时间由此参数设置。
