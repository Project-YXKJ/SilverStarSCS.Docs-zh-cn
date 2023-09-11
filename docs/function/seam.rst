.. _seam:

====
Seam
====

**Program and seam**

A seam is the basic concept, usually a seam is divided into three parts: start bartack, middle sewing, end bartack and thread cutting. A seam starts from stepping on pedal position 1 for the first time, and ends when stepping on position -2.

A sewing program contains at least one seam. Let's call it Seam-01, Seam-02 ... Seam-n, program controls them sewing automatically, when Seam-n is finished, program end.



**Fixed stitches program**

Fixed stitch sewing is a sewing program that allows users to freely program. Up to 25 seam segments can be programmed, each with a maximum of 99 stitches.

The functions of the sewing program are divided into two areas: the global functions related to the sewing program and the local functions related to the seam segment.

Global functions:

- Soft start

Local functions:

- Number of stitches
- Start/end bartack
- Thread clamp
- Thread trim
- Needle position when sewing stops
- Automatic elevation of sewing foot when sewing stops
- Automatic elevation of sewing foot after thread trim(seam end)

The seam segment whose stitch number is equal to 0 is considered as the end of the program. If the stitch number of the next segment is 0, the program will return to the first segment; After any seam section ends, if you step on the pedal -2, the whole program will be ended. If the thread trimming has not been executed at this time, the thread trimming will be executed and return to the first section, otherwise program will be directly returned to the first section.

**Correction(Needle up/down)**

If **A03** is equal to 0:

When press the key, the needle moves form the current position to the position set by parameter **D15** or **D16**, which one is the closest, the target position is that one. E.g, current position is 40 degrees, **D15** is 70, **D16** is 200, when you press the button, the motion trace is "40->70->200->70->200...".

If **A03** is equal to 1:

when you press the button, two cases: if you set stop at upper position, the needle moves form the current position to the position set by parameter **D01**. if you set stop at lower position, the needle moves form the current position to the position set by parameter **D02**:

Parameter List
==============

S 05
----

.. dropdown:: Speed in W-Sewing
   :animate: fade-in-slide-down
   
   -Max  4500
   -Min  100
   -Unit  spm
   -Description  Maximum speed in W-Sewing

S 06
----

.. dropdown:: Speed in Program Sewing
   :animate: fade-in-slide-down
   
   -Max  4500
   -Min  100
   -Unit  spm
   -Description  Maximum speed in programmed stitches sewing

A 01
----

.. dropdown:: Needle Position
   :animate: fade-in-slide-down

   -Max  1
   -Min  0
   -Unit  --
   -Description
     | Postion of the needle when sewing stop:     
     | 0 = in the material;
     | 1 = upper needle position.

A 02
----

.. dropdown:: Auto Sewing for Program Sewing
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | 0 = The middle speed of the sewing is controlled by the pedal;
     | 1 = The sewing is performed automatically.  

A 03
----

.. dropdown:: Correction mode
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | 0 = Half stitch;
     | 1 = One stitch

A 16
----

.. dropdown:: Mode After Start Bartack in Programmed Sewing 
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | After start tacking is finished in programmed sewing:
     | 0 = machine stops and must restart with the pedal;
     | 1 = sewing continues after end.

A 17
----

.. dropdown:: Auto End bartack and Trim when Programmed Sewing is finished
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description  
     | Whether end tacking and trim is automatically activated at seam end im programmed seam:
     | 0 = continue by pedal;
     | 1 = automatic.

A 30
----

.. dropdown:: Correction Mode
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | 0 = single correction;
     | 1 = continuous correction.

A 31
----

.. dropdown:: Manual Revserse SW.
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | 0 = Normal;
     | 1 = Reverse at stop.

D 11
----

.. dropdown:: The minimum angle of Off reverse key function
   :animate: fade-in-slide-down
   
   -Max  359
   -Min  0
   -Unit  1°
   -Description  If the needle position is greater than this angle, the manual reverse
                 sewing button will not work.

D 11
----

.. dropdown:: The maximum angle of Off reverse key function
   :animate: fade-in-slide-down
   
   -Max  359
   -Min  0
   -Unit  1°
   -Description  If the needle position is greater than this angle, the manual reverse
                 sewing button will not work.

D 15
----

.. dropdown:: Correction:Upper Position
   :animate: fade-in-slide-down
   
   -Max  359
   -Min  0
   -Unit  1°
   -Description  Upper needle position in correction mode.

D 16
----

.. dropdown:: Correction:Lower Position
   :animate: fade-in-slide-down
   
   -Max  359
   -Min  0
   -Unit  1°
   -Description  Lower needle position in correction mode.

D 18
----

.. dropdown:: Sewing mode
   :animate: fade-in-slide-down
   
   -Max  3
   -Min  1
   -Unit  --
   -Description  Sewing mode(read only).

O 69
----

.. dropdown:: Correction Timming
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description  
     | Choose when you can correction:
     | 0 = Unavailable after trim;
     | 1 = Available during machine stop.





O 37
----

.. dropdown:: < > Detail 
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description  
     | No-position mode, stop at random position:
     | 0 = Off;
     | 1 = On.
