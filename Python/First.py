# Author: Renzo Caballero,
# Association: King Abdullah University of Science and Technology (KAUST),
# email 1: Renzo.CaballeroRosas@kaust.edu.sa,
# email 2: CaballeroRenzo@hotmail.com,
# email 3: CaballeroRen@gmail.com,
# Website: https://renzocaballero.org/,
# November 2020; Last revision: 20/11/2020.

import numpy as np
import matplotlib.pyplot as plt
import math

def f_theta_alpha(theta_alpha_ini,t): # positioning of alpha over time.
    return 2 * math.pi * t + theta_alpha_ini

def f_theta_beta(theta_beta_ini,t): # we do not use this since alpha pushes beta.
    return 2 * math.pi * t + theta_beta_ini

def f_polar_to_car(r,theta):
    return [r * math.cos(theta), r * math.sin(theta)]

def f_polar_to_car_x(r,theta):
    return r * math.cos(theta)

def f_polar_to_car_y(r,theta):
    return r * math.sin(theta)

def f_position_alpha(perfect,N_theet):
    if perfect == True:
        return np.linspace(0, 2*math.pi*((N_theet-1)/N_theet), N_theet)
    elif perfect == False:
        # read from a file or something else.
        return 1

def f_position_beta(N_theet,gear_ratio):
    N_theet = N_theet * gear_ratio
    return np.linspace(0, 2*math.pi*((N_theet-1)/N_theet), N_theet)

def f_point_1(r_1,theta_point,theta_1,action):
    [x,y] = f_polar_to_car(r_1,theta_point+theta_1) # it is okay if the angles pass 2.pi since we use sin() and cos().
    if action == 'xy':
        return [x,y]
    elif action == 'x':
        return x
    elif action == 'y':
        return y       
    
def f_point_2(r_1,r_2,theta_point,theta_2,action):
    [x,y] = f_polar_to_car(r_1+r_2,theta_point+theta_2) # it is okay if the angles pass 2.pi since we use sin() and cos().
    if action == 'xy':
        return [x,y]
    elif action == 'x':
        return x
    elif action == 'y':
        return y   
    
def f_point_3(r_1,r_2,theta_point,theta_2,action):
    [x,y] = f_polar_to_car(r_1+r_2,theta_point-theta_2) # it is okay if the angles pass 2.pi since we use sin() and cos().
    if action == 'xy':
        return [x,y]
    elif action == 'x':
        return x
    elif action == 'y':
        return y  
    
def f_point_4(r_1,theta_point,theta_1,action):
    [x,y] = f_polar_to_car(r_1,theta_point-theta_1) # it is okay if the angles pass 2.pi since we use sin() and cos().
    if action == 'xy':
        return [x,y]
    elif action == 'x':
        return x
    elif action == 'y':
        return y  
    
def j_points(j):
    return [4*j, 4*j + 1, 4*j + 2, 4*j + 3]

def point_in_line(p_1,p_2,t):
    return p_1 + (p_2-p_1) * t

def f_t_hat(p_beta_3,p_alpha_1,p_alpha_2):
    return (p_beta_3 - p_alpha_1) / (p_alpha_2 - p_alpha_1)

def f_t_star(p_alpha_2,p_beta_3,p_beta_4):
    return (p_alpha_2 - p_beta_4) / (p_beta_3 - p_beta_4)

def plot_and_save_gears(alpha,beta,alpha_xy,beta_xy,name,xx,yy,cp):
    
    for i in range(0,len(alpha)):
        [x,y] = [alpha[i][0],alpha[i][1]]
        plt.plot(x,y,'go')
        
    for i in range(0,len(beta)):
        [x,y] = [beta[i][0],beta[i][1]]
        plt.plot(x,y,'mo')
    
    for i in range(0,len(alpha_xy)-1):
        [x1,x2] = [alpha_xy[i][0],alpha_xy[i+1][0]]
        [y1,y2] = [alpha_xy[i][1],alpha_xy[i+1][1]]
        plt.plot([x1,x2],[y1,y2],'k')
  
    for i in range(0,len(beta_xy)-1):
        [x1,x2] = [beta_xy[i][0],beta_xy[i+1][0]]
        [y1,y2] = [beta_xy[i][1],beta_xy[i+1][1]]
        plt.plot([x1,x2],[y1,y2],'b')
        
    if cp != []:
        plt.plot(cp[0],cp[1],'ro')
        
    dir_save = ''.join(['plots/fps/',name,'.jpg']) # it can also save in eps.
    plt.axis('scaled')
    axes = plt.gca()
    axes.set_xlim(xx)
    axes.set_ylim(yy)
    plt.savefig(dir_save)
    plt.clf()
    
