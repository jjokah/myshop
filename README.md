# MYSHOP

A fully featured online shop.

## Table of Contents

- [Snippet](#snippet)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Features](#features)
- [Deployment](#deployment)
- [License](#license)

## Snippet

```python
# python code snippet goes here..
```

### Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

## Prerequisites

Required packages for installation setup:

- Python 3
- Pip install packages

## Installation

To get a development environment running:

> clone this repo to your local machine

```shell
git clone https://github.com/JohnJohnsonOkah/myshop.git
```

> install requirements

```shell
pip install -r requirements.txt
```

> setup database

```shell
python manage.py migrate
```

> create superuser

```shell
python manage.py createsuperuser
```

> run development server

```shell
python manage.py runserver
```

... 👯 Now development server is up and running...

## Features

- enable clients to browse products
- enable clients to add products to the cart
- enable clients to apply discount codes
- enable clients to go through the checkout process
- enable clients to pay with a credit card
- enable clients to obtain an invoice
- recommendation engine to recommend products to the customers
- internationalization to offer the site in multiple languages.

## Deployment

Additional notes about how to deploy this on a live system

## License

[MIT](LICENSE)
