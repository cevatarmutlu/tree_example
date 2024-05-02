## INTRODUCTION

This repo read the given excel file and create tree from data of the excel file. For create tree, use `Pandas` and for to store the tree use `Neo4j`.

## Used Technologies

Tecnology | Information
----------|------------
Python | As a Programming language
Pandas    | For to read from given excel file and transform it and filter it and to create the tree.
Neo4j     | For to store the tree
Docker    | As Neo4j environment

## INSTALL

### NEO4j

This project use `Docker` as `Neo4j` environment. If you don't use `Docker` you can read this [doc](https://neo4j.com/docs/operations-manual/current/installation/) for installing `Neo4j`. If you use `Docker` run following command at root directory of the project::

```
docker compose up -d
```

> username: `neo4j`, password: `test1234?_`
> For connect to `Neo4j browser` you visit http://localhost:7474/


### Python

Run following command at root directory of the project:

```
pip install -r requirenments.txt
```

## How to run and how to work?

For run the project run following command at root directory of the project:

```
python main.py
```

after run above command, the program:

* reads the excel file with `pandas`
* creates `nodes` from `assets` sheet from the excel file to Neo4j
* find outs matching `asset`s
* creates relationship between `asset nodes` in Neo4j