def order_circle_points(points):
    ordered_points      = []
    ordered_points_aux1 = []
    ordered_points_aux2 = []
    for j in points:
        if j >= 0 and j <= math.pi:
            ordered_points_aux1.append(j)
    for j in points:
        if j > math.pi:
            ordered_points_aux2.append(j)
    ordered_points_aux1.sort()
    ordered_points_aux2.sort()
    ordered_points = np.concatenate((ordered_points_aux2, ordered_points_aux1))
    return ordered_points[::-1] # [::-1] reverses the array.
    
# simulation and design:
N_time     = 2500 # num. disc. in time.
N_theta    = 10000 # num. disc. 360.
N_theet    = 16
gear_ratio = 10
dt         = 1/N_time
d_theta    = 2 * math.pi / N_theta # minimum discrete artificial displacement.
t          = np.linspace(0,1,N_time)
perfect    = True
xx         = [3.5, 6]
yy         = [-4, 4]
save_plots = False

# constants:
theta_alpha_ini = 0 # initial rotation for alpha.
theta_beta_ini  = 2 * math.pi / (160*2) # initial rotation for beta.
r_alpha_1       = 5
r_alpha_2       = 0.5
r_beta_1        = r_alpha_1 * gear_ratio
r_beta_2        = 0.5
eps             = 0.6
L               = r_alpha_1 + r_beta_1 + eps
position_alpha  = f_position_alpha(perfect,N_theet) # initial angles for the theet.
position_beta   = f_position_beta(N_theet,gear_ratio) # initial angles for the theet.
windows_alpha   = 0.24 * math.pi
windows_beta    = 0.022 * math.pi
theta_alpha_1   = 0.0323 * math.pi
theta_alpha_2   = 0.0106 * math.pi
theta_beta_1    = 0.00322 * math.pi
theta_beta_2    = 0.00117 * math.pi

# variables:
theta_alpha  = [theta_alpha_ini]
theta_beta   = [theta_beta_ini]
omega_alpha  = [0]
omega_beta   = [0]
keep_in_loop = True
points_alpha = []
points_beta  = []

