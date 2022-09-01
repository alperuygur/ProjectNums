# ProjectNums - with Python Fastapi
Converts given number to short form.


Examples:
- input: 500 output 500
- input: 3400 outputs 3.4k
- input: 1000000 output: 1M
- input: 2500000.34 output: 2.5M
- input: 1123456789 output: 1.1B
- input: -2545.266555555 output: -2.5K
- input: -15000 output: -15K

## Demo
For demo version:
https://projectnums.herokuapp.com/


## Quickstart

First, clone the repo and cd to directory

```bash
  $ git clone https://github.com/alperuygur/ProjectNums.git && cd ProjectNums
```

Then install dependencies in the project folder (ProjectNums) with any command prompt:

```bash
  pipenv install
```

To activate this project's virtualenv, run the following:

```bash
  pipenv shell
```

Run program in command prompt with the following:
```bash
  uvicorn main:app --reload
```

You can now visit the app on browser:
```bash
  http://127.0.0.1:8000 
```

## Screenshots

### Home Page
![Home page](https://github.com/alperuygur/ProjectNums/blob/master/screenshots/ss1.png?raw=true)

### Result Page
![Numbers](https://github.com/alperuygur/ProjectNums/blob/master/screenshots/ss2.png?raw=true)

### Swagger Docs
![swagger](https://github.com/alperuygur/ProjectNums/blob/master/screenshots/ss3.png?raw=true)

![swagger](https://github.com/alperuygur/ProjectNums/blob/master/screenshots/ss4.png?raw=true)
