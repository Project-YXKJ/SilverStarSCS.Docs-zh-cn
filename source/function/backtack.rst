前后加固
========

线迹重合性调整
--------------

.. important::

    在调整之前，请确保机械已经校准完毕，使用倒缝扳手时正缝和倒缝针距一致。

正缝转入倒缝时出现针迹不一致的情况，调整 :option:`T01` 可以参考下面进行调整：

.. figure:: ../_static/common/add_t01.excalidraw.svg
    :scale: 150 %
    :alt: Increase T01

    增大 T01

.. figure:: ../_static/common/sub_t01.excalidraw.svg
    :scale: 150 %
    :alt: Decrease T01

    减小 T01

倒缝转入正缝时出现针迹不一致的情况，调整 :option:`T02` 可以参考下面进行调整：

.. figure:: ../_static/common/add_t02.excalidraw.svg
    :scale: 150 %
    :alt: Increase T02

    增大 T02

.. figure:: ../_static/common/sub_t02.excalidraw.svg
    :scale: 150 %
    :alt: Decrease T02

    减小 T02

SD 模式
-------

SD 模式是前后加固的一种特殊模式，用于尽可能的保证对针眼效果。

当 SD 模式启用时，在加固转折点，电机会停车，并且等待 :option:`T11` 所设置的时间，确保倒缝动作到位， 之后继续运行。

可以分别对前加固或者后加固启动 SD 模式，由 :option:`A20` 和 :option:`A22` 控制。

快速参考
--------

下表总结了前后加固功能所使用到的参数：

========================== ====== =============
参数                       权限   参见
========================== ====== =============
前加固速度                 操作员 :option:`S03`
后加固速度                 操作员 :option:`S04`
前加固SD模式选择           操作员 :option:`A20`
后加固SD模式选择           操作员 :option:`A22`
倒缝电磁铁吸合到位所需时间 技术员 :option:`T01`
倒缝电磁铁释放到位所需时间 技术员 :option:`T02`
SD模式拐点停顿时间         技术员 :option:`T11`
前加固后恒定速度           技术员 :option:`A34`
倒缝开始角度               技术员 :option:`D05`
倒缝结束角度               技术员 :option:`D06`
倒缝自动释放使能           技术员 :option:`O10`
倒缝最大维持时间           技术员 :option:`O11`
1 针的限速                 技术员 :option:`O12`
2 针的限速                 技术员 :option:`O13`
3 针的限速                 技术员 :option:`O14`
前加固匀速保持针数         技术员 :option:`O41`
时间（t1）                 开发者 :option:`T08`
维持出力（t2）             开发者 :option:`O09`
========================== ====== =============

参数列表
------------

.. option:: S03

    -Max  4500
    -Min  50
    -Unit  spm
    -Description  前加固能达到的最大速度

.. option:: S04

    -Max  4500
    -Min  50
    -Unit  spm
    -Description  后加固能达到的最大速度

.. option:: A20

    -Max  1
    -Min  0
    -Unit  --
    -Description
      | 设为 1 时，前加固在缝纫方向转换时电机会停下来等待倒缝动作：
      | 0 = 关闭；
      | 1 = 打开。

.. option:: A22

    -Max  1
    -Min  0
    -Unit  --
    -Description
      | 设为 1 时，后加固在缝纫方向转换时电机会停下来等待倒缝动作：
      | 0 = 关闭；
      | 1 = 打开。

.. option:: T01

    -Max  200
    -Min  1
    -Unit  ms
    -Description  倒缝电磁铁从开始动作到吸合到位需要的时间。

.. option:: T02

    -Max  200
    -Min  1
    -Unit  ms
    -Description  倒缝电磁铁从开始动作到释放到位需要的时间。

.. option:: T11

    -Max  1000
    -Min  1
    -Unit  ms
    -Description  SD加固模式下，加固缝缝纫方向转换点电机停下来等待倒缝电磁铁动作到位的时间。

.. option:: A34

    -Max  1
    -Min  0
    -Unit  --
    -Description
      | 为了使线迹重合效果更好，前加固结束后维持当前加固速度，若干针后速度才由调速器接管：
      | 0 = 关闭；
      | 1 = 打开。

.. option:: D05

    -Max  359
    -Min  0
    -Unit  1°
    -Description  倒缝电磁铁动作角度。

.. option:: D06

    -Max  359
    -Min  0
    -Unit  1°
    -Description  倒缝电磁铁释放角度。

.. option:: O10

    -Max  1
    -Min  0
    -Unit  --
    -Description
      | 经过一定时间后抬倒缝电磁铁是否自动释放：
      | 0 = 关闭；
      | 1 = 打开。

.. option:: O11

    -Max  30
    -Min  5
    -Unit  s
    -Description  如果自动释放打开，倒缝释放时间由此参数设置。

.. option:: O12

    -Max  4500
    -Min  50
    -Unit  spm
    -Description  前后加固，折返缝只有 1 针时限速。

.. option:: O13

    -Max  4500
    -Min  50
    -Unit  spm
    -Description  前后加固，折返缝只有 2 针时限速。

.. option:: O14

    -Max  4500
    -Min  50
    -Unit  spm
    -Description  前后加固，折返缝只有 3 针时限速。

.. option:: O41

    -Max  10
    -Min  0
    -Unit  针
    -Description  前加固后保持当前速度的针数，之后速度才由调速器接管。

.. option:: T08

    -Max  999
    -Min  1
    -Unit  ms
    -Description  倒缝：全力 100% 占空比出力的持续 :term:`时间 t1` 。

.. option:: O09

    -Max  100
    -Min  1
    -Unit  %
    -Description  倒缝：维持出力 :term:`时间 t2` 内的占空比。
