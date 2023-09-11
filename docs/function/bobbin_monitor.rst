.. _bobbin_monitor:

==============
Bobbin Counter
==============

Using Lower thread counter allows users to know the remaining thread amount.


**Here is a formula**:

Remaining thread amount = reset value of the bobbin thread counter(O43) - bobbin thread counter value(O44).

**Setup steps**:

- Set an appropriate value for O19, every time N stitches are sewn which set by parameter O19, the counter(O44) increases by 1.

- Set an appropriate value for O43, this is a very variable value, which depends on the size of the bobbin and the thickness of the thread.

- Choose when to throw a warning by setting O20, immediately or after thread cutting.

- Enable counter.
- As the sewing, the remaining thread amount(O43-O44) is counted down, when it reaches 0, the machine will stop, and the controller will throw a warning(Code 5). A reset is needed if you want continue.


Parameter List
==============

A 12
----

.. dropdown:: Bobbin Stitch Counter <...>
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | Activate the Bobbin stitch counter:
     | 0: Off;
     | 1: On.

O 19
----

.. dropdown:: Factor of bobbin counter <...>
   :animate: fade-in-slide-down
   
   -Max  200
   -Min  1
   -Unit  stitches
   -Description  Every sew over this number of stitches,increment the counter by 1.

O 20
----

.. dropdown:: Timming of Warning(Bobbin Counter) <...>
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  stitches
   -Description  
     | When to throw a warning if bobbin counter reaches 0:
     | 0 = after thread cutting;
     | 1 = immediately
     
O 43
----

.. dropdown:: Bobbin Stitch Counter Reset Value <...>
   :animate: fade-in-slide-down
   
   -Max  9999
   -Min  1
   -Unit  --
   -Description  Bobbin supply capacity. This is a very variable value,which depends
     on the size of the bobbin and the thickness of the thread

O 44
----

.. dropdown:: Bobbin Stitch Counter Value <...>
   :animate: fade-in-slide-down
   
   -Max  9999
   -Min  0
   -Unit  --
   -Description  The current value of bobbin stitch counter, the reset value minus 
     this value is remaining value.
