# Messaging system

## Project Summary:

A simple rest API backend system that is responsible for handling
messages between users.

## Technologies used:

- Python3 (Django framework)

## How to run the project:

To get this project up and running you should start by having Python installed on your computer. It's advised you create a virtual environment to store your projects dependencies separately. You can install virtualenv with
---

```
pip install virtualenv
```

**Clone or download this repository and open it in your editor of choice. In a terminal (mac/linux) or windows terminal, run the following command in the base directory of this project**

```
python -m virtualenv myenv
```
That will create a new folder `myenv` in your project directory. Next activate it with this command on mac/linux:

```
myenv\Scripts\activate
```
Then install the project dependencies with

```
pip install -r requirements.txt
```
Now you can run the project with this command:

```
python manage.py runserver
```
---



## postman examples

## login

[!(https://i.gyazo.com/c4afb0cc4b529f1035649879569a1730.png)](https://gyazo.com/c4afb0cc4b529f1035649879569a1730)

## logout

[![Image from Gyazo](https://i.gyazo.com/1bde423ecefd0ce3dcb067bd848c3230.png)](https://gyazo.com/1bde423ecefd0ce3dcb067bd848c3230)

## register

[![Image from Gyazo](https://i.gyazo.com/ce6f95643c7fb9af4b7b06873927951e.png)](https://gyazo.com/ce6f95643c7fb9af4b7b06873927951e)

## add new message (must login before)

[![Image from Gyazo](https://i.gyazo.com/99cb91a48b0e0a0f86301c66c20bbc8d.png)](https://gyazo.com/99cb91a48b0e0a0f86301c66c20bbc8d)

## delete message (must log in before)

[![Image from Gyazo](https://i.gyazo.com/3e0f8340538d6d51d71e05e3829b4496.png)](https://gyazo.com/3e0f8340538d6d51d71e05e3829b4496)

## show all message per user (must log in before)

[![Image from Gyazo](https://i.gyazo.com/42be85748bc82585afce62f9e13bc48a.png)](https://gyazo.com/42be85748bc82585afce62f9e13bc48a)
 
## ahow unread message per user (must log in before)

[![Image from Gyazo](https://i.gyazo.com/6f1a859547f9c50f54e2a235bfc399a9.png)](https://gyazo.com/6f1a859547f9c50f54e2a235bfc399a9)

## read message (must log in before)

[![Image from Gyazo](https://i.gyazo.com/2cc11b0284dc1d9845416af54d2a56a1.png)](https://gyazo.com/2cc11b0284dc1d9845416af54d2a56a1)