for i in range(0,len(t)-1):
    
    print(i/len(t))
    
    theta_alpha.append(f_theta_alpha(theta_alpha_ini,t[i])) # we add the i+1.
    theta_beta.append(theta_beta[i] + omega_beta[i] * dt)   # we add the i+1.
    
    intercept      = False
    keep_in_loop   = True
    times_inter    = 0
    contact_point  = []
    
    while keep_in_loop == True:
                
        # empty arrays to collect points in windows:
        points_windows_alpha      = []
        points_windows_beta       = []
        points_windows_alpha_plot = []
        points_windows_beta_plot  = []
        points_windows_alpha_xy   = []
        points_windows_beta_xy    = []
        
        # if they intercept, we move slightly beta:
        if intercept == True:
            theta_beta[i+1] = theta_beta[i+1] + d_theta
            intercept = False
        
        # we find the positions of points over circles:
        points_alpha = position_alpha + theta_alpha[i+1]
        points_beta  = position_beta + theta_beta[i+1]

        # we find the points in windows:
        for j in points_alpha:
            aux = j
            if aux > 2 * math.pi:
                aux = aux - 2 * math.pi
            if aux < windows_alpha or aux > 2 * math.pi - windows_alpha:
                points_windows_alpha.append(aux)
                points_windows_alpha_plot.append(f_polar_to_car(r_alpha_1,aux))
                 
        for j in points_beta:
            aux = j
            if aux > 2 * math.pi:
                aux = aux - 2 * math.pi
            if aux < windows_beta or aux > 2 * math.pi - windows_beta:
                points_windows_beta.append(aux)
                points_windows_beta_plot.append(f_polar_to_car(r_beta_1,aux))
                points_windows_beta_plot[-1][0] = -1 * points_windows_beta_plot[-1][0] + L
                
        points_windows_alpha = order_circle_points(points_windows_alpha)
        points_windows_beta  = order_circle_points(points_windows_beta)
                
        # we find the (x,y) coordinates for the windows' points in alpha:
        for theta_point in points_windows_alpha:
            # f_point_1(r_1,theta_point,theta_1,action)
            # f_point_2(r_1,r_2,theta_point,theta_2,action)
            # f_point_3(r_1,r_2,theta_point,theta_2,action)
            # f_point_4(r_1,theta_point,theta_1,action)
            points_windows_alpha_xy.append(f_point_1(r_alpha_1,theta_point,theta_alpha_1,'xy'))
            points_windows_alpha_xy.append(f_point_2(r_alpha_1,r_alpha_2,theta_point,theta_alpha_2,'xy'))
            points_windows_alpha_xy.append(f_point_3(r_alpha_1,r_alpha_2,theta_point,theta_alpha_2,'xy'))
            points_windows_alpha_xy.append(f_point_4(r_alpha_1,theta_point,theta_alpha_1,'xy'))
            
        # we find the (x,y) coordinates for the windows' points in beta:
        for theta_point in points_windows_beta:
            x = -1 * f_point_1(r_beta_1,theta_point,theta_beta_1,'x') + L
            y = f_point_1(r_beta_1,theta_point,theta_beta_1,'y')
            points_windows_beta_xy.append([x,y])
            
            x = -1 * f_point_2(r_beta_1,r_beta_2,theta_point,theta_beta_2,'x') + L
            y = f_point_2(r_beta_1,r_beta_2,theta_point,theta_beta_2,'y')
            points_windows_beta_xy.append([x,y])
            
            x = -1 * f_point_3(r_beta_1,r_beta_2,theta_point,theta_beta_2,'x') + L
            y = f_point_3(r_beta_1,r_beta_2,theta_point,theta_beta_2,'y')
            points_windows_beta_xy.append([x,y])
            
            x = -1 * f_point_4(r_beta_1,theta_point,theta_beta_1,'x') + L
            y = f_point_4(r_beta_1,theta_point,theta_beta_1,'y')
            points_windows_beta_xy.append([x,y])
            
        # we check if there is interception:
        for j in range(0,int(len(points_windows_alpha_xy)/4)):
                 
            [j_1,j_2,j_3,j_4] = j_points(j)
            x_alpha_2 = points_windows_alpha_xy[j_2][0] # ...[j_2][0 or 1] is x or y.
            y_alpha_2 = points_windows_alpha_xy[j_2][1] # ...[j_2][0 or 1] is x or y.
            
            for k in range(0,int(len(points_windows_beta_xy)/4)):
                
                [k_1,k_2,k_3,k_4] = j_points(k)
                x_beta_3 = points_windows_beta_xy[k_3][0]
                y_beta_3 = points_windows_beta_xy[k_3][1]
                x_beta_4 = points_windows_beta_xy[k_4][0]
                y_beta_4 = points_windows_beta_xy[k_4][1]
                
                if y_alpha_2 < y_beta_3 and y_alpha_2 > y_beta_4:
                    
                    t_star = f_t_star(x_alpha_2,x_beta_3,x_beta_4)
                    y_beta_3_4 = point_in_line(y_beta_4,y_beta_3,t_star)
                    
                    if y_alpha_2 > y_beta_3_4 and x_alpha_2 > x_beta_3 and x_alpha_2 < x_beta_4:
                        
                        intercept     = True
                        contact_point = [points_windows_alpha_xy[j_2][0],y_alpha_2]
                    
        for j in range(0,int(len(points_windows_beta_xy)/4)):
                 
            [j_1,j_2,j_3,j_4] = j_points(j)
            x_beta_3 = points_windows_beta_xy[j_3][0] # ...[j_2][0 or 1] is x or y.
            y_beta_3 = points_windows_beta_xy[j_3][1] # ...[j_2][0 or 1] is x or y.
            
            for k in range(0,int(len(points_windows_alpha_xy)/4)):
                
                [k_1,k_2,k_3,k_4] = j_points(k)
                x_alpha_1 = points_windows_alpha_xy[k_1][0]
                y_alpha_1 = points_windows_alpha_xy[k_1][1]
                x_alpha_2 = points_windows_alpha_xy[k_2][0]
                y_alpha_2 = points_windows_alpha_xy[k_2][1]
                
                if y_beta_3 < y_alpha_1 and y_beta_3 > y_alpha_2:
                    
                    t_hat = f_t_hat(x_beta_3,x_alpha_1,x_alpha_2)
                    y_alpha_1_2 = point_in_line(y_alpha_1,y_alpha_2,t_hat)
                    
                    if y_alpha_1_2 > y_beta_3 and x_beta_3 > y_alpha_1 and x_beta_3 < x_alpha_2:
                        
                        intercept = True
                        contact_point = [points_windows_beta_xy[j_3][0],y_beta_3]
            
        # events when intercepting or not:
        if intercept == False:
            keep_in_loop = False
            omega_beta.append(times_inter * d_theta / dt)
            omega_beta[-1] = 0 # for now, we are setting this speed to 0.
            if save_plots == True:
                plot_and_save_gears(points_windows_alpha_plot,points_windows_beta_plot,
                                    points_windows_alpha_xy,points_windows_beta_xy,str(i),
                                    xx,yy,contact_point)

        elif intercept == True:
            times_inter = times_inter + 1
        
exit()