.. _motor: 

=====
电机
=====

**电机保持力**

打开此功能，需要将 `A 54`_ 设置为1。

当启用保持里功能时，电机在停车时会维持一定的力度来“锁定”在当前位置，此处锁定非固定,
这项功能对于改善停车时不希望的针杆下落有一定帮助，要感受锁定力度可以通过手动盘动手轮来感受。

保持力维持调节的最大时间由参数 `A 66`_ 决定:

- 如果 `A 66`_ 设置为0，那么保持力在停车时可以一直维持。
- 如果 `A 66`_ 设置不为0，那么保持力在停车时只是维持一定时间，之后释放电机，
  此时 `A 66`_ 参数值表示维持时间。

参数列表
========

S 01
----

.. dropdown:: 最高限速 <...>
   :animate: fade-in-slide-down
   
   -Max  4500
   -Min  100
   -Unit  spm
   -Description  调速器踩至最深时的最大速度。
     
S 02
----
.. dropdown:: 最低缝速 <...>
   :animate: fade-in-slide-down
  
   -Max  4500
   -Min  100
   -Unit  spm
   -Description  调速器处于位置1即低速段时的缝制速度，也是补针速度。

     
A 18
----
.. dropdown:: 上电自动上针位 <...>
   :animate: fade-in-slide-down
  
   -Max  4500
   -Min  100
   -Unit  spm
   -Description  
     | 上电后电机自动运行至上针位：
     | 0 = 关闭；
     | 1 = 打开。

.. danger:: 
   请谨慎设置A18参数，可能会导致人身危险。

A 54
----

.. dropdown:: 电机保持力 <...>
   :animate: fade-in-slide-down
  
   -Max  1
   -Min  0
   -Unit  --
   -Description  
     | 停车时是否让电机维持一定的力度来锁定在当前位置：
     | 0 = 关闭；
     | 1 = 打开。

A 55
----

.. dropdown:: 锁定齿 <...>
   :animate: fade-in-slide-down
  
   -Max  720
   -Min  1
   -Unit  --
   -Description  锁定在此角度内。

A 56
----

.. dropdown:: 偏移角度大于此值开始调节 <...>
   :animate: fade-in-slide-down
  
   -Max  720
   -Min  1
   -Unit  --
   -Description  位置误差大于此值开始调节。

A 57
----

.. dropdown:: 偏移角度小于此值调节结束 <...>
   :animate: fade-in-slide-down
  
   -Max  720
   -Min  1
   -Unit  --
   -Description  位置误差小于此值结束调节。

A 66
----

.. dropdown:: 电机保持力模式 <...>
   :animate: fade-in-slide-down
  
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | 0 = 一直维持；
     | 不为0 = 此参数表示维持的时间，设置的时间过后保持力消失。

O 04
----

.. dropdown:: 机头同步信号来源  <...>
   :animate: fade-in-slide-down
  
   -Max  1
   -Min  0
   -Unit  --
   -Description  
     | 0 = 外置针位检测器；
     | 1 = 电机自带。

O 36
----

.. dropdown:: 输入速度打折 <...>
   :animate: fade-in-slide-down
  
   -Max  5
   -Min  0
   -Unit  --
   -Description  对输入速度比例缩小使机器运行速度比设定低。

O 37
----

.. dropdown:: 简易模式 <...>
   :animate: fade-in-slide-down
  
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | 简易模式下，除了电机可以运行, 没有缝型、剪线、停针位等功能：
     | 0 = 关闭；
     | 1 = 打开。

O 67
----

.. dropdown:: 电机旋转方向 <...>
   :animate: fade-in-slide-down
  
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | 0 = 逆时针；
     | 1 = 顺时针，视角为手轮方向看电机。  

I 01
----

.. dropdown:: 加速度 <...>
   :animate: fade-in-slide-down
  
   -Max  500
   -Min  150
   -Unit  毫秒
   -Description  0~4500rpm加速时间。

I 02
----

.. dropdown:: 减速度 <...>
   :animate: fade-in-slide-down
  
   -Max  500
   -Min  150
   -Unit  毫秒
   -Description  4500rpm~0减速时间。

I 03
----

.. dropdown:: 电角度 <...>
   :animate: fade-in-slide-down
  
   -Max  4096
   -Min  0
   -Unit  --
   -Description  电角度补偿值。

I 04
----

.. dropdown:: 传动比 <...>
   :animate: fade-in-slide-down
  
   -Max  4096
   -Min  1 
   -Unit  --
   -Description  主轴转动一周对应的电机编码信号数量。

I 05
----

.. dropdown:: Kp(CSC-t) <...>
   :animate: fade-in-slide-down
  
   -Max  9999
   -Min  0
   -Unit  --
   -Description  剪线速度环Kp。

