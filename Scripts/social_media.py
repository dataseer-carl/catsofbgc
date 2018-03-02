import ig_cats
import twitter_cats
from datetime import datetime as dt
import pandas as pd

hdf = pd.HDFStore('cats_of_bgc.h5')
hdf.open()

ig = hdf['ig']
twitter = hdf['twitter']

twitter['time'] = [
    dt.strptime(
        str(t),
        '%a %b %d %H:%M:%S %z %Y'
    ).strftime('%Y-%m-%d') for t in twitter['time'].tolist()
]


ig['time'] = [
    dt.strptime(
        str(t),
        '%Y-%m-%d %H:%M:%S'
    ).strftime('%Y-%m-%d') for t in ig['time'].tolist()
]

twitter['platform'] = 'tw'
ig['platform'] = 'ig'

main_df = pd.concat([ig, twitter])

main_df.reset_index(drop=True, inplace=True)

with open('main_df.json', 'w') as df:
    df.write(main_df.to_json(orient='index'))
