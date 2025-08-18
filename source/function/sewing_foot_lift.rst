缝制压脚
========

功能特性
--------

抬压脚
~~~~~~

- **线迹中** ：反踩调速器至半后踏（\ :term:`POSITION -1`\ ），或者当 :option:`A14` 设置为 1 时自动抬起；
- **剪线之后** ：反踩调速器（\ :term:`POSITION -1` 或 :term:`POSITION -2`\ ），或者 当 :option:`A15` 设置为
  1 时自动抬起。

压脚抬起后的维持力度
~~~~~~~~~~~~~~~~~~~~

抬压脚一开始是全力输出的，之后会自动切换到 PWM 控制，以减少控制器和电磁铁（阀）上承载的电流。

全力输出时间由参数 :option:`T07` 决定，维持力度由参数 :option:`O05` 控制。

定时释放
~~~~~~~~

为了减少热量产生，尤其是压脚由电磁铁驱动时，可以设置定时释放。

将参数 :option:`O06` 设置为 1，压脚最大抬起时间由参数 :option:`O07` 决定。

下落时间
~~~~~~~~

当压脚处于抬起状态时，为了保证缝料被压紧之后机器才开始运行，当前踩调速器机时一段延时时间会插入， 此时间由参数 :option:`T06` 控制。

快速参考
--------

下表总结了缝制压脚功能所使用到的参数：

============================== ====== =============
参数                           权限   参见
============================== ====== =============

压脚功能                       操作员 :option:`A09`
抬压脚位置判断时间             技术员 :option:`T05`
压脚下落时间                   技术员 :option:`T06`
自动压脚延迟时间               技术员 :option:`T10`
中间停车后自动抬压脚           技术员 :option:`A14`
剪线后自动抬压脚               技术员 :option:`A15`
压脚自动释放                   技术员 :option:`O06`
压脚最大抬起时间               技术员 :option:`O07`
压脚缓放                       技术员 :option:`O39`
时间（t1）                     开发者 :option:`T07`
维持出力（t2）                 开发者 :option:`O05`
抬压脚缓放力度                 技术员 :option:`O40`
夹线时压脚微抬力度（无前加固） 技术员 :option:`O53`
夹线时压脚微抬力度（缓缝）     技术员 :option:`O54`
夹线时压脚微抬力度             技术员 :option:`O55`
============================== ====== =============

参数列表
--------

.. option:: A09

    -Max  1
    -Min  0
    -Unit  --
    -Description
      | 压脚功能开关：
      | 0 = 关闭；
      | 1 = 打开。

.. option:: T05

    -Max  500
    -Min  1
    -Unit  ms
    -Description  抬压脚等待时间，用于反踩剪线时避免抬压脚动作。

.. option:: T06

    -Max  500
    -Min  1
    -Unit  ms
    -Description  压脚下落需要的时间，缝制开始之前延迟一段时间，确保压脚已经压紧了缝料。

.. option:: T10

    -Max  500
    -Min  1
    -Unit  ms
    -Description  自动压脚功能打开时，延迟抬压脚的时间。

.. option:: A14

    -Max  1
    -Min  0
    -Unit  --
    -Description
      | 在一段线迹的中间部分停车时自动抬起压脚：
      | 0 = 关闭；
      | 1 = 打开。

.. option:: A15

    -Max  1
    -Min  0
    -Unit  --
    -Description
      | 在剪线后或者一段线迹的结束后自动抬起压脚：
      | 0 = 关闭；
      | 1 = 打开。

.. option:: O06

    -Max  1
    -Min  0
    -Unit  --
    -Description
      | 经过一定时间后抬压脚电磁铁是否自动释放：
      | 0 = 关闭；
      | 1 = 打开。

.. option:: O07

    -Max  30
    -Min  5
    -Unit  s
    -Description  如果自动释放打开，压脚释放时间由此参数设置。

.. option:: O39

    -Max  1
    -Min  0
    -Unit  --
    -Description
      | 通过 PWM 控制，减缓压脚下落速度：
      | 0 = 关闭；
      | 1 = 打开。

.. option:: T07

    -Max  999
    -Min  1
    -Unit  ms
    -Description  压脚：全力 100% 占空比出力的持续 :term:`时间 t1` 。

.. option:: O05

    -Max  100
    -Min  1
    -Unit  %
    -Description  压脚：维持出力 :term:`时间 t2` 内的占空比。

.. option:: O40

    -Max  9
    -Min  1
    -Unit  --
    -Description  数值越大，压脚下落速度越慢。

.. option:: O53

    -Max  10
    -Min  1
    -Unit  --
    -Description  自由缝无前后加固时，起缝夹线时压脚微抬占空比。

.. option:: O54

    -Max  10
    -Min  1
    -Unit  --
    -Description  起针缓缝打开时，起缝夹线时压脚微抬占空比。

.. option:: O55

    -Max  10
    -Min  1
    -Unit  --
    -Description  起缝夹线时压脚微抬占空比。
