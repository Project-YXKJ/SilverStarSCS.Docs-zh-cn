.. _soft_start:

======
缓启动
======

参数列表
========

一段新的线迹开始时，在起始的缓缝针数 `O 01`_ 内，缝制速度虽然由踏板控制
但会被限制在不超过软启动速度 `S 08`_ 。

S 08
----

.. dropdown:: 软启动速度 <...>
   :animate: fade-in-slide-down
   
   -Max  500
   -Min  200
   -Unit  spm 
   -Description  执行起针缓缝的速度。

A 21
----

.. dropdown:: 软启动 <...>
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  -- 
   -Description
     | 新的线迹开始时缓启动：
     | 0 = 关闭；
     | 1 = 打开。
     
O 01
----

.. dropdown:: 软启动针数 <...>
   :animate: fade-in-slide-down
   
   -Max  10
   -Min  1
   -Unit  针 
   -Description  剪线后下次起针时的缓缝针数。
