.. _thread_cutter:

=============
Thread cutter
=============

**Thread cutting procedure**

Thread cutting singnal is switched on when the angle value **D03** has been reached,
the switched off when the angle value **D04**. If the position is not reached because
of a mechanical error, the thread cutter signal is switched off after 500ms for protect
the magnet from damage.


Parameter List
==============

S 07
----

.. dropdown:: Trimming Speed
   :animate: fade-in-slide-down
   
   -Max  300
   -Min  150
   -Unit  spm
   -Description  Speed of the machine during trimming

A 06
----

.. dropdown:: Thread Trim
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | Thread trim:
     | 0 = Off;
     | 1 = On.

A 42
----

.. dropdown:: Short Thread Cutter
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | Feature for specific models:
     | 0 = Off;
     | 1 = On.     

A 67
----

.. dropdown:: Short Thread Cutter Stitches
   :animate: fade-in-slide-down
   
   -Max  10
   -Min  0
   -Unit  stitches
   -Description  When short thread cutter active,number of short length stitches before trim.

D 03
----

.. dropdown:: Start trim position
   :animate: fade-in-slide-down
   
   -Max  359
   -Min  0
   -Unit  1°
   -Description  Position when the magnet of thread cutter is activated.


D 04
----

.. dropdown:: Stop trim position
   :animate: fade-in-slide-down
   
   -Max  359
   -Min  0
   -Unit  1°
   -Description  Position when the magnet of thread cutter is deactivated.

D 17
----

.. dropdown:: Start Movable Knife Position(STC)
   :animate: fade-in-slide-down
   
   -Max  359
   -Min  0
   -Unit  1°
   -Description  Position when the magnet of movable knife(short thread cutter) is activated.

D 18
----

.. dropdown:: Stop Movable Knife Position(STC)
   :animate: fade-in-slide-down
   
   -Max  359
   -Min  0
   -Unit  1°
   -Description  Position when the magnet of movable knife(short thread cutter) is deactivated.

D 19
----

.. dropdown:: Start Reverse Position(STC)
   :animate: fade-in-slide-down
   
   -Max  359
   -Min  0
   -Unit  1°
   -Description  Position when the magnet of the reverse(short thread cutter) is activated.

D 20
----

.. dropdown:: Stop Reverse Position(STC)
   :animate: fade-in-slide-down
   
   -Max  359
   -Min  0
   -Unit  1°
   -Description  Position when the magnet of the reverse(short thread cutter) is deactivated.

D 21
----

.. dropdown:: Start Zero Stitch Length Position(STC)
   :animate: fade-in-slide-down
   
   -Max  359
   -Min  0
   -Unit  1°
   -Description  Position when the magnet of zero stitch length(short thread cutter) is activated.

D 22
----

.. dropdown:: Stop Zero Stitch Length Position(STC)
   :animate: fade-in-slide-down
   
   -Max  359
   -Min  0
   -Unit  1°
   -Description  Position when the magnet of zero stitch length(short thread cutter) is deactivated.
   
O 38
----

.. dropdown:: Pedal Reset After Trim
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | Whether the pedal need to return Position 0 before restart a new seam after trim:
     | 0 = Off;
     | 1 = On.

O 95
----

.. dropdown:: Time(t1)
   :animate: fade-in-slide-down
   
   -Max  999
   -Min  1
   -Unit  ms
   -Description  Short thread zero length:activation duration of in :term:`time period t1`
                 (100% duty cycle).

O 96
----

.. dropdown:: Duty cycle(t2)
   :animate: fade-in-slide-down
   
   -Max  100
   -Min  1
   -Unit  %
   -Description  Short thread zero length:duty cycle[%] in :term:`time period t2`.
