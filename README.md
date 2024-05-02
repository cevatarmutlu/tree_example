## INTRODUCTION

This repo read the given excel file and create tree from data of the excel file. For create tree, use `Pandas` and for to store the tree use `Neo4j`.

## Used Technologies

Tecnology | Information
----------|------------
Python | As a Programming language
Pandas    | For to read from given excel file and transform it and filter it and to create the tree.
Neo4j     | For to store the tree
Docker    | As Neo4j environment

## INSTALL

### NEO4j

Neo4j installed with docker:

```
docker pull neo4j;
docker run -p 7474:7474 -p 7687:7687 -d --env=NEO4J_AUTH=neo4j/deneme123_ neo4j:latest
```
visit: http://localhost:7474/

user: neo4j

password: deneme123_

### Python

```
pip install -r requirenments.txt
```