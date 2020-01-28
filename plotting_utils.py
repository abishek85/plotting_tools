#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Plotting: Central repository for plots
1) Templates for plot types
2) Personalize style

References:
    1) https://matplotlib.org/tutorials/introductory/customizing.html
    2) https://matplotlib.org/gallery/style_sheets/style_sheets_reference.html

Created on Mon Jan 27 12:39:06 2020

@author: abishekk
"""

import matplotlib as mpl
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

class Plotting(object):
    """
    Class for personalized plotting functions. Used mainly to change default 
    values, font preferences across a project
    """
    
    def __init__(self):
        """
        Set matplotlib preferences

        Returns
        -------
        None.
        """
        
        font_size = 16
        label_size=14
        tick_size = label_size - 2
        
        plt.style.use('seaborn')
        
        mpl.rc('lines',linewidth=3.0)
        
        mpl.rc('axes',labelsize=label_size,linewidth=0.8,edgecolor='0.25')
        # if box is not needed
        #mpl.rc('axes.spines',top=False,right=False)
        
        mpl.rc('xtick',labelsize=tick_size)
        mpl.rc('ytick',labelsize=tick_size)
        mpl.rc('xtick.major',size=3.0)
        mpl.rc('ytick.major',size=3.0)
        
        # Font: Latex styling for all text, change mathtext to cm
        font_style = {'family' : 'sans-serif',
                'sans-serif' : ['Computer Modern Sans serif'],
                'size': font_size}
        mpl.rc('font',**font_style)
        
        # Install latex packages: type1cm, dvipng
        mpl.rc('text',usetex=True)
        
        mpl.rc('mathtext', fontset='cm')
        
    
    def plot_colored_sinusoidal_lines(self):
        """
        Plot sinusoidal lines with colors following the style color cycle.
        """
    
        # crearte sine curves
        L = 2 * np.pi
        x = np.linspace(0, L)
        nb_colors = len(plt.rcParams['axes.prop_cycle'])
        shift = np.linspace(0, L, nb_colors, endpoint=False)
          
        for s in shift:
            plt.plot(x, np.sin(x + s), '-')
        
        plt.xlim([x[0], x[-1]])
        plt.xlabel('$x$')
        plt.ylabel('$\sin(x)$')
        
        plt.show()
