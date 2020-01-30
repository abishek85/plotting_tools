#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Plotting: Central repository for plots
Uses:
1) Templates for plot types
2) Personalized style

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
        
        font_size = 14
        label_size = 18
        tick_size = 12
        
        plt.style.use('seaborn')
        
        mpl.rc('lines',linewidth=3.0)
        
        mpl.rc('axes', titlesize=label_size, labelsize=label_size,
               linewidth=0.8,edgecolor='0.25')
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
        mpl.rc('font', **font_style)
        
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
    def pandas_histogram(self, dataframe, fig_size=(20,20)):
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
    def pandas_scatter_plot(self,dataframe,x_series,y_series, size, 
                            size_label,color):
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
        myplot.pandas_scatter_plot(housing_data,'latitude','longitude',
        housing_data['population']/100., 'population', 'median_house_value')

        """
        # Jet is not a great colormap
        # Try viridis, inferno, magma, tab20c
        
        dataframe.plot(kind="scatter", x=x_series, y=y_series, alpha=0.4, 
                       s=size, label=size_label,
                       c=color, cmap=plt.get_cmap("viridis"), colorbar=True)
        plt.show()
    
    ##########################################################################
    def pandas_scatter_matrix(self, dataframe, fig_size=(12,12)):
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
        myplot.pandas_scatter_matrix(housing_data[attributes])
        """
        pd.plotting.scatter_matrix(dataframe,figsize=fig_size,diagonal='kde')
        plt.show()
    
    ##########################################################################
    def sns_scatter_matrix(self,dataframe,hue_str=None,diag_plt='kde'):
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
        myplot.sns_scatter_matrix(iris,'species')
        """
        # Using pairplot
        # Note: PairGrid is much more flexible than pairplot but also 
        # considerably slower
        sns.pairplot(dataframe, hue=hue_str, palette='viridis', 
                     kind='scatter', diag_kind=diag_plt, height=2.5)
        
        plt.show()
    
    ##########################################################################
    def sns_lineplot(self,dataframe, x_name=None, y_name=None, hue_str=None):
        """
        Line plot

        Parameters
        ----------
        dataframe : dataframe
            data container
        x_name : str, optional
            column name for the x-axis. The default is None.
        y_name : str, optional
            column name for the y-axis. The default is None.
        hue_str : str, optional
            name of categorical data to color by. The default is None.

        Returns
        -------
        None.
        
        eg. 
        df = pd.DataFrame(dict(time=np.arange(500),
                          value=np.random.randn(500).cumsum()))
        myplot.sns_lineplot(df,'time','value')
        """
        
        sns.lineplot(data=dataframe, x=x_name, y=y_name, hue=hue_str)
        plt.show()
    
    ##########################################################################
    def sns_boxenplot(self, dataframe, x_name=None, y_name=None, hue_str=None):
        """
        Boxenplot - similar to box plots but provides more information about
        the distribution as it plots more quantiles. Useful for large datasets

        Parameters
        ----------
        dataframe : dataframe
            data container
        x_name : str, optional
            column name for the x-axis. The default is None.
        y_name : str, optional
            column name for the y-axis. The default is None.
        hue_str : str, optional
            name of categorical data to color by. The default is None.

        Returns
        -------
        None.
        
        eg. 
        diamonds = sns.load_dataset('diamonds').sort_values('color')
        myplot.sns_boxenplot(diamonds,'color','price')
        """
        sns.boxenplot(data=dataframe, x=x_name, y=y_name, hue=hue_str, 
                      palette='deep')
        plt.show()
        
    ##########################################################################
    def sns_barplot(self, dataframe, x_name=None, y_name=None, hue_str=None):
        """
        Barplot - categorical estimatation

        Parameters
        ----------
        dataframe : dataframe
            data container
        x_name : str, optional
            column name for the x-axis. The default is None.
        y_name : str, optional
            column name for the y-axis. The default is None.
        hue_str : str, optional
            name of categorical data to color by. The default is None.

        Returns
        -------
        None.
        
        eg. 
        titanic = sns.load_dataset('titanic')
        myplot.sns_barplot(titanic,'sex','survived','class')
        """
        sns.barplot(data=dataframe, x=x_name, y=y_name, hue=hue_str)        
        plt.show()
        
    ##########################################################################
    def sns_heatmap(self, data2d, data_type):
        """
        Heatmap of 2d data with data annotated 

        Parameters
        ----------
        data2d : data in 2d representation
        
        data_type : type of data to be annotated - 'int', 'float'
        
        fig_size: tuple, define figure size

        Returns
        -------
        None.

        eg. 
        flights=sns.load_dataset('flights').pivot('month','year','passengers')
        myplt.sns_heatmap(flights,'int')
        """
        
        data_string = {'int':'d','float':'0.1f'}

        sns.heatmap(data2d, annot=True, linewidths=0.5,
                    fmt=data_string[data_type])

        plt.show()
        
    ##########################################################################
    ###                    II - MODEL VISUALIZATION                        ###
    ##########################################################################