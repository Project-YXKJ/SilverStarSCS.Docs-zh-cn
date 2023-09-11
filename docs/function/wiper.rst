.. _thread_wiper:

============
Thread wiper
============

The thread wiper function runs after the cutting procedure.

When thread cutter is completed and the time set by **T03** is delayed, the wiper 
will switch on, it will switch off after the time set by **T04**.

Parameter List
==============

A 08
----

.. dropdown:: Wiper
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | Wiper upper thread:
     | 0: Off;
     | 1: On.
     
T 03
----

.. dropdown:: Wiper Delay time
   :animate: fade-in-slide-down
   
   -Max  200
   -Min  1
   -Unit  ms
   -Description  Lag time, after which, wiper is activaed after trim

T 04
----

.. dropdown:: Wiper Activation Duration
   :animate: fade-in-slide-down
   
   -Max  200
   -Min  1
   -Unit  ms
   -Description  Time form activation to deactivation of the magnet of wiper.
