import pandas as pd
from src.my_neo4j import MyNeo4j

def create_nodes(df, conn_obj):
  for _, row in df.iterrows():
    conn_obj.create_asset_node(
      asset_name=row['AssetName'],
      asset_type=row['AssetType'],
      asset_cluster=row['AssetCluster']
    )

if __name__ == '__main__':
  ### READ SECTION ###
  assets = pd.read_excel('src/resources/CaseData.xlsx', sheet_name='assets')[['AssetName', 'AssetType', 'AssetCluster']].drop_duplicates()
  needs = pd.read_excel('src/resources/CaseData.xlsx', sheet_name='needs')[['asset_name', 'need_value', 'group_id']].drop_duplicates()
  offers = pd.read_excel('src/resources/CaseData.xlsx', sheet_name='offers')[['asset_name', 'offer_value', 'group_id']].drop_duplicates()
  ### READ SECTION ###

  
  ### JOIN SECTION ###
  new_needs = pd.merge(needs, assets, how='left', left_on='asset_name', right_on='AssetName')
  new_offers = pd.merge(offers, assets, how='left', left_on='asset_name', right_on='AssetName')
  ### JOIN SECTION ###


  ### NEO4j SECTION ###
  my_neo4j = MyNeo4j("bolt://localhost:7687", "neo4j", "test1234?_")
  create_nodes(assets, my_neo4j)
  ### NEO4j SECTION ###

  ### FIND MATHING ASSETS SECTION ###
  needs_group_ids = sorted(list(new_needs['group_id'].unique())) # [1, 2, 3, 4, 5]
  matching_array = []

  for group_id in needs_group_ids:
    needs_rows = new_needs[new_needs['group_id'] == group_id]
    offers_rows = new_offers[new_offers['group_id'] == (group_id + 1)]
    if needs_rows.shape[0] == 0 or offers_rows.shape[0] == 0:
      break
    # print(needs_rows.shape[0], offers_rows.shape[0])

    for _, need_row in needs_rows.iterrows():
      matching_df = offers_rows[offers_rows['offer_value'] == need_row['need_value']]
      
      if matching_df.shape[0] > 0:
        #print(matching_df.shape[0])

        for _, row in matching_df.iterrows():
          #print('need: ', need_row['asset_name'], need_row['need_value'], need_row['group_id'], need_row['AssetType'], need_row['AssetCluster'], 'row: ', row['asset_name'], row['offer_value'], row['group_id'], row['AssetType'], row['AssetCluster'])
          matching_array.append([need_row['asset_name'], need_row['AssetType'], need_row['AssetCluster'], row['asset_name'], row['AssetType'], row['AssetCluster']])
  ### FIND MATHING ASSETS SECTION ###

  df = pd.DataFrame(matching_array, columns=['need_asset_name', 'need_asset_type', 'need_asset_cluster', 'offer_asset_name', 'offer_asset_type', 'offer_asset_cluster'])

  for _, row in df.drop_duplicates().iterrows():
    my_neo4j.create_asset_relation(
              needs_asset_name=row['need_asset_name'],
              needs_asset_type=row['need_asset_type'],
              needs_asset_cluster=row['need_asset_cluster'],
              offers_asset_name=row['offer_asset_name'],
              offers_asset_type=row['offer_asset_type'],
              offers_asset_cluster=row['offer_asset_cluster']
    )


  my_neo4j.close()