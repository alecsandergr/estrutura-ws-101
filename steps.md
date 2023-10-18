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

# Step 2: Virtual environment

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

