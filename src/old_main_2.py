import pandas as pd
from my_neo4j import MyNeo4j

assets = pd.read_excel('CaseData.xlsx', sheet_name='assets').drop_duplicates()

needs = pd.read_excel('CaseData.xlsx', sheet_name='needs').drop_duplicates()
offers = pd.read_excel('CaseData.xlsx', sheet_name='offers').drop_duplicates()

new_needs = pd.merge(needs, assets, how='left', left_on='asset_name', right_on='AssetName')
new_offers = pd.merge(offers, assets, how='left', left_on='asset_name', right_on='AssetName')

needs_group_ids = list(new_needs['group_id'].unique())

arr = []

my_neo4j = MyNeo4j("bolt://localhost:7687", "neo4j", "deneme123_")

for group_id in [1]:
  needs_rows = new_needs[new_needs['group_id'] == group_id]
  offers_rows = new_offers[new_offers['group_id'] == (group_id + 1)]
  if needs_rows.shape[0] == 0 or offers_rows.shape[0] == 0:
    break
  # print(needs_rows.shape[0], offers_rows.shape[0])

  for need_index, need_row in needs_rows.iterrows():
    matching_df = offers_rows[offers_rows['offer_value'] == need_row['need_value']]
    
    if matching_df.shape[0] > 0:
      print(matching_df.shape[0])

      for index, row in matching_df.iterrows():
        print('need: ', need_row['asset_name'], need_row['need_value'], need_row['group_id'], need_row['AssetType'], need_row['AssetCluster'], 'row: ', row['asset_name'], row['offer_value'], row['group_id'], row['AssetType'], row['AssetCluster'])
        arr.append([[need_row['asset_name'], need_row['AssetType'], need_row['AssetCluster']], [row['asset_name'], row['AssetType'], row['AssetCluster']]])
        my_neo4j.create_relation(
            needs_asset_name=need_row['asset_name'],
            needs_asset_type=need_row['AssetType'],
            needs_asset_cluster=need_row['AssetCluster'],
            offers_asset_name=row['asset_name'],
            offers_asset_type=row['AssetType'],
            offers_asset_cluster=row['AssetCluster']
        )


my_neo4j.close()