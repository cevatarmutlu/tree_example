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

This project use `Docker` as `Neo4j` environment. If you don't use `Docker` you can read this [doc](https://neo4j.com/docs/operations-manual/current/installation/). If you can use `Docker` run follow command at project root:

```
docker compose up -d
```

> username: `neo4j`, password: `test1234?_`
> connect to `Neo4j browser` you can visit http://localhost:7474/


### Python

Run follow command at root project:

```
pip install -r requirenments.txt
```