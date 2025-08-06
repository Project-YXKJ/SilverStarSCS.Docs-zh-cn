.. _multitest:

综合测试
====

.. caution::

    请谨慎设置这些选项！

    运动、切割和锋利部件有造成伤害的危险！

当耐久试验功能启用时，机器将会自动运转直至设定的时间结束，此时间由参数 :option:`O25` 决定。

快速参考
----

下表总结了综合测试功能所使用到的参数：

======== === =============
参数       权限  参见
======== === =============
运行时间（EC） 技术员 :option:`O23`
停止时间（EC） 技术员 :option:`O24`
总时间（EC）  技术员 :option:`O25`
耐久试验     技术员 :option:`O26`
======== === =============

参数列表
----

.. option:: O23

    -Max  60
    -Min  1
    -Unit  s
    -Description  拖车试验一个循环的运行时间。

.. option:: O24

    -Max  60
    -Min  1
    -Unit  s
    -Description  拖车试验停止时间。

.. option:: O25

    -Max  720
    -Min  1
    -Unit  h
    -Description  拖车试验总时间。

.. option:: O26

    -Max  1
    -Min  0
    -Unit  --
    -Description
      | 耐久试验功能开关：
      | 0 = 关闭；
      | 1 = 打开。
