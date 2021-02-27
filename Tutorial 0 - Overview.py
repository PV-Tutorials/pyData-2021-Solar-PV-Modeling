#!/usr/bin/env python
# coding: utf-8

# ![tutorial banner](images/tutorial_banner.PNG)
# 
# 
# # Welcome! 
# 
# Welcome to the  PV Software 101: from Sun position to AC Output! tutorial
# 
# Modeling tools for all aspects of photovoltaic systems are rapidly growing, and there are solutions for many of the things you might want to simulate. Python is becoming one of the scientific languages of choice, and many open-source tools are available for PV modeling. This tutorial will focus on teaching attendees PV modeling in python through the use of PVlib. 
# 
# In this interactive tutorial we will go from getting acquainted with some common data used or measured in pv systems (i.e. weather), to modeling the AC energy output of a single-axis tracker system. This includes learning and simulating sun position, plane of array irradiances, temperature models, single-diode models and more. 
# 
# We will review common vocabulary around python and ``data aggregation`` by hour, week, month, and visualization. 
# 
# The tutorial will present hands-on examples in python, enabled via jupyter notebooks and a Jupyterhub (remote hosted server for jupyter notebooks and python language) so you, the attende, don’t have to install anything, and follow along while we go over the theory and code! In case it's not obviuos, a computer <b> is </b> required.  
# 
# The tutorial will finalize with an overview of other available open-source tools for other aspects of modeling PV systems. 
# 

# 
# ### More on your teachers:
# 
# The three of us have ample experience in data, coding, and PV field performance modeling, so bring all your questions. 
# 
# <table style='margin: 10 auto'>
# 
# 
# <tr><td><img src="images/tutorial_0_mark.PNG"></td><td>Mark Mikofski. I research, analyze, and predict PV system performance, degradation, and reliability. My goal is to make modeling tools that are robust, accurate, fast, well-documented, and easy to use. I believe solar energy is an important resource that can be profitable and preserve our environment. 
# <br> <br> Specialties: solar energy, PV, thermodynamics, heat transfer, fluid dynamics, multiphysics, numerical methods, optimization, computer modeling, Python, MATLAB, COMSOL, Java, C#, C/C++, FORTRAN.  </td></tr>
# 
# <tr><td><img src="images/tutorial_0_silvana.PNG"> </td><td>Silvana Ayala Pelaez. I am a research scientists at NREL, focusing mostly on bifacial PV system's performance, and circular economy. Python is my daily bread and butter for data analysis and building tools. </td></tr>
# 
# <tr><td><img src="images/tutorial_0_kevin.PNG"> </td><td>Kevin Anderson. I am a research scientists at NREL doing cool stuff! </td></tr>
# 
# </table>
# 

# ### Learning Objectives
# 
# 1.	Access weather data (TMY3), understand irradiance data, and visualize it monthly.
# 2.	Calculate sun position, plane of array irradiance, and aggregate irradiance data into average daily insolation by month and year.
# 3.	Calculate module temperature from ambient data. 
# 4.	Use POA and module temperature to forecast a module's performance. 
# 
# 
# [Overview](images\tutorial_overview.PNG)

# 
# 
# ### Why learn this? 
# 
# PV-lib is a library of algorithms and routines that you might encounter the need to use if you're donig anything PV-modeling related.  It is managed by members of the PV research community, who make sure the formulas and code are not only sleek but accurate. 
# 
# You want to know the sun position? No need to code from zero the SPA (Solar Position algorithm), it's in PVlib. 
# 
# You want to reproduce the Sandia-King model to calculate module performance? It's there, also. 
# 
# You can find the most well-known models, as well as recently accepted values and approaches in published PV literature.
# 
# We hope adding this tool to your skillset will empower you to do better, faster research with an already solid foundation. Don't reinvent the wheel!
# 
# 
# 
# 
# 

# 
# 
# ## Tutorial Setup
# 
# This tutorial is designed to run on [Binder](https://mybinder.org/). This will
# allow you to run the tutorial in the cloud without any additional setup. To get
# started, simply click
# 
# [here](https://mybinder.org/v2/gh/xarray-contrib/xarray-tutorial/master?urlpath=lab):
# [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/xarray-contrib/xarray-tutorial/master)
# 
# 

# 
# If you choose to install the tutorial locally, follow these steps:
# 
# 1. Clone the repository:
# 
#    ```
#    git clone https://github.com/mikofski/PVSC48-Python-Tutorial.git
#    ```
# 
# 1. Install the environment. The repository includes an `environment.yaml` in the
#    `.binder` subdirectory that contains a list of all the packages needed to run
#    this tutorial. To install them using conda run:
# 
#    ```
#    conda env create -f .binder/environment.yml
#    conda activate pvlibenv
#    ```
# 
# 1. Start a Jupyter session:
# 
#    ```
#    jupyter lab
#    ```
# 

# 
# ## Useful links
# 
# <ol>
#     <li>References</li>
#     <ul>
#         <li> <a href="https://pvlib-python.readthedocs.io/en/stable/"> PVlib Documentation </a> </li>
#         <li> <a href="https://github.com/pvlib/pvlib-python"> Github Code Repository </a> </li>
#     </ul>
#     <li> Ask for help:</li>
#     <ul>
#         <li> <a href="https://stackoverflow.com/questions/tagged/pvlib-python"> Use the pvlib-python tag on StackOverflow </a> </li>
#         <li> <a href="https://github.com/pyvlib/pvlib-python/issues"> Open an Issue on the Github Repository </a> </li>
#         <li> <a href="https://groups.google.com/g/pvlib-python"> Google Group - Discussions and more! </a> </li>
#     </ul>
# </ol>
#     
# 

# ## Tutorial Structure
# 
# This tutorial is made up of multiple Jupyter Notebooks. These notebooks mix
# code, text, visualization, and exercises.
# 
# If you haven't used JupyterLab before, it's similar to the Jupyter Notebook. If
# you haven't used the Notebook, the quick intro is
# 
# 1. There are two modes: ``command`` and ``edit``
# 
# 1. From ``command`` mode, press `Enter` to edit a cell (like this markdown cell)
# 
# 1. From ``edit`` mode, press `Esc` to change to command mode
# 1. Press `shift+enter` to execute a cell and move to the next cell.
# 1. The toolbar has commands for executing, converting, and creating cells.
# 
# The layout of the tutorial will be as follows:
# 
# 

# ## Exercise: Print Hello, world!
# 
# Each notebook will have exercises for you to solve. You'll be given a blank or
# partially completed cell, followed by a hidden cell with a solution. For
# example.
# 
# Print the text "Hello, world!".
# 

# In[5]:


# Your code here
print("Hello, world!")


# In[6]:


a = 2
b = 3
a + b


# ## Going Deeper
# 
# We've designed the notebooks above to cover the basics of pvlib from beginning
# to end. To help you go deeper, we've also create a list of notebooks that
# demonstrate real-world applications of pvlib in a variety of use cases. These
# need not be explored in any particular sequence, instead they are meant to
# provide a sampling of what pvlib can be used for.
# 
# ### PVLIB and Weather/Climate Model Data
# 
# 1. [Sun path diagram](https://pvlib-python.readthedocs.io/en/stable/auto_examples/index.html):
#    Start with `global_mean_surface_temp.ipynb` then feel free to explore the
#    rest of the notebooks.
# 
