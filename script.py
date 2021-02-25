'''
Generate an alphabatized report of artists names and the alphabatized tags associated with their works.

For example, an artist with three tags should be formatted as follows:
ARTIST: TAG1, TAG2, TAG3

If an artists has no tags associated with their works, omit them from the report.
'''

import pandas as pd
import numpy as np

url = 'https://raw.githubusercontent.com/ecds/intro-to-python/main/MetObjects1000.csv'

data = pd.read_csv(url)
data = data.replace(np.nan, '', regex=True)
data = data.astype(str)

artist_dict = {}
for index, row in data.iterrows():
    artists = row['Artist Display Name']
    tags = row['Tags']

    artists = artists.split('|')
    tags = tags.split('|')

    for artist in artists:
        if artist not in artist_dict.keys():
            artist_dict[artist] = tags
        else:
            artist_dict[artist].extend(tags)

for artist in sorted(artist_dict.keys()):
    if artist != '':
        tags = [x for x in artist_dict[artist] if x != '']
        tags = list(set(tags))
        tags = sorted(tags)
        if len(tags) > 0:
            print(artist + ': ' + ', '.join(tags))
