.. _bartack:

=========
前后加固
=========

**线迹重合性调整**

在调整之前，请确保机械已经校准完毕，使用倒缝扳手时正缝和倒缝针距一致。

正缝转入倒缝时出现针迹不一致的情况，调整 `T 01`_ 可以参考下面进行调整：

+------------------------------------------+------------------------------------------+
| 减小 T01                                 | 增大 T01                                 |
+==========================================+==========================================+
| .. image:: ../_static/common/sub-T01.svg | .. image:: ../_static/common/add-T01.svg |
+    :scale: 150 %                         +    :scale: 150 %                         +
|                                          |                                          |
+------------------------------------------+------------------------------------------+

倒缝转入正缝时出现针迹不一致的情况，调整 `T 02`_ 可以参考下面进行调整：

+------------------------------------------+------------------------------------------+
| 减小 T02                                 | 增大 T02                                 |
+==========================================+==========================================+
| .. image:: ../_static/common/sub-T02.svg | .. image:: ../_static/common/add-T02.svg |
+    :scale: 150 %                         +    :scale: 150 %                         +
|                                          |                                          |
+------------------------------------------+------------------------------------------+

**SD模式**

SD模式是前后加固的一种特殊模式，用于尽可能的保证对针眼效果。

当SD模式启用时，在加固转折点，电机会停车，并且等待 `T 11`_ 所设置的时间，确保倒缝动作到位，
之后继续运行。

可以分别对前加固或者后加固启动SD模式，由 `A 20`_ 和 `A 22`_ 控制。

参数列表
========

S 03
----
.. dropdown:: 前加固速度 <...>
   :animate: fade-in-slide-down
   
   -Max  4500
   -Min  100
   -Unit  spm
   -Description  前加固能达到的最大速度

S 04
----
.. dropdown:: 后加固速度 <...>
   :animate: fade-in-slide-down
   
   -Max  4500
   -Min  100
   -Unit  spm
   -Description  后加固能达到的最大速度

T 01
----

.. dropdown:: 倒缝电磁铁吸合到位所需时间 <...>
   :animate: fade-in-slide-down
   
   -Max  200
   -Min  1
   -Unit  毫秒
   -Description  倒缝电磁铁从开始动作到吸合到位需要的时间。

T 02
----

.. dropdown:: 倒缝电磁铁释放到位所需时间 <...>
   :animate: fade-in-slide-down
   
   -Max  200
   -Min  1
   -Unit  毫秒
   -Description  倒缝电磁铁从开始动作到释放到位需要的时间。

T 08
----

.. dropdown:: 时间（t1） <...>
   :animate: fade-in-slide-down
   
   -Max  200
   -Min  1
   -Unit  毫秒
   -Description  倒缝:全力100%占空比出力的持续 :term:`时间t1` 。

T 11
----
.. dropdown:: SD模式拐点停顿时间 <...> 
   :animate: fade-in-slide-down
   
   -Max  4500
   -Min  100
   -Unit  spm
   -Description  SD加固模式下,加固缝缝纫方向转换点电机停下来等待倒缝电磁铁动作到位的时间

A 20
----

.. dropdown:: 前加固SD模式选择 <...> 
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | 设为1时,前加固在缝纫方向转换时电机会停下来等待倒缝动作：
     | 0 = 关闭；
     | 1 = 打开。

A 22
----

.. dropdown:: 后加固SD模式选择 <...>
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | 设为1时，后加固在缝纫方向转换时电机会停下来等待倒缝动作：
     | 0 = 关闭；
     | 1 = 打开。

A 34
----

.. dropdown:: 前加固后恒定速度 <...>
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description  Reverse power on angle
     | 为了使线迹重合效果更好,前加固结束后维持当前加固速度,若干针后速度才由调速器接管：
     | 0 = 关闭；
     | 1 = 打开。

D 05
----

.. dropdown:: 倒缝开始角度 <...>
   :animate: fade-in-slide-down
   
   -Max  359
   -Min  0
   -Unit  1°
   -Description  倒缝电磁铁动作角度。

D 06
----

.. dropdown:: 倒缝结束角度 <...>
   :animate: fade-in-slide-down
   
   -Max  359
   -Min  0
   -Unit  1°
   -Description  倒缝电磁铁释放角度。
   
O 09
----

.. dropdown:: 维持出力（t2） <...>
   :animate: fade-in-slide-down
   
   -Max  100
   -Min  1
   -Unit  %
   -Description  倒缝:维持出力 :term:`时间t2` 内的占空比。

O 10
----

.. dropdown:: 倒缝自动释放使能 <...>
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

.. dropdown:: 倒缝最大维持时间 <...>
   :animate: fade-in-slide-down
   
   -Max  30
   -Min  5
   -Unit  s
   -Description  如果自动释放打开，倒缝释放时间由此参数设置。

O 12
___

.. dropdown:: 1针的限速 <...> 
   :animate: fade-in-slide-down
   
   -Max  4500
   -Min  100
   -Unit  spm
   -Description  前后加固,折返缝只有1针时限速

O 13 
----

.. dropdown:: 2针的限速 <...>  
   :animate: fade-in-slide-down
   
   -Max  4500
   -Min  100
   -Unit  spm
   -Description  前后加固，折返缝只有2针时限速。

O 14
----

.. dropdown:: 3针的限速 <...> 
   :animate: fade-in-slide-down
   
   -Max  4500
   -Min  100
   -Unit  spm
   -Description  前后加固，折返缝只有3针时限速。

O 41
----

.. dropdown:: 前加固匀速保持针数 <...> 
   :animate: fade-in-slide-down
   
   -Max  10
   -Min  0
   -Unit  针
   -Description  前加固后保持当前速度的针数，之后速度才由调速器接管。
