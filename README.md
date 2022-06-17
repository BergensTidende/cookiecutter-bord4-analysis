# Bord4 Data Analysis Cookiecutter

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#development">Development</a></li>
    <li><a href="#push-local-changes">Push local changes</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About The Project

Data journalism analysis projects tend to become a bit messy. To make it easier for your future self and your colleagues to make sense of your work, we propose both a reasonable structure that's also flexible. With code for sharing your analysis while you work on it and for publishing. Nothing in this template is carved in stone, both critisism and PR's are welcome. 


### Inspiration
-----------
Heavily inspired by the following projects:

* [AP Python Cookiecutter](https://github.com/associatedpress/cookiecutter-python-project)
* [Cookiecutter Data Science](http://drivendata.github.io/cookiecutter-data-science/)
* [Zego's fork of the above cookiecutter](https://github.com/zegocover/cookiecutter-zego-data-science)
* [EasyData](https://github.com/hackalog/easydata)


### Requirements
-----------
 - pyenv - manage python versions
 - pipenv - manage python dependencies
 - [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html) >= 1.4.0

To install on mac you can use homebrew:

``` bash
brew upgrade
brew install pyenv
brew install pipenv
pip install cookiecutter
```

To create a new analysis using the cookiecutter template, run the following command

```bash
cookiecutter https://github.com/BergensTidende/cookiecutter-bord4-analysis
```

### Env variables
-----------
Some functionality requries you to set a few enviroment varibales. Theese can either be set in a .env file on root in the project. Or in your .zshenv-file (or equal for the bash you're using). You'll find theese values in 1pass

#### Datawrapper

* DATAWRAPPER_API_TOKEN

#### API keys for insertion of Multimedia Content

* MM_API_BASE_URL
* MM_API_BASE_URL

#### S3

* S3_BUCKET_INTERNAL_NOTEBOOK_DATA
* S3_BUCKET_PUBLIC

#### Deploy analysis somewhere

* ANALYSE_CONNECTION
* ANALYSE_URL

### Templates
------------
[There are a collection of templates that can be used](https://github.com/BergensTidende/bord4-analysis-templates/)

To use a template in your project run the command `make template` and follow the instructions on the screen.

### The resulting directory structure
------------

```
.
├── README.md
├── data
│   ├── processed
│   ├── source
│   └── untracked
├── report
│   ├── css
│   ├── figures
│   └── notes
├── output
├── eda
├── etl
├── publish
├── scratch
└── src
    └── utils
```

- `README.md`
  - Project-specific readme with instructions how to recreate the analysis, contact information and technical instructions.
- `data`
  - This is the directory used for storing and saving data
  - `data/processed`
    - Contains data that has either been transformed from an `etl` script or output from an `analysis` jupyter notebook.
    - Data that has been transformed from an `etl` script will follow a naming convention: `etl_{file_name}.[csv,json...]`
  - `data/source``
    - Raw untouched data. Data in this folder should never be altered
  - `data/untracked`
    - Files that are either to large or to sensitive to be on github goes here. 
- `report`
  - The folder where your report lives. The `eda` and `publish` folders are symlinked so the notebooks can stay in their folder
  - `css`
    - custom css for all your customization needs. Used to hide input cells in notebooks. Remove if you want to show them.
  - `figures`
    - figures used in your reports
  - `notes`
    - interviews, strain of thought, anything you want.
  - index.md
    - The root file for the docs.
- `report_build`
  - Folder will be created by Mkdocs build script
- `eda`
  - This folder is used for analysis that explore the data. Typically this is the first step of your analysis.
  - This folder is symlinked in the docs folder for easy reference to notebooks and files you wish to include in reports.
  - When you find analysis you wish to publish you organize them in the publish folder. 
  - Notebooks in this folder can ingest data from either `data/source` (if that data comes from the source in a workable format) or `data/processed` (if the data required some prep).
  - Dataframes from analysis notebooks should be written out to `data/processed`
  - `eda/labnotes.md`
    - your scratchpad to use while exploring data. 
- `etl`
  - This is where we keep python scripts or notebooks involved with collecting, transforming and washing data for analysis.
  - If you wish to save data from this step you save them to the `data/processed`-folder
- `publish`
  - This is where all the content for the final artilce is created. Figures, numbers and json-files. 
  - This folder is symlinked in the docs folder for easy reference to notebooks and files you wish to include in reports.
  - Notebooks in this folder can ingest data from either `data/source` (if that data comes from the source in a workable format) or `data/processed` (if the data required some prep).
- `output`
  - Public-facing data files go here - data files which are 'live'.
- `scratch`
  - Directory to stash away things that are not needed in the project, but that you want to keep for future reference
  - This directory is not git tracked.
- `src`
  - Python files used as utils that can be imported from notebooks and script.
  - `src/dataframe`
    - util functions for working with dataframes
  - `src/integration`
    - helper functions when working with Schibsted MM API
  - `src/log`
    - better log functions
  - `src/scripts`
    - for scripts used by the make file

## Make commands

### Run jupyter lab
```bash
make lab
```

### Create TOC for the mkdocs folder.
```bash
make toc
```

### Use mkdocs to build the content from the `report` folder to `report_build`.
```bash
make build
```

### Serve the content from `report_build`
```bash
make serve
```

### Run build and then serve the content from `report_build`
```bash
make site
```

### Use one of our many fancy templates!
```bash
make template
``` 

## Contributing

Do you have write permissions to the repo? Then you can clone this project to a folder on your computer. 

```bash
git clone cookiecutter-bord4-analysis
```

If not do the following:

- Create a personal fork of the project on Github.
- Clone the fork on your local machine. Your remote repo on Github is called `origin`.
- Add the original repository as a remote called `upstream`.
- If you created your fork a while ago be sure to pull upstream changes into your local repository.

This will clone the template into `cookiecutter-bord4-analysis`. To learn about the directory structure and special cookiecutter variables read [Project templates and Cookiecutter](https://medium.com/worldsensing-techblog/project-templates-and-cookiecutter-6d8f99a06374) and the [cookiecutter documentation](https://cookiecutter.readthedocs.io/en/latest/installation.html)

Create a branch for your changes

```bash
git checkout -b name-of-branch
```

Make your changes, rememeber to commit. And always write your commit messages in the present tense. Your commit message should describe what the commit, when applied, does to the code – not what you did to the code.

Run the following command to create a template and test your changes

```bash
cookiecutter cookiecutter-bord4-analysis
```

If you're working on a clone push the branch to github and make PR.

If your're working a fork:
- Squash your commits into a single commit with git's [interactive rebase](https://help.github.com/articles/interactive-rebase). Create a new branch if necessary.
- Push your branch to your fork on Github, the remote `origin`.
- From your fork open a pull request in the correct branch. Target the project's `develop` branch if there is one, else go for `master`!
- …
- If the maintainer requests further changes just push them to your branch. The PR will be updated automatically.
- Once the pull request is approved and merged you can pull the changes from `upstream` to your local repo and delete
your extra branch(es).


<!-- CONTACT -->

## Contact

Lasse Lambrechts - [@lambrechts](https://twitter.com/lambrechts) - lasse.lambrechts@bt.no


TODO:

To use plotly in notebook:
fig.show(renderer="jupyterlab"