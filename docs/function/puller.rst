.. _puller:

======
Puller
======

**How it works**:

- During lifting, raising of puller when lifting the sewing foot.
- During bartack, raising of puller when sewing the start/end bartack.
- During backwards, raising of puller when reverse button pressed.
- The puller is to be switched on via a button, if the puller is switched off, it is always up, if the button is pressed, the puller goes down.

# Parameter List
================

A 64
----

.. dropdown:: Delay stitch
   :animate: fade-in-slide-down

   -Max  255
   -Min  0
   -Unit  stitch
   -Description  Number of stitches until the puller is lowered after seam begin,
                 depens on stitch length and application.

A 89
----

.. dropdown:: Puller
   :animate: fade-in-slide-down

   -Max  1
   -Min  0
   -Unit  --
   -Description
     | Upper puller:
     | 0 = Off;
     | 1 = On.

A 90
----

.. dropdown:: Upper Puller Status
   :animate: fade-in-slide-down

   -Max  1
   -Min  0
   -Unit  --
   -Description  Upper puller status,up or down(read only).

O 97
----

.. dropdown:: Time(t1)
   :animate: fade-in-slide-down

   -Max  999
   -Min  1
   -Unit  ms
   -Description  Puller lifter:activation duration of in :term:`time period t1` (100% duty cycle).

O 98
----

.. dropdown:: Duty cycle(t2)
   :animate: fade-in-slide-down

   -Max  100
   -Min  1
   -Unit  --
   -Description  Puller lifter:duty cycle[%] in :term:`time period t2`.
