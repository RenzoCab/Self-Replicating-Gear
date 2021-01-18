# Author: Renzo Caballero,
# Association: King Abdullah University of Science and Technology (KAUST),
# email 1: Renzo.CaballeroRosas@kaust.edu.sa,
# email 2: CaballeroRenzo@hotmail.com,
# email 3: CaballeroRen@gmail.com,
# Website: https://renzocaballero.org/,
# Status: Active,
# December 2020; Last revision: 08/12/2020.

import matplotlib.pyplot as plt
import numpy as np
import math
import First_library as fl
import statistics

t               = np.linspace(0,1,360)
position_alpha  = fl.f_position_alpha(perfect = True, N_theet = 3, artificial_positions = 0)
theta_alpha_ini = 0.0001
theta_alpha     = [theta_alpha_ini]

triangle_edge = np.linspace(8,16,100)
triangle_edge = [12.686868686868687]
differences   = []

for l in range(0,len(triangle_edge)):

    r_c    = 6.11 # mm.
    a      = triangle_edge[l] # mm.
    r_t    = a * math.sqrt(3) / 3
    x      = 38.5 # mm.
    belt_c = r_c * math.pi + 2 * x
    y      = (14.5 + 12.75) / 2
    belt_d = []
    x_lim  = [-10, 40]
    y_lim  = [-10, 10]

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
        pp_p = 0; pn_p = 0; nn_p = 0; np_p = 0
        
        for j in range(0,len(points_alpha)):
            
            [xx,yy] = fl.f_polar_to_car(r_t, points_alpha[j])
            x_set.append(xx)
            y_set.append(yy)
            if xx > 0 and yy >= 0:
                pp_p = 1; pp_x = xx; pp_y = yy
            elif xx >= 0 and yy < 0:
                pn_p = 1; pn_x = xx; pn_y = yy
            elif xx < 0 and yy <= 0:
                nn_p = 1; nn_x = xx; nn_y = yy
            elif xx <= 0 and yy > 0:
                np_p = 1; np_x = xx; np_y = yy
                
        if np_p == 0:
            
            slope_tri_point_up = fl.slope(nn_x,nn_y,x_u,y_u)
            slope_tri_tri_up   = fl.slope(nn_x,nn_y,pp_x,pp_y)
            
            slope_tri_point_down = fl.slope(nn_x,nn_y,x_l,y_l)
            slope_tri_tri_down   = fl.slope(nn_x,nn_y,pn_x,pn_y)
            
            if slope_tri_tri_up > slope_tri_point_up and slope_tri_tri_down < slope_tri_point_down:
                
                belt_t = 2 * a + fl.dist_two_points(pp_x, pp_y, x_u, y_u) + fl.dist_two_points(pn_x, pn_y, x_l, y_l)
                x_plot_1 = pp_x; x_plot_2 = pp_y; y_plot_1 = pn_x; y_plot_2 = pn_y
                
            elif slope_tri_tri_up < slope_tri_point_up and slope_tri_tri_down < slope_tri_point_down:
                
                belt_t = a + fl.dist_two_points(nn_x, nn_y, x_u, y_u) + fl.dist_two_points(pn_x, pn_y, x_l, y_l)
                x_plot_1 = nn_x; nn_y = pp_y; y_plot_1 = pn_x; y_plot_2 = pn_y
                
            elif slope_tri_tri_up < slope_tri_point_up and slope_tri_tri_down > slope_tri_point_down:
                
                belt_t = fl.dist_two_points(nn_x, nn_y, x_u, y_u) + fl.dist_two_points(nn_x, nn_y, x_l, y_l)
                x_plot_1 = nn_x; nn_y = pp_y; y_plot_1 = nn_x; y_plot_2 = nn_y
                
            elif slope_tri_tri_up > slope_tri_point_up and slope_tri_tri_down > slope_tri_point_down:
                
                belt_t = a + fl.dist_two_points(pp_x, pp_y, x_u, y_u) + fl.dist_two_points(nn_x, nn_y, x_l, y_l)
                x_plot_1 = pp_x; x_plot_2 = pp_y; y_plot_1 = nn_x; y_plot_2 = nn_y
                
        if pp_p == 0:
            
            slope_tri_point_up = fl.slope(nn_x,nn_y,x_u,y_u)
            slope_tri_tri_up   = fl.slope(nn_x,nn_y,np_x,np_y)
            
            slope_tri_point_down = fl.slope(nn_x,nn_y,x_l,y_l)
            slope_tri_tri_down   = fl.slope(nn_x,nn_y,pn_x,pn_y)
            
            if slope_tri_tri_up > slope_tri_point_up and slope_tri_tri_down < slope_tri_point_down:
                
                belt_t = 2 * a + fl.dist_two_points(np_x, np_y, x_u, y_u) + fl.dist_two_points(pn_x, pn_y, x_l, y_l)
                x_plot_1 = np_x; x_plot_2 = np_y; y_plot_1 = pn_x; y_plot_2 = pn_y
                
            elif slope_tri_tri_up < slope_tri_point_up and slope_tri_tri_down < slope_tri_point_down:
                
                belt_t = a + fl.dist_two_points(nn_x, nn_y, x_u, y_u) + fl.dist_two_points(pn_x, pn_y, x_l, y_l)
                x_plot_1 = nn_x; x_plot_2 = nn_y; y_plot_1 = pn_x; y_plot_2 = pn_y
                
            elif slope_tri_tri_up < slope_tri_point_up and slope_tri_tri_down > slope_tri_point_down:
                
                belt_t = fl.dist_two_points(nn_x, nn_y, x_u, y_u) + fl.dist_two_points(nn_x, nn_y, x_l, y_l)
                x_plot_1 = nn_x; x_plot_2 = nn_y; y_plot_1 = nn_x; y_plot_2 = nn_y
                
            elif slope_tri_tri_up > slope_tri_point_up and slope_tri_tri_down > slope_tri_point_down:
                
                belt_t = a + fl.dist_two_points(np_x, np_y, x_u, y_u) + fl.dist_two_points(nn_x, nn_y, x_l, y_l)
                x_plot_1 = np_x; x_plot_2 = np_y; y_plot_1 = nn_x; y_plot_2 = nn_y
                
        if nn_p == 0:
            
            slope_tri_point_up = fl.slope(np_x,np_y,x_u,y_u)
            slope_tri_tri_up   = fl.slope(np_x,np_y,pp_x,pp_y)
            
            slope_tri_point_down = fl.slope(np_x,np_y,x_l,y_l)
            slope_tri_tri_down   = fl.slope(np_x,np_y,pn_x,pn_y)
            
            if slope_tri_tri_up > slope_tri_point_up and slope_tri_tri_down < slope_tri_point_down:
                
                belt_t = 2 * a + fl.dist_two_points(pp_x, pp_y, x_u, y_u) + fl.dist_two_points(pn_x, pn_y, x_l, y_l)
                x_plot_1 = pp_x; x_plot_2 = pp_y; y_plot_1 = pn_x; y_plot_2 = pn_y
                
            elif slope_tri_tri_up < slope_tri_point_up and slope_tri_tri_down < slope_tri_point_down:
                
                belt_t = a + fl.dist_two_points(np_x, np_y, x_u, y_u) + fl.dist_two_points(pn_x, pn_y, x_l, y_l)
                x_plot_1 = np_x; x_plot_2 = np_y; y_plot_1 = pn_x; y_plot_2 = pn_y
                
            elif slope_tri_tri_up < slope_tri_point_up and slope_tri_tri_down > slope_tri_point_down:
                
                belt_t = fl.dist_two_points(np_x, np_y, x_u, y_u) + fl.dist_two_points(np_x, np_y, x_l, y_l)
                x_plot_1 = np_x; x_plot_2 = np_y; y_plot_1 = np_x; y_plot_2 = np_y
                
            elif slope_tri_tri_up > slope_tri_point_up and slope_tri_tri_down > slope_tri_point_down:
                
                belt_t = a + fl.dist_two_points(pp_x, pp_y, x_u, y_u) + fl.dist_two_points(np_x, np_y, x_l, y_l)
                x_plot_1 = pp_x; x_plot_2 = pp_y; y_plot_1 = np_x; y_plot_2 = np_y
                
        if pn_p == 0:
            
            slope_tri_point_up = fl.slope(np_x,np_y,x_u,y_u)
            slope_tri_tri_up   = fl.slope(np_x,np_y,pp_x,pp_y)
            
            slope_tri_point_down = fl.slope(np_x,np_y,x_l,y_l)
            slope_tri_tri_down   = fl.slope(np_x,np_y,nn_x,nn_y)
            
            if slope_tri_tri_up > slope_tri_point_up and slope_tri_tri_down < slope_tri_point_down:
                
                belt_t = 2 * a + fl.dist_two_points(pp_x, pp_y, x_u, y_u) + fl.dist_two_points(np_x, np_y, x_l, y_l)
                x_plot_1 = pp_x; x_plot_2 = pp_y; y_plot_1 = np_x; y_plot_2 = np_y
                
            elif slope_tri_tri_up < slope_tri_point_up and slope_tri_tri_down < slope_tri_point_down:
                
                belt_t = a + fl.dist_two_points(np_x, np_y, x_u, y_u) + fl.dist_two_points(nn_x, nn_y, x_l, y_l)
                x_plot_1 = np_x; x_plot_2 = np_y; y_plot_1 = nn_x; y_plot_2 = nn_y
                
            elif slope_tri_tri_up < slope_tri_point_up and slope_tri_tri_down > slope_tri_point_down:
                
                belt_t = fl.dist_two_points(np_x, np_y, x_u, y_u) + fl.dist_two_points(np_x, np_y, x_l, y_l)
                x_plot_1 = np_x; x_plot_2 = np_y; y_plot_1 = np_x; y_plot_2 = np_y
                
            elif slope_tri_tri_up > slope_tri_point_up and slope_tri_tri_down > slope_tri_point_down:
                
                belt_t = a + fl.dist_two_points(pp_x, pp_y, x_u, y_u) + fl.dist_two_points(np_x, np_y, x_l, y_l)
                x_plot_1 = pp_x; x_plot_2 = pp_y; y_plot_1 = np_x; y_plot_2 = np_y
        
            
        belt_d.append(abs(belt_t-belt_c) / belt_c)
        
        if len(triangle_edge) == 1:
            fl.plot_and_save_triangle(x_plot_1, y_plot_1, x_plot_2, y_plot_2, x_u, y_u, x_l, y_l, x_lim, y_lim, str(i), x_set, y_set)
        
    differences.append(statistics.mean(belt_d))
    
if len(triangle_edge) == 1:
    plt.plot(belt_d)
    dir_save = ''.join(['plots/triangles/diff.jpg']) # it can also save in eps.
    plt.savefig(dir_save)

if len(triangle_edge) != 1:
    plt.plot(triangle_edge, differences)
    plt.plot(triangle_edge[differences.index(min(differences))],min(differences),'ro')
    print(triangle_edge[differences.index(min(differences))])
    dir_save = ''.join(['plots/triangles/diff_cir_tri.jpg']) # it can also save in eps.
    plt.savefig(dir_save)