.. _safety-sensor:

=============
Safety Sensor
=============

Tilt safaty switch
==================

Parameter List
--------------


T 09
^^^^

.. dropdown:: Debouncing of Tilt safaty Switch <...>
   :animate: fade-in-slide-down
   
   -Max  1000
   -Min  1
   -Unit  ms
   -Description  The time is less and the sensitivity is higher,perfect debounce
     time can prevent false alarm

O 31
^^^^

.. dropdown:: Warning: Tilt safety switch <...>
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | Whether to throw a warning when the machine is tilted:
     | 0 = Off;
     | 1 = On.
     
O 32
^^^^

.. dropdown:: Sensor Polarity(Tilt Safety) <...>
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | 0 = Normal close;
     | 1 = Normal open.



Eye Guard
=========

Parameter List
--------------

O 28
^^^^

.. dropdown:: Warning: Eye Guard <...>
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | Optional features,whether to throw a warning when the eye guard isn't in the
       right place:
     | 0 = Off;
     | 1 = On.

Hook cover missing
==================

Parameter List
--------------

O 29
^^^^

.. dropdown:: Warning: Hook Cover <...> 
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | Optional features,whether to throw a warning when the hook cover is removed:
     | 0 = Off;
     | 1 = On.
     

Oil Level
=========

Parameter List
--------------

O 34
^^^^

.. dropdown:: Warning:Oil Level <...> 
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | Optional features,whether to throw a warning when the lubricating oil level
       is too low:
     | 0 = Off;
     | 1 = On.


Upper Thread Breaking
=====================

Parameter List
--------------

T 13
^^^^

.. dropdown:: Debouncing of Upper Thread Break <...> 
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description  The time is less and the sensitivity is higher, perfect debounce
     time can prevent false alarm.

O 92
^^^^

.. dropdown:: Sensor Polarity(Upper Thread Breaking) <...> 
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | 0 = Normal open;
     | 1 = Normal closed.
