# Jupyter Seed 

This project provides the common infrastructure that a Jupyter project needs. 
It provides a folder structure to accomodate data files, py files for modular logic, and notebooks.
The folder structure can be extended with a models or test folders, depending on the needs.
The project uses a local SQLite database, though other databases can also be woven into it.

## Items Included 

**requirements.txt:** This file can be used to install all of the virtual env's packages. 
The packages installed are meant for any minimal project: jupyter, pandas and sqlalchemy. 
The only more specialized package is selenium, not every project will use it.

**base_module:** This module serves as the seed module. 
This means that it does not solve a business problem, instead it serves to typecast the boilerplate code that is common for all custom modules.
Therefore, to create a new module, you should copy+paste this one and rename it.
It includes the following sample notebooks:
- generic: The seed notebook that should be copy+paste to create all new notebooks.
- database: Sample database code for connection and CRUD operations. 
Also provides advanced examples for user defined functions and table joins.
- dataframe: Showcases common use cases for pandas dataframes, such as deleting columns, calculating derived columns, and aggregation.
- graphs: A primer into the plotly package. The Lego data is used to show scatter plots and histograms.
- images: Basic sample of showing an image in a notebook. Further image work will require the OpenCV package.

**pictures_manager:** A toy project of mine for scraping the DeviantArt website. 
It also keeps a database of the artists that I have inspected or downloaded from. 
Uses [Selenium](https://pypi.org/project/selenium/) to log in and web crawl the site, 
and [urllib](https://docs.python.org/3/library/urllib.html) for the actual downloads.