I 06
----

.. dropdown:: Kp增益(CSC-t) <...>
   :animate: fade-in-slide-down
  
   -Max  99
   -Min  0
   -Unit  --
   -Description  剪线速度环Kp增益系数。

I 07
----

.. dropdown:: Ki(CSC-t)  <...>
   :animate: fade-in-slide-down
  
   -Max  9999
   -Min  0
   -Unit  --
   -Description  剪线速度环Ki。

I 08
----

.. dropdown:: Ki增益(CSC-t) <...>
   :animate: fade-in-slide-down
  
   -Max  99
   -Min  0
   -Unit  --
   -Description  剪线速度环Ki增益。

I 09
----

.. dropdown:: Kp(CSC) <...>
   :animate: fade-in-slide-down
  
   -Max  9999
   -Min  0
   -Unit  --
   -Description  速度环Kp。

I 10
----

.. dropdown:: Kp增益(CSC) <...>
   :animate: fade-in-slide-down
  
   -Max  99
   -Min  0
   -Unit  --
   -Description  速度环Kp增益。

I 11
----

.. dropdown:: Ki(CSC) <...>
   :animate: fade-in-slide-down
  
   -Max  9999
   -Min  0
   -Unit  --
   -Description  速度环Ki。

I 12
----

.. dropdown:: Ki增益(CSC) <...>
   :animate: fade-in-slide-down
  
   -Max  99
   -Min  0
   -Unit  --
   -Description  速度环Ki增益。


I 13
----

.. dropdown:: 输出上限(CSC) <...>
   :animate: fade-in-slide-down
  
   -Max  20
   -Min  1
   -Unit  --
   -Description  速度环输出上限。


I 14
----

.. dropdown:: 前馈(CSC) <...>
   :animate: fade-in-slide-down
  
   -Max  500
   -Min  0
   -Unit  --
   -Description  速度环前馈系数。

I 15
----

.. dropdown:: Kp(CCC-d) <...>
   :animate: fade-in-slide-down
  
   -Max  9999
   -Min  0
   -Unit  --
   -Description  电流环d轴Kp。

I 16
----

.. dropdown:: Kp增益(CCC-d) <...>
   :animate: fade-in-slide-down
  
   -Max  99
   -Min  0
   -Unit  --
   -Description  电流环d轴Kp增益。

I 17
----

.. dropdown:: Ki(CCC-d) <...>
   :animate: fade-in-slide-down
  
   -Max  9999
   -Min  0
   -Unit  --
   -Description  电流环d轴Ki。

I 18
----

.. dropdown:: Ki增益(CCC-d) <...>
   :animate: fade-in-slide-down
  
   -Max  99
   -Min  0
   -Unit  --
   -Description  电流环d轴Ki增益。

I 19
----

.. dropdown:: 输出上限(CCC-d) <...>
   :animate: fade-in-slide-down
  
   -Max  3276
   -Min  0
   -Unit  --
   -Description  电流环Id输出上限。

I 20
----

.. dropdown:: 输出下限(CCC-d) <...>
   :animate: fade-in-slide-down
  
   -Max  3276
   -Min  0
   -Unit  --
   -Description  电流环Id输出下限。

I 21
----

.. dropdown:: Kp(CCC-q) <...>
   :animate: fade-in-slide-down
  
   -Max  9999
   -Min  0
   -Unit  --
   -Description  电流环q轴Kp。

I 22
----

.. dropdown:: Kp增益(CCC-q) <...>
   :animate: fade-in-slide-down
  
   -Max  99
   -Min  0
   -Unit  --
   -Description  电流环q轴Kp增益。

I 23
----

.. dropdown:: Ki(CCC-q) <...>
   :animate: fade-in-slide-down
  
   -Max  9999
   -Min  0
   -Unit  --
   -Description  电流环q轴Ki。

I 24
----

.. dropdown:: Ki增益(CCC-q) <...>
   :animate: fade-in-slide-down
  
   -Max  9999
   -Min  0
   -Unit  --
   -Description  电流环q轴Ki增益。

I 25
----

.. dropdown:: 输出上限(CCC-q) <...>
   :animate: fade-in-slide-down
  
   -Max  3276
   -Min  0
   -Unit  --
   -Description  电流环Iq输出上限。

I 26
----

.. dropdown:: 输出下限(CCC-q) <...>
   :animate: fade-in-slide-down
  
   -Max  3276
   -Min  0
   -Unit  --
   -Description  电流环Iq输出下限。

I 27
----

.. dropdown:: 码盘分辨率 <...>
   :animate: fade-in-slide-down
  
   -Max  9999
   -Min  1
   -Unit  --
   -Description  电机编码器的每圈线数。

