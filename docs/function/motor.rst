.. _motor: 

=====
Motor
=====

**Holding force of the motor:**

Enable this function by set **A54** to 1.

This function prevents unwanted wandering of the needle when machine has stopped. The effect can be checked by turning the hand wheel.

The maximum time the holding force can keep takes effect is determined by parameter **A66**.

- If **A66** equal to 0, it take effect always when stopped.
- If **A66** is not equal to 0, effective time is the value set by **A66**.

Parameter List
==============

S 01
----

.. dropdown:: Max. Speed
   :animate: fade-in-slide-down
   
   -Max  4500
   -Min  100
   -Unit  spm
   -Description  Maximum speed by press the pedal to the end position.
     
S 02
----
.. dropdown:: Min. Speed
   :animate: fade-in-slide-down
  
   -Max  4500
   -Min  100
   -Unit  spm
   -Description  Minimum sewing speed, it is also the needle position up-down speed

     
A 18
----
.. dropdown:: Auto Upper Position When Power-on
   :animate: fade-in-slide-down
  
   -Max  4500
   -Min  100
   -Unit  spm
   -Description  
     | Needle position is automatically moved to upper position after power-on:
     | 0:Off;
     | 1:On.

A 54
----

.. dropdown:: Holding Force
   :animate: fade-in-slide-down
  
   -Max  1
   -Min  0
   -Unit  --
   -Description  
     | Setting the holding force of the motor after stop:
     | 0 = Off;
     | 1 = On.

A 55
----

.. dropdown:: Lock Shaft Slot Angle
   :animate: fade-in-slide-down
  
   -Max  720
   -Min  1
   -Unit  --
   -Description  The shaft is locked a range within this angle.

A 56
----

.. dropdown:: Position Error Threshold of Lock Shaft Function takes effect
   :animate: fade-in-slide-down
  
   -Max  720
   -Min  1
   -Unit  --
   -Description  When the position error is large than the parameters, the motor will 
                 start to adjust the position.

A 57
----

.. dropdown:: Position Error Threshold of Lock Shaft Function does not take effect
   :animate: fade-in-slide-down
  
   -Max  720
   -Min  1
   -Unit  --
   -Description  When the position error is small than the parameters,the motor will 
                 standby. 

A 66
----

.. dropdown:: Holding Force Mode
   :animate: fade-in-slide-down
  
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | 0 = The motor holds always;
     | Not 0 = The holding force turns off after the time set by this parameter.

D 01
----

.. dropdown:: Upper Needle Position
   :animate: fade-in-slide-down
  
   -Max  359
   -Min  0
   -Unit  1°
   -Description  Needle in the upper position.

D 02
----

.. dropdown:: Lower Needle Position
   :animate: fade-in-slide-down
  
   -Max  359
   -Min  0
   -Unit  1°
   -Description  Needle in the lower position.

O 04
----

.. dropdown:: Machine Sync Signal Source 
   :animate: fade-in-slide-down
  
   -Max  1
   -Min  0
   -Unit  --
   -Description  
     | 0 = Extern;
     | 1 = Motor.

O 36
----

.. dropdown:: Input Speed Scaling
   :animate: fade-in-slide-down
  
   -Max  5
   -Min  0
   -Unit  --
   -Description  Speed scaling allows the machine to run at lower speed than the set.

O 37
----

.. dropdown:: Input Speed Scaling
   :animate: fade-in-slide-down
  
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | In Simple mode, no seam program,no trim,no position, etc, except the motor can run:
     | 0 = Off;
     | 1 = On.

O 67
----

.. dropdown:: Directions of Motor Rotation
   :animate: fade-in-slide-down
  
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | 0 = Counterclockwise;
     | 1 = Clockwise, viewing the motor from handwheel  

I 01
----

.. dropdown:: Acceleration
   :animate: fade-in-slide-down
  
   -Max  500
   -Min  150
   -Unit  ms
   -Description  The time for accelerating from 0rpm to 4500rpm

I 02
----

.. dropdown:: Deacceleration
   :animate: fade-in-slide-down
  
   -Max  500
   -Min  150
   -Unit  ms
   -Description  The time for deaccelerating from 4500rpm to 0rpm

I 03
----

.. dropdown:: Electrical Angle
   :animate: fade-in-slide-down
  
   -Max  4096
   -Min  0
   -Unit  --
   -Description  The offset of electrical angle

I 04
----

.. dropdown:: Transmission Ratio
   :animate: fade-in-slide-down
  
   -Max  4096
   -Min  1 
   -Unit  --
   -Description  The number of pulses output by motor encoder corresponding to one
                 rotation of the machine


I 05
----

.. dropdown:: Kp(CSC-t)
   :animate: fade-in-slide-down
  
   -Max  9999
   -Min  0
   -Unit  --
   -Description  Kp in Closed-loop Speed Control-trimming 

I 06
----

