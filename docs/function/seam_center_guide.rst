.. _seam_center_guide:

=================
Seam center guide
=================

**When to lift automatically**

Automatic lifting seam center guide is associated with three situations: footlifter, bartack(start or end tack) or reverse, and stroke. Mode is seted by **A51**.

- 0 = Toggle seam center guide raise up/down via a manual button;

- 1 = Raising of seam center guide when lifting the sewing foot;
- 2 = Raising of seam center guide when sewing the bartack/reverse;
- 3 = Raising of seam center guide when sewing the bartack/reverse and lifting the sewing foot;
- 4 = Raising of seam center guide when high stroke;
- 5 = Raising of seam center guide when lifting the sewing foot and high stroke;
- 6 = Raising of seam center guide when sewing the bartack/reverse and high stroke；
- 7 = Raising of seam center guide when lifting the sewing foot, sewing the bartack/reverse and high stroke.


Parameter List
==============

A 33
----

.. dropdown:: Status of Seam Center Guide
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description  Status of the seam center guide solenoid(read only)

A 47
----

.. dropdown:: Seam Center Guide
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | Seam center guide function:
     | 0 = Off;
     | 1 = On.

A 51
----

.. dropdown:: Auto Mode for Seam Center Guide
   :animate: fade-in-slide-down
   
   -Max  7
   -Min  0
   -Unit  --
   -Description
     | 0 = Manual;
     | 1 = Automatically up when foot lifting;
     | 2 = Automatically up when bartacking and reverse;
     | 3 = Both 1&2;
     | 4 = Automatically up when high stroke;
     | 5 = Both 1&4;
     | 6 = Both 2&4;
     | 7 = Both 1&2&4.

O 89
----

.. dropdown:: Time(t1)
   :animate: fade-in-slide-down
   
   -Max  999
   -Min  1
   -Unit  ms
   -Description  Seam Center Guide:activation duration of in :term:`time period t1`
                 (100% duty cycle).

O 90
----

.. dropdown:: Duty cycle(t2)
   :animate: fade-in-slide-down
   
   -Max  100
   -Min  1
   -Unit  %
   -Description  Seam Center Guide:duty cycle[%] in :term:`time period t2`.
