# Python WebUI Test Automation For I&M Bank

This Readme will assist in setting up and configuring the run setup.

## Table of Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Running UI Tests](#running-ui-tests)
- [Allure Report](#allure-report)

## Introduction

This Repo is aimed to show how to traverse the I&M website with the help of Playwright.

## Prerequisites

Before getting started, make sure you have the following prerequisites installed:

- [Python 3.x](https://www.python.org/downloads/)
- PIP
 ```shell
    python3 -m ensurepip
```
- venv
 ```shell
    pip install virtualenv
```


## Getting Started

To get started with Python and Playwright, follow these steps:

1. Clone or download this repository.
2. Open a terminal and navigate to the project directory.
3. Create and activate an isolated environment by running the following commands
```shell
python3 -m venv venv
```
For Linux & Mac, run 
```shell
source venv/bin/activate
```
For Windows run
```shell
venv\Scripts\activate.bat
```
4. Install the project dependencies by running the following command:
```shell
pip3 install -r requirements.txt
```
Also, ensure to run the below to have Playwright install its browsers
```shell
playwright install
```

## Running UI Tests

1. Running UI tests in headless mode Chrome

```shell
python3 -m pytest -m webtest tests --verbose
```
2. Running UI tests in headed mode & specific browser(chromium,firefox,webkit)

```shell
python3 -m pytest -m webtest tests --browser webkit  --headed --verbose
```

## Allure Report

By default, the test summary will be posted into the command line

To generate an HTML report using the Allure reporting framework, run tests with `--alluredir` parameter

```shell
python3 -m pytest -s --alluredir=allure-results tests --browser chromium  --screenshot on --video on --headed --verbose
```

And the generate and open report in the browser by running
```shell
allure serve -h localhost
```
``` shell
npm install -g allure-commandline --save-dev
```
Please run the above command to have Allure reports adequately configured.

