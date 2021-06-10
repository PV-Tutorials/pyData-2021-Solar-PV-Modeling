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
cloud without any additional setup. On the day of the tutorial, you can log
into the tutorial [here](http://pvsc-python-tutorial.ml/):

http://pvsc-python-tutorial.ml/

The first time you visit the tutorial, you will need to create an account. Use
any username and password you like.

![jupyter login](https://user-images.githubusercontent.com/1385621/119911747-c9bd3600-bf0e-11eb-8f7b-c622d8890f04.png)

The first time you log into the tutorial, you will only see the scratch and shared-data folders.

![first login](https://user-images.githubusercontent.com/1385621/119912003-5cf66b80-bf0f-11eb-874d-67ba2ff1bb66.png)

After you log in, you need to download the tutorial from this GitHub repository by following this
[link](https://pvsc-python-tutorial.ml/hub/user-redirect/git-pull?repo=https://github.com/PVSC-Python-Tutorials/PVSC48-Python-Tutorial&branch=main):

https://pvsc-python-tutorial.ml/hub/user-redirect/git-pull?repo=https://github.com/PVSC-Python-Tutorials/PVSC48-Python-Tutorial&branch=main

You only need to download the repository once, but you can always use either link to start the tutorial during the conference.
From now on you will see the PVSC48-Python-Tutorial folder in the list.

![download tutorial](https://user-images.githubusercontent.com/1385621/119912192-ce361e80-bf0f-11eb-8f62-36e54509fdcc.png)

Click the folder to open, and you'll see the full list. Click `Tutorial 0 - Overview.ipynb` to get started.

![full list of tutorials](https://user-images.githubusercontent.com/1385621/119912314-15241400-bf10-11eb-8a2c-1fc371e0f4e8.png)

Sometimes, if you are idle too long, the tutorial dies. Just click the [link to the tutorial](http://pvsc-python-tutorial.ml/) again to reconnect.

http://pvsc-python-tutorial.ml/

### Jupyter Book docs

The full tutorial is now also hosted as a beautiful [Jupyter book](https://jupyterbook.org/intro.html). This book has navigation, search, and can even run code cells interactively. Check it out!

https://pvsc-python-tutorials.github.io/PVSC48-Python-Tutorial/index.html

### My Binder

After the conference the tutorials will remain available here on GitHub, and you can run
the tutorial anytime in [Binder](https://mybinder.org) by clicking the
following link:

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/PVSC-Python-Tutorials/PVSC48-Python-Tutorial/main)

### Locally

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


### Licensing

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.