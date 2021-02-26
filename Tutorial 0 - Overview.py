#!/usr/bin/env python
# coding: utf-8

# <img src="https://pvlib-python.readthedocs.io/en/stable/_images/pvlib_logo_horiz.png" align="right" width="30%">
# 
# # Introduction
# 
# Welcome to the pvlib Tutorial.
# 
# pvliby is a community supported tool that provides a set of functions and classes for simulating the performance of photovoltaic energy systems. 
# 
# pvlib introduces ............
# 
# 
# ## Tutorial Setup
# 
# This tutorial is designed to run on [Binder](https://mybinder.org/). This will
# allow you to run the turoial in the cloud without any additional setup. To get
# started, simply click
# [here](https://mybinder.org/v2/gh/xarray-contrib/xarray-tutorial/master?urlpath=lab):
# [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/xarray-contrib/xarray-tutorial/master)
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
# ## Useful links
# 
# <ol>
#     <li>References</li>
#     <ul>
#         <li> [Documentation](https://pvlib-python.readthedocs.io/en/stable/) </li>
#         <li> [Code Repository](https://github.com/pvlib/pvlib-python) </li>
#     </ul>
#     <li> Ask for help:</li>
#     <ul>
#     <li> Use the   [pvlib-python](https://stackoverflow.com/questions/tagged/pvlib-python) on
#   StackOverflow </li>
#         <li> [GitHub Issues](https://github.com/pyvlib/pvlib-python/issues) for bug reports and
#             feature requests </li>
#         <li> [Google Group - Discussions and more!](https://groups.google.com/g/pvlib-python)</li>
# </ol>
# ## Tutorial Structure
# 
# This tutorial is made up of multiple Jupyter Notebooks. These notebooks mix
# code, text, visualization, and exercises.
# 
# If you haven't used JupyterLab before, it's similar to the Jupyter Notebook. If
# you haven't used the Notebook, the quick intro is
# 
# 1. There are two modes: command and edit
# 1. From command mode, press Enter to edit a cell (like this markdown cell)
# 1. From edit mode, press Esc to change to command mode
# 1. Press shift+enter to execute a cell and move to the next cell.
# 1. The toolbar has commands for executing, converting, and creating cells.
# 
# The layout of the tutorial will be as follows:
# 
# 1. [Introduction + Weater Data](Tutorial 1 - TMY Weather Data.ipynb)
# 1. [Working with irradiance to calculate POA](Tutorial 2 - POA Irradiance.ipynb)
# 1. [Calculate module temperature](Tutorial 3 - Module Temperature.ipynb)
# 1. [Array Power](Tutorial 4 - Array Power.ipynb)
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

# In[ ]:


# Your code here


# In some cases, the next cell will have the solution. Click the ellipses to
# expand the solution, and always make sure to run the solution cell, in case
# later sections of the notebook depend on the output from the solution.
# 

# In[ ]:



print("Hello, world!")


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
#    <!-- 1. [Natural climate variability in the CESM Large Ensemble](https://aws-uswest2-binder.pangeo.io/v2/gh/NCAR/cesm-lens-aws/master?urlpath=lab) -->
# 
# 2. [SOMETHING ELSE HERE](https://google.com):
#     Write something here of another one of the tutorials.
#     <!-- 1. [something something](https://google.com) -->
#     
# ### PVLIB and Satellite Data
# 
# 2. [SOMETHING ELSE HERE](https://google.com):
#     Write something here of another one of the tutorials.
#     <!-- 1. [something something](https://google.com) -->

# In[ ]:




