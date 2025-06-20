.. _tension:

========
面线张力
========

由电磁阀还是电磁铁驱动？
========================

如果面线张力机构是由电磁铁驱动而不是电磁阀，则需要格外留意 :option:`O75` 的值。

因为电磁铁持续供电进而热量堆积可能会烧毁电磁铁，所以 :option:`O75` 必须设置一个合理值来避免这种情况。

剪线时面线张力如何运行？
========================

面线张力动作流程：

剪线时，面线张力的放松是随角度动作的，在达到 :option:`D13` 设置的角度时，面线放松，之后在达到
:option:`D14` 设置的角度时，面线再次收紧。


抬压脚时面线张力模式
====================

在压脚抬起时，依据此时有没有进行剪线，分为缝制中和剪线后两个场景，缝线张力的自动模式可以有4
种选择。

模式选择可以参考 :option:`A27`：

* 0 = 在缝制中抬压脚时不松线，剪线后抬压脚时也不松线；
* 1 = 在缝制中抬压脚时松线，剪线后抬压脚时不松线；
* 2 = 在缝制中抬压脚时不松线，剪线后抬压脚时松线；
* 3 = 在缝制中抬压脚时松线，剪线后抬压脚时松线。

额外面线张力自动化规则
======================

自动化规则可以让额外面线张力跟随三种情况自动动作：

* 交互量
* 前加固
* 后加固

自动模式如何工作？
------------------

在切换大交互量时，额外面线张力可以自动生效，以收紧缝线得到更好的缝制效果，之后如果交互量再次
切换为正常状态，额外的面线张力也可以自动恢复。

当缝制前加固时，额外面线张力也可以自动生效，前加固缝制完成后，额外的面线张力也可以自动恢复。

当缝制后加固时，额外面线张力也可以自动生效，前加固缝制完成后，额外的面线张力也可以自动恢复。

规则由参数 :option:`A28` 决定，你可以通过下表速查你需要设置的参数值：

====== ====== ===================== =================== 
参数值 交互量 前加固                后加固
====== ====== ===================== ===================
0      关闭   关闭                  关闭
1      开启   关闭                  关闭
2      关闭   开启                  关闭
3      开启   开启                  关闭
4      关闭   关闭                  开启
5      开启   关闭                  开启
6      关闭   开启                  开启
7      开启   开启                  开启
====== ====== ===================== ===================

快速参考
===============

下表总结了面线张力功能所使用到的参数：

==================================================== ========== ==============
参数                                                 权限       参见
==================================================== ========== ==============
第二夹线器状态                                       开发者     :option:`A26`
压脚抬起时面线张力的工作模式                         技术员     :option:`A27`
自动收紧面线张力                                     技术员     :option:`A28`
松线开始角度                                         技术员     :option:`D13`
松线结束角度                                         技术员     :option:`D14`
时间（t1）                                           开发者     :option:`O49`
维持出力（t2）                                       开发者     :option:`O50`
挺线最大维持时间                                     开发者     :option:`O75`
时间（t1）                                           开发者     :option:`O86`
维持出力（t2）                                       开发者     :option:`O87`
额外面线张力电磁阀工作模式                           开发者     :option:`O88`
==================================================== ========== ==============

参数列表
========

.. option:: A26
   
   -Max  1
   -Min  0
   -Unit  --
   -Description  第二夹线器状态（只读）。

.. option:: A27
   
   -Max  3
   -Min  0
   -Unit  --
   -Description
     | 0 = 缝制中不松线，剪线后不松线；
     | 1 = 缝制中松线，剪线后不松线；
     | 2 = 缝制中不松线，剪线后松线；
     | 3 = 缝制中松线，剪线后松线。
     
.. option:: A28
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | 额外面线张力的自动化规则：
     | 0 = 完全手动；
     | 1 = 切换交互量时自动激活；
     | 2 = 缝制前加固时自动激活；
     | 3 = 1 和 2；
     | 4 = 缝制后加固时自动激活；
     | 5 = 1 和 4；
     | 6 = 2 和 4；
     | 7 = 1 和 2 和 4。  

.. option:: D13
   
   -Max  359
   -Min  0
   -Unit  1°
   -Description  剪线时面线张力电磁铁动作角度。

.. option:: D14
   
   -Max  359
   -Min  0
   -Unit  1°
   -Description  剪线时面线张力释放角度。

.. option:: O49
   
   -Max  999
   -Min  1
   -Unit  ms
   -Description  面线张力：全力 100% 占空比出力的持续 :term:`时间 t1` 。

.. option:: O50
   
   -Max  100
   -Min  1
   -Unit  %
   -Description  面线张力：维持出力 :term:`时间 t2` 内的占空比。

.. option:: O75
   
   -Max  9999
   -Min  0
   -Unit  ms
   -Description 
     | 0 = 挺线可以一直维持；
     | 不为 0 = 经过此时间后挺线自动释放。
     
.. option:: O86
   
   -Max  999
   -Min  1
   -Unit  ms
   -Description  第二面线张力：全力 100% 占空比出力的持续 :term:`时间 t1`。

.. option:: O87
   
   -Max  100
   -Min  1
   -Unit  %
   -Description  第二面线张力：维持出力 :term:`时间 t2` 内的占空比。

.. option:: O88
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | 0 = 通电，通气，挺线打开；
     | 1 = 通电，不通气，挺线关闭。