.. dropdown:: Divisor of Kp(CSC-t)
   :animate: fade-in-slide-down
  
   -Max  99
   -Min  0
   -Unit  --
   -Description  Divisor of Kp in Closed-loop Speed Control-trimming

I 07
----

.. dropdown:: Ki(CSC-t) 
   :animate: fade-in-slide-down
  
   -Max  9999
   -Min  0
   -Unit  --
   -Description  Ki in Closed-loop Speed Control-trimming

I 08
----

.. dropdown:: Divisor of Ki(CSC-t)
   :animate: fade-in-slide-down
  
   -Max  99
   -Min  0
   -Unit  --
   -Description  Divisor of Ki in Closed-loop Speed Control-trimming

I 09
----

.. dropdown:: Kp(CSC)
   :animate: fade-in-slide-down
  
   -Max  9999
   -Min  0
   -Unit  --
   -Description  Kp in Closed-loop Speed Control

I 10
----

.. dropdown:: Divisor of Kp(CSC)
   :animate: fade-in-slide-down
  
   -Max  99
   -Min  0
   -Unit  --
   -Description  Divisor of Kp in Closed-loop Speed Control

I 11
----

.. dropdown:: Ki(CSC)
   :animate: fade-in-slide-down
  
   -Max  9999
   -Min  0
   -Unit  --
   -Description  Ki in Closed-loop Speed Control

I 12
----

.. dropdown:: Divisor of Ki(CSC)
   :animate: fade-in-slide-down
  
   -Max  99
   -Min  0
   -Unit  --
   -Description  Divisor of Ki in Closed-loop Speed Control


I 13
----

.. dropdown:: Upper Output limit(CSC)
   :animate: fade-in-slide-down
  
   -Max  20
   -Min  1
   -Unit  --
   -Description  Upper Output limit in Closed-loop Speed Control


I 14
----

.. dropdown:: Feedforward(CSC)
   :animate: fade-in-slide-down
  
   -Max  500
   -Min  0
   -Unit  --
   -Description  Feedforward in Closed-loop Speed Control

I 15
----

.. dropdown:: Kp(CCC-d)
   :animate: fade-in-slide-down
  
   -Max  9999
   -Min  0
   -Unit  --
   -Description  Kp in Closed-loop Current Control-d axis

I 16
----

.. dropdown:: Divisor of Kp(CCC-d)
   :animate: fade-in-slide-down
  
   -Max  99
   -Min  0
   -Unit  --
   -Description  Divisor of Kp in Closed-loop Current Control-d axis

I 17
----

.. dropdown:: Ki(CCC-d)
   :animate: fade-in-slide-down
  
   -Max  9999
   -Min  0
   -Unit  --
   -Description  Ki in Closed-loop Current Control-d axis

I 18
----

.. dropdown:: Divisor of Ki(CCC-d)
   :animate: fade-in-slide-down
  
   -Max  99
   -Min  0
   -Unit  --
   -Description  Divisor of Ki in Closed-loop Current Control-d axis

I 19
----

.. dropdown:: Upper Output limit(CCC-d)
   :animate: fade-in-slide-down
  
   -Max  3276
   -Min  0
   -Unit  --
   -Description  Upper Output limit in Closed-loop Current Control-d axis

I 20
----

.. dropdown:: Lower Output limit(CCC-d)
   :animate: fade-in-slide-down
  
   -Max  3276
   -Min  0
   -Unit  --
   -Description  Lower Output limit in Closed-loop Current Control-d axis

I 21
----

.. dropdown:: Kp(CCC-q)
   :animate: fade-in-slide-down
  
   -Max  9999
   -Min  0
   -Unit  --
   -Description  Kp in Closed-loop Current Control-q axis

I 22
----

.. dropdown:: Divisor of Kp(CCC-q)
   :animate: fade-in-slide-down
  
   -Max  99
   -Min  0
   -Unit  --
   -Description  Divisor of Kp in Closed-loop Current Control-q axis

I 23
----

.. dropdown:: Ki(CCC-q)
   :animate: fade-in-slide-down
  
   -Max  9999
   -Min  0
   -Unit  --
   -Description  Ki in Closed-loop Current Control-q axis

I 24
----

.. dropdown:: Divisor of Ki(CCC-q)
   :animate: fade-in-slide-down
  
   -Max  9999
   -Min  0
   -Unit  --
   -Description  Divisor of Ki in Closed-loop Current Control-q axis

I 25
----

.. dropdown:: Upper Output limit(CCC-q)
   :animate: fade-in-slide-down
  
   -Max  3276
   -Min  0
   -Unit  --
   -Description  Upper Output limit in Closed-loop Current Control-q axis

I 26
----

.. dropdown:: Lower Output limit(CCC-q)
   :animate: fade-in-slide-down
  
   -Max  3276
   -Min  0
   -Unit  --
   -Description  Lower Output limit in Closed-loop Current Control-q axis

