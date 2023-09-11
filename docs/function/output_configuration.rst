.. _output_configuration:

====================
Output configuration
====================

Output Mode Code List:

  - 0 = No function;
  - 1 = Thread cutter;
  - 2 = Thread tension;
  - 3 = Thread clamp;
  - 4 = Reverse;
  - 5 = Sewing foot lifter;
  - 6 = Stroke;
  - 7 = Additional thread tension;
  - 8 = Thread wiper;
  - 9 = Second stitch length;
  - 10 = Needle cooling;
  - 11 = Additional cutter for short thread cutter machine;
  - 12 = Seam center guide;
  - 13 = Zero stitch length for short thread cutter machine;
  - 14 = Auto corner for 2-needle machine;
  - 15 = Puller

**How to setup the function of output ports**:

follow the steps:

- Confirm which output port is connected to the solenoid valve, like output-07 or output-06. 
  In this step, you need to know the specific model of the system you are using, then refer to its wiring diagram.

- Refer to the table at the beginning of this chapter, get the parameter value you need.

- Restart the system

Let's take an example:

For example, if **Output-01** is connected, set the function of **Output-01** to puller, that is, **A71** is set to 15 (15 is the code for puller function).


Parameter List
==============

A 71
----

.. dropdown:: Mode Output-01 
   :animate: fade-in-slide-down
   
   -Max  maximum
   -Min  minimum
   -Unit  unit
   -Description  Function definition of Output-01

A 72
----

.. dropdown:: Mode Output-02 
   :animate: fade-in-slide-down
   
   -Max  maximum
   -Min  minimum
   -Unit  unit
   -Description  Function definition of Output-02    

A 73
----

.. dropdown:: Mode Output-03
   :animate: fade-in-slide-down
   
   -Max  maximum
   -Min  minimum
   -Unit  unit
   -Description  Function definition of Output-03

A 74
----

.. dropdown:: Mode Output-4 
   :animate: fade-in-slide-down
   
   -Max  maximum
   -Min  minimum
   -Unit  unit
   -Description  Function definition of Output-04

A 75
----

.. dropdown:: Mode Output-05 
   :animate: fade-in-slide-down
   
   -Max  maximum
   -Min  minimum
   -Unit  unit
   -Description  Function definition of Output-05


A 76
----

.. dropdown:: Mode Output-06
   :animate: fade-in-slide-down
   
   -Max  maximum
   -Min  minimum
   -Unit  unit
   -Description  Function definition of Output-06

A 77
----

.. dropdown:: Mode Output-07 
   :animate: fade-in-slide-down
   
   -Max  maximum
   -Min  minimum
   -Unit  unit
   -Description  Function definition of Output-07

A 78
----

.. dropdown:: Mode Output-08 
   :animate: fade-in-slide-down
   
   -Max  maximum
   -Min  minimum
   -Unit  unit
   -Description  Function definition of Output-08

A 79
----

.. dropdown:: Mode Output-09 
   :animate: fade-in-slide-down
   
   -Max  maximum
   -Min  minimum
   -Unit  unit
   -Description  Function definition of Output-09

A 80
----

.. dropdown:: Mode Output-10 
   :animate: fade-in-slide-down
   
   -Max  maximum
   -Min  minimum
   -Unit  unit
   -Description  Function definition of Output-10
