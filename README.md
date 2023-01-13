# publish-package
Instructions to publish a Python package using Pycharm and Anaconda Prompt.\
<br/>
Instructions are given in the README file. Required directory structure and exemplary contents are given in the repo.\
<br/>
This repo is created by following [this](https://medium.com/analytics-vidhya/how-to-create-a-python-library-7d5aea80cc3f) Medium post about how to create a library, [this](https://realpython.com/pypi-publish-python-package/#build-your-package) tutorial about how to publish one, and some extra search.

## Steps
### Virtual Environment
Create a virtual environment and install the necessary packages with specific versions. These packages will be the dependencies for your new package.
1. Create a virtual environment with name **venv**: <code>conda create -n venv</code>
2. Activate the virtual environment: <code>conda activate venv</code>
3. Install pip (will be used to install other packages): <code>conda install pip</code>
4. Install necessary packages. If conda distribution is available, [it is better to install it](https://www.reddit.com/r/Python/comments/w564g0/comment/ih7jo6v/?utm_source=share&utm_medium=web2x&context=3). Else, you can install using pip.
    * For conda installation: <code>conda install numpy=1.23.5</code>
    * For pip installation: <code>pip install numpy==1.23.5</code>


### Creating Project
Create a project which will be the contents of your package. Project directory should have the following structure

