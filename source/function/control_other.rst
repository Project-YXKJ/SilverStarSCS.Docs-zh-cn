.. _control_other:

============
控制器, 其他
============

参数列表
========

T 14
----

.. dropdown:: 发送间隔 <...>
   :animate: fade-in-slide-down
   
   -Max  9999
   -Min  1
   -Unit  毫秒
   -Description  发送物联网数据的时间间隔

A 49
----

.. dropdown:: 物联网 <...>
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | 物联网功能(可选功能):
     | 0 = 关闭；
     | 1 = 打开。

A 52
----

.. dropdown:: 操作板锁定 <...>
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | 决定压脚抬起时可否操作面板:
     | 0 = 不允许;
     | 1 = 允许操作.

A 58
----

.. dropdown:: 调试 <...> 
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | 调试串口输出功能:
     | 0 = 关闭；
     | 1 = 打开。

A 59
----

.. dropdown:: 重置统计信息区 <...> 
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description  设置为1,重新开机后统计信息将恢复为默认值.

O 15
----

.. dropdown:: 密码使能 <...>
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | 进入参数调整是否需要输入用户密码:
     | 0 = 关闭；
     | 1 = 打开。

O 17
----

.. dropdown:: 清除错误记录 <...>
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description  设置为1,重启后错误记录将被清除.

O 27
----

.. dropdown:: 用户密码 <...>
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description  用户可自行设定的参数区密码.

O 51
----

.. dropdown:: 重置参数区 <...>
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description  设置为1,重新开机后参数将恢复为默认值.

O 52
----

.. dropdown:: 重置机械零点 <...>
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description  设置为1,重新开机后 :term:`机械零点` 将恢复为默认值.

O 66
----

.. dropdown:: 重置所有信息 <...>
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description  设置为1, 重启后参数恢复至出厂值, 清除错误记录以及统计信息,
                 :term:`机械零点` 恢复至默认值

O 70
----

.. dropdown:: 母线过压检测 <...>
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description 
     | 检测母线电压过高时是否报错:
     | 0 = 关闭；
     | 1 = 打开。
   
O 71
----

.. dropdown:: 交流过压检测 <...>
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | 检测到交流电压过高时是否报错:
     | 0 = 关闭；
     | 1 = 打开。


I 44
----

.. dropdown:: 最大母线电压 <...>
   :animate: fade-in-slide-down
   
   -Max  460
   -Min  400
   -Unit  --
   -Description  母线电压的最大值

I 45
----

.. dropdown:: 最大AC电压 <...>
   :animate: fade-in-slide-down
   
   -Max  300
   -Min  260
   -Unit  V
   -Description  AC 220v电压的最大值