I 28
----

.. dropdown:: 停车流程限时 <...>
   :animate: fade-in-slide-down
  
   -Max  9999
   -Min  0
   -Unit  毫秒
   -Description  停车流程中距离电机刹停的时间。

I 30
----

.. dropdown:: 停车模式 <...>
   :animate: fade-in-slide-down
  
   -Max  1
   -Min  0 
   -Unit  --
   -Description
     | 选择到达目标位置的模式：
     | 0 = 速度模式；
     | 1 = 位置模式。 


I 33
----

.. dropdown:: 机械零点偏移量 <...>
   :animate: fade-in-slide-down
  
   -Max  1
   -Min  0 
   -Unit  --
   -Description  机械零点距离电机同步点的偏移量。

I 37
----

.. dropdown:: 刹车P-S阶段距离 <...>
   :animate: fade-in-slide-down
  
   -Max  359
   -Min  0 
   -Unit  1°
   -Description  刹车角度与速度规划阶段的距离。

I 38
----

.. dropdown:: 刹车P-S阶段初速度 <...>
   :animate: fade-in-slide-down
  
   -Max  500
   -Min  100 
   -Unit  spm
   -Description  刹车角度与速度规划阶段的入口速度。

I 39
----

.. dropdown:: 刹车P-S阶段末速度 <...>
   :animate: fade-in-slide-down
  
   -Max  100
   -Min  20 
   -Unit  spm
   -Description  刹车角度与速度规划阶段的终点速度。


I 40
----

.. dropdown:: Kp(CPC-s) <...>
   :animate: fade-in-slide-down
  
   -Max  9999
   -Min  0 
   -Unit  --
   -Description  停车位置环Kp。

I 41
----

.. dropdown:: Kp增益(CPC-s) <...>
   :animate: fade-in-slide-down
  
   -Max  99
   -Min  1
   -Unit  --
   -Description  停车位置环Kp增益。

I 42
----

.. dropdown:: Kd(CPC-s) <...>
   :animate: fade-in-slide-down
  
   -Max  9999
   -Min  0
   -Unit  --
   -Description  停车位置环Kd。

I 43
----

.. dropdown:: Kd增益(CPC-s) <...>
   :animate: fade-in-slide-down
  
   -Max  99
   -Min  1
   -Unit  --
   -Description  停车位置环Kd增益。

I 46
----

.. dropdown:: 最大锁定电流 <...>
   :animate: fade-in-slide-down
  
   -Max  40
   -Min  1
   -Unit  0.1A
   -Description  锁定电流最大值。

I 47
----

.. dropdown:: 弱磁 <...>
   :animate: fade-in-slide-down
  
   -Max  1
   -Min  0
   -Unit  --
   -Description  
     | 弱磁扩速，以便电机可以达到更高的转速：
     | 0 = 关闭；
     | 1 = 打开。

I 48
----

.. dropdown:: 弱磁生效速度 <...>
   :animate: fade-in-slide-down
  
   -Max  3500
   -Min  2000
   -Unit  rpm  
   -Description  高于此速度，弱磁扩速生效。

I 49
----

.. dropdown:: 弱磁扩速电流 <...>
   :animate: fade-in-slide-down
  
   -Max  40
   -Min  1
   -Unit  0.1A
   -Description  弱磁扩速ID电流上限。

I 50
----

.. dropdown:: 输出上限(CPC-h) <...>
   :animate: fade-in-slide-down
  
   -Max  500
   -Min  0
   -Unit  --
   -Description  锁定位置环输出上限。

I 51
----

.. dropdown:: 输出下限(CPC-h) <...>
   :animate: fade-in-slide-down
  
   -Max  100
   -Min  0
   -Unit  --
   -Description  锁定位置环输出下限。

I 52
----

.. dropdown:: Kp(CPC-h) <...>
   :animate: fade-in-slide-down
  
   -Max  9999
   -Min  0
   -Unit  --
   -Description  位置环Kp。

I 53
----

.. dropdown:: Kp增益(CPC-h) <...>
   :animate: fade-in-slide-down
  
   -Max  99
   -Min  1
   -Unit  --
   -Description  锁定位置环Kp增益。

I 54
----

.. dropdown:: Kd(CPC-h) <...>
   :animate: fade-in-slide-down
  
   -Max  9999
   -Min  0
   -Unit  --
   -Description  锁定位置环Kd。

I 55
----

.. dropdown:: Kd增益(CPC-h) <...>
   :animate: fade-in-slide-down
  
   -Max  99
   -Min  1
   -Unit  --
   -Description  锁定位置环Kd增益。
