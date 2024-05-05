import pandas as pd
from src.my_neo4j import MyNeo4j

if __name__ == '__main__':
  excel_path = 'src/resources/CaseData.xlsx'
  
  ### READ EXCEL ###
  assets = pd.read_excel(excel_path, sheet_name='assets')[['AssetName', 'AssetType', 'AssetCluster']].drop_duplicates()
  needs = pd.read_excel(excel_path, sheet_name='needs')[['asset_name', 'need_value', 'group_id']].drop_duplicates()
  offers = pd.read_excel(excel_path, sheet_name='offers')[['asset_name', 'offer_value', 'group_id']].drop_duplicates()
  ### READ EXCEL ###

  ### NEO4j ###
  neo4j_conn = MyNeo4j("bolt://localhost:7687", "neo4j", "test1234?_")

  for _, row in assets.iterrows():
    neo4j_conn.create_asset_node(
      asset_name=row['AssetName'],
      asset_type=row['AssetType'],
      asset_cluster=row['AssetCluster']
    )
  ### NEO4j ###

  ### SECTION ###
  needs_assets = pd.merge(needs, assets, how='left', left_on='asset_name', right_on='AssetName') \
    .rename(columns= {
      'group_id': 'need_group_id', 
      'AssetName': 'need_asset_name', 
      'AssetType': 'need_asset_type',
      'AssetCluster': 'need_asset_cluster'
    }).drop(columns='asset_name')
  
  offers_assets = pd.merge(offers, assets, how='left', left_on='asset_name', right_on='AssetName') \
    .rename(columns= {
      'group_id': 'offer_group_id', 
      'AssetName': 'offer_asset_name', 
      'AssetType': 'offer_asset_type',
      'AssetCluster': 'offer_asset_cluster'
    }).drop(columns='asset_name')
  ### SECTION ###

  ### FIND MATHING ASSETS ####
  df = pd.merge(needs_assets, offers_assets, how='inner', left_on='need_value', right_on='offer_value')
  df = df.loc[df['need_group_id'] + 1 == df['offer_group_id']][['need_asset_name', 'need_asset_type', 'need_asset_cluster', 'offer_asset_name', 'offer_asset_type', 'offer_asset_cluster']].drop_duplicates(ignore_index=True)
  ### FIND MATHING ASSETS ####

  # CREATE RELATIONSHIPS BETWEEN ASSET NODES
  for _, row in df.iterrows():
    neo4j_conn.create_asset_relation(
      needs_asset_name=row['need_asset_name'],
      needs_asset_type=row['need_asset_type'],
      needs_asset_cluster=row['need_asset_cluster'],
      offers_asset_name=row['offer_asset_name'],
      offers_asset_type=row['offer_asset_type'],
      offers_asset_cluster=row['offer_asset_cluster']
    )

  # CLOSE CONNECTION
  neo4j_conn.close()
