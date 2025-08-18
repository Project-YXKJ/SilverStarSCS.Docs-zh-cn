安装
====

.. attention::

    如果此类别中的某些参数设置不正确，机器可能会出现意外问题。

快速参考
--------

下表总结了安装类别所使用到的参数：

============================================================== ====== =============
参数                                                           权限   参见
============================================================== ====== =============
调速器半后踏功能                                               开发者 :option:`A19`
:term:`机头识别码`                                             开发者 :option:`O03`
调速器类型                                                     开发者 :option:`O08`
:term:`机头识别码` 存储位置                                    开发者 :option:`O30`
调速器校准：正向最大                                           开发者 :option:`O56`
调速器校准：:term:`POSITION 2` 和 :term:`POSITION 1` 分界点    开发者 :option:`O57`
调速器校准：:term:`POSITION 1` 和 :term:`POSITION 0` 分界点    开发者 :option:`O58`
调速器校准：:term:`POSITION 0` 和 :term:`POSITION -1` 分界点   开发者 :option:`O59`
调速器校准：:term:`POSITION -1` 和 :term:`POSITION -2` 分界点  开发者 :option:`O60`
调速器校准：反踩最深                                           开发者 :option:`O61`
调速器校准：施密特值                                           开发者 :option:`O62`
调速器调速曲线                                                 开发者 :option:`O63`
:term:`热键盒` 类型                                            开发者 :option:`O80`
============================================================== ====== =============

参数列表
------------

.. option:: A19

    -Max  2
    -Min  1
    -Unit  --
    -Description
      | 决定调速器处于 :term:`POSITION -1` 位置时执行什么动作
      | 1 = 抬压脚；
      | 2 = 剪线

.. option:: O03

    -Max  9999
    -Min  0
    -Unit  --
    -Description  :term:`机头识别码`

.. option:: O08

    -Max  1
    -Min  0
    -Unit  --
    -Description
      | 使用原装调速器还是站立操作踏板：
      | 0 = 原装；
      | 1 = 站立操作踏板。

.. option:: O30

    -Max  2
    -Min  1
    -Unit  --
    -Description
      | 选择 :term:`机头识别码` 存储位置:
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
    -Description  调速器正踩 :term:`POSITION 2` 和正踩 :term:`POSITION 1` 的分界点的采样值，O56 < 值 < O58

.. option:: O58

    -Max  4095
    -Min  0
    -Unit  --
    -Description  调速器正向 :term:`POSITION 1` 和 :term:`POSITION 0` 的分界点的采样值，O57 < 值 < O59

.. option:: O59

    -Max  4095
    -Min  0
    -Unit  --
    -Description  调速器 :term:`POSITION 0` 和反踩 :term:`POSITION -1` 的分界点的采样值，O58 < 值 < O60

.. option:: O60

    -Max  4095
    -Min  0
    -Unit  --
    -Description  调速器 :term:`POSITION -1` 和反踩 :term:`POSITION -2` 的分界点的采样值，O59 < 值 < O61

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

    -Max  5
    -Min  0
    -Unit  --
    -Description
      | 0 = 直线；
      | 1 = 两段直线；
      | 2 = 曲线 1：先缓后快；
      | 3 = 曲线 2：先快后缓；
      | 4 = S 曲线 1：先缓后快再缓；
      | 5 = S 曲线 2：先快后缓再快。

.. option:: O80

    -Max  3
    -Min  0
    -Unit  --
    -Description
      | 热键盒类型:
      | 0 = 无热键盒；
      | 1 = 6 键型；
      | 2 = 7 键型；
      | 3 = 12 键型。
