import numpy as np
import roboticstoolbox as rtb
l1, l2 = 1, 0.5
E1 = rtb.ET.Rz()
E2t = rtb.ET.tz(l1)
E2x = rtb.ET.Rx(np.pi/2)
E2y = rtb.ET.Ry(np.pi/2)
E3z = rtb.ET.Rz()
E3t = rtb.ET.tx(l2)

# TODO: Create an ETS object with the above elements

print(ets)
robot = rtb.ERobot(ets)
print(robot)
q = [0, 0]
robot.plot(q, block=True)

