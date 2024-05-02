import pandas as pd
from my_neo4j import MyNeo4j

if __name__ == '__main__':
  assets = pd.read_excel('CaseData.xlsx', sheet_name='assets').drop_duplicates()

  my_neo4j = MyNeo4j("bolt://localhost:7687", "neo4j", "deneme123_")
  
  for index, row in assets.iterrows():
    print(row['AssetName'], row['AssetType'], row['AssetCluster'])
    my_neo4j.create_note(
      asset_name=row['AssetName'],
      asset_type=row['AssetType'],
      asset_cluster=row['AssetCluster']
    )
  

  my_neo4j.close()