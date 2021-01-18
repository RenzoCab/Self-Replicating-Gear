# Author: Renzo Caballero,
# Association: King Abdullah University of Science and Technology (KAUST),
# email 1: Renzo.CaballeroRosas@kaust.edu.sa,
# email 2: CaballeroRenzo@hotmail.com,
# email 3: CaballeroRen@gmail.com,
# Website: https://renzocaballero.org/,
# Status: Obsolete,
# December 2020; Last revision: 08/12/2020.

import matplotlib.pyplot as plt
import numpy as np
import math
import First_library as fl

t               = np.linspace(0,1,360)
position_alpha  = fl.f_position_alpha(perfect = True, N_theet = 3, artificial_positions = 0)
theta_alpha_ini = 0
theta_alpha     = [theta_alpha_ini]

r_c    = 6.11 / 2 # mm.
a      = 6 # mm.
r_t    = a * math.sqrt(3) / 3
x      = 38.5 # mm.
belt_c = r_c * math.pi + 2 * x
y      = (14.5 + 12.75) / 2
belt_d = []
x_lim  = [-10, 40]
y_lim  = [-5, 15]

x_u = x
x_l = x
y_u = y - r_c
y_l = - r_c

for i in range(0,len(t)-1):
    
    theta_alpha.append(fl.f_theta_alpha(theta_alpha_ini,t[i]))
    points_alpha = position_alpha + theta_alpha[i+1] # they are in radians.
    print(points_alpha)
    points_LHP = 0
    points_UHP = 0
    x_set = []
    y_set = []
    x_plot = []
    y_plot = []
    
    for j in range(0,len(points_alpha)):
        [xx,yy] = fl.f_polar_to_car(r_t, points_alpha[j])
        x_set.append(xx)
        y_set.append(yy)
        if xx <= 0:
            points_LHP = points_LHP + 1
        if yy >= 0:
            points_UHP = points_UHP + 1
            
    if points_LHP == 1:
        
        if points_UHP == 2:
            
            for k in range(0,len(x_set)):
                if x_set[k] > 0 and y_set[k] > 0:
                    k1 = k
                elif x_set[k] < 0 and y_set[k] > 0:
                    k2 = k
                    
            slope_tri = fl.slope(x_set[k2],y_set[k2],x_set[k1],y_set[k1])
            slope_lin = fl.slope(x_set[k2],y_set[k2],x_u,y_u)
            
            if slope_tri > slope_lin:
                
                belt_t = 2 * a
        
                for j in range(0,len(points_alpha)):
                    if x_set[j] > 0 and y_set[j] > 0:
                        belt_t = belt_t + fl.dist_two_points(x_set[j], y_set[j], x_u, y_u)
                        x_plot.append(x_set[j])
                        y_plot.append(y_set[j])
                        
                    elif x_set[j] > 0 and y_set[j] < 0:
                        belt_t = belt_t + fl.dist_two_points(x_set[j], y_set[j], x_l, y_l)
                        x_plot.append(x_set[j])
                        y_plot.append(y_set[j])
                        
            else:
                
                belt_t = a
        
                for j in range(0,len(points_alpha)):
                    if x_set[j] < 0 and y_set[j] > 0:
                        belt_t = belt_t + fl.dist_two_points(x_set[j], y_set[j], x_u, y_u)
                        x_plot.append(x_set[j])
                        y_plot.append(y_set[j])
                        
                    elif x_set[j] > 0 and y_set[j] < 0:
                        belt_t = belt_t + fl.dist_two_points(x_set[j], y_set[j], x_l, y_l)
                        x_plot.append(x_set[j])
                        y_plot.append(y_set[j])
                        
                
        elif points_UHP == 1:
            
            belt_t = a
        
            for j in range(0,len(points_alpha)):
                if x_set[j] < 0 and y_set[j] > 0:
                    belt_t = belt_t + fl.dist_two_points(x_set[j], y_set[j], x_u, y_u)
                    x_plot.append(x_set[j])
                    y_plot.append(y_set[j])
                    
                elif x_set[j] < 0 and y_set[j] < 0:
                    belt_t = belt_t + fl.dist_two_points(x_set[j], y_set[j], x_l, y_l)
                    x_plot.append(x_set[j])
                    y_plot.append(y_set[j])
        
        
                
    if points_LHP == 2:
        belt_t = a
        
        for j in range(0,len(points_alpha)):
            if x_set[j] < 0 and y_set[j] > 0:
                belt_t = belt_t + fl.dist_two_points(x_set[j], y_set[j], x_u, y_u)
                x_plot.append(x_set[j])
                y_plot.append(y_set[j])
            elif x_set[j] < 0 and y_set[j] < 0:
                belt_t = belt_t + fl.dist_two_points(x_set[j], y_set[j], x_l, y_l)
                x_plot.append(x_set[j])
                y_plot.append(y_set[j])
        
    belt_d.append(abs(belt_t-belt_c) / belt_c)
    fl.plot_and_save_triangle_obs(x_plot, y_plot, x_u, y_u, x_l, y_l, x_lim, y_lim, str(i), x_set, y_set)
        
plt.plot(belt_d)
dir_save = ''.join(['plots/triangles/diff.jpg']) # it can also save in eps.
plt.savefig(dir_save)
