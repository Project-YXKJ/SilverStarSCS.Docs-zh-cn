.. _multitest:

=========
Multitest
=========

When the endurance test starts, the machine will run automatically until the test time 
which set by **O25** is reached.


Parameter List
==============

O 23
----

.. dropdown:: Running Time(EC) 
   :animate: fade-in-slide-down
   
   -Max  60
   -Min  1
   -Unit  s
   -Description  Running time of an endurance cycle,unit:second

O 24
----

.. dropdown:: Standby Time(EC)
   :animate: fade-in-slide-down
   
   -Max  60
   -Min  1
   -Unit  s
   -Description  Standby time of an endurance cycle,unit:second

O 25
----

.. dropdown:: Total Time(EC)
   :animate: fade-in-slide-down
   
   -Max  720
   -Min  1
   -Unit  h
   -Description  Total endurance time,unit:hour

O 26
----

.. dropdown:: Endurance Running
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description 
     | Whether to start an endurance running test:
     | 0 = Off;
     | 1 = On.
