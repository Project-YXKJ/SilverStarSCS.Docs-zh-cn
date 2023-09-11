.. _soft_start:

==========
Soft start
==========

Parameter List
==============

When beginning a new seam, speed is determined by the pedal and limited to the soft 
start speed.

S 08
----

.. dropdown:: Soft Start Speed
   :animate: fade-in-slide-down
   
   -Max  500
   -Min  200
   -Unit  spm 
   -Description  Speed for soft start

A 21
----

.. dropdown:: Soft start 
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  -- 
   -Description
     | Soft start when a new seam start:
     | 0 = On;
     | 1 = Off.
     
O 01
----

.. dropdown:: Number of soft start stitches
   :animate: fade-in-slide-down
   
   -Max  10
   -Min  1
   -Unit  stitches 
   -Description  Number of stitches to be made during a soft start.
