# Advent of Code 2022 by msoria
I'm using a custom structure in order to reuse the same node environment every day and share some common and util code.

    msoria-serial
    |
    |-assets
      |-day1
      |-day2
    |-src
      |-day1
      |-day2

## Add a day
- add day X folder structure with `gulp new --day X`
- add example data in `assets/dayX/example.txt`
- add example answer in `assets/dayX/example-answer.txt`

## Run test on example data
To run the current day test

`npm run test`

## Run exercices
To run the current day exercice

`npm run start`

## Switch to an existing day
To run the current day test

`gulp switch --day X`
