.. _stroke:

==================
Sewing foot stroke
==================


**Speed limitation sewing foot stroke**

if parameter **A35** set to 1, when 2nd sewing foot stroke is activated, the speed is 
reduced down to the desired value of 2nd sewing foot stroke which set by **S15**.

**Number of stitches 2nd stroke off**

if **A32** is not 0, when switching to 2nd sewing foot stroke, after sewing N stitches 
set by **A32**, the second sewing foot stroke is automatically deactivated.


Parameter List
==============

S 09
----

.. dropdown:: Max. Speed Stroke Whell Mark 1
   :animate: fade-in-slide-down
   
   -Max  4500
   -Min  100
   -Unit  spm
   -Description  The stroke height knob type is switch: Limit speed when turn adjusting 
                 wheel to mark 1 position

S 10
----

.. dropdown:: Max. Speed for Small Stroke
   :animate: fade-in-slide-down
   
   -Max  4500
   -Min  100
   -Unit  spm
   -Description  The stroke height knob type is potentiometer: Limit speed for the small
                 stork height

S 11
----

.. dropdown:: Max. Speed Stroke Whell Mark 2
   :animate: fade-in-slide-down
   
   -Max  4500
   -Min  100
   -Unit  spm
   -Description  The stroke height knob type is switch: Limit speed when turun adjusting
                 wheel to mark 2 position

S 12
----

.. dropdown:: Max. Speed Stroke Whell Mark 3
   :animate: fade-in-slide-down
   
   -Max  4500
   -Min  100
   -Unit  spm
   -Description  The stroke height knob type is switch:Limit speed when turun adjusting
                 wheel to mark 3 position

S 13
----

.. dropdown:: Max. Speed Stroke Whell Mark 4
   :animate: fade-in-slide-down
   
   -Max  4500
   -Min  100
   -Unit  spm
   -Description  The stroke height knob type is switch: Limit speed when turun adjusting
                 wheel to mark 4 position

S 14
----

.. dropdown:: Max. Speed for High Stroke
   :animate: fade-in-slide-down
   
   -Max  4500
   -Min  100
   -Unit  spm
   -Description  The stroke height knob type is potentiometer:Limit speed for the high
                 stork height

S 15
----

.. dropdown:: Max. Speed for Elevated Stroke
   :animate: fade-in-slide-down
   
   -Max  4500
   -Min  100
   -Unit  spm
   -Description  Limit speed for the elevated sewing foot storke

A 24
----

.. dropdown:: Status of Stroke
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description  Status of stroke height solenoid(read only)

A 32
----

.. dropdown:: Number of Stitches 2nd Stroke Off
   :animate: fade-in-slide-down
   
   -Max  99
   -Min  0
   -Unit  stitches
   -Description  
     | 0 = Manually switch;
     | Not 0 = Number of stitches after which the second stroke height is automatically deactivated.

A 35
----

.. dropdown:: Auto Speed Limit 
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  stitches
   -Description
     | If the second stroke is activated, speed reduced down to Parameter S15:
     | 0 = Off
     | 1 = On

A 45
----

.. dropdown:: Stroke
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  stitches
   -Description
     | Stroke height function:
     | 0 = Off
     | 1 = On

O 21
----

.. dropdown:: Min. Stroke Border
   :animate: fade-in-slide-down
   
   -Max  4095
   -Min  0
   -Unit  stitches
   -Description  The sensor value at the boundary position of the minimum stroke,
                 the speed is reduced down as continue to increase stroke height.

O 22
----

.. dropdown:: Max. Stroke Point
   :animate: fade-in-slide-down
   
   -Max  4095
   -Min  0
   -Unit  stitches
   -Description  Sensor value at position of maximum stroke.

0 76
----

.. dropdown::Time(t1)
   :animate: fade-in-slide-down
   
   -Max  999
   -Min  1
   -Unit  ms
   -Description  Stroke height:activation duration of in :term:`time period t1`
                 (100% duty cycle)

0 77
----

.. dropdown:: Duty cycle(t2)
   :animate: fade-in-slide-down
   
   -Max  100
   -Min  1
   -Unit  %
   -Description  Stroke height:duty cycle[%] in :term:`time period t2`.

0 85
----

.. dropdown:: The Stroke Height Sensor Type
   :animate: fade-in-slide-down
   
   -Max  2
   -Min  0
   -Unit  stitches
   -Description
     | 0 = Off;
     | 1 = Switch;
     | 2 = Potentiometer.
