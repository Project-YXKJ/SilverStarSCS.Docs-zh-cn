.. _multitest:

=========
综合测试
=========

当耐久试验功能启用时，机器将会自动运转直至设定的时间结束，此时间由参数 `O 25`_ 决定。

参数列表
==============

O 23
----

.. dropdown:: 运行时间(EC) 
   :animate: fade-in-slide-down
   
   -Max  60
   -Min  1
   -Unit  s
   -Description  拖车试验一个循环的运行时间。

O 24
----

.. dropdown:: 停止时间(EC)
   :animate: fade-in-slide-down
   
   -Max  60
   -Min  1
   -Unit  s
   -Description  拖车试验停止时间。

O 25
----

.. dropdown:: 总时间(EC)
   :animate: fade-in-slide-down
   
   -Max  720
   -Min  1
   -Unit  h
   -Description  拖车试验总时间。

O 26
----

.. dropdown:: 耐久试验
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description 
     | 耐久试验功能开关：
     | 0 = 关闭；
     | 1 = 打开。
