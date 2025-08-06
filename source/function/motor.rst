.. _motor:

电机
==

静止时的电机保持力
---------

打开此功能，需要将 :option:`A54` 设置为 1。

此功能可防止机器停止时机针意外偏移，可通过转动手轮检查效果。

此功能生效期间，电机会保持一定的力量来 *锁定* 在当前位置，但这里的 *锁定* 不代表 *静止*\ ，
如果参数设置不当，或者电机所处位置外力过大/过小，都可能导致针杆上下抖动。

保持力生效时机：

- 一段线迹的中间停车
- 线迹结束后的剪线停车

保持力维持调节的最大时间由参数 :option:`A66` 决定：

等于0
    那么保持力在停车时可以一直维持。

不等于0
    那么保持力在停车时只是维持一定时间，之后释放电机，此时参数值表示维持时间。

该效果的力度可以通过参数 :option:`I46` 设定，值越高，保持力越强。

快速参考
----

下表总结了电机功能所使用到的参数：

=================== === =============
参数                  权限  参见
=================== === =============
最高限速                技术员 :option:`S01`
最低缝速                技术员 :option:`S02`
上电自动上针位             技术员 :option:`A18`
电机保持力               技术员 :option:`A54`
锁定齿（CPC-h）          开发者 :option:`A55`
偏移角度大于此值开始调节（CPC-h） 开发者 :option:`A56`
偏移角度小于此值调节结束（CPC-h） 开发者 :option:`A57`
电机保持力模式             技术员 :option:`A66`
机头同步信号来源            技术员 :option:`O04`
输入速度打折              技术员 :option:`O36`
简易模式                技术员 :option:`O37`
电机旋转方向              开发者 :option:`O67`
加速度                 技术员 :option:`I01`
减速度                 技术员 :option:`I02`
电角度                 开发者 :option:`I03`
传动比                 开发者 :option:`I04`
Kp（CSC-t）           开发者 :option:`I05`
Kp增益（CSC-t）         开发者 :option:`I06`
Ki（CSC-t）           开发者 :option:`I07`
Ki增益（CSC-t）         开发者 :option:`I08`
Kp（CSC）             开发者 :option:`I09`
Kp增益（CSC）           开发者 :option:`I10`
Ki（CSC）             开发者 :option:`I11`
Ki增益（CSC）           开发者 :option:`I12`
输出上限（CSC）           开发者 :option:`I13`
前馈（CSC）             开发者 :option:`I14`
Kp（CCC-d）           开发者 :option:`I15`
Kp增益（CCC-d）         开发者 :option:`I16`
Ki（CCC-d）           开发者 :option:`I17`
Ki增益（CCC-d）         开发者 :option:`I18`
输出上限（CCC-d）         开发者 :option:`I19`
输出下限（CCC-d）         开发者 :option:`I20`
Kp（CCC-q）           开发者 :option:`I21`
Kp增益（CCC-q）         开发者 :option:`I22`
Ki（CCC-q）           开发者 :option:`I23`
Ki增益（CCC-q）         开发者 :option:`I24`
输出上限（CCC-q）         开发者 :option:`I25`
输出下限（CCC-q）         开发者 :option:`I26`
码盘分辨率               开发者 :option:`I27`
停车流程限时              开发者 :option:`I28`
停车模式                开发者 :option:`I30`
机械零点偏移量             开发者 :option:`I33`
刹车P-S阶段距离           开发者 :option:`I37`
刹车P-S阶段初速度          开发者 :option:`I38`
刹车P-S阶段末速度          开发者 :option:`I39`
Kp（CPC-s）           开发者 :option:`I40`
Kp增益（CPC-s）         开发者 :option:`I41`
Kd（CPC-s）           开发者 :option:`I42`
Kd增益（CPC-s）         开发者 :option:`I43`
最大锁定电流              开发者 :option:`I46`
弱磁                  开发者 :option:`I47`
弱磁生效速度              开发者 :option:`I48`
弱磁扩速电流              开发者 :option:`I49`
输出上限（CPC-h）         开发者 :option:`I50`
输出下限（CPC-h）         开发者 :option:`I51`
Kp（CPC-h）           开发者 :option:`I52`
Kp增益（CPC-h）         开发者 :option:`I53`
Kd（CPC-h）           开发者 :option:`I54`
Kd增益（CPC-h）         开发者 :option:`I55`
=================== === =============

