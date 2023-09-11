.. _second_stitch_length:

====================
Second stitch length
====================


**Speed limit when second stitch length activated:**

If parameter **O33** set to 1, the speed is reduced down to parameter **S17** when 
2nd stitch length activated.


Parameter List
==============

S 17
----

.. dropdown:: Max. Speed Long Stitch Length
   :animate: fade-in-slide-down
   
   -Max  4500
   -Min  100
   -Unit  spm
   -Description  Limiting speed if long stitch length is activated

A 25
----

.. dropdown:: Status of Second Stitch Length
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description  Status of the second stitch length solenoid(read only)

A 46
----

.. dropdown:: Stitch Length
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | Short/Long stitch length:
     | 0 = Off;
     | 1 = On.

A 50
----

.. dropdown:: Stitch length during bartack
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | Choose whether to switch short stitch length automatically:
     | 0 = Off;
     | 1 = On.

O 33
----

.. dropdown:: Speed limitation stitch length
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | The speed is limited during using long stitch length:
     | 0 = Off;
     | 1 = On.

O 78
----

.. dropdown:: Time(t1)
   :animate: fade-in-slide-down
   
   -Max  999
   -Min  1
   -Unit  ms
   -Description  Second stitch length:activation duration of in :term:`time period t1`
                 (100% duty cycle).

O 79
----

.. dropdown:: Duty cycle(t2)
   :animate: fade-in-slide-down
   
   -Max  100
   -Min  1
   -Unit  %
   -Description  Second stitch length:duty cycle[%] in :term:`time period t2`.
