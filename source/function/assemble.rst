.. _assemble:

====
安装
====

参数列表
========

A 07
----

.. dropdown:: 机头热键锁定 <...>
   :animate: fade-in-slide-down
    
   -Max  1  
   -Min  0
   -Unit  --
   -Description
     | 缝料过厚时，用于防止缝料误触热键:
     | 0 = 关闭；
     | 1 = 打开。

A 19
----

.. dropdown:: 调速器半后踏功能<...> 
   :animate: fade-in-slide-down
   
   -Max  2
   -Min  1
   -Unit  --
   -Description  
     | 决定调速器处于 :term:`POSITION -1` 位置时执行什么动作
     | 1 = Sewing foot lift；
     | 2 = Thread trim。

O 03
----

.. dropdown:: 机头识别码 <...> 
   :animate: fade-in-slide-down
   
   -Max  2
   -Min  1
   -Unit  --
   -Description  :term:`机头识别码`

O 08
----

.. dropdown:: 调速器类型 <...> 
   :animate: fade-in-slide-down
   
   -Max  2
   -Min  1
   -Unit  --
   -Description
     | 使用原装调速器还是站立操作踏板：
     | 0 = 原装；
     | 1 = 站立操作踏板。

O 30
----

.. dropdown:: 机头识别器存储位置 <...> 
   :animate: fade-in-slide-down
   
   -Max  9999
   -Min  0
   -Unit  --
   -Description  
     | 选择 :term:`机头识别码` 
       存储位置:
     | 1 = 存储于控制器中；
     | 2 = 存储与机头识别器中。

O 56
----

.. dropdown:: 调速器校准:正向最大 <...>
   :animate: fade-in-slide-down
    
    -Max  4095  
    -Min  0
    -Unit  --
    -Description  调速器正向踩到底时的电压采样值，值 > O57

O 57
----

.. dropdown:: 调速器校准:POSITION 2 and POSITION 1 <...>
   :animate: fade-in-slide-down

    -Max  4095  
    -Min  0
    -Unit  --
    -Description  调速器正踩第二段和正踩第一段的分界点的采样值，O56 < 值 < O58

O 58
----
.. dropdown:: 调速器校准:POSITION 1 and POSITION 0 <...>
   :animate: fade-in-slide-down

    -Max  4095  
    -Min  0
    -Unit  --
    -Description  调速器正向第一段和默认位置的分界点的采样值，O57 < 值 < O59

O 59
----
.. dropdown:: 调速器校准:POSTIION 0 and POSTIION -1 <...>
   :animate: fade-in-slide-down

    -Max  4095  
    -Min  0
    -Unit  --
    -Description  调速器默认位置和反踩第一段的分界点的采样值，O58 < 值 < O60

O 60
----
.. dropdown:: 调速器校准:POSTIION -1 and POSTIION -2 <...>
   :animate: fade-in-slide-down

    -Max  4095  
    -Min  0
    -Unit  --
    -Description  调速器反踩第一段和反踩第二段的分界点的采样值，O59 < 值 < O61

O 61
----
.. dropdown:: 调速器校准:反踩最深 <...>
   :animate: fade-in-slide-down

    -Max  4095  
    -Min  0
    -Unit  --
    -Description  调速器反踩到最深处时采样值，值 < O60

O 62
----
.. dropdown:: 调速器校准:施密特值 <...>
   :animate: fade-in-slide-down

    -Max  4095  
    -Min  0
    -Unit  --
    -Description  调速器施密特区间的采样值

O 63
----
.. dropdown:: 调速器调速曲线 <...>
   :animate: fade-in-slide-down

   -Max  4095  
   -Min  0
   -Unit  --
   -Description
     | 0 = 直线；
     | 1 = 两段直线；
     | 2 = 曲线(先缓后快)；
     | 3 = 曲线(先快后缓)；
     | 4 = S曲线(先缓后快再缓)；
     | 5 = S曲线(先快后缓再快)。

O 80
----
.. dropdown:: 热键盒类型 <...>
   :animate: fade-in-slide-down

   -Max  3  
   -Min  1
   -Unit  --
   -Description
     | Type of the keypad:
     | 1 = 6键型；
     | 2 = 7键型；
     | 3 = 12键型。
