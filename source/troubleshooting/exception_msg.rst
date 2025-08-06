.. _exception_msg:

警告、错误和通知信息
==========

*银星缝纫控制系统* 的异常信息分为三组，如下表：

== === ================
程度 缩写  说明
== === ================
错误 Err 严重故障，必须关机排除故障
警告 Wrn 排除导致的原因，控制器将继续工作
信息 Inf 工作可以继续，仅异常信息需要确认
== === ================

异常信息快速参考
--------

错误信息
~~~~

================= =========== =============================
代码                可能的原因       补救措施
================= =========== =============================
:exc:`ExcCode101` 供电电压过高      :meth:`ExcCode101.solution()`
:exc:`ExcCode103` 母线电压过压      :meth:`ExcCode103.solution()`
:exc:`ExcCode106` 电机过流        :meth:`ExcCode106.solution()`
:exc:`ExcCode107` 负载过大/电机转速过低 :meth:`ExcCode107.solution()`
:exc:`ExcCode108` 电机相电流过流     :meth:`ExcCode108.solution()`
:exc:`ExcCode109` 电机启动时堵转     :meth:`ExcCode109.solution()`
:exc:`ExcCode110` 电机堵转        :meth:`ExcCode110.solution()`
:exc:`ExcCode111` 码盘霍尔信号异常    :meth:`ExcCode111.solution()`
:exc:`ExcCode112` 码盘编码器信号异常   :meth:`ExcCode112.solution()`
:exc:`ExcCode113` 输出端口短路过流    :meth:`ExcCode113.solution()`
:exc:`ExcCode114` 码盘编码器信号异常   :meth:`ExcCode114.solution()`
:exc:`ExcCode126` 操作盒连接错误     :meth:`ExcCode126.solution()`
:exc:`ExcCode127` 操作盒失去连接     :meth:`ExcCode127.solution()`
:exc:`ExcCode128` 数据校验错误      :meth:`ExcCode128.solution()`
:exc:`ExcCode129` 步进连接异常      :meth:`ExcCode129.solution()`
:exc:`ExcCode130` 数据校验错误      :meth:`ExcCode130.solution()`
:exc:`ExcCode191` 控制器：升级      :meth:`ExcCode191.solution()`
:exc:`ExcCode192` 控制器：升级      :meth:`ExcCode192.solution()`
:exc:`ExcCode193` 控制器：升级      :meth:`ExcCode193.solution()`
:exc:`ExcCode194` 控制器：升级      :meth:`ExcCode194.solution()`
:exc:`ExcCode195` 控制器：升级      :meth:`ExcCode195.solution()`
:exc:`ExcCode196` 控制器：升级      :meth:`ExcCode196.solution()`
:exc:`ExcCode197` 控制器：升级      :meth:`ExcCode197.solution()`
:exc:`ExcCode198` 控制器：升级      :meth:`ExcCode198.solution()`
:exc:`ExcCode199` 控制器：升级      :meth:`ExcCode199.solution()`
:exc:`ExcCode181` 操作盒：升级      :meth:`ExcCode181.solution()`
:exc:`ExcCode182` 操作盒：升级      :meth:`ExcCode182.solution()`
:exc:`ExcCode183` 操作盒：升级      :meth:`ExcCode183.solution()`
:exc:`ExcCode184` 操作盒：升级      :meth:`ExcCode184.solution()`
:exc:`ExcCode185` 操作盒：升级      :meth:`ExcCode185.solution()`
:exc:`ExcCode186` 操作盒：升级      :meth:`ExcCode186.solution()`
:exc:`ExcCode187` 操作盒：升级      :meth:`ExcCode187.solution()`
:exc:`ExcCode188` 操作盒：升级      :meth:`ExcCode188.solution()`
:exc:`ExcCode189` 操作盒：升级      :meth:`ExcCode189.solution()`
================= =========== =============================

警告信息
~~~~

报警信息的代码总是小于100.

