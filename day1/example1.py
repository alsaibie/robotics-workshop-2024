import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Rectangle


def robot_fk(theta1, theta2):
    global l1, l2  # link lengths
    l1, l2 = 1, 1  # link lengths
    
    # TODO: Implement the forward kinematics function
    

# Setup Figure
fig, ax = plt.subplots()
ax.set_xlim([-3, 3])
ax.set_ylim([-2, 2])
ax.set_aspect('equal')
ax.grid()
ax.add_patch(Rectangle((-0.1, -0.1), 0.2, 0.2, fill=True, color='gray'))

# Set up the initial conditions and the plot
theta1 = 120 * np.pi / 180
theta2 = -60 * np.pi / 180
p1, p2 = robot_fk(theta1, theta2)

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
    theta1 += 0.025
    theta2 += 0.025
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
ani.save('robot_2link_fk_animation.mp4', writer='ffmpeg', fps=30)
