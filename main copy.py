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

  df = pd.merge(new_needs, new_offers, how='inner', left_on='need_value', right_on='offer_value')
  #print(df.loc[df['group_id_x'] + 1 == df['group_id_y']].dtypes)
  df.loc[
    df['group_id_x'] + 1 == df['group_id_y']
  ][
    ['AssetName_x', 'AssetType_x', 'AssetCluster_x', 'AssetName_y', 'AssetType_y', 'AssetCluster_y']
  ].drop_duplicates(ignore_index=True, inplace=True)

  

#  df = pd.DataFrame(matching_array, columns=['need_asset_name', 'need_asset_type', 'need_asset_cluster', 'offer_asset_name', 'offer_asset_type', 'offer_asset_cluster'])
