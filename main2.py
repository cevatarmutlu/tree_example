import pandas as pd
from src.my_neo4j import MyNeo4j

class Asset:
  
  def __init__(self, name, type, cluster) -> None:
    self.name = name
    self.type = type
    self.cluster = cluster
    self.enter = []
    self.out = []


#assets = pd.read_excel('src/resources/CaseData.xlsx', sheet_name='assets')[['AssetName', 'AssetType', 'AssetCluster']].drop_duplicates()
#needs = pd.read_excel('src/resources/CaseData.xlsx', sheet_name='needs')[['asset_name', 'need_value', 'group_id']].drop_duplicates(ignore_index=True)
offers = pd.read_excel('src/resources/CaseData.xlsx', sheet_name='offers')
print(offers)
offers = offers.loc[offers['group_id'] != '1']
print(offers.loc[offers['group_id'] != '1'])