I 27
----

.. dropdown:: Encoder Resolution
   :animate: fade-in-slide-down
  
   -Max  9999
   -Min  1
   -Unit  --
   -Description  Lines Per Revolution of the motor encoder

I 28
----

.. dropdown:: Stop Routine Max. Time
   :animate: fade-in-slide-down
  
   -Max  9999
   -Min  0
   -Unit  ms
   -Description  The maxmum time of stop routine

I 30
----

.. dropdown:: Stop mode
   :animate: fade-in-slide-down
  
   -Max  1
   -Min  0 
   -Unit  --
   -Description
     | Select the mode of reaching the target position:
     | 0 = Speed mode;
     | 1 = Position mode.  


I 33
----

.. dropdown:: MACHINE ZERO Offset
   :animate: fade-in-slide-down
  
   -Max  1
   -Min  0 
   -Unit  --
   -Description  The offset of between MACHINE ZERO and motor synchronization point.

I 37
----

.. dropdown:: Distance(Brake P-S process)
   :animate: fade-in-slide-down
  
   -Max  359
   -Min  0 
   -Unit  1°
   -Description  The distance of brake Position-Speed process

I 38
----

.. dropdown:: Initial Speed(Brake P-S process)
   :animate: fade-in-slide-down
  
   -Max  500
   -Min  100 
   -Unit  spm
   -Description  The initial speed of brake Position-Speed process

I 39
----

.. dropdown:: Terminal speed(Brake P-S process)
   :animate: fade-in-slide-down
  
   -Max  100
   -Min  20 
   -Unit  spm
   -Description  The terminal speed of brake Position-Speed process


I 40
----

.. dropdown:: Kp(CPC-s)
   :animate: fade-in-slide-down
  
   -Max  9999
   -Min  0 
   -Unit  --
   -Description  Kp in Closed-loop Position Control-stop

I 41
----

.. dropdown:: Divisor of Kp(CPC-s)
   :animate: fade-in-slide-down
  
   -Max  99
   -Min  1
   -Unit  --
   -Description  Divisor of Kp in Closed-loop Position Control-stop

I 42
----

.. dropdown:: Kd(CPC-s)
   :animate: fade-in-slide-down
  
   -Max  9999
   -Min  0
   -Unit  --
   -Description  Kd in Closed-loop Position Control-stop

I 43
----

.. dropdown:: Divisor of Kd(CPC-s)
   :animate: fade-in-slide-down
  
   -Max  99
   -Min  1
   -Unit  --
   -Description  Divisor of Kd in Closed-loop Position Control-stop

I 46
----

.. dropdown:: Max. Hold Force Current
   :animate: fade-in-slide-down
  
   -Max  40
   -Min  1
   -Unit  0.1A
   -Description  Maximum current during the motor holding

I 47
----

.. dropdown:: Field Weaken
   :animate: fade-in-slide-down
  
   -Max  1
   -Min  0
   -Unit  --
   -Description  
     | Field weaken for higher speed:
     | 0 = Off;
     | 1 = On.

I 48
----

.. dropdown:: Field Weakening Effective Speed
   :animate: fade-in-slide-down
  
   -Max  3500
   -Min  2000
   -Unit  rpm  
   -Description  Above this speed, field weakening takes effect.

I 49
----

.. dropdown:: Max. Id current
   :animate: fade-in-slide-down
  
   -Max  40
   -Min  1
   -Unit  0.1A
   -Description  Maximum Id current during field weakening.

I 50
----

.. dropdown:: Upper Output limit(CPC-h)
   :animate: fade-in-slide-down
  
   -Max  500
   -Min  0
   -Unit  --
   -Description  Upper Output limit in Closed-loop Position Control-holding

I 51
----

.. dropdown:: Lower Output limit(CPC-h)
   :animate: fade-in-slide-down
  
   -Max  100
   -Min  0
   -Unit  --
   -Description  Lower Output limit in Closed-loop Position Control-holding

I 52
----

.. dropdown:: Kp(CPC-h)
   :animate: fade-in-slide-down
  
   -Max  9999
   -Min  0
   -Unit  --
   -Description  Kp in Closed-loop Position Control-holding

I 53
----

.. dropdown:: Divisor of Kp(CPC-h)
   :animate: fade-in-slide-down
  
   -Max  99
   -Min  1
   -Unit  --
   -Description  Divisor of Kp in Closed-loop Position Control-holidng

I 54
----

.. dropdown:: Kd(CPC-h)
   :animate: fade-in-slide-down
  
   -Max  9999
   -Min  0
   -Unit  --
   -Description  Kd in Closed-loop Position Control-holding

I 55
----

.. dropdown:: Divisor of Kd(CPC-h)
   :animate: fade-in-slide-down
  
   -Max  99
   -Min  1
   -Unit  --
   -Description  Divisor of Kd in Closed-loop Position Control-holidng