=============== ===== ===========================
代码              可能的原因 补救措施
=============== ===== ===========================
:exc:`ExcCode1` 调速器   :meth:`ExcCode1.solution()`
:exc:`ExcCode2` 倾倒开关  :meth:`ExcCode2.solution()`
:exc:`ExcCode3` 热键    :meth:`ExcCode3.solution()`
:exc:`ExcCode4` 热键    :meth:`ExcCode4.solution()`
:exc:`ExcCode5` 底线检测  :meth:`ExcCode5.solution()`
:exc:`ExcCode6` 面线检测  :meth:`ExcCode6.solution()`
:exc:`ExcCode7` 保养计数器 :meth:`ExcCode7.solution()`
:exc:`ExcCode8` 护眼板   :meth:`ExcCode8.solution()`
:exc:`ExcCode9` 旋梭盖板  :meth:`ExcCode9.solution()`
=============== ===== ===========================

通知信息
~~~~

通知信息的代码总是小于100.

================ ======= ============================
代码               可能的原因   补救措施
================ ======= ============================
:exc:`ExcCode50` 润滑油余量不足 :meth:`ExcCode50.solution()`
================ ======= ============================

故障信息列表
------

.. exception:: ExcCode101

    交流电压过高

    .. method:: solution()

       测量交流输入电压；
       控制器电压检测电路有问题，可以更换控制器后查看报错是否消失。

.. exception:: ExcCode103

    母线电压过高

    .. method:: solution()

       检查泄放电路，可以更换泄放电阻可否解决；
       控制器电压检测电路有问题，可以更换控制器后查看报错是否消失。

.. exception:: ExcCode106

    电机电流过载

    .. method:: solution()

       检查电机码盘线束连接是否牢靠；
       确认 :term:`机头识别码` 是否被正确设置；
       硬件故障，更换控制器后查看报错是否消失。

.. exception:: ExcCode107

    过载，电机持续低速

    .. method:: solution()

       主轴堵转，负载过大；
       缝料过厚。

.. exception:: ExcCode108

    过载，电机相电流过大

    .. method:: solution()

       主轴堵转，负载过大；
       缝料过厚。

.. exception:: ExcCode109

    电机启动失败

    .. method:: solution()

       从缝料较薄的地方重新启动电机；
       主轴堵转，负载过大；
       缝料过厚。

.. exception:: ExcCode110

    电机同步信号长时检测不到

    .. method:: solution()

       检查电机同步信号；
       主轴堵转，负载过大；
       缝料过厚。

.. exception:: ExcCode111

    电机UVW信号异常

    .. method:: solution()

       检查UVW信号，检查码盘线束连接；
       更换电机码盘。

.. exception:: ExcCode112

    电机启动后检测不到同步信号

    .. method:: solution()

       检查电机同步信号，检查码盘线束连接；
       更换电机码盘。

.. exception:: ExcCode113

    电磁铁（铁）过流

    .. method:: solution()

       检查电磁铁（阀）连接是否有接错；
       更换控制箱或者电磁铁（阀）。

.. exception:: ExcCode114

    电角度值异常

    .. method:: solution()

       检查电机同步信号，检查码盘线束连接；
       检查电机UVW信号。

.. exception:: ExcCode126

    控制箱和操作盒之间参数同步失败

    .. method:: solution()

       检查操作盒线束连接；
       重启控制器。

.. exception:: ExcCode127

    操作盒断联

    .. method:: solution()

       插好操作盒线束之后重启控制器。

.. exception:: ExcCode128

    控制箱和操作盒之间参数校验失败

    .. method:: solution()

       插好操作盒线束之后重启控制器。

.. exception:: ExcCode129

    步进电机通讯失败

    .. method:: solution()

       重启控制器；
       检查连接线束。

.. exception:: ExcCode130

    控制箱和操作盒之间参数版本不匹配

    .. method:: solution()

       升级控制器和操作盒的软件版本不匹配，重新升级两者的软件。

.. exception:: ExcCode191

    控制器应用程序不完整

    .. method:: solution()

       升级控制器软件。

.. exception:: ExcCode192

    控制器升级文件数据错误: 数据页数

    .. method:: solution()

       重新拷贝升级文件，之后重启升级过程。

.. exception:: ExcCode193

    控制器升级文件数据错误: 校验失败

    .. method:: solution()

       重新拷贝升级文件，之后重启升级过程。

.. exception:: ExcCode194

    控制器升级文件数据错误: 数据大小

    .. method:: solution()

       重新拷贝升级文件，之后重启升级过程。

