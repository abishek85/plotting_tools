#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Plotting: Central repository for plots
1) Templates for plot types
2) Personalize style

References:
1) Matplotlib
    a) https://matplotlib.org/tutorials/introductory/customizing.html
    b) https://matplotlib.org/gallery/style_sheets/style_sheets_reference.html
2) Pandas
    a)https://pandas.pydata.org/pandas-docs/version/0.23.4/visualization.html
3) Seaborn
    a) https://seaborn.pydata.org/tutorial.html
    b) https://seaborn.pydata.org/examples/index.html
4) Colormaps:
    a) https://matplotlib.org/3.1.0/tutorials/colors/colormaps.html
    b) https://seaborn.pydata.org/tutorial/color_palettes.html

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
    Class for personalized plotting functions. Use as a template to change  
    default values, font and color palette preferences across a project
    """
    ##########################################################################
    def __init__(self):
        """
        Set matplotlib style preferences

        Returns
        -------
        None.
        """
        
        font_size = 16
        label_size = 14
        tick_size = label_size - 2
        
        plt.style.use('seaborn')
        
        mpl.rc('lines',linewidth=3.0)
        
        mpl.rc('axes',labelsize=label_size,linewidth=0.8,edgecolor='0.25')
        # remove box
        #mpl.rc('axes.spines',top=False,right=False)
        
        mpl.rc('xtick',labelsize=tick_size)
        mpl.rc('ytick',labelsize=tick_size)
        mpl.rc('xtick.major',size=3.0)
        mpl.rc('ytick.major',size=3.0)
        
        # Font: cm font for all text, change mathtext to cm
        # Note: 
        # Use mpl.font_manager.findSystemFonts(fontpaths=None, fontext='ttf')
        # to find fonts on the system
        # If CMU fonts are missing:
        # $brew tap homebrew/cask-fonts
        # $brew cask install font-computer-modern
        font_style = {'family' : 'sans-serif',
                'sans-serif' : ['CMU Sans Serif'],
                'size': font_size}
        mpl.rc('font',**font_style)
        
        # Install latex packages: type1cm, dvipng
        # Issues: special char such as _ are not read correctly until '\' is
        # provided. 
        #mpl.rc('text',usetex=True)
        
        mpl.rc('mathtext', fontset='cm')
        
    ##########################################################################
    def plot_colored_sinusoidal_lines(self):
        """
        Plot sinusoidal lines with colors following the style color cycle.
        Use: visualize formatting
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
        plt.title('Shifted sine plots')
        
        plt.show()
    ##########################################################################
        
    ##########################################################################
    ###                     I - DATA EXPLORATION                           ###
    ##########################################################################
        
    ##########################################################################
    def plot_pandas_histogram(self, dataframe, fig_size=(20,20)):
        """
        histogram from pandas dataframe or series

        Parameters
        ----------
        dataframe : Pandas dataframe
        fig_size: tuple, width x height

        Returns
        -------
        None.

        """
        dataframe.hist(bins=50,figsize=fig_size)
        plt.show()
        
    ##########################################################################
    def plot_pandas_scatter_plot(self,dataframe,x_series,y_series,
                                 size, size_label,color):
        """
        

        Parameters
        ----------
        dataframe : pandas dataframe
        x_series : str, series for x
        y_series : str, series for y
        size : series, determines size of scatter dot
        size_label: str, defines legend string
        color : str, determines color of scatter dot from series
                
        Returns
        -------
        None.

        eg.
        myplot.plot_pandas_scatter_plot(housing_data,'latitude','longitude',
        housing_data['population']/100., 'population', 'median_house_value')

        """
        # Jet is not a great colormap
        # Try viridis, inferno, magma, tab20c
        
        dataframe.plot(kind="scatter", x=x_series, y=y_series, alpha=0.4, 
                       s=size, label=size_label,
                       c=color, cmap=plt.get_cmap("viridis"), colorbar=True)
        plt.show()
    
    ##########################################################################
    def plot_pandas_scatter_matrix(self, dataframe, fig_size=(12,12)):
        """
        Tool for data exploration, observing correlations

        Parameters
        ----------
        dataframe : pandas dataframe
        fig_size: tuple, width x height
        
        Returns
        -------
        None.

        eg.
        attributes = ["median_house_value","median_income","total_rooms"]
        myplot.plot_pandas_scatter_matrix(housing_data[attributes])
        """
        pd.plotting.scatter_matrix(dataframe,figsize=fig_size,diagonal='kde')
        plt.show()
    
    ##########################################################################
    def plot_sns_scatter_matrix(self,dataframe,hue_str=None,diag_plt='kde'):
        """
        Pair-wise scatter plot between variables in data. Plots on diagonal
        can be histogram or kde.

        Parameters
        ----------
        dataframe : pandas dataframe
        hue_str : str, optional
             Column name in dataframe to use for color. Default is None
        diag_plt : str, optional
            Type of plot on diagonal('hist','kde'). The default is 'kde'.

        Returns
        -------
        None.
        
        
        eg.
        iris = sns.load_dataset('iris')
        myplot.plot_sns_scatter_matrix(iris,'species')
        """
        # Using pairplot
        # Note: PairGrid is much more flexible than pairplot but also 
        # considerably slower
        sns.pairplot(dataframe, hue=hue_str, palette='viridis', 
                     kind='scatter', diag_kind=diag_plt, height=2.5)
        
        plt.show()
        
    ##########################################################################
    ###                    II - MODEL VISUALIZATION                        ###
    ##########################################################################