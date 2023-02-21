from math import sin, cos, pi, sqrt
import numpy as np

def omnidirectional_robot_model(vx, vy, omega,d):

    # Inverse Kinematics
    Ug = np.matrix([[vx],[vy],[omega]]) 

    Sg = np.matrix([[-sin(pi/3), cos(pi/3),d],
                    [0,-1,d],
                    [-sin(pi/3),cos(pi/3),d]])
    
    Vtot = Sg.dot(Ug)
    return Vtot[0,0],Vtot[1,0],Vtot[2,0]
    

Vx, Vy, Theta = omnidirectional_robot_model(1, 1, pi/2,0.5)
print("x: ", Vx, "y: ", Vy, "theta: ", Theta)