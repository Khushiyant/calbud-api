# Calbud REST API
This repository contains the source code for Zulip's PyPI packages:
* ```foodapi``` : Package for food nutrient profile
* ```tips``` : Generate random fitness tips 
* ```cards``` : Handle user entered food profile
* ```base``` : Contains basic database schema

__The source code__ is written in _Python 3_.

## Development
1. Fork and clone the Git repo, and set upstream to Khushiyant/calbud-api:

```bash
git clone https://github.com/<your_username>/calbud-api.git
cd cabled-api
git remote add upstream https://github.com/Khushiyant/calbud-api.git
git fetch upstream
```
2. Make sure you have [pip](https://pip.pypa.io/en/stable/installing/)

3. Setup virtual environment
```bash
pip install virtualenv
virtualenv venv
```

4. Activate the Virtual environment 