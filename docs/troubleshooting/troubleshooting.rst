.. _troubleshooting:

==========
错误信息表
==========

警告信息列表
============

.. warning:: 
   定位引起告警的原因，在排除故障之后控制器将会恢复正常工作。

.. dropdown:: 1 
   :animate: fade-in-slide-down
   :open:

   -Level  警告
   -Description  倾倒开关警告
   -Solution  
     | 开机时调速器必须在 :term:`POSITION 0` ；
     | 如果使用的是站立式三踏板而非原装调速器，调速器类型要正确设置；
     | 调速器本身有问题，更换调速器.

.. dropdown:: 2 
   :animate: fade-in-slide-down
   :open:

   -Level  警告
   -Description  倾倒开关警告
   -Solution  
     | 机头被翻起，等待机头被正常放置后，警告将自动解除； 
     | 检查机头倾倒开关的信号是否异常。  

.. dropdown:: 3 
   :animate: fade-in-slide-down
   :open:

   -Level  警告
   -Description  热键1触发警告
   -Solution  
     | 开机时不允许按压热键；
     | 检查热键的信号是否异常。

.. dropdown:: 4 
   :animate: fade-in-slide-down
   :open:

   -Level  警告
   -Description  热键2触发警告
   -Solution       
     | 开机时不允许按压热键；
     | 检查热键的信号是否异常。

.. dropdown:: 5 
   :animate: fade-in-slide-down
   :open:

   -Level  警告
   -Description  底线余量警告
   -Solution  
     | 底线计数器功能激活时，底线余量为0时出现的警告，更换新的锁芯后进行重置操作可以清除报警。

.. dropdown:: 6 
   :animate: fade-in-slide-down
   :open:

   -Level  警告
   -Description   面线短线警告
   -Solution  
     | 面线检测功能激活时，面线发生断裂时报警，重新接好面线；
     | 检查热键的信号是否异常。

.. dropdown:: 7 
   :animate: fade-in-slide-down
   :open:

   -Level  警告
   -Description  保养提醒
   -Solution  
     | 保养计数器功能激活时，待保养针数为0出现的警告，机器例行保养后进行重置操作可以清除报警。

.. dropdown:: 8 
   :animate: fade-in-slide-down
   :open:

   -Level  警告
   -Description  护眼板未归位
   -Solution
     | 护眼板应该被推至正确的位置；
     | 检查护眼板的信号是否异常。

.. dropdown:: 9 
   :animate: fade-in-slide-down
   :open:

   -Level  警告
   -Description  旋梭盖板被推开
   -Solution
     | 闭合旋梭盖板；
     | 检查旋梭盖板的信号是否异常。

.. dropdown:: 10 
   :animate: fade-in-slide-down
   :open:

   -Level  警告
   -Description  润滑油位警告
   -Solution  
     | 增加润滑油至正常油位；
     | 检查油位传感器的信号是否异常。

故障信息列表
============

.. error::
  必须关闭控制器，并解决故障。

.. dropdown:: 101 
   :animate: fade-in-slide-down
   :open:

   -Level  报错
   -Description  交流电压过高
   -Solution
     | 测量交流输入电压;
     | 控制器电压检测电路有问题，可以更换控制器后查看报错是否消失。

.. dropdown:: 103 
   :animate: fade-in-slide-down
   :open:

   -Level  报错
   -Description  母线电压过高
   -Solution
     | 检查泄放电路，可以更换泄放电阻可否解决；
     | 控制器电压检测电路有问题，可以更换控制器后查看报错是否消失。

.. dropdown:: 106 
   :animate: fade-in-slide-down
   :open:

   -Level  报错
   -Description  电机电流过载
   -Solution
     | 检查电机码盘线束连接是否牢靠；
     | 确认 :term:`机头识别码` 是否被正确设置；
     | 硬件故障，更换控制器后查看报错是否消失。

.. dropdown:: 107 
   :animate: fade-in-slide-down
   :open:

   -Level  报错
   -Description  过载，电机持续低速
   -Solution
     | 主轴堵转，负载过大；
     | 缝料过厚。

.. dropdown:: 108 
   :animate: fade-in-slide-down
   :open:

   -Level  报错
   -Description  过载，电机相电流过大
   -Solution
     | 主轴堵转，负载过大；
     | 缝料过厚。

.. dropdown:: 109 
   :animate: fade-in-slide-down
   :open:

   -Level  报错
   -Description  电机启动失败
   -Solution
     | 从缝料较薄的地方重新启动电机；
     | 主轴堵转，负载过大；
     | 缝料过厚。

.. dropdown:: 110
   :animate: fade-in-slide-down
   :open:

   -Level  报错
   -Description  电机同步信号长时检测不到
   -Solution
     | 检查电机同步信号；
     | 主轴堵转，负载过大；
     | 缝料过厚。

.. dropdown:: 111
   :animate: fade-in-slide-down
   :open:

   -Level  报错
   -Description  电机UVW信号异常
   -Solution
     | 检查UVW信号，检查码盘线束连接；
     | 更换电机码盘。

.. dropdown:: 112
   :animate: fade-in-slide-down
   :open:

   -Level  报错
   -Description  电机启动后检测不到同步信号  
   -Solution
     | 检查电机同步信号，检查码盘线束连接；
     | 更换电机码盘。