参数列表
----

.. option:: S01

    -Max  4500
    -Min  50
    -Unit  spm
    -Description  调速器踩至最深时的最大速度。

.. option:: S02

    -Max  1000
    -Min  50
    -Unit  spm
    -Description  调速器处于位置 1 即低速段时的缝制速度，也是补针速度。

.. option:: A18

    -Max  1
    -Min  0
    -Unit  --
    -Description
      | 上电后电机自动运行至上针位：
      | 0 = 关闭；
      | 1 = 打开。

.. danger::

    请谨慎设置 A18 参数，可能会导致人身危险。

.. option:: A54

    -Max  1
    -Min  0
    -Unit  --
    -Description
      | 停车时是否让电机维持一定的力度来锁定在当前位置：
      | 0 = 关闭；
      | 1 = 打开。

.. option:: A55

    -Max  720
    -Min  1
    -Unit  --
    -Description  锁定在此角度内。

.. option:: A56

    -Max  720
    -Min  1
    -Unit  --
    -Description  位置误差大于此值开始调节。

.. option:: A57

    -Max  720
    -Min  1
    -Unit  --
    -Description  位置误差小于此值结束调节。

.. option:: A66

    -Max  1
    -Min  0
    -Unit  --
    -Description
      | 0 = 一直维持；
      | 不为0 = 此参数表示维持的时间，设置的时间过后保持力消失。

.. option:: O04

    -Max  1
    -Min  0
    -Unit  --
    -Description
      | 0 = 外置针位检测器；
      | 1 = 电机自带。

.. option:: O36

    -Max  5
    -Min  0
    -Unit  --
    -Description  对输入速度比例缩小使机器运行速度比设定低，参数值每增大 1，减少十分之一。

.. option:: O37

    -Max  1
    -Min  0
    -Unit  --
    -Description
      | 简易模式下，除了电机可以运行, 没有缝型、剪线、停针位等功能：
      | 0 = 关闭；
      | 1 = 打开。

.. option:: O67

    -Max  1
    -Min  0
    -Unit  --
    -Description
      | 0 = 逆时针；
      | 1 = 顺时针，视角为手轮方向看电机。

.. option:: I01

    -Max  500
    -Min  150
    -Unit  ms
    -Description  0 ~ 4500rpm 加速时间。

.. option:: I02

    -Max  500
    -Min  150
    -Unit  ms
    -Description  4500rpm ~ 0 减速时间。

.. option:: I03

    -Max  4096
    -Min  0
    -Unit  --
    -Description  电角度补偿值。

.. option:: I04

    -Max  4096
    -Min  1
    -Unit  --
    -Description  主轴转动一周对应的电机编码信号数量。

.. option:: I05

    -Max  9999
    -Min  0
    -Unit  --
    -Description  剪线速度环 Kp。

.. option:: I06

    -Max  99
    -Min  0
    -Unit  --
    -Description  剪线速度环 Kp 增益系数。

.. option:: I07

    -Max  9999
    -Min  0
    -Unit  --
    -Description  剪线速度环 Ki。

.. option:: I08

    -Max  99
    -Min  0
    -Unit  --
    -Description  剪线速度环 Ki 增益。

.. option:: I09

    -Max  9999
    -Min  0
    -Unit  --
    -Description  速度环 Kp。

.. option:: I10

    -Max  99
    -Min  0
    -Unit  --
    -Description  速度环 Kp增益。

.. option:: I11

    -Max  9999
    -Min  0
    -Unit  --
    -Description  速度环 Ki。

.. option:: I12

    -Max  99
    -Min  0
    -Unit  --
    -Description  速度环 Ki增益。

.. option:: I13

    -Max  20
    -Min  1
    -Unit  --
    -Description  速度环输出上限。

.. option:: I14

    -Max  500
    -Min  0
    -Unit  --
    -Description  速度环前馈系数。

.. option:: I15

    -Max  9999
    -Min  0
    -Unit  --
    -Description  电流环 d 轴 Kp。

