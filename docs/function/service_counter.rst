.. _service_counter: 

===============
保养计数器
===============

使用保养计数器可以让提醒用户定期进行机器维护。

**计算公式**:

.. math::
   :name: 保养余量方程

   N_{\text{余量}}
    = A61_{\text{保养计数器复位值}} - A63_{\text{保养计数器值}}.

**设置步骤**:

1. 设置合适的值给 `A 62`_ ，每缝纫其设置的针数，计数器加1。
2. 根据实际需要保养间隔，设置 `A 61`_ 的值。
3. 将 `A 60`_ 设置为1，打开计数器功能。
4. 按照本章节开头 `保养余量方程`_ ，当余量减小到到0时，机器将自动停车并显示告警信息，
   进行保养后进行重置操作。

参数列表
==============

A 60
----

.. dropdown:: 保养计数器
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | 激活保养针数计数器：
     | 0 = 关闭；
     | 1 = 打开。

A 61
----

.. dropdown:: 保养计数器复位值
   :animate: fade-in-slide-down
   
   -Max  9999
   -Min  1
   -Unit  --
   -Description  保养针数计数器的复位值。
   
A 62
----

.. dropdown:: 保养计数器因子
   :animate: fade-in-slide-down
   
   -Max  200
   -Min  1
   -Unit  针
   -Description  决定机器每缝制多少针保养计数器计数值才加1。

A 63
----

.. dropdown:: 保养计数器值
   :animate: fade-in-slide-down
   
   -Max  9999
   -Min  0
   -Unit  -- 
   -Description  保养针数计数器的当前计数值。
