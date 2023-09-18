.. _sewing_foot_lift:

====
压脚
====

**抬压脚**

- 线迹中
  
  反踩调速器至半后踏（:term:`POSITION -1`） 或者当 `A 14`_ 设置为1时自动抬起。

- 剪线之后

  反踩调速器（:term:`POSITION -1` or :term:`POSITION -2`） 或者 当 `A 15`_ 设置为1时自动抬起。

**压脚抬起后的维持力度**

抬压脚一开始是全力输出的，之后会自动切换到PWM控制，以减少控制器和电磁铁(阀)上承载的电流。

全力输出时间由参数 `T 07`_ 决定，维持力度由参数 `O 05`_ 控制。

**定时释放**

为了减少热量产生，尤其是压脚由电磁铁驱动时，可以设置定时释放。

将参数 `O 06`_ 设置为1，压脚最大抬起时间由参数 `O 07`_ 决定。

**下落时间**

当压脚处于抬起状态时，为了保证缝料被压紧之后机器才开始运行，当前踩调速器机时一段延时时间会插入，
此时间由参数 `T 06`_ 控制。

参数列表
==============

T 05
----

.. dropdown:: 抬压脚位置判断时间
   :animate: fade-in-slide-down
   
   -Max  500
   -Min  1
   -Unit  毫秒
   -Description  抬压脚等待时间，用于反踩剪线时避免抬压脚动作。

T 06
----

.. dropdown:: 压脚下落时间
   :animate: fade-in-slide-down
   
   -Max  500
   -Min  1
   -Unit  毫秒
   -Description  压脚下落需要的时间，缝制开始之前延迟一段时间，确保压脚已经压紧了缝料。

T 07
----

.. dropdown:: 时间（t1） 
   :animate: fade-in-slide-down
   
   -Max  999
   -Min  1
   -Unit  毫秒
   -Description  压脚：全力100%占空比出力的持续 :term:`时间t1` 。

T 10
----

.. dropdown:: 自动压脚延迟时间
   :animate: fade-in-slide-down
   
   -Max  200
   -Min  1
   -Unit  毫秒
   -Description  自动压脚功能打开时，延迟抬压脚的时间。

A 09
----

.. dropdown:: 压脚功能
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | 压脚功能开关：
     | 0 = 关闭；
     | 1 = 打开。

A 14
----

.. dropdown:: 中间停车后自动抬压脚
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | 在一段线迹的中间部分停车时自动抬起压脚：
     | 0 = 关闭；
     | 1 = 打开。

A 15
----

.. dropdown:: 剪线后自动抬压脚
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | 在剪线后或者一段线迹的结束后自动抬起压脚：
     | 0 = 关闭；
     | 1 = 打开。

O 05
----

.. dropdown:: 维持出力（t2）
   :animate: fade-in-slide-down
   
   -Max  100
   -Min  1
   -Unit  %
   -Description  压脚：维持出力 :term:`时间t2` 内的占空比。
   
O 06
----

.. dropdown:: 压脚自动释放
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | 经过一定时间后抬压脚电磁铁是否自动释放：
     | 0 = 关闭；
     | 1 = 打开。

O 07
----

.. dropdown:: 压脚最大抬起时间
   :animate: fade-in-slide-down
   
   -Max  30
   -Min  5
   -Unit  s
   -Description  如果自动释放打开，压脚释放时间由此参数设置。

O 39
----

.. dropdown:: 压脚缓放
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description  
     | 通过PWM控制，减缓压脚下落速度：
     | 0 = 关闭；
     | 1 = 打开。

O 40
----

.. dropdown:: 抬压脚缓放力度
   :animate: fade-in-slide-down
   
   -Max  9
   -Min  1
   -Unit  --
   -Description  数值越大，压脚下落速度越慢。

O 53
----

.. dropdown:: 夹线时压脚微抬力度(无前加固)
   :animate: fade-in-slide-down
   
   -Max  10
   -Min  1
   -Unit  --
   -Description  自由缝无前后加固时，起缝夹线时压脚微抬占空比。

O 54
----

.. dropdown:: 夹线时压脚微抬力度(缓缝)
   :animate: fade-in-slide-down
   
   -Max  10
   -Min  1
   -Unit  --
   -Description  起针缓缝打开时，起缝夹线时压脚微抬占空比。


O 55
----

.. dropdown:: 夹线时压脚微抬力度
   :animate: fade-in-slide-down
   
   -Max  10
   -Min  1
   -Unit  --
   -Description  起缝夹线时压脚微抬占空比。
