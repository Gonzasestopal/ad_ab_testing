import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')

utm_source_count = ad_clicks.groupby('utm_source').count().reset_index()

ad_clicks['is_click'] = ~ad_clicks\
   .ad_click_timestamp.isnull()

clicks_by_source = ad_clicks.groupby(['utm_source', 'is_click']).user_id.count().reset_index()

clicks_pivot = clicks_by_source.pivot(
  index='utm_source',
  values='user_id',
  columns='is_click'
).reset_index()

total_users_by_group = ad_clicks.groupby('experimental_group').user_id.count().reset_index()

ab_count = ad_clicks.groupby(['experimental_group', 'is_click']).user_id.count().reset_index()


a_clicks = ad_clicks[ad_clicks.experimental_group == 'A']

b_clicks = ad_clicks[ad_clicks.experimental_group == 'B']

a_clicks_by_day = a_clicks.groupby(['is_click', 'day']).user_id.count().reset_index()

b_clicks_by_day = b_clicks.groupby(['is_click', 'day']).user_id.count().reset_index()

a_clicks_by_day_pivot = a_clicks_by_day.pivot(
  columns='day',
  values='user_id',
  index='is_click',
)

b_clicks_by_day_pivot = b_clicks_by_day.pivot(
  columns='day',
  values='user_id',
  index='is_click',
)

print(a_clicks_by_day_pivot)

print(b_clicks_by_day_pivot)
