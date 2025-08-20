剪线
====

剪线执行流程
    在达到 :option:`D03` 设置的位置后，剪线电磁铁接通，之后达到 :option:`D04` 的位置后关断。

    如果在剪线过程发生机械堵转，那么剪线电磁铁会在500毫秒之后自动关断，以防止烧毁电磁铁。

使能短线头
----------

配备短剪线系统的缝纫机可通过参数 :option:`A42` 使能短线头功能，剪线功能必须同时开启。

快速参考
--------

下表总结了剪线功能所使用到的参数：

================================== ====== =============
参数                               权限   参见
================================== ====== =============
剪线功能                           操作员 :option:`A06`
剪线速度                           技术员 :option:`S07`
短线头功能                         技术员 :option:`A42`
短线头针数                         技术员 :option:`A67`
剪线接通角度                       技术员 :option:`D03`
剪线关断角度                       技术员 :option:`D04`
短线头动刀接通角度                 技术员 :option:`D17`
短线头动刀关断角度                 技术员 :option:`D18`
短线头倒缝接通角度                 技术员 :option:`D19`
短线头倒缝关断角度                 技术员 :option:`D20`
短线头零针距接通角度               技术员 :option:`D21`
短线头零针距关断角度               技术员 :option:`D22`
剪线后检查调速器位置               技术员 :option:`O38`
短线头零针距：全力时间             开发者 :option:`O95`
短线头零针距：维持出力阶段的占空比 开发者 :option:`O96`
================================== ====== =============

参数列表
--------

.. option:: A06

    -Max  1
    -Min  0
    -Unit  --
    -Description
      | 剪线功能开关：
      | 0 = 关闭；
      | 1 = 打开

.. option:: S07

    -Max  1000
    -Min  50
    -Unit  spm
    -Description  剪线动作的速度

.. option:: A42

    -Max  1
    -Min  0
    -Unit  --
    -Description
      | 可选功能, 只针对特定型号：
      | 0 = 关闭；
      | 1 = 打开

.. option:: A67

    -Max  10
    -Min  0
    -Unit  针
    -Description  短线头功能打开时，剪线前的小针距针数

.. option:: D03

    -Max  359
    -Min  0
    -Unit  1°
    -Description  剪线信号接通角度

.. option:: D04

    -Max  359
    -Min  0
    -Unit  1°
    -Description  剪线信号关断角度

.. option:: D17

    -Max  359
    -Min  0
    -Unit  1°
    -Description  短线头动刀信号接通角度

.. option:: D18

    -Max  359
    -Min  0
    -Unit  1°
    -Description  短线头动刀信号关断角度

.. option:: D19

    -Max  359
    -Min  0
    -Unit  1°
    -Description  短线头倒缝信号接通角度

.. option:: D20

    -Max  359
    -Min  0
    -Unit  1°
    -Description  短线头倒缝信号关断角度

.. option:: D21

    -Max  359
    -Min  0
    -Unit  1°
    -Description  短线头零针信号体接通角度

.. option:: D22

    -Max  359
    -Min  0
    -Unit  1°
    -Description  短线头零针信号体关断角度

.. option:: O38

    -Max  1
    -Min  0
    -Unit  --
    -Description
      | 剪线后开始一段新线迹之前，调速器是否需要回到位置0：
      | 0 = 关闭；
      | 1 = 打开

.. option:: O95

    -Max  999
    -Min  1
    -Unit  ms
    -Description  短线头零针距：全力时间，:term:`时间 t1`

.. option:: O96

    -Max  100
    -Min  1
    -Unit  %
    -Description  短线头零针距：维持出力阶段 :term:`时间 t2` 的占空比