.. exception:: ExcCode195

    控制器升级文件数据错误: 起始地址

    .. method:: solution()

       重新拷贝升级文件，之后重启升级过程。

.. exception:: ExcCode196

    控制器升级文件数据错误: 文件和产品型号不符

    .. method:: solution()

       重新拷贝升级文件，之后重启升级过程。

.. exception:: ExcCode197

    控制器升级文件不存在

    .. method:: solution()

       重新拷贝升级文件，之后重启升级过程。

.. exception:: ExcCode198

    控制器升级过程中数据传输超时

    .. method:: solution()

       检查操作盒连接线束，之后重启升级过程。

.. exception:: ExcCode199

    USB设备检测不到

    .. method:: solution()

       重新插拔下U盘并且重启升级过程。

.. exception:: ExcCode181

    操作盒应用程序不完整

    .. method:: solution()

       重新升级操作盒软件。

.. exception:: ExcCode182

    操作盒升级文件数据错误: 数据页数

    .. method:: solution()

       重新拷贝升级文件，之后重启升级过程。

.. exception:: ExcCode183

    操作盒升级文件数据错误: 校验失败

    .. method:: solution()

       重新拷贝升级文件，之后重启升级过程。

.. exception:: ExcCode184

    操作盒升级文件数据错误: 数据大小

    .. method:: solution()

       重新拷贝升级文件，之后重启升级过程。

.. exception:: ExcCode185

    操作盒升级文件数据错误: 起始地址

    .. method:: solution()

       重新拷贝升级文件，之后重启升级过程。

.. exception:: ExcCode186

    操作盒升级文件数据错误: 文件和产品型号不符

    .. method:: solution()

       重新拷贝升级文件，之后重启升级过程。

.. exception:: ExcCode187

    操作盒升级文件不存在

    .. method:: solution()

       重新拷贝升级文件，之后重启升级过程。

.. exception:: ExcCode188

    操作盒升级过程中数据传输超时

    .. method:: solution()

       检查操作盒连接线束，之后重启升级过程。

.. exception:: ExcCode189

    USB设备检测不到

    .. method:: solution()

       重新插拔下U盘并且重启升级过程。

警告信息列表
------

.. exception:: ExcCode1

    调速器报警

    .. method:: solution()

       开机时调速器必须在 :term:`POSITION 0` ；
       如果使用的是站立式三踏板而非原装调速器，调速器类型要正确设置；
       调速器本身有问题，更换调速器.

.. exception:: ExcCode2

    倾倒开关警告

    .. method:: solution()

       机头被翻起，等待机头被正常放置后，警告将自动解除；
       检查机头倾倒开关的信号是否异常。

.. exception:: ExcCode3

    热键1触发警告

    .. method:: solution()

       开机时不允许按压热键；
       检查热键的信号是否异常。

.. exception:: ExcCode4

    热键2触发警告

    .. method:: solution()

       开机时不允许按压热键；
       检查热键的信号是否异常。

.. exception:: ExcCode5

    底线余量警告

    .. method:: solution()

       底线计数器功能激活时，底线余量为0时出现的警告，更换新的锁芯后进行重置操作可以清除报警。

.. exception:: ExcCode6

    面线短线警告

    .. method:: solution()

       面线检测功能激活时，面线发生断裂时报警，重新接好面线；
       检查热键的信号是否异常。

.. exception:: ExcCode7

    保养提醒

    .. method:: solution()

    保养计数器功能激活时，待保养针数为0出现的警告，机器例行保养后进行重置操作可以清除报警。

.. exception:: ExcCode8

    护眼板未归位

    .. method:: solution()

       护眼板应该被推至正确的位置；
       检查护眼板的信号是否异常。

.. exception:: ExcCode9

    旋梭盖板被推开

    .. method:: solution()

       闭合旋梭盖板；
       检查旋梭盖板的信号是否异常。

通知信息列表
------

.. exception:: ExcCode50

    润滑油位过低

    .. method:: solution()

       增加润滑油至正常油位；
       检查油位传感器的信号是否异常。

    .. versionchanged:: 90A0-v1.08.05

       曾经，这个异常信息的代码是 *10* ，并且归类为 *警告* 组。
