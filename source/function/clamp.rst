.. _thread_clamp:

========
电子抓线
========

**线迹开始时**:

电子抓线可以在起缝制第一针的一定角度内动作，接通角度由 `D 07`_ 控制，关断角度由 `D 08`_ 控制。

只会在一段新的线迹开始时动作一次，剪线后重置。

**剪线反转时**:

电子抓线在剪线反转过程中接通，最大时间由 `T 15`_ 进行控制，为防止烧毁请合理设置此时间。

**压脚抬起时**:

电子抓线随压脚抬起而接通，最大时间由 `T 15`_ 进行控制，为防止烧毁请合理设置此时间。

参数列表
========

T 15 
----

.. dropdown:: 接通时间 <...>
   :animate: fade-in-slide-down
   
   -Max  2000
   -Min  1
   -Unit  毫秒
   -Description  当设置剪线反转提针或抬压脚动作夹线时，夹线器接通的时间。

A 10
----

.. dropdown:: 电子抓线 <...>
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | 电子抓线功能：
     | 0 = 关闭；
     | 1 = On。

A 29
----

.. dropdown:: 电子抓线自动模式 <...> 
   :animate: fade-in-slide-down
   
   -Max  3
   -Min  0
   -Unit  --
   -Description
     | 0 = 仅在缝制启动时夹线；
     | 1 = 在缝纫启动和反转提针时夹线；
     | 2 = 在缝纫启动和抬压脚时夹线；
     | 3 = 1和2场景下都夹线。


D 07
----

.. dropdown:: 电子抓线开始角度 <...> 
   :animate: fade-in-slide-down
   
   -Max  359
   -Min  0
   -Unit  1°
   -Description  电子抓线电磁铁动作角度。

D 08
----

.. dropdown:: 电子抓线结束角度 <...>
   :animate: fade-in-slide-down
   
   -Max  359
   -Min  0
   -Unit  1°
   -Description  电子抓线电磁铁释放角度。

O 42
----

.. dropdown:: 夹线接通时压脚微抬 <...>
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description  
     | 起针缓缝夹线动作时,减小压脚压力：
     | 0 = 关闭；
     | 1 = 打开。 

O 48
----

.. dropdown:: 维持出力（t2） <...>
   :animate: fade-in-slide-down
   
   -Max  100
   -Min  0
   -Unit  %
   -Description  夹线：维持出力 :term:`时间t2` 内的占空比。
