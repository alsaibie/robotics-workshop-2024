import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Rectangle

def robot_fk(theta1_, theta2_):
    global l1, l2, theta1, theta2
    l1, l2 = 1, .5
    theta1 , theta2 = theta1_, theta2
    p = np.array([0, 0, 0, 1])
    T1 = np.array([[np.cos(theta1), -np.sin(theta1), 0, 0],
                   [np.sin(theta1), np.cos(theta1), 0, 0],
                   [0, 0, 1, 0],
                   [0, 0, 0, 1]])
    T2 = np.array([[0, 1, 0, 0], [0, 0, 1, 0], [1, 0, 0, l1], [0, 0, 0, 1]])
    T3 = np.array([[np.cos(theta2), -np.sin(theta2), 0, np.sin(theta2)*l2], 
                   [np.sin(theta2), np.cos(theta2), 0, np.cos(theta2)*l2], 
                   [0, 0, 1, 0],
                   [0, 0, 0, 1]])
                    
    # TODO return the point positions

# Setup Figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

elevation = 30
azimuth = 0
ax.view_init(elev=elevation,azim=azimuth,)
ax.dist = 7

ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])
ax.set_zlim([0, 1.6])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_aspect('equal')
ax.grid()

def draw_base():
    from mpl_toolkits.mplot3d.art3d import Poly3DCollection
    vertices = np.array([[-1, -1, -0.1],
                        [1, -1, -0.1],
                        [1, 1, -0.1],
                        [-1, 1, -0.1],
                        [-1, -1, 0],
                        [1, -1, 0],
                        [1, 1, 0],
                        [-1, 1, 0]])
    faces = [[vertices[j] for j in face] for face in [[0,1,5,4], [7,6,2,3], [0,1,2,3], [7,6,5,4], [0,3,7,4], [1,2,6,5]]]
    return Poly3DCollection(faces, linewidths=1, edgecolors='k', alpha=0.2)

ax.add_collection3d(draw_base())

# Set up the initial conditions and the plot
theta1 = 90 * np.pi / 180
theta2 = 0 * np.pi / 180
p0, p1, p2, p3 = robot_fk(theta1, theta2)

# Add robot to figure
pointP2, = ax.plot([p2[0]], [p2[1]], [p2[2]], 'bo')
pointP3, = ax.plot([p3[0]], [p3[1]], [p3[2]], 'ro')
line1, = ax.plot([0, p2[0]], [0, p2[1]], [0, p2[2]], 'r-', linewidth=3)
line2, = ax.plot([p2[0], p3[0]], [p2[1], p3[1]], [p2[2], p3[2]], 'y-', linewidth=3)

# Animation function
trace_endeffector = []
def animate(t):
    global theta1, theta2
    global trace_endeffector
    
    theta1 = np.sin(t)
    theta2 += .2
    p0, p1, p2, p3 = robot_fk(theta1, theta2)
    pointP2.set_data([p2[0]], [p2[1]])
    pointP2.set_3d_properties([p2[2]])
    pointP3.set_data([p3[0]], [p3[1]])
    pointP3.set_3d_properties([p3[2]])
    new_trace, = ax.plot(p3[0], p3[1], p3[2], 'o', color='lightblue', alpha=1)
    trace_endeffector.append(new_trace)
    
    # Update lines
    line1.set_data([0, p2[0]], [0, p2[1]])
    line1.set_3d_properties([0, p2[2]])
    line2.set_data([p2[0], p3[0]], [p2[1], p3[1]])
    line2.set_3d_properties([p2[2], p3[2]])
    
    for i, point in enumerate(trace_endeffector):

        point.set_alpha(.2)
    return [pointP2, pointP3, line1, line2] + trace_endeffector


T_end = 10
ani = animation.FuncAnimation(fig, animate, frames=np.linspace(
    0, T_end, 300), interval=10, blit=True)

plt.show()
# ani.save('robot_2R_fk_animation.mp4', writer='ffmpeg', fps=30)
