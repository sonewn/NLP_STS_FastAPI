import pandas as pd


rawdf = pd.read_csv('sports_news_data - sports_news_data.csv')
pororo = pd.read_csv('pororo_total_v2.csv')

rawdf.shape[0]
pororo.shape[0]

rawdf.columns
pororo.columns

po = pororo[['TITLE','SUMMARY']]

rawdf.shape[0]

len(po['TITLE'].unique())
unipo = po.drop_duplicates(['TITLE'])
unipo.reset_index(drop=True ,inplace=True)
unipo

rawdf.iloc[[7,8]]['PUBLISH_DT']

rawdf['SUMMARY'] = None
for t , s in zip(unipo['TITLE'],unipo['SUMMARY']):
    idx = rawdf[rawdf.TITLE==t].index
    rawdf.loc[idx, 'SUMMARY'] = s

rawdf[rawdf.SUMMARY.isnull()]['CONTENT']

po[po.TITLE == 'GOAL50 2021 투표하기']
rawdf.to_csv('sportsnews_add_pororo.csv', encoding='utf-8-sig')