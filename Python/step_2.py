# Author: Renzo Caballero,
# Association: King Abdullah University of Science and Technology (KAUST),
# email 1: Renzo.CaballeroRosas@kaust.edu.sa,
# email 2: CaballeroRenzo@hotmail.com,
# email 3: CaballeroRen@gmail.com,
# Website: https://renzocaballero.org/,
# November 2020; Last revision: 24/11/2020.

import matplotlib.pyplot as plt
import numpy as np
import math
import First_library as fl

def rightRotate(lists, num): 
    output_list = [] 
      
    # Will add values from n to the new list 
    for item in range(len(lists) - num, len(lists)): 
        output_list.append(lists[item]) 
      
    # Will add the values before 
    # n to the end of new list     
    for item in range(0, len(lists) - num):  
        output_list.append(lists[item]) 
          
    return output_list 

# inputs function (1/2):
N_time               = 200 # num. disc. in time.
N_theta              = 360 * 5 # num. disc. 360.
N_theet              = 16
gear_ratio           = 10
save_plots           = False
perfect              = False
artificial_positions = np.linspace(0,2*math.pi*((N_theet-1)/N_theet),N_theet)
artificial_positions_backup = artificial_positions

desviation = 2 * math.pi * 0.01 * 0
artificial_positions[8] = artificial_positions[8] + desviation

all_art_positions = [artificial_positions]
all_beta_position = []
all_beta_dots     = []
total_beta_path   = []
total_alpha_path  = []
t_loop            = 15
r_alpha_1         = 5
iterations        = 24
initial_beta_fix  = 2 * math.pi / (160*2)
transitions       = []
n                 = True

for j in range(0,iterations):
    
    theta_beta_aux      = []
    ran = 1 / 360
    if np.random.normal() < 0:
        ran = ran * (-1)
        
    # inputs function (1/2):
    t_frac          = 5/8 + ran * 0 # 1 is a complete rotation (2.pi).
    theta_alpha_ini = 0 # initial rotation for alpha.
    theta_beta_ini  = initial_beta_fix # initial rotation for beta.
    
    artificial_positions_aux = [theta_beta_ini - initial_beta_fix] # this is 0.
    
    for i in range(0,t_loop):
        
        [theta_alpha,theta_beta] = fl.position_beta(N_time,N_theta,N_theet,gear_ratio,t_frac,theta_alpha_ini,theta_beta_ini,save_plots,
                                                    perfect, artificial_positions)
        
        total_alpha_path = total_alpha_path + theta_alpha
        total_beta_path  = total_beta_path + theta_beta
        
        theta_alpha_ini = total_alpha_path[-1]
        theta_beta_ini  = total_beta_path[-1]
        
        all_beta_position = all_beta_position + theta_beta
        
        artificial_positions_aux.append(theta_beta[-1] - initial_beta_fix)
        
        all_beta_dots.append([len(all_beta_position) - N_time, artificial_positions_aux[i] + initial_beta_fix])
    
    artificial_positions = artificial_positions_aux
    all_art_positions.append(artificial_positions)
    #plt.plot(np.linspace(0,t_frac,N_time * t_loop),total_beta_path)
    for i in range(0,len(artificial_positions)):
        plt.polar(artificial_positions[i],r_alpha_1,'ro')
    dir_save = ''.join(['plots/iterations/',str(j),'.jpg']) # it can also save in eps.
    plt.savefig(dir_save)
    plt.clf()
    #plt.show()

if False:
    plt.plot(all_beta_position)
    for j in range(0,len(all_beta_dots)):
        plt.plot(all_beta_dots[j][0],all_beta_dots[j][1],'ro')
    plt.show()
    
if True:
    
    colors = ['b','g','r','c','m','y','k']
    
    for i in range(0,len(all_art_positions)-1):
        
        transitions_aux       = []
        
        for j in range(0,16):
        
            if artificial_positions_backup[j] != 0:
                transitions_aux.append((all_art_positions[i+1][j] - artificial_positions_backup[j])/artificial_positions_backup[j])
            else:
                transitions_aux.append(0)
    
        transitions.append(transitions_aux)

        colors = rightRotate(colors,1)

        col = "".join([colors[0],'o'])        
        plt.plot(np.linspace(0,15,16),transitions[i],col)
            
        dir_save = ''.join(['plots/errors/',str(i),'.jpg']) # it can also save in eps.
        plt.savefig(dir_save)
        #plt.clf()
                
exit()