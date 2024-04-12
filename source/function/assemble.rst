.. _assemble:

====
安装
====

.. attention::
   如果此类别中的某些参数设置不正确，机器可能会出现意外问题。

快速参考
===============

下表总结了安装类别所使用到的参数：

==================================================== ========== ==============
参数                                                 权限       参见
==================================================== ========== ==============
机头热键锁定                                         开发者     :option:`A07`
调速器半后踏功能                                     开发者     :option:`A19` 
机头识别码                                           开发者     :option:`O03` 
调速器类型                                           开发者     :option:`O08` 
机头识别器存储位置                                   开发者     :option:`O30` 
调速器校准:正向最大                                  开发者     :option:`O56`
调速器校准:POSITION 2 and POSITION 1                 开发者     :option:`O57`
调速器校准:POSITION 1 and POSITION 0                 开发者     :option:`O58`
调速器校准:POSTIION 0 and POSTIION -1                开发者     :option:`O59`
调速器校准:POSTIION -1 and POSTIION -2               开发者     :option:`O60`
调速器校准:反踩最深                                  开发者     :option:`O61`
调速器校准:施密特值                                  开发者     :option:`O62`
调速器调速曲线                                       开发者     :option:`O63`
热键盒类型                                           开发者     :option:`O80`
==================================================== ========== ==============


参数列表
========

.. option:: A07
   
   -Max  1  
   -Min  0
   -Unit  --
   -Description
     | 缝料过厚时，用于防止缝料误触热键:
     | 0 = 关闭；
     | 1 = 打开。

.. option:: A19
   
   -Max  2
   -Min  1
   -Unit  --
   -Description  
     | 决定调速器处于 :term:`POSITION -1` 位置时执行什么动作
     | 1 = Sewing foot lift；
     | 2 = Thread trim。

.. option:: O03
   
   -Max  2
   -Min  1
   -Unit  --
   -Description  :term:`机头识别码`

.. option:: O08

   -Max  2
   -Min  1
   -Unit  --
   -Description
     | 使用原装调速器还是站立操作踏板：
     | 0 = 原装；
     | 1 = 站立操作踏板。

.. option:: O30
   
   -Max  9999
   -Min  0
   -Unit  --
   -Description  
     | 选择 :term:`机头识别码` 
       存储位置:
     | 1 = 存储于控制器中；
     | 2 = 存储与机头识别器中。

.. option:: O56

   -Max  4095  
   -Min  0
   -Unit  --
   -Description  调速器正向踩到底时的电压采样值，值 > O57

.. option:: O57

   -Max  4095  
   -Min  0
   -Unit  --
   -Description  调速器正踩第二段和正踩第一段的分界点的采样值，O56 < 值 < O58

.. option:: O58

   -Max  4095  
   -Min  0
   -Unit  --
   -Description  调速器正向第一段和默认位置的分界点的采样值，O57 < 值 < O59

.. option:: O59

   -Max  4095  
   -Min  0
   -Unit  --
   -Description  调速器默认位置和反踩第一段的分界点的采样值，O58 < 值 < O60

.. option:: O60

   -Max  4095  
   -Min  0
   -Unit  --
   -Description  调速器反踩第一段和反踩第二段的分界点的采样值，O59 < 值 < O61

.. option:: O61

   -Max  4095  
   -Min  0
   -Unit  --
   -Description  调速器反踩到最深处时采样值，值 < O60

.. option:: O62

   -Max  4095  
   -Min  0
   -Unit  --
   -Description  调速器施密特区间的采样值

.. option:: O63

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

.. option:: O80
   
   -Max  3  
   -Min  1
   -Unit  --
   -Description
     | Type of the keypad:
     | 1 = 6键型；
     | 2 = 7键型；
     | 3 = 12键型。
