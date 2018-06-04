
[![Build Status](https://travis-ci.org/Melvin1Atieno/MnR-Tracker.svg?branch=ft-user-post-requests-157931267)](https://travis-ci.org/Melvin1Atieno/MnR-Tracker)

[![Coverage Status](https://coveralls.io/repos/github/Melvin1Atieno/MnR-Tracker/badge.svg?branch=ft-user-post-requests-157931267)](https://coveralls.io/github/Melvin1Atieno/MnR-Tracker?branch=master)

# MnR-tracker

Maintenance Tracker App is an application that provides users with the ability to reach out to operations or repairs department regarding repair or maintenance requests and monitor the status of their request.

*Landing page*:
![MnRlanding Page](/UI/static/images/land.png)

## The project contains designs for

 1. _**A landing page.**_
 2. _**A signup page.**_
 3. _**A Login page.**_
 4. _**An admin's homepage.**_
 5. _**A Users homepage.**_

## Installation

 To get your own copy of the designs or get a feel:
clone the repo:
```
$ https://github.com/Melvin1Atieno/MnR-Tracker.git
```

cd into the repo:
```
$ /MNR-TRACKER/UI/template
```

copy the link to your favourite browser


## Usage

View demo on ghpages hosted platform: [click](https://melvin1atieno.github.io/MnR-Tracker)

### API
--------------------------------------------------------------------------------------------------------------------------

### ENDPOINTS

 **METHOD**| **Endpoints**                    |**Functionality**
 ----------|----------------------------------|--------------------------------------|
 GET       |/api/v1/users/requests            | Fetch all requests                   |
 GET       |/api/v1/users/requests/<int:id>   | Fetch a single request               |
 PUT       |/api/v1/users/requests/<int:id>   | Modify request details               |
 POST      |/api/v1/users/requests            | Logged in users can create a request |
 POST      |/api/v1/users/registration        | Handles user registration           |
 POST     |/api/v1/users/                    | Handles users login                  |

### Technologies and languages

1. [**Project management (Agile)**](https://www.pivotaltracker.com/n/projects/2173280)

2. python

3. flask framework

### Run locally

create a virtual environment for the project:
```
$ virtualenv --python=python3.5 virtualenv-name
```

activate the virtual environment:
```
$ source virtualenv-name/bin/activate
```

use virtualenv-wrapper alternative:
```
$ mkvirtualenv --python=python3.5 virtualenv-name
```

to use it:
```
$ workon virtualenv-name
```

remember to run ``` $ pip install -r requirements.txt``` to install libraries


--------------------------------------------------------------------------------------------------

### Acknowledgement

------------------------------------------------------------------------------------------------------------------------------------------------

Andela Bootcamp - cohort 28