.. _second_stitch_length:

第二针距
====

根据设备的不同，机器可用于缝制两种不同的针迹长度，并且可以通过按按钮来激活第二针距。

自动化规则
-----

自动化消除了手动执行重复性任务的繁琐，对于第二针距有以下规则：

长针距自动限速
-------

如果参数 :option:`O33` 设置为 1，当切换到长针距时缝纫速度将被限制在参数 :option:`S17` 所设置的值。

快速参考
----

下表总结了第二针距功能所使用到的参数：

======== === =============
参数       权限  参见
======== === =============
大小针距     操作员 :option:`A46`
大针距限速值   操作员 :option:`S17`
大小针距状态   技术员 :option:`A25`
加固缝针距    技术员 :option:`A50`
针距限速     技术员 :option:`O33`
时间（t1）   开发者 :option:`O78`
维持出力（t2） 开发者 :option:`O79`
======== === =============

参数列表
----

.. option:: A46

    -Max  1
    -Min  0
    -Unit  --
    -Description
      | 大小针距功能：
      | 0 = 关闭；
      | 1 = 打开。

.. option:: S17

    -Max  4500
    -Min  50
    -Unit  spm
    -Description  当使用大针距时的限速值。

.. option:: A25

    -Max  1
    -Min  0
    -Unit  --
    -Description  大小针距状态（只读）。

.. option:: A50

    -Max  1
    -Min  0
    -Unit  --
    -Description
      | 选择是否在前后加固时自动切换到小针距：
      | 0 = 关闭；
      | 1 = 打开。

.. option:: O33

    -Max  1
    -Min  0
    -Unit  --
    -Description
      | 当切换为大针距时进行限速：
      | 0 = 关闭；
      | 1 = 打开。

.. option:: O78

    -Max  999
    -Min  1
    -Unit  ms
    -Description  第二针距：全力 100% 占空比出力的持续 :term:`时间 t1` 。

.. option:: O79

    -Max  100
    -Min  1
    -Unit  %
    -Description  第二针距：维持出力 :term:`时间 t2` 内的占空比。
