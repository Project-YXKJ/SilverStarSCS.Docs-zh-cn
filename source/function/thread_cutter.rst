.. _thread_cutter:

剪线
==

如何运行？
-----

剪线执行流程：

在达到 :option:`D03` 设置的位置后，剪线电磁铁接通，之后达到 :option:`D04` 的位置后关断。

如果在剪线过程发生机械堵转，那么剪线电磁铁会在500毫秒之后自动关断，以防止烧毁电磁铁。

快速参考
----

下表总结了剪线功能所使用到的参数：

============ === =============
参数           权限  参见
============ === =============
剪线功能         操作员 :option:`A06`
剪线速度         技术员 :option:`S07`
短线头功能        技术员 :option:`A42`
短线头针数        技术员 :option:`A67`
剪线开始角度       技术员 :option:`D03`
剪线结束角度       技术员 :option:`D04`
动刀开始角度（STC）  技术员 :option:`D17`
动刀结束角度（STC）  技术员 :option:`D18`
倒缝开始角度（STC）  技术员 :option:`D19`
倒缝结束角度（STC）  技术员 :option:`D20`
零针距开始角度（STC） 技术员 :option:`D21`
零针距结束角度（STC） 技术员 :option:`D22`
剪线后检查调速器位置   技术员 :option:`O38`
时间（t1）       开发者 :option:`O95`
维持出力（t2）     开发者 :option:`O96`
============ === =============

参数列表
----

.. option:: A06

    -Max  1
    -Min  0
    -Unit  --
    -Description
      | 剪线功能开关：
      | 0 = 关闭；
      | 1 = 打开。

.. option:: S07

    -Max  1000
    -Min  50
    -Unit  spm
    -Description  剪线动作的速度。

.. option:: A42

    -Max  1
    -Min  0
    -Unit  --
    -Description
      | 可选功能, 只针对特定型号：
      | 0 = 关闭；
      | 1 = 打开。

.. option:: A67

    -Max  10
    -Min  0
    -Unit  针
    -Description  短线头功能打开时，剪线前的小针距针数。

.. option:: D03

    -Max  359
    -Min  0
    -Unit  1°
    -Description  剪线电磁铁动作角度。

.. option:: D04

    -Max  359
    -Min  0
    -Unit  1°
    -Description  剪线电磁铁释放角度。

.. option:: D17

    -Max  359
    -Min  0
    -Unit  1°
    -Description  短线头机型剪线时动刀电磁铁动作角度。

.. option:: D18

    -Max  359
    -Min  0
    -Unit  1°
    -Description  短线头机型剪线时动刀电磁铁释放角度。

.. option:: D19

    -Max  359
    -Min  0
    -Unit  1°
    -Description  短线头机型剪线时倒缝电磁体动作角度。

.. option:: D20

    -Max  359
    -Min  0
    -Unit  1°
    -Description  短线头机型剪线时倒缝电磁体释放角度。

.. option:: D21

    -Max  359
    -Min  0
    -Unit  1°
    -Description  短线头机型剪线时零针距电磁体动作角度。

.. option:: D22

    -Max  359
    -Min  0
    -Unit  1°
    -Description  短线头机型剪线时零针距电磁体释放角度。

.. option:: O38

    -Max  1
    -Min  0
    -Unit  --
    -Description
      | 剪线后开始一段新线迹之前，调速器是否需要回到位置0：
      | 0 = 关闭；
      | 1 = 打开。

.. option:: O95

    -Max  999
    -Min  1
    -Unit  ms
    -Description  短线头零针距：全力 100% 占空比出力的持续 :term:`时间 t1` 。

.. option:: O96

    -Max  100
    -Min  1
    -Unit  %
    -Description  短线头零针距：维持出力 :term:`时间 t2` 内的占空比。
