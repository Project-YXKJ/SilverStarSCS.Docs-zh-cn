.. _daily_piece_counter:

===================
产量统计
===================

快速参考
===============

下表总结了产量统计功能所使用到的参数：

==================================================== ========== ==============
参数                                                 权限       参见
==================================================== ========== ==============
产量统计                                             技术员     :option:`A11`
计件判定针数                                         技术员     :option:`O45`
计件判定剪线次数                                     技术员     :option:`O46`
已计件数                                             技术员     :option:`O47`
==================================================== ========== ==============

参数列表
==============

.. option:: A11
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | 产量统计计数器功能开关：
     | 0 = 关闭；
     | 1 = 打开。

.. option:: O45
   
   -Max  999
   -Min  1
   -Unit  针
   -Description  超过此针数判定为计件有效。

.. option:: O46
   
   -Max  99
   -Min  1
   -Unit  --
   -Description  超过此剪线次数判定为计件有效。

.. option:: O47
   
   -Max  9999
   -Min  0
   -Unit  --
   -Description  当前计件计数器的值。
