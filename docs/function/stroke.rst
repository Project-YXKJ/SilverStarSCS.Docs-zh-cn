.. _stroke:

==========
压脚交互量
==========

**快速切换交互量时限速**

如果参数 `A 35`_ 设置为1，当快速切换至大交互量时，缝纫速度将被限制在最大交互量的限速值，
由 `S 15`_ 决定。

**交互量轮盘限速**

如果交互量调节轮盘内安装了传感器，在调节交互量高度时，系统会自动进行限速，依据
传感器类型限速有两种策略：

- 开关式
  
  挡位式限速，如果安装有2个开关，则就是四个挡位。

- 电位器
  
  无极变速，在一个交互量高度之前不限速，之后随着交互量高度继续增大，限制速度随之线性越来越小。

**切换交互量后依据针数自动复位**

如果 `A 32`_ 不为0，当快速切换至大交互量后，缝制设置的针数之后，交互量将自动恢复至
正常状态。

参数列表
========

S 09
----

.. dropdown:: 压脚交互量第一档限速
   :animate: fade-in-slide-down
   
   -Max  4500
   -Min  100
   -Unit  spm
   -Description  限速轮盘类型开关式：压脚交互量第一档限速。

S 10
----

.. dropdown:: 小交互量时的限速
   :animate: fade-in-slide-down
   
   -Max  4500
   -Min  100
   -Unit  spm
   -Description  限速轮盘类型电位器式：小交互量时的限速。

S 11
----

.. dropdown:: 交互量第二档限速
   :animate: fade-in-slide-down
   
   -Max  4500
   -Min  100
   -Unit  spm
   -Description  限速轮盘类型开关式：压脚交互量第二档限速。

S 12
----

.. dropdown:: 交互量第三档限速
   :animate: fade-in-slide-down
   
   -Max  4500
   -Min  100
   -Unit  spm
   -Description  限速轮盘类型开关式：压脚交互量第三档限速。

S 13
----

.. dropdown:: 交互量第四档限速
   :animate: fade-in-slide-down
   
   -Max  4500
   -Min  100
   -Unit  spm
   -Description  限速轮盘类型开关式：压脚交互量第四档限速。

S 14
----

.. dropdown:: 大交互量时的限速
   :animate: fade-in-slide-down
   
   -Max  4500
   -Min  100
   -Unit  spm
   -Description  限速轮盘类型电位器式：大交互量时的限速。

S 15
----

.. dropdown:: 交互量最大时限速
   :animate: fade-in-slide-down
   
   -Max  4500
   -Min  100
   -Unit  spm
   -Description  交互量最大时限速。

A 24
----

.. dropdown:: 交互量状态
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description  压脚交互量状态（只读）。

A 32
----

.. dropdown:: 交互量自动恢复
   :animate: fade-in-slide-down
   
   -Max  99
   -Min  0
   -Unit  针
   -Description  
     | 0 = 手动切换;
     | 不为0 = 切换为大交互量后运行设定的针数，交互量自动恢复。

A 35
----

.. dropdown:: 自动限速
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  针
   -Description
     | 切换到大交互量时，速度将被自动限制至参数S15所设置的值：
     | 0 = 关闭；
     | 1 = 打开。

A 45
----

.. dropdown:: 交互量
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  针
   -Description
     | 交互量功能开关：
     | 0 = 关闭；
     | 1 = 打开。

O 21
----

.. dropdown:: 交互量限速生效分界点
   :animate: fade-in-slide-down
   
   -Max  4095
   -Min  0
   -Unit  针
   -Description  限速生效分界点位置的传感器值，依据此值，交互量继续增大时将进行限速。

O 22
----

.. dropdown:: 最大交互量分界点
   :animate: fade-in-slide-down
   
   -Max  4095
   -Min  0
   -Unit  针
   -Description  最大交互量位置的传感器值。

0 76
----

.. dropdown:: 时间（t1）
   :animate: fade-in-slide-down
   
   -Max  999
   -Min  1
   -Unit  毫秒
   -Description  交互量：全力100%占空比出力的持续 :term:`时间t1` 。

0 77
----

.. dropdown:: 维持出力（t2）
   :animate: fade-in-slide-down
   
   -Max  100
   -Min  1
   -Unit  %
   -Description  交互量：维持出力 :term:`时间t2` 内的占空比。

0 85
----

.. dropdown:: 交互量轮盘传感器类型
   :animate: fade-in-slide-down
   
   -Max  2
   -Min  0
   -Unit  针
   -Description
     | 0 = 无传感器；
     | 1 = 轻触开关；
     | 2 = 电位器。
