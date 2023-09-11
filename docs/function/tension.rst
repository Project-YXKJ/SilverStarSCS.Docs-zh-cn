.. _tension:

==============
Thread tension
==============

**During thread cutting:**

The thread tension power on when position is reached with D13 and power off when
position is reached with D14 during thread trimming.

**During foot lifting:**

Adjust parameter of the thread tension during active foot lift: the mode for thread
tension is determined by parameter A27, the default value is 2.

**During 2nd Sewing foot stroke:**

Adjust parameter of the sewing foot stroke during active the second thread tension:
the mode is determined by parameter A28, the default value 1.

**Electromagnetor solenoid valve:**

If tension is controlled by electromagnet not solenoid valve, you need to be careful
when setting tha value of **O75**. Over premissible power on time, the electromagnet
may burn out, thus a electromagnet with a small value of **O75** is protected form damage.


Parameter List
==============

A 26
----

.. dropdown:: Status of Additional Thread Tension
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description  Status of the additional tension solenoid(read only)

A 27
----

.. dropdown:: Auto mode for tension at foot lifting
   :animate: fade-in-slide-down
   
   -Max  3
   -Min  0
   -Unit  --
   -Description
     | Mode for lifting the tension during active sewing foot lift:
     | 0 = tension is not lifted;
     | 1 = tension is lifted as the foot is lifted during sewing;
     | 2 = tension is lifted after trim;
     | 3 = tension is lifted as the foot is lifted during sewing and after trim.
     
A 28
----

.. dropdown:: Auto Additional Thread Tension
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | If the second stroke active,the additional thread tenson is automatically activated:
     | 0 = Off;
     | 1 = On.    

D 13
----

.. dropdown:: Start Tension Position
   :animate: fade-in-slide-down
   
   -Max  359
   -Min  0
   -Unit  1°
   -Description  Position when the magnet of tenison is activated during trimming

D 14
----

.. dropdown:: Stop Tension Position
   :animate: fade-in-slide-down
   
   -Max  359
   -Min  0
   -Unit  1°
   -Description  Position when the magnet of tension is deactivated during trimming

O 49
----

.. dropdown:: Time(t1)
   :animate: fade-in-slide-down
   
   -Max  999
   -Min  1
   -Unit  ms
   -Description  Tension:activation duration of in :term:`time period t1` 
                 (100% duty cycle)

O 50
----

.. dropdown:: Duty cycle(t2)
   :animate: fade-in-slide-down
   
   -Max  100
   -Min  1
   -Unit  %
   -Description  Tension:duty cycle[%] in :term:`time period t2`.

O 75
----

.. dropdown:: Tension Max. Lifting Time
   :animate: fade-in-slide-down
   
   -Max  9999
   -Min  0
   -Unit  ms
   -Description 
     | 0 = Always Lifting;
     | Not 0 = This parameter sets the power-off time.
     
O 86
----

.. dropdown:: Time(t1)
   :animate: fade-in-slide-down
   
   -Max  500
   -Min  1
   -Unit  ms
   -Description  Additional Tension:activation duration of in :term:`time period t1`
                 (100% duty cycle)

O 87
----

.. dropdown:: Duty cycle(t2)
   :animate: fade-in-slide-down
   
   -Max  100
   -Min  1
   -Unit  %
   -Description  Additional Tension:duty cycle[%] in :term:`time period t2`.

O 88
----

.. dropdown:: Addition tension solenoid work mode
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | 0 = solenoid on,tension off;
     | 1 = solenoid on,tension on.
