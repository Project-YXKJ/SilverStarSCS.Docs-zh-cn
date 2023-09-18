.. _bartack:

=========
前后加固
=========

**线迹重合性调整**

todo

**SD模式**

todo

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
