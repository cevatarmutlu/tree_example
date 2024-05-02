import pandas as pd

assets = pd.read_excel('CaseData.xlsx', sheet_name='assets').drop_duplicates()

needs = pd.read_excel('CaseData.xlsx', sheet_name='needs').drop_duplicates()
offers = pd.read_excel('CaseData.xlsx', sheet_name='offers').drop_duplicates()

needs_group_ids = list(needs['group_id'].unique())


for group_id in needs_group_ids:
  needs_rows = needs[needs['group_id'] == group_id]
  offers_rows = offers[offers['group_id'] == (group_id + 1)]
  # print(needs_rows.shape[0], offers_rows.shape[0])
  if needs_rows.shape[0] == 0 or offers_rows.shape[0] == 0:
    break

  for need_index, need_row in needs_rows.iterrows():
    matching_df = offers_rows[offers_rows['offer_value'] == need_row['need_value']]
    
    if matching_df.shape[0] > 0:
      # print(matching_df.shape[0])

      for index, row in matching_df.iterrows():
        print('need: ', need_row['asset_name'], need_row['need_value'], need_row['group_id'], 'row: ', row['asset_name'], row['offer_value'], row['group_id'])
        print(assets[assets['AssetName'] == need_row['asset_name']])
        print(assets[assets['AssetName'] == row['asset_name']])
    


