.. _bobbin_monitor:

==========
底线计数器
==========

使用底线计数器可以让用户大概知道锁芯余量。

**计算公式**:

.. math::
   :name: 底线余量方程

   N_{\text{余量}} 
   = O43_{\text{底线计数器复位值}} - O44_{\text{底线计数器值}}

**设置步骤**:

1. 设置合适 `O 19`_ 的值，每缝纫其设置的针数，计数值`O 44`_加1。
2. 设置合适 `O 43`_ 的值，这是个很宽泛的数值，反应你的锁芯供线能力，取决使用的锁芯大小以及缝线的粗细。
3. 设置 `O 20`_, 选择报警时机，可以选择立刻报警还是剪线后报警。
4. 将 `A 12`_ 设置为1，打开计数器功能。
5. 按照本章节开头 `底线余量方程`_ ， 当余量减小到到0时，机器将自动停车并显示告警信息，
   更换锁芯后进行重置操作。

参数列表
========

A 12
----

.. dropdown:: 底线计数 <...>
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | 底线计数功能开关：
     | 0 = 关闭；
     | 1 = 打开。

O 19
----

.. dropdown:: 底线计数因子 <...>
   :animate: fade-in-slide-down
   
   -Max  200
   -Min  1
   -Unit  针
   -Description  每缝纫因子所设置的针数，计数器加1。

O 20
----

.. dropdown:: 报警时机(底线计数) <...>
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  针
   -Description  
     | 选择当底线计数值达到0时何时报警：
     | 0 = 剪线后；
     | 1 = 立刻。
     
O 43
----

.. dropdown:: 底线计数器重置值 <...>
   :animate: fade-in-slide-down
   
   -Max  9999
   -Min  1
   -Unit  --
   -Description  梭芯供应能力，这是一个很宽泛的值，取决你使用的锁芯大小以及线的粗细。

O 44
----

.. dropdown:: 底线计数器当前值 <...>
   :animate: fade-in-slide-down
   
   -Max  9999
   -Min  0
   -Unit  --
   -Description  底线计数器当前值，预设值减去此值为余量。
