# Widget Application

Write a CRUD REST API using Python for a single resource type. You may use a framework (we use Tornado, but that is not required for this assessment).

The application must satisfy these requirements:

1. Written in Python 3.8 or later.
2. Endpoints to create, read, list, update, and delete objects called "Widgets"
3. Widget objects include the following properties (at least):
   * Name (utf8 string, limited to 64 chars)
   * Number of parts (integer)
   * Created date (date, automatically set)
   * Updated date (date, automatically set)
4. Widgets are persisted to and retrieved from a SQLite file database.
5. Include a README that describes how to setup and run the application.

Ideas to make the project even better:

* Include unit or functional test coverage
* Include an OpenAPI spec
* PEP8 compliance
* Pass standard lint tests (ie: flake8 or similar)
* Pass bandit security analysis
* Use Python type annotations

## Setup

Assume virtenv. tested on Ubuntu 18.04

```
./setup.sh
```

## Run Server

Run the server with

```
$ source ./env/bin/activate
(env) $ ./RunServer.py
```

## Example Client

Sample client that will remove any existing widgets,
and the do CRUD with sample data

```
$ source ./env/bin/activate
(env) $ ./Client.py
```

## Run Tests
```
$ source ./env/bin/activate
(env) $ ./Client.py
```

## Run Static Analysis

Run analysis with:

* PEP8
* Bandit
* Flake8

```
$ source ./env/bin/activate
(env) $ pre-commit run --all-files
```
