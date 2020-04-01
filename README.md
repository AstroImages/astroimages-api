![Logo](ASTROIMAGES-API.png)

AstroImages API (astroimages-api)
=================================

![Version](https://img.shields.io/badge/version-1.0.0-blue.svg?cacheSeconds=2592000)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](#)
![Python application](https://github.com/AstroImages/astroimages-api/workflows/Astroimages-API/badge.svg?branch=master)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=AstroImages_astroimages-api&metric=alert_status)](https://sonarcloud.io/dashboard?id=AstroImages_astroimages-api)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/AstroImages/astroimages-api.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/AstroImages/astroimages-api/context:python)
[![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/AstroImages/astroimages-api/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/AstroImages/astroimages-api/?branch=master)
[![Build Status](https://travis-ci.com/AstroImages/astroimages-api.svg?branch=master)](https://travis-ci.com/AstroImages/astroimages-api)


REST API for listing processed images


Usage
-----

Clone the repo:

```console
$ git clone https://github.com/AstroImages/astroimages-api/
$ cd astroimages-api
```


Create and activate virtualenv:

```console
$ virtualenv -p python3 env
$ source env.sh
(env) $ pip3 install -r requirements.txt
```

Run the server via CLI

```console
(env) $ ./start-server.sh
```
    
Or build the docker image

```console
(env) $ docker build -t astroimages-api:latest .
```
Then run the docker image silently

```console
(env) $ docker run -d -p 5000:5000 astroimages-api
```
Or verbose

```console
(env) $ docker run --rm -ti -p 5000:5000 astroimages-api
```

And finally try the endpoints:

```console
(env) $ ./tests/start-tests-fits.sh
```

## Testing

To run unit tests:

```console
(env) $ python -m unittest discover test/unit -v
```

## Author

**Rodrigo de Souza**

* Website: http://www.rodrigosouza.net.br
* Github: [@rsouza01](https://github.com/rsouza01)
* LinkedIn: [@rsouza01](https://linkedin.com/in/rsouza01)

## Tools

- Banner made with BannerSnack

## Show your support

Give a ⭐️ if this project helped you!


## [References](REFERENCES.md)


License
-------

Astroimages-api is released under the [MIT License](LICENSE).

