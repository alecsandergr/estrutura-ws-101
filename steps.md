## Step 1: Select your python version

If you use pyenv, you can add a new python version and select it using the following command:

```sh
# List all available versions
pyenv install --list

# Install python
pyenv install <python-version>

# Select your python version
pyenv local <your-python-version>
```

After selecting your python version, a new file `.python-version` will be created in your repository.

## Step 2: Virtual environment

A good practice is to set a new environment for your project. You can use `venv`, `poetry`, among others. For this project, I will use `poetry` beacuse it offers not only the a separate environment, but also the ability to document all the packages from the environment and if anyone wants to reproduce your repository it could be done using a single command, `poetry install`.

```sh
# Setting the environment
poetry config virtualenvs.in-project true
poetry init
# You can define:
# - package name 
# - version
# - description
# - author
# - license
# - compatible python versions
# - main and development dependencies interactively 
```

After the definitions a new file `pyproject.toml` is created with all the the configurations for your project and you can use `poetry shell` to use your brand new environment.

## Step 3: Create the folder structure

Add a basic folder structure, you can add:
- src: your code goes here
- data: if you have any data, add it here
- tests: for your tests
- docs: for your documentation

## Step 4: Create a .gitignore file

You can use gitignore.io website and search for Python to get a template.

## Step 5: Format your code

You can use some libraries or extensions to help you with that, like:
    - black (also has a vscode extension)
    - isort (also has a vscode extension)
    - blue
    - flake8
    - ruff (also has a vscode extension), this one combines black and isort libraries
    - pydocstyle (you can use autoDocstring to help you to create the docstring): check if you docstring is correct

Add the following lines to your `pyproject.toml` file:
```toml
[tool.isort]
profile = "black" # change this accordingly
known_third_party = []
```

### black commands
```sh
# format the scripts for the whole project
black .
# format one file
black {path}
```

### isort commands
```sh
# sort the libraries for the whole project
isort .
# sort one file
isort {path}
```

### blue commands
```sh
# format the scripts for the whole project
blue .
# format one file
blue {path}
```

### pydocstyle commands
```sh
# check the docstring format for the whole project
pydocstyle .
# check the docstring format one file
pydocstyle {path}
```

## Step 6: Automation of your tasks

Instead of running all the commands you need manually, you can create tasks using `taskipy` to run them for you.

```toml
# Add this to your pyproject.toml file
# if you are using blue format comment the isort configuration
[tool.taskipy.tasks]
format = 'isort . && black .'
```

```bash
# Install the library
poetry add taskipy
# Run the task
task format # format is name of the task
```


