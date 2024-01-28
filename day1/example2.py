import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Rectangle

def robot_fk(theta1, theta2):
    global l1, l2  # link lengths
    l1, l2 = 1, 1 
    x1 = l1 * np.cos(theta1)
    y1 = l1 * np.sin(theta1)
    x2 = x1 + l2 * np.cos(theta1 + theta2)
    y2 = y1 + l2 * np.sin(theta1 + theta2)
    return np.array([x1, y1]), np.array([x2, y2])  # P1, P2

r = 0.5
 
def circle(t):
    # The function generates the end-effector trajectory as a function of time
    global x_center, y_center, r
    T = 10
   
    x_ref = x_center + r * np.cos(2 * t * np.pi / T)
    y_ref = y_center + r * np.sin(2 * t * np.pi / T)
    return x_ref, y_ref

def robot_ik(p2_desired, theta1_measured, theta2_measured):
    # Here we get the latest values of theta1 and theta2
    global l1, l2
   
    # TODO: Implement the inverse kinematics function



# Setup Figure
fig, ax = plt.subplots()
ax.set_xlim([-3, 3])
ax.set_ylim([-2, 2])
ax.set_aspect('equal')
ax.grid()
ax.add_patch(Rectangle((-0.1, -0.1), 0.2, 0.2, fill=True, color='gray'))

# Set up the initial conditions and the plot
theta1 = 120 * np.pi / 180
theta2 = 60 * np.pi / 180
p1, p2 = robot_fk(theta1, theta2)
x_center = p2[0] + r
y_center = p2[1]

# Add robot to figure
pointP1, = ax.plot(p1[0], p1[1], 'bo')
pointP2, = ax.plot(p2[0], p2[1], 'bo')
linel1, = ax.plot([0, p1[0]], [0, p1[1]], 'r-')
linel2, = ax.plot([p1[0], p2[0]], [p1[1], p2[1]], 'g-')

# Animation function

trace_endeffector = [] 
def animate(t):
    global theta1, theta2
    global pointP1, pointP2, linel1, linel2, trace_endeffector

    x_ref, y_ref = circle(t)
    theta1, theta2 = robot_ik([x_ref, y_ref], theta1, theta2)
    
    p1, p2 = robot_fk(theta1, theta2)
    
    new_trace, = ax.plot(p2[0], p2[1], 'o', color='lightblue', alpha=1)
    trace_endeffector.append(new_trace)
    pointP1.set_data([p1[0]], [p1[1]])
    pointP2.set_data([p2[0]], [p2[1]])
    linel1.set_data([0, p1[0]], [0, p1[1]])
    linel2.set_data([p1[0], p2[0]], [p1[1], p2[1]])
    if len(trace_endeffector) > 200:
        old_trace = trace_endeffector.pop(0)
        old_trace.remove()
    for i, point in enumerate(trace_endeffector):
        alpha = (i + 1) / len(trace_endeffector) 
        point.set_alpha(alpha)
    return [pointP1, pointP2, linel1, linel2] + trace_endeffector


T_end = 10
ani = animation.FuncAnimation(fig, animate, frames=np.linspace(
    0, T_end, 300), interval=10, blit=True)

plt.show()
ani.save('robot_2link_ik_animation.mp4', writer='ffmpeg', fps=30)
