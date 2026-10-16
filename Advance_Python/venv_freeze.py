# Virtual Environment in Python
# A virtual environment is an isolated Python environment with its own
# packages, separate from packages installed in other environments.

# If we run `pip install pandas`, pip installs pandas in the currently
# active Python environment. If no virtual environment is active,
# it usually installs into the global environment.

# If we want a specific version of pandas, we can install it using:
# pip install pandas==1.3.5
# The == symbol specifies the exact version we want.
# Installing this version in a virtual environment does not replace
# the pandas version installed in the global environment.

# To avoid conflicts between package versions, we create a virtual environment.
# Each environment can have its own packages and package versions.

# Install virtualenv if we want to use that tool:
# pip install virtualenv

# Create a virtual environment named "env":
# virtualenv env

# We can also use Python's built-in venv module:
# python -m venv env

# To activate the environment in Windows PowerShell:
# .\env\Scripts\Activate.ps1
# After activation, (env) usually appears in the terminal.
# Packages installed using pip will now be installed in this environment.

# To deactivate the virtual environment:
# deactivate


# 1. Listing installed packages
# pip freeze lists the installed packages and their versions
# in the currently active Python environment.
# Run this command in the terminal:
# pip freeze


# 2. Creating a requirements.txt file
# We can save the list of installed packages and their versions
# into a file named requirements.txt using:
# pip freeze > requirements.txt
# The > symbol redirects the output into the file.
# Example contents:
# pandas==2.2.3
# numpy==2.1.0
# The actual versions depend on the packages installed in our environment.


# 3. Installing packages from requirements.txt
# To install all the packages listed in this file, run:
# pip install -r requirements.txt
# This installs the listed packages into the currently active environment.
# So we can use this file to recreate the package setup in another environment.


# 4. Checking the version of an installed module
# Run Python in the terminal:
# python
# >>> import pandas
# >>> print(pandas.__version__)