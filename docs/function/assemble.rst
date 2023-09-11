.. _assemble:

========
Assemble
========

Parameter List
==============

A 07
----

.. dropdown:: Lock the Shortkeys <...>
   :animate: fade-in-slide-down
    
   -Max  1  
   -Min  0
   -Unit  --
   -Description
     | To avoid the very thick material from triggering the shortkeys:
     | 0 = Off;
     | 1 = On.

A 19
----

.. dropdown:: Function POSITION -1 <...> 
   :animate: fade-in-slide-down
   
   -Max  2
   -Min  1
   -Unit  --
   -Description  
     | When pedal at :term:`POSITION -1` 
       which funcition is activared:
     | 1 = Sewing foot lift;
     | 2 = Thread trim.

O 03
----

.. dropdown:: MACHINE ID <...> 
   :animate: fade-in-slide-down
   
   -Max  2
   -Min  1
   -Unit  --
   -Description  :term:`MACHINE ID`

O 08
----

.. dropdown:: Pedal Type <...> 
   :animate: fade-in-slide-down
   
   -Max  2
   -Min  1
   -Unit  --
   -Description
     | Choice between an native and standing operation pedal:
     | 0 = Native;
     | 1 = Standing Operation Pedal.

O 30
----

.. dropdown:: Machine ID Storage Location <...> 
   :animate: fade-in-slide-down
   
   -Max  9999
   -Min  0
   -Unit  --
   -Description  
     | Choose where :term:`MACHINE ID` 
       is stored:
     | 1 = Stored in the controller;
     | 2 = Stored in the machine head

O 56
----

.. dropdown:: Pedal Calibration:POSITION END(Forward) <...>
   :animate: fade-in-slide-down
    
    -Max  4095  
    -Min  0
    -Unit  --
    -Description  ADC value by step forward the pedal to the end position, value > O57

O 57
----

.. dropdown:: Pedal Calibration:POSITION 2 and POSITION 1 <...>
   :animate: fade-in-slide-down

    -Max  4095  
    -Min  0
    -Unit  --
    -Description  ADC value of the border between POSITION 2 and POSITION 1, O56 < value < O58

O 58
----
.. dropdown:: Pedal Calibration:POSITION 1 and POSITION 0 <...>
   :animate: fade-in-slide-down

    -Max  4095  
    -Min  0
    -Unit  --
    -Description  ADC value of the border between POSITION 1 and POSITION 0, O57 < value < O59

O 59
----
.. dropdown:: Pedal Calibration:POSTIION 0 and POSTIION -1 <...>
   :animate: fade-in-slide-down

    -Max  4095  
    -Min  0
    -Unit  --
    -Description  ADC value of the border between POSTIION 0 and POSTIION -1, O58 < value < O60

O 60
----
.. dropdown:: Pedal Calibration:POSTIION -1 and POSTIION -2 <...>
   :animate: fade-in-slide-down

    -Max  4095  
    -Min  0
    -Unit  --
    -Description  ADC value of the border between POSTIION -1 and POSTIION -2, O59 < value < O61

O 61
----
.. dropdown:: Pedal Calibration:POSITION END(Backward) <...>
   :animate: fade-in-slide-down

    -Max  4095  
    -Min  0
    -Unit  --
    -Description  ADC value by step forward the pedal to the end position,value < O60. 

O 62
----
.. dropdown:: Pedal Calibration:Schmitt Loop value <...>
   :animate: fade-in-slide-down

    -Max  4095  
    -Min  0
    -Unit  --
    -Description  ADC value of the schmitt loop.

O 63
----
.. dropdown:: Speed Curve Pedal <...>
   :animate: fade-in-slide-down

   -Max  4095  
   -Min  0
   -Unit  --
   -Description
     | 0 = linear;
     | 1 = 2 lines;
     | 2 = Curve(start slowly,end fast);
     | 3 = Curve(start fast,end slowly);
     | 4 = S curve(start slowly,middle fast,end slowly);
     | 5 = S curve(start fast,middle slowly,end fast).

O 80
----
.. dropdown:: Keypad Type <...>
   :animate: fade-in-slide-down

   -Max  3  
   -Min  1
   -Unit  --
   -Description
     | Type of the keypad:
     | 1 = 6 keys;
     | 2 = 7 keys;
     | 3 = 12 keys.
