.. _control_other:

============
控制器，其他
============

快速参考
===============

下表总结了控制器，其他功能所使用到的参数：

==================================================== ========== ==============
参数                                                 权限       参见
==================================================== ========== ==============
发送间隔                                             技术员     :option:`T14`
物联网                                               技术员     :option:`A49`
操作板锁定                                           技术员     :option:`A52`
调试                                                 开发者     :option:`A58`
重置统计信息区                                       技术员     :option:`A59` 
密码使能                                             技术员     :option:`O15`
清除错误记录                                         技术员     :option:`O17`
用户密码                                             技术员     :option:`O27`
重置参数区                                           技术员     :option:`O51`
重置机械零点                                         技术员     :option:`O52`
重置所有信息                                         技术员     :option:`O66`
母线过压检测                                         技术员     :option:`O70`
交流过压检测                                         技术员     :option:`O71`
最大母线电压                                         技术员     :option:`I44`
最大AC电压                                           技术员     :option:`I45`
==================================================== ========== ==============

参数列表
========

.. option:: T14
   
   -Max  9999
   -Min  1
   -Unit  ms
   -Description  发送物联网数据的时间间隔。

.. option:: A49
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | 物联网功能（可选功能）：
     | 0 = 关闭；
     | 1 = 打开。

.. option:: A52
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | 决定压脚抬起时可否操作面板：
     | 0 = 不允许；
     | 1 = 允许操作。

.. option:: A58
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | 调试串口输出功能：
     | 0 = 关闭；
     | 1 = 打开。

.. option:: A59
   
   -Max  1
   -Min  0
   -Unit  --
   -Description  设置为1，重新开机后统计信息将恢复为默认值。

.. option:: O15
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | 进入参数调整是否需要输入用户密码：
     | 0 = 关闭；
     | 1 = 打开。

.. option:: O17
   
   -Max  1
   -Min  0
   -Unit  --
   -Description  设置为1，重启后错误记录将被清除。

.. option:: O27
   
   -Max  1
   -Min  0
   -Unit  --
   -Description  用户可自行设定的参数区密码。

.. option:: O51
   
   -Max  1
   -Min  0
   -Unit  --
   -Description  设置为1，重新开机后参数将恢复为默认值。

.. option:: O52
   
   -Max  1
   -Min  0
   -Unit  --
   -Description  设置为1，重新开机后 :term:`机械零点` 将恢复为默认值。

.. option:: O66
   
   -Max  1
   -Min  0
   -Unit  --
   -Description  设置为1，重启后参数恢复至出厂值，清除错误记录以及统计信息，
                 :term:`机械零点` 恢复至默认值。

.. option:: O70
   
   -Max  1
   -Min  0
   -Unit  --
   -Description 
     | 检测母线电压过高时是否报错：
     | 0 = 关闭；
     | 1 = 打开。
   
.. option:: O71
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | 检测到交流电压过高时是否报错：
     | 0 = 关闭；
     | 1 = 打开。

.. option:: I44
   
   -Max  460
   -Min  400
   -Unit  V
   -Description  母线电压的最大值

.. option:: I45
   
   -Max  300
   -Min  260
   -Unit  V
   -Description  AC 220V 电压的最大值
