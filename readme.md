## 10.020 Cohort Exercise

### Requirements

You can run this project either globally or using virtual environments. Since we need pretty standard packages: `pandas, numpy, seaborn, matplotlib, pytest`, it doesn't really matter if you install this globally or in a virtual environment.

The `Pipfile` and `requirements.txt` files mirror one another.

#### Global Installation

Install all required modules listed in `requirements.txt` with the command:

```
python -m pip install -r requirements.txt
```

#### Using `pipenv` Virtual Environment

Install `pipenv` globally if you don't have it already:

```
pip install pipenv
```

Then install the packages listed in the `Pipfile`, and activate the `shell`:

```
pipenv install
pipenv shell
```

### Usage

Change your current directory to `/weekX` before running `pytest`.

All source code resides inside `/weekX/source` directory. This is where you want to do your work on. Once done and you want to test, directly run `pytest`.
![](/images/readme/2023-11-05-11-55-59.png)

This will test ALL `test_*` files under `/weekX` directory. If you'd like to run a particular test file, do:

```
pytest tests/test_cs_<number>.py
```

![](/images/readme/2023-11-05-11-58-53.png)

### Running Pytest with VSCode

If you use VSCode integrated test environment, go to the root path, and put this under `.vscode/settings.json`, and change `weekX` to the week you're currently testing.

```
{
  "python.testing.pytestArgs": ["weekX"],
  "python.testing.unittestEnabled": false,
  "python.testing.pytestEnabled": true
}
```
