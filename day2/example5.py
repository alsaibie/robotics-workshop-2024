import numpy as np
import roboticstoolbox as rtb
import spatialmath as sm
l1, l2 = 1, 0.5
E1 = rtb.ET.Rz()
E2t = rtb.ET.tz(l1)
E2x = rtb.ET.Rx(np.pi/2)
E2y = rtb.ET.Ry(np.pi/2)
E3z = rtb.ET.Rz()
E3t = rtb.ET.tx(l2)

ets = rtb.ETS([E1
               , E2t
               , E2x
               , E2y
               , E3z
               , E3t
               ])
robot = rtb.ERobot(ets)

# TODO: Create the forward kinematics test

# TODO: Create the inverse kinematics test