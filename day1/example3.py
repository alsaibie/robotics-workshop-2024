import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Rectangle


def robot_fk(theta1_, theta2_):
    
    
    # TODO: Implement the forward kinematics function


# Setup Figure
fig, ax = plt.subplots()
ax.set_xlim([-1.5, 1.5])
ax.set_ylim([-.5, 2.5])
ax.set_aspect('equal')
ax.grid()
ax.add_patch(Rectangle((-0.1, -0.1), 0.2, 0.2, fill=True, color='gray'))

# Set up the initial conditions and the plot
theta1 = 85 * np.pi / 180
theta2 = 60 * np.pi / 180
p30, p3 = robot_fk(theta1, theta2)

# Add robot to figure
p31 = np.array([l31*np.sin(theta2), l31*np.cos(theta2)])
dgg = theta30 - np.pi + theta1 
p2 = np.array([p30[0] + l30*np.cos(dgg), p30[1] + l30*np.sin(dgg)])
pointP31, = ax.plot(p31[0], p31[1], 'bo')
pointP30, = ax.plot(p30[0], p30[1], 'bo')
pointP2, = ax.plot(p2[0], p2[1], 'bo')
pointP3, = ax.plot(p3[0], p3[1], 'bo')
linel1, = ax.plot([0, p30[0]], [0, p30[1]], 'r-')
linel2, = ax.plot([p31[0], p2[0]], [p31[1], p2[1]], 'y-')
linel3, = ax.plot([p30[0], p3[0]], [p30[1], p3[1]], 'g-')
linel30, = ax.plot([p30[0], p2[0]], [p30[1], p2[1]], 'k-')
linel31, = ax.plot([0, p31[0]], [0, p31[1]], 'b-')

# Animation function

trace_endeffector = []
def animate(t):
    global theta1, theta2
    global trace_endeffector
    theta1 += 0.001
    theta2 += 0.001
    p30, p3 = robot_fk(theta1, theta2)
    
    p31 = np.array([l31*np.sin(theta2), l31*np.cos(theta2)])
    dgg = theta30 - np.pi + theta1 
    p2 = np.array([p30[0] + l30*np.cos(dgg), p30[1] + l30*np.sin(dgg)])
    new_trace, = ax.plot(p3[0], p3[1], 'o', color='lightblue', alpha=1)
    trace_endeffector.append(new_trace)
    pointP2.set_data([p2[0]], [p2[1]])
    pointP3.set_data([p3[0]], [p3[1]])
    pointP30.set_data([p30[0]], [p30[1]])
    pointP31.set_data([p31[0]], [p31[1]])
    linel1.set_data([0, p30[0]], [0, p30[1]])
    linel2.set_data([p31[0], p2[0]], [p31[1], p2[1]])
    linel3.set_data([p30[0], p3[0]], [p30[1], p3[1]])
    linel30.set_data([p30[0], p2[0]], [p30[1], p2[1]])
    linel31.set_data([0, p31[0]], [0, p31[1]])
    if len(trace_endeffector) > 200:
        old_trace = trace_endeffector.pop(0)
        old_trace.remove()
    for i, point in enumerate(trace_endeffector):
        alpha = (i + 1) / len(trace_endeffector) 
        point.set_alpha(alpha)
    return [pointP2, pointP3, pointP30, pointP31, linel1, linel2, linel30, linel31, linel3] + trace_endeffector


T_end = 10
ani = animation.FuncAnimation(fig, animate, frames=np.linspace(
    0, T_end, 300), interval=10, blit=True)

plt.show()
# ani.save('robot_parallel_fk_animation.mp4', writer='ffmpeg', fps=30)
