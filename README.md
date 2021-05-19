![tutorialpromo](images/tutorial_banner.PNG)

# PVSC48-Python-Tutorial
PVSC48 computing tutorial with focus on PV computing packages, Python, data
wrangling with Pandas, and data viz

## Tutorial Summary:
* Tutorial 0: Introduction to the tutorial, the lesson plan, and resources
* Tutorial 1: Access TMY weather data and visualize monthly irradiance data
* Tutorial 2: Calculate solar position, plane-of-array irradiance, and
  visualize average daily insolation
* Tutorial 3: Estimate module temperature from ambient
* Tutorial 4: Use POA irradiance and module temperature to model output power
  from a single module
* Tutorial 5: Combine modules to form strings, calculate inverter efficiency
  and total array output

## Tutorial Setup
These tutorials are designed to run on [Jupyter](https://jupyter.org), a
browser based interactive notebook that allows you to run the tutorial in the
cloud without any additional setup. During the conference, June 20-25, you will
be provided with a link and credentials to join the tutorial. After the
conference the tutorials will remain available here on GitHub, and you can run
the tutorial anytime in [Binder](https://mybinder.org) by clicking the
following link:

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/PVSC-Python-Tutorials/PVSC48-Python-Tutorial/main)

You can also run the tutorial locally with
[miniconda](https://docs.conda.io/en/latest/miniconda.html) by following thes
steps:

1. Install [miniconda](https://docs.conda.io/en/latest/miniconda.html).

1. Clone the repository:

   ```
   git clone https://github.com/PVSC-Python-Tutorials/PVSC48-Python-Tutorial.git
   ```

1. Create the environment and install the requirements. The repository includes
   a `requirements.txt` file that contains a list the packages needed to run
   this tutorial. To install them using conda run:

   ```
   conda create -n pvsc48 jupyter -c pvlib --file requirements.txt
   conda activate pvsc48
   ```

1. Start a Jupyter session:

   ```
   jupyter notebook
   ```

1. Use the file explorer in Jupyter lab to browse to `PVSC48-Python-Tutorial`
   and start the first Tutorial.