.. option:: I16

    -Max  99
    -Min  0
    -Unit  --
    -Description  电流环 d 轴 Kp增益。

.. option:: I17

    -Max  9999
    -Min  0
    -Unit  --
    -Description  电流环 d 轴 Ki。

.. option:: I18

    -Max  99
    -Min  0
    -Unit  --
    -Description  电流环 d 轴 Ki增益。

.. option:: I19

    -Max  3276
    -Min  0
    -Unit  --
    -Description  电流环 Id 输出上限。

.. option:: I20

    -Max  3276
    -Min  0
    -Unit  --
    -Description  电流环 Id 输出下限。

.. option:: I21

    -Max  9999
    -Min  0
    -Unit  --
    -Description  电流环 q 轴 Kp。

.. option:: I22

    -Max  99
    -Min  0
    -Unit  --
    -Description  电流环 q 轴 Kp 增益。

.. option:: I23

    -Max  9999
    -Min  0
    -Unit  --
    -Description  电流环 q 轴 Ki。

.. option:: I24

    -Max  9999
    -Min  0
    -Unit  --
    -Description  电流环 q 轴 Ki增益。

.. option:: I25

    -Max  3276
    -Min  0
    -Unit  --
    -Description  电流环 Iq 输出上限。

.. option:: I26

    -Max  3276
    -Min  0
    -Unit  --
    -Description  电流环 Iq 输出下限。

.. option:: I27

    -Max  9999
    -Min  1
    -Unit  --
    -Description  电机编码器的每圈线数。

.. option:: I28

    -Max  9999
    -Min  0
    -Unit  ms
    -Description  停车流程中距离电机刹停的时间。

.. option:: I30

    -Max  1
    -Min  0
    -Unit  --
    -Description
      | 选择到达目标位置的模式：
      | 0 = 速度模式；
      | 1 = 位置模式。

.. option:: I33

    -Max  1
    -Min  0
    -Unit  --
    -Description  机械零点距离电机同步点的偏移量。

.. option:: I37

    -Max  359
    -Min  0
    -Unit  1°
    -Description  刹车角度与速度规划阶段的距离。

.. option:: I38

    -Max  500
    -Min  1
    -Unit  spm
    -Description  刹车角度与速度规划阶段的入口速度。

.. option:: I39

    -Max  100
    -Min  0
    -Unit  spm
    -Description  刹车角度与速度规划阶段的终点速度。

.. option:: I40

    -Max  9999
    -Min  0
    -Unit  --
    -Description  停车位置环 Kp。

.. option:: I41

    -Max  99
    -Min  1
    -Unit  --
    -Description  停车位置环 Kp 增益。

.. option:: I42

    -Max  9999
    -Min  0
    -Unit  --
    -Description  停车位置环 Kd。

.. option:: I43

    -Max  99
    -Min  1
    -Unit  --
    -Description  停车位置环 Kd 增益。

.. option:: I46

    -Max  40
    -Min  1
    -Unit  0.1A
    -Description  锁定电流最大值。

.. option:: I47

    -Max  1
    -Min  0
    -Unit  --
    -Description
      | 弱磁扩速，以便电机可以达到更高的转速：
      | 0 = 关闭；
      | 1 = 打开。

.. option:: I48

    -Max  4500
    -Min  50
    -Unit  rpm
    -Description  高于此速度，弱磁扩速生效。

.. option:: I49

    -Max  40
    -Min  1
    -Unit  0.1A
    -Description  弱磁扩速 ID 电流上限。

.. option:: I50

    -Max  500
    -Min  0
    -Unit  --
    -Description  锁定位置环输出上限。

.. option:: I51

    -Max  100
    -Min  0
    -Unit  --
    -Description  锁定位置环输出下限。

.. option:: I52

    -Max  9999
    -Min  0
    -Unit  --
    -Description  位置环 Kp。

.. option:: I53

    -Max  99
    -Min  1
    -Unit  --
    -Description  锁定位置环 Kp 增益。

.. option:: I54

    -Max  9999
    -Min  0
    -Unit  --
    -Description  锁定位置环 Kd。

.. option:: I55

    -Max  99
    -Min  1
    -Unit  --
    -Description  锁定位置环 Kd增益。
