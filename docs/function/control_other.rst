.. _control_other:

==============
Control, other
==============

Parameter List
==============

T 14
----

.. dropdown:: Data Sending Interval <...>
   :animate: fade-in-slide-down
   
   -Max  9999
   -Min  1
   -Unit  ms
   -Description  Interval time for sending IoT data

A 49
----

.. dropdown:: IoT <...>
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | IoT network:
     | 0 = Off;
     | 1 = On.

A 52
----

.. dropdown:: Lock Panel
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | Whether the panel can be operated when foot lifting:
     | 0 = Not allowed;
     | 1 = Allowed.

A 58
----

.. dropdown:: Debug <...> 
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | Debug serial port output function:
     | 0 = Off;
     | 1 = On.

A 59
----

.. dropdown:: Reset statisc data <...> 
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description  Set to 1, statisc data will be restored to default values after power cycle.

O 15
----

.. dropdown:: Password Required <...>
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | Whether a password is required for parameter adjustment:
     | 0 = Off;
     | 1 = On.

O 17
----

.. dropdown:: Clear error log <...>
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description  Set to 1,error log clead after power cycle.

O 27
----

.. dropdown:: Password <...>
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description  Password required to adjust parameters.

O 51
----

.. dropdown:: Reset parameter <...>
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description  Set to 1, parameters will be restored to default values after power cycle.

O 52
----

.. dropdown:: Reset the MACHINE ZERO <...>
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description  Set to 1,the :term:`MACHINE ZERO` will be reset after power cycle

O 66
----

.. dropdown:: Factory reset 
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description  Set to 1,reset all parameters to default value,clear the error log and stastics information,reset MACHINE ZERO after power cycle.

O 70
----

.. dropdown:: Bus Voltage Error Reporting <...>
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description 
     | Whether to throw a error if bus voltage is too high:
     | 0: Off;
     | 1: On.
   
O 71
----

.. dropdown:: AC Voltage Error Reporting <...>
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | Whether to throw a error if AC 220 voltage is too high:
     | 0: Off;
     | 1: On.


I 44
----

.. dropdown:: Max. Bus Voltage <...>
   :animate: fade-in-slide-down
   
   -Max  460
   -Min  400
   -Unit  --
   -Description  Maximum bus voltage

I 45
----

.. dropdown:: Max. AC Voltage <...>
   :animate: fade-in-slide-down
   
   -Max  300
   -Min  260
   -Unit  V
   -Description  Maximum AC voltage
