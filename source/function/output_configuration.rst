.. _output_configuration:

输出配置
====

输出端口允许控制器驱动机器上的元件。这些元件主要包括各类电磁铁和电磁阀。

每个输出端口都很灵活的。大多数情况下，您可以根据自己的实际接线情况自由配置各个端口的模式。

.. attention::

    确保两个输出端口未配置为相同的模式。

    根据机器型号的不同，某些模式可能不可用。

.. _output_mode_code_list:

输出端口模式代码表
---------

输出端口可配置的模式代码表如下：

- 0 = 无功能；
- 1 = 剪线；
- 2 = 面线张力；
- 3 = 夹线器；
- 4 = 倒缝；
- 5 = 压脚；
- 6 = 交互量；
- 7 = 额外的面线张力；
- 8 = 扫线器（面线）；
- 9 = 第二针距；
- 10 = 机针冷却；
- 11 = 额外剪线定刀（短线头机型）；
- 12 = 缝线中心导向；
- 13 = 零针距（短线头机型）；
- 14 = 自动复位（双针机型）；
- 15 = 送料滚轮；
- 16 = 扫线（底线）；

如何设置输入端口的模式？
------------

按照以下步骤：

1. 确认你需要修改那一路端口，比如时 *输出 01* 还是 *输出 02*\ ，这部分需要参考具体产品的接线图。 之后参考本章节
   :ref:`output_params_quick_reference` 部分，查找控制此端口功能的参数序号；
2. 参考本章节开头 :ref:`output_mode_code_list` 部分，得到你需要的功能代码；
3. 将步骤1得到的参数修改为步骤2得到的功能代码；
4. 重启控制器以应用设定。

举例说明：

1. 想把输出 01 的模式修改为拖布滚轮；
2. 查询 :ref:`output_params_quick_reference` 章节，可知 :option:`A71` 控制输出 01 的模式:

       A71 = 输出 01 模式

3. 查询 :ref:`output_mode_code_list` 章节，\ *15* 是送料滚轮的代码，那么将 :option:`A71` 修改为 15：

       15 = 送料滚轮

4. 重启控制器。

.. _output_params_quick_reference:

快速参考
----

下表总结了输出配置功能所使用到的参数：

======== === =============
参数       权限  参见
======== === =============
输出 01 模式 技术员 :option:`A71`
输出 02 模式 技术员 :option:`A72`
输出 03 模式 技术员 :option:`A73`
输出 04 模式 技术员 :option:`A74`
输出 05 模式 技术员 :option:`A75`
输出 06 模式 技术员 :option:`A76`
输出 07 模式 技术员 :option:`A77`
输出 08 模式 技术员 :option:`A78`
输出 09 模式 技术员 :option:`A79`
输出 10 模式 技术员 :option:`A80`
======== === =============

参数列表
----

.. option:: A71

    -Max  99
    -Min  0
    -Unit  --
    -Description  定义输出 01 的模式。

.. option:: A72

    -Max  99
    -Min  0
    -Unit  --
    -Description  定义输出 02 的模式。

.. option:: A73

    -Max  99
    -Min  0
    -Unit  --
    -Description  定义输出 03 的模式。

.. option:: A74

    -Max  99
    -Min  0
    -Unit  --
    -Description  定义输出 04 的模式。

.. option:: A75

    -Max  99
    -Min  0
    -Unit  --
    -Description  定义输出 05 的模式。

.. option:: A76

    -Max  99
    -Min  0
    -Unit  --
    -Description  定义输出 06 的模式。

.. option:: A77

    -Max  99
    -Min  0
    -Unit  --
    -Description  定义输出 07 的模式。

.. option:: A78

    -Max  99
    -Min  0
    -Unit  --
    -Description  定义输出 08 的模式。

.. option:: A79

    -Max  99
    -Min  0
    -Unit  --
    -Description  定义输出 09 的模式。

.. option:: A80

    -Max  99
    -Min  0
    -Unit  --
    -Description  定义输出 10 的模式。
