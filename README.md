# iig_admin

[![Generic badge](https://img.shields.io/badge/maintained-no-RED.svg)](https://aahnik.github.io/)
[![No Maintenance Intended | Archived](https://unmaintained.tech/badge.svg)](https://gitHub.com/aahnik/iig_admin/graphs/commit-activity)
[![Generic badge](https://img.shields.io/badge/bugs-yes-YELLOW.svg)](https://aahnik.github.io/)

## Note

- This project is not for general public use.
- `iig-admin` was made keeping in mind the academic structure of IIG ( Ideal Institute of Geography)
- This is a portal only for admins.
- It does not have multi-year support.
- This is not under development and is not used by anybody.
- There may be uncaught bugs.
- No support | No issues | No PRs.

## Work flow

- [x] link to admin in home page
- [x] successfully import data from existing sheets
- [x] to see students in feeRecord month in Django Admin
- [x] search by student name
- [x] sort by grade and acadTarget
- [x] filter by class, study center and section
- [x] to select months for actions to be applied for those
- [x] to bulk select or unselect months
- [x] define a method 'cleared' which returns true for students who cleared selected month fees
- [x] see a tick or cross based on above.
- [x] action to mark selected months paid for selected query-set of students
- [x] **Release Beta 1.0**
- [x] learn more about deployment, make security changes required for deployment
- [x] deploy on python-anywhere.

Note: This is currently not deployed and not used by anybody.

## How to run this

The following steps will be directly applicable for Unix systems like Linux or Mac.
If you are on windows, you need to make certain changes. Google is your best friend here.

System requirements:

- Python3.x ( where `x >= 6` )
- pip
- make

1. First of all clone this repo from GitHub.

        git clone https://github.com/aahnik/iig_admin.git

2. Run this single magic command to setup everything and run server.

        make first_time

Read the `Makefile` to see what happens behind the above command.

The data in `sample_data.csv` contains dummy phone numbers and emails.
