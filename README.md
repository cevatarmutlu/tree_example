## INTRODUCTION

This repo reads the given excel file and creates a tree from the excel file. For creates a tree, uses `Neo4j`.

## Used Technologies

Tecnology | Information
----------|------------
Python | Programming language
Neo4j     | To create tree from given excel file
Docker    | For Neo4j Enviroment
Pandas    | For filter data and transform data

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