.. dropdown:: 113
   :animate: fade-in-slide-down
   :open:

   -Level  报错
   -Description  电磁铁（铁）过流
   -Solution
     | 检查电磁铁（阀）连接是否有接错；
     | 更换控制箱或者电磁铁（阀）。
     
.. dropdown:: 114
   :animate: fade-in-slide-down
   :open:

   -Level  报错
   -Description  电角度值异常
   -Solution
     | 检查电机同步信号，检查码盘线束连接；
     | 检查电机UVW信号。

.. dropdown:: 126
   :animate: fade-in-slide-down
   :open:

   -Level  报错
   -Description  控制箱和操作盒之间参数同步失败
   -Solution
     | 检查操作盒线束连接；
     | 重启控制器。

.. dropdown:: 127
   :animate: fade-in-slide-down
   :open:

   -Level  报错
   -Description  操作盒断联
   -Solution  插好操作盒线束之后重启控制器。

.. dropdown:: 128
   :animate: fade-in-slide-down
   :open:

   -Level  报错
   -Description  控制箱和操作盒之间参数校验失败
   -Solution
     | 插好操作盒线束之后重启控制器。


.. dropdown:: 129
   :animate: fade-in-slide-down
   :open:

   -Level  报错
   -Description  步进电机通讯失败
   -Solution
     | 重启控制器；
     | 检查连接线束。

.. dropdown:: 130
   :animate: fade-in-slide-down
   :open:

   -Level  报错
   -Description  控制箱和操作盒之间参数版本不匹配
   -Solution  
     | 升级控制器和操作盒的软件版本不匹配，重新升级两者的软件。

.. dropdown:: 191
   :animate: fade-in-slide-down
   :open:

   -Level  报错
   -Description  控制器应用程序不完整
   -Solution  升级控制器软件。

.. dropdown:: 192
   :animate: fade-in-slide-down
   :open:

   -Level  报错
   -Description  控制器升级文件数据错误: 数据页数
   -Solution  重新拷贝升级文件，之后重启升级过程。

.. dropdown:: 193
   :animate: fade-in-slide-down
   :open:

   -Level  报错
   -Description  控制器升级文件数据错误: 校验失败
   -Solution  重新拷贝升级文件，之后重启升级过程。

.. dropdown:: 194
   :animate: fade-in-slide-down
   :open:

   -Level  报错
   -Description  控制器升级文件数据错误: 数据大小
   -Solution  重新拷贝升级文件，之后重启升级过程。

.. dropdown:: 195
   :animate: fade-in-slide-down
   :open:

   -Level  报错
   -Description  控制器升级文件数据错误: 起始地址
   -Solution  重新拷贝升级文件，之后重启升级过程。

.. dropdown:: 196
   :animate: fade-in-slide-down
   :open:

   -Level  报错
   -Description  控制器升级文件数据错误: 文件和产品型号不符
   -Solution  重新拷贝升级文件，之后重启升级过程。

.. dropdown:: 197
   :animate: fade-in-slide-down
   :open:

   -Level  报错
   -Description  控制器升级文件不存在
   -Solution  重新拷贝升级文件，之后重启升级过程。

.. dropdown:: 198
   :animate: fade-in-slide-down
   :open:

   -Level  报错
   -Description  控制器升级过程中数据传输超时
   -Solution  检查操作盒连接线束，之后重启升级过程。

.. dropdown:: 199
   :animate: fade-in-slide-down
   :open:

   -Level  报错
   -Description  USB设备检测不到
   -Solution  重新插拔下U盘并且重启升级过程。

.. dropdown:: 181
   :animate: fade-in-slide-down
   :open:

   -Level  报错
   -Description  操作盒应用程序不完整
   -Solution  重新升级操作盒软件。

.. dropdown:: 182
   :animate: fade-in-slide-down
   :open:

   -Level  报错
   -Description  操作盒升级文件数据错误: 数据页数
   -Solution  重新拷贝升级文件，之后重启升级过程。

.. dropdown:: 183
   :animate: fade-in-slide-down
   :open:

   -Level  报错
   -Description  操作盒升级文件数据错误: 校验失败
   -Solution  重新拷贝升级文件，之后重启升级过程。

.. dropdown:: 184
   :animate: fade-in-slide-down
   :open:

   -Level  报错
   -Description  操作盒升级文件数据错误: 数据大小
   -Solution  重新拷贝升级文件，之后重启升级过程。

.. dropdown:: 185
   :animate: fade-in-slide-down
   :open:

   -Level  报错
   -Description  操作盒升级文件数据错误: 起始地址
   -Solution  重新拷贝升级文件，之后重启升级过程。

.. dropdown:: 186
   :animate: fade-in-slide-down
   :open:

   -Level  报错
   -Description  操作盒升级文件数据错误: 文件和产品型号不符
   -Solution  重新拷贝升级文件，之后重启升级过程。

.. dropdown:: 187
   :animate: fade-in-slide-down
   :open:

   -Level  报错
   -Description  操作盒升级文件不存在
   -Solution  重新拷贝升级文件，之后重启升级过程。

.. dropdown:: 188
   :animate: fade-in-slide-down
   :open:

   -Level  报错
   -Description  操作盒升级过程中数据传输超时
   -Solution  检查操作盒连接线束，之后重启升级过程。

.. dropdown:: 189
   :animate: fade-in-slide-down
   :open:

   -Level  报错
   -Description  USB设备检测不到
   -Solution  重新插拔下U盘并且重启升级过程。
