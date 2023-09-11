.. _service_counter: 

===============
Service counter
===============

Using service counter allows users to remind regular mechanical maintenance.

**Here is a formula**:

Remaining amount = reset value of the bobbin thread counter(A61) – bobbin thread counter value(A63).

**Setup steps**:

- Set an appropriate value for **A62**, every time N stitches are sewn which set by parameter **A63**, the counter(O44) increases by 1.
- Set an appropriate value for **A61**, this is a very variable value, which depends on how often you want to maintain.
- Enable counter.
- As the sewing, the remaining thread amount(A61-A63) is counted down, when it reaches 0, the machine will stop, and the controller will throw a warning(Code 7). A reset is needed if you want continue.

Parameter List
==============

A 60
----

.. dropdown:: Service Stitch Counter
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | Active service stitch counter:
     | 0 = Off;
     | 1 = On.

A 61
----

.. dropdown:: Service Counter Reset Value
   :animate: fade-in-slide-down
   
   -Max  9999
   -Min  1
   -Unit  --
   -Description  Reset value of service stitch counter
   
A 62
----

.. dropdown:: Service Counter Factor
   :animate: fade-in-slide-down
   
   -Max  200
   -Min  1
   -Unit  stitches
   -Description  Every sew over this number of stitches,increment the counter by 1

A 63
----

.. dropdown:: Service Counter Value
   :animate: fade-in-slide-down
   
   -Max  9999
   -Min  0
   -Unit  -- 
   -Description  The current value of service stitch counter
