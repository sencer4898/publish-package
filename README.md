# publish-package
Instructions to publish a Python package using Pycharm and Anaconda Prompt.\
<br/>
Instructions are given in the README file. Required directory structure and exemplary contents are given in the repo.\
<br/>
This repo is created by following [this](https://medium.com/analytics-vidhya/how-to-create-a-python-library-7d5aea80cc3f) Medium post about how to create a library, [this](https://realpython.com/pypi-publish-python-package/#build-your-package) tutorial about how to publish one, and some extra research.

## Steps
### Virtual Environment
Create a virtual environment and install the necessary packages with specific versions. These packages will be the dependencies for your new package. Anaconda creates the new environment at <code>C:\Users\yourusername\Anaconda3\envs</code> by default.
1. Create a virtual environment with name **venv**: <code>conda create -n venv</code>
2. Activate the virtual environment: <code>conda activate venv</code>
3. Install pip (will be used to install other packages): <code>conda install pip</code>
4. Install package dependencies. If conda distribution is available, [it is better to install it](https://www.reddit.com/r/Python/comments/w564g0/comment/ih7jo6v/?utm_source=share&utm_medium=web2x&context=3). Else, you can install using pip.
    * For conda installation: <code>conda install numpy=1.23.5</code>
    * For pip installation: <code>pip install numpy==1.23.5</code>
5. Install packages necessary to create a package (setuptools, wheel) and to upload it (twine). In my case, only twine was missing.
      * <code>conda install setuptools</code>
      * <code>conda install wheel</code>
      * <code>conda install twine</code>
6. Install packages necessary to test the package.
      * <code>conda install pytest==7.1.2</code>
      * <code>conda install pytest-runner==6.0.0</code>

### Creating Project 
Create a project which will be the contents of your package. [This chapter](https://py-pkgs.org/04-package-structure.html) of the **Python Packages** book gives a detailed explanation on the structure of Python packages, feel free to check it out if you wish. Project directory for package creation should have the following structure:
```
package_project
|   README.md
|   setup.py
|
+---package_name
|   |   module1.py
|   |   __init__.py
|   |
|   \---subpkg
|           module2.py
|           __init__.py
|
\---tests
        test_module1.py
        __init__.py
```

* **README.md** file should include the information about the package. You can leave it empty or explain the basics and purpose of the package as a reference for the users of the package.
* **setup.py** file includes the metadata of the package, such as version, dependencies, license, etc.
* **package_name** is the main package folder. This is how the package will be imported, i.e. <code>import package_name</code>. It has modules and subpackages.
* **\_\_init\_\_.py** file indicates that this folder is a package. When we import a package (not a module), this file can import from modules so that we can use functions/classes of other modules as if they are part of an imaginary module named **package_name**. Also, when we run <code>?package_name</code>, we see the contents of docstring of \_\_init\_\_.py.
* **module1** is a python file. Modules can have functions, classes, and variables.<br/>
* **subpkg** is a subpackage under our main package. For example, ensemble is a subpackage under sklearn (sklearn.ensemble).<br/>
* **module2.py** is a module under subpackage.
* **tests** folder includes test module. Test module is used to check if our package produces expected outcomes (for example, using assert to check if a function returns the expected value for specific input values).

For example, **sklearn** is a package and **ensemble** is its subpackage. When we run <code>from sklearn import ensemble</code>, ensemble subpackage is imported. Even though **ensemble** is not a module, we can create an object using <code>ensemble.RandomForestClassifier()</code>. This is because **\_\_init\_\_.py** file of the ensemble subpackage imports this class definition form another module (.\_forest.py).

### Creating Package
In this step, you will write your own functions and classes inside module files. You should e<br/><br/>
When creating the package, you should use the virtual environment. In Pycharm, you can click the bottom right button (on the left of lock button) where it says something similar to 'Python 3.x ...'. Then, <code>Add New Interpreter>Add Local Interpreter>Existing>Click Three Dot.</code> Here, you need to locate the virtual environment that we created in the Virtual Environment step.
<br/><br/>
This is important for the consistency of your package. Whenever you need to install a package, you should install it to the virtual environment. This way, you will know exactly which versions of which packages your new package is requiring. These will be the dependencies for your package. Also, by using a virtual environment, you ensure that your package is guaranteed to work under these conditions.
<br/><br/>
If you want to go one step further, you can check every version of the packages that you are requiring and instead of writing <code>numpy==1.23.5</code> as dependency, you can write <code>numpy>=1.23.5</code>.


### Testing Package
To test the package, run <code>python setup.py pytest</code>. This will run all the tests inside the test function.

### Building and Publishing the Package
* To build the package, run <code>python setup.py sdist bdist_wheel</code>. This will create two files under the **dist** file: one wheel file and one tar.gz file
* To install the package locally, you can run <code>pip install dist/name_of_wheel_file</code>. Then, you can import it in your python files.
* To check if your package description is convenient for PyPI, run <code>twine check dist/&ast;</code>.
* To publish your package to PyPI, run <code>twine upload dist/&ast;</code>. You will be required to provide you PyPI username and password. After providing them, your package will be published to PyPI. From now on, anybody can install your package using <code>pip install package_name</code>.
