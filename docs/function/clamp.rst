.. _thread_clamp:

============
Thread clamp
============

**Thread clamp at seam start**:

Switch on at position set by **D07**, switch off at position set by **D08**.

Action only during the first stitch, reset after thread trim.

**Thread clamp at turning back**:

Switch on during turning back, the Max. permissible time is set by **T15** to protect from damage.

**Thread clamp at sewing foot lifting**:

Switch on during foot lifting, the Max. permissible time is set by **T15** to protect from damage.

Parameter List
==============

T 15
----

.. dropdown:: Action Time of Clamp <...>
   :animate: fade-in-slide-down
   
   -Max  2000
   -Min  1
   -Unit  ms
   -Description  Action time of clamp when lifting the foot or lifting the needlebar after trim.

A 10
----

.. dropdown:: Thread clamp <...>
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | Thread clamp:
     | 0: Off;
     | 1: On.

A 29
----

.. dropdown:: Auto Mode for Clamp <...> 
   :animate: fade-in-slide-down
   
   -Max  3
   -Min  0
   -Unit  --
   -Description
     | 0 = actions when start sewing;
     | 1 = actions when start sewing and lifting the needle after trim;
     | 2 = actions when start sewing and lifting the foot;
     | 3 = both 1&2.


D 07
----

.. dropdown:: Start Clamp Position <...> 
   :animate: fade-in-slide-down
   
   -Max  359
   -Min  0
   -Unit  1°
   -Description  Position when the magnet of clamp is activated.

D 08
----

.. dropdown:: Stop Clamp Position <...>
   :animate: fade-in-slide-down
   
   -Max  359
   -Min  0
   -Unit  1°
   -Description  Position when the magnet of clamp is deactivated.

O 42
----

.. dropdown:: PrePressure duiring Clamp <...>
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description  
     | Reduce the sewing foot pressure during the clamping cycle:
     | 0: Off;
     | 1: On.  

O 48
----

.. dropdown:: Duty cycle(t2) <...>
   :animate: fade-in-slide-down
   
   -Max  100
   -Min  0
   -Unit  %
   -Description  Clamp:duty cycle[%] in :term:`time period t2`.
