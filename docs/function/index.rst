========
缝制功能
========

基本

.. grid:: 1 2 3 4
  :margin: 4 4 0 0
  :gutter: 1

  .. grid-item-card:: 前后加固 
    :link: bartack
    :link-type: doc

  .. grid-item-card:: 线迹
    :link: seam
    :link-type: doc 

  .. grid-item-card:: 底线计数器 
    :link: bobbin_monitor
    :link-type: doc

  .. grid-item-card:: 产量计数
    :link: daily_piece_counter
    :link-type: doc

  .. grid-item-card:: 软启动
    :link: soft_start
    :link-type: doc

  .. grid-item-card:: 反转
    :link: turn_back
    :link-type: doc

  .. grid-item-card:: 保养计数器
    :link: service_counter
    :link-type: doc 

功能性

.. grid:: 1 2 3 4
  :margin: 4 4 0 0
  :gutter: 1

  .. grid-item-card:: 倒缝 
    :link: reverse
    :link-type: doc

  .. grid-item-card:: 剪线 
    :link: thread_cutter
    :link-type: doc

  .. grid-item-card:: 压脚
    :link: sewing_foot_lift
    :link-type: doc

  .. grid-item-card:: 压脚交互量 
    :link: stroke
    :link-type: doc
  
  .. grid-item-card:: 电子抓线
    :link: clamp
    :link-type: doc

  .. grid-item-card:: 面线张力
    :link: tension
    :link-type: doc 

  .. grid-item-card:: 电子手轮
    :link: elec_hand_wheel
    :link-type: doc 

  .. grid-item-card:: 缝线中心导向
    :link: seam_center_guide
    :link-type: doc

  .. grid-item-card:: 第二针距
    :link: second_stitch_length
    :link-type: doc

  .. grid-item-card:: 送料滚轮
    :link: puller
    :link-type: doc

  .. grid-item-card:: 机针冷却
    :link: needle_cooling
    :link-type: doc

  .. grid-item-card:: 扫线
    :link: wiper
    :link-type: doc

其他

.. grid:: 1 2 3 4
  :margin: 4 4 0 0
  :gutter: 1

  .. grid-item-card:: 安装 
    :link: assemble
    :link-type: doc

  .. grid-item-card:: 控制器/其他 
    :link: control_other
    :link-type: doc
  
  .. grid-item-card:: 输入配置
    :link: input_configuration
    :link-type: doc

  .. grid-item-card:: 输出配置
    :link: output_configuration
    :link-type: doc 

  .. grid-item-card:: 综合测试
    :link: multitest
    :link-type: doc 

  .. grid-item-card:: 电机
    :link: multitest
    :link-type: doc 

  .. grid-item-card:: 安全传感器
    :link: safety-sensor
    :link-type: doc 



词汇表
========
**下表解释了本手册一些常用术语的具体含义, 比如** :term:`机械零点`：
 
.. glossary::
  机械零点
    机械零点定义为机针的最高点。电磁铁（阀）动作/释放的角度，以及电机停止的位置等等, 本手册提到
    角度都是以机械零点为参考的。

    .. warning:: 
       这非常重要，请确保正确设置了它。

  机头识别码
    机头识别码，一串数字代码，和具体的机头型号一一对应。

    .. warning::
       这非常重要，请确保正确设置了它。
    
  POSITION 2
    位置2，调速器正踩第一段，也叫高速位置。

  POSITION 1
    调速器正踩第二段，也叫低速位置。
  
  POSITION 0
    调速器默认位置。
  
  POSITION -1
    调速器反踩第一段，也叫压脚位置。
    
  POSITION -2
    调速器反踩第二段，也叫剪线位置。
  
  时间t1
    输出端口控制策略中100%出力的时间。
  
  时间t2
    输出端口控制策略中PWM阶段(非100%出力)的占空比。
    

**下表解释了本手册一些常用单位的具体含义，比如** :term:`ms`：

.. glossary::
  spm
    针每分钟，用以表示主轴转速

  ms
    毫秒

  s
    秒

  m
    分钟    

  h
    小时  

  %
    百分比

  1°
    度，主轴完整一圈为360度

  V
    伏特，电压单位

  A
    安倍，电流单位. 本手册会出现 **0.1A**，表示1安培的十分之一 

目录
====

.. toctree::
  :maxdepth: 4

  bartack
  assemble
  clamp
  wiper
  control_other
  daily_piece_counter
  elec_hand_wheel
  input_configuration
  output_configuration
  stroke
  tension
  seam_center_guide
  soft_start
  thread_cutter
  turn_back
  bobbin_monitor
  motor
  multitest
  needle_cooling
  puller
  seam
  second_stitch_length
  service_counter
  sewing_foot_lift
  reverse
  safety-sensor
