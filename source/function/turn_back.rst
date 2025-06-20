.. _turn_back:

========
剪线回拉
========

设置 :option:`A13` 为 1，可以选择启用反转提针，此功能方便取出缝料以避免机针刮伤面料。

在剪线流程结束之后，延迟 :option:`T12` 设定的时间之后，
提针速度被限制在 :option:`S16` 之内，当位置达到 :option:`O35` 后，电机停止。

快速参考
===============

下表总结了剪线回拉功能所使用到的参数：

==================================================== ========== ==============
参数                                                 权限       参见
==================================================== ========== ==============
剪线回拉                                             操作员     :option:`A13`
反拉速度                                             技术员     :option:`S16`
反拉延迟时间                                         技术员     :option:`T12`
剪线反转目标位置                                     技术员     :option:`O35`
==================================================== ========== ==============

参数列表
========

.. option:: A13
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | 剪线后提针回拉：
     | 0 = 关闭；
     | 1 = 打开。

.. option:: S16
   
   -Max  1000
   -Min  50
   -Unit  spm
   -Description  剪线后提针反拉速度。

.. option:: T12
   
   -Max  1000
   -Min  1
   -Unit  ms
   -Description  剪线完成后经过此延时时间机针开始反转。

.. option:: O35
   
   -Max  359
   -Min  0
   -Unit  1°
   -Description  剪线反转后针杆到达的位置。
