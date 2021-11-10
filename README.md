# Monitoring tool for mining progress
## _Tracking the daily progress of mining on flexpool_

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

This monitoring tool was created to monitor the daily progress of mining Ethereum on flexpool. It was created to run daily on a specific time to get the actual Ethereum amount and update a sheet on Google Docs.

## Features

- Checks ETH amount on Flexpool for a specific wallet
- Updates a Sheet on Google Docs with the current day amount

## Utilization

Use the pre written script to initialize install the required products and setup your environment. Then activate the virtual environment.
```sh
chmod +x install.sh
./install.sh
. ./activate
```

Run the `setup.py` script to install all the required packages to run the application.
```sh
python setup.py develop #use install for production
```

Run the script using `run.py`.

```sh
python run.py
```
