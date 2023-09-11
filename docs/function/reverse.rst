.. _reverse:

========
Revserse
========


Parameter List
==============

T 01
----

.. dropdown:: Reverse Action In Place Time
   :animate: fade-in-slide-down
   
   -Max  200
   -Min  1
   -Unit  ms
   -Description  The time for the reverse solenoid finish the action,unit ms

T 02
----

.. dropdown:: Reverse Release In Place Time
   :animate: fade-in-slide-down
   
   -Max  200
   -Min  1
   -Unit  ms
   -Description  The time for reverse solenoid finish the releasing,unit ms

D 05
----

.. dropdown:: Start Reverse Position
   :animate: fade-in-slide-down
   
   -Max  359
   -Min  0
   -Unit  1°
   -Description  Position when the magnet of reverse is activated.
  
D 06
----

.. dropdown:: Stop Reverse Position
   :animate: fade-in-slide-down
   
   -Max  359
   -Min  0
   -Unit  1°
   -Description  Position when the magnet of reverse is deactivated.

T 08
----

.. dropdown:: Time(t1)
   :animate: fade-in-slide-down
   
   -Max  200
   -Min  1
   -Unit  ms
   -Description  Reverse:activation duration of in :term:`time period t1`
                 (100% duty cycle),unit ms

O 09
----

.. dropdown:: Duty cycle(t2)
   :animate: fade-in-slide-down
   
   -Max  100
   -Min  1
   -Unit  %
   -Description  Reverse:duty cycle[%] in :term:`time period t2`.

O 10
----

.. dropdown:: Auto Power-off Reverse
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description 
     | Whether the magnet of reverse automatic power-off after the set time:
     | 0 = Off;
     | 1 = On


O 11
----

.. dropdown:: Reverse Max. Holding Time
   :animate: fade-in-slide-down
   
   -Max  30
   -Min  5
   -Unit  s
   -Description  If Auto Power-off Reverse is turned on,this parameter sets the power-off time.
