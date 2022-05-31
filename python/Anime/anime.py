from itertools import cycle
import numpy as np
import pandas as pd
from datetime import date
import re
import matplotlib.pyplot as plt



MONTH_NAMES = {'Jan' : 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}
class badDate():
    def __init__(self, year = '????', month='??', day='??'):
        self.year = year
        self.month = month
        self.day = day

    def getDate(self):
        return date(
                int(self.year) if not ('?' in self.year) else 1970,
                MONTH_NAMES[self.month] if not ('?' in self.month) else 1, 
                int(self.day) if not ('?' in self.day) else 1 
            )

    def __repr__(self):
        return f'{self.month} {self.day}, {self.year}'

    def isMissing(self):
        return ('?' in self.year) or ('?' in self.month) or ('?' in self.day)


dateRe = '([\?\w]{3}) ([\?\d]{1,2}), ([\d\?]{4})'
def parseBadDate(x):
    if(pd.notna(x)):
        match = re.search(dateRe, x)
        if(match):
            g = match.groups()
            return badDate(year=g[2], month=g[0], day=g[1])
        else:
            print('Nomatch', x)
            return badDate()
    else:
        return badDate()

def getTagCounts(column: pd.Series):
    tags = list(set(sum(column.values.tolist(), [])))
    column = column.map(lambda x: ", ".join(x))

    return pd.Series({
        tag:  column[ column.str.contains(tag) ].count() for tag in sorted(tags)
    }) #mappign each tag to its count and returning as Series

infoOut = '''
Title: str(unicue)
Prod.: str(category nominal)
Episodes: int(discrete)
Source: str(cathegorical nominal)
Genre: str(cathegorical nominal)
Airdate: str(converted to datetime obj.) (discrete)
Rating: float(continous)
Voters: int(discrete)
Theme: tuple(nominals)
'''

infoMissing = '''
Title: no missing
Production: missing values, replaced by "-", grouped into one group
Episodes: missing values, replaced by NaN
Source: missing values, replaced by "-", grouped into one group
Genre: no missing values
Airdate: missing values, saved as "??? ??, ????" badDate objects
Rating: missing values, saves as nan, not counted in grades
Voters: no missing values 
Theme: missing values, replaced by "-", grouped into one group
'''


def main(doTask=[], doGraph=[]):
    out = open('.\output.txt', 'w', encoding="iso-8859-1")
    headersSM = ["Title","Production","Episodes","Source","Genre","Airdate","Rating","Voters","Theme"]
    anime = pd.read_csv('./anime.csv', names=headersSM, sep=',', encoding='ISO-8859-1')[1:]

    # 4
    # if 4 in doTask:
    anime.columns = [x.lower() for x in headersSM]

    # anime.astype({"title": str, "production": str, "episodes": int, "source": str, "genre": str, "airdate": str, "rating": float, "voters": str, "theme": str})
    
    anime["episodes"] = anime["episodes"].map(lambda x: int(x) if x != '?' else -1 )
    anime["rating"] = anime["rating"].map(lambda x: float(x))
    anime["voters"] = anime["voters"].map(lambda x: int(x.replace(',','')))
    anime["airdate"] = anime["airdate"].map( lambda x: parseBadDate(x) )
    anime["theme"] = anime["theme"].map(lambda x: x.split(','))
    anime["genre"] = anime["genre"].map(lambda x: x.split(','))
    # anime["source"] = anime["source"].map(lambda x: 'Diomedea' if 'Г©' in x else x.split(','))
    # anime["production"] = anime["production"].map(lambda x: x.split(','))

    pd.set_option('display.max_columns', None) 

    # 2
    if 2 in doTask:
        out.write(anime.head(10).to_string())
        out.write('\n')
    # 3
    if 3 in doTask:
        out.write(infoOut)
        out.write('\n')

    # 5
    if 5 in doTask:
        numDesc = [ 
            f"\t{column}\n" + anime[column.lower()].describe()[1:].to_string() 
            for column in ['Episodes', 'Rating', 'Voters'] 
        ]
        for val in numDesc:
            out.write(val)
            out.write('\n\n')
    
    # 6
    themesTagsCount = getTagCounts( anime['theme'])
    if 6 in doTask:
        out.write('\tGenre\n')
        out.write( getTagCounts( anime['genre']).to_string() )
        out.write('\n\n\tTheme\n')
        out.write( themesTagsCount.to_string() )
        out.write('\n\n\tProduction\n')
        out.write( anime["production"].value_counts().to_string() )
        out.write('\n\n\tSource\n')
        out.write( anime["source"].value_counts().to_string() )
        out.write('\n')

    # 7
    if 7 in doTask:
        out.write(infoMissing)
        out.write('\n')

    # 8
    #   8.a
    if 8 in doTask:
        prodToNum = anime["production"].value_counts().sort_values(ascending=True)
        keysPN = prodToNum.keys()
        valsPN = prodToNum.values
        if(1 in doGraph):
            plt.title('Number of releases by company')
            plt.bar( range(len(keysPN)), valsPN, width=0.9 )
            plt.xlabel("Company name")
            plt.ylabel("Number of titles")
            plt.show()
        out.write(f'Most releases: "{keysPN[-1]}" with {valsPN[-1]} title\n')
        out.write(f'Least releases: "{keysPN[0]}" with {valsPN[0]} title\n')
        #   8.b
        titleToEpisodes = anime[['title', 'episodes']].groupby(['episodes']).count()
        keysTE = titleToEpisodes.index.to_list()
        if -1 in keysTE:
            keysTE[ keysTE.index(-1) ] = '?'
        valsTE = titleToEpisodes['title'].tolist()
        if(2 in doGraph):
            plt.bar( range(len(keysTE)), valsTE, align='center', width=0.9)
            spaces = cycle(['', '|\n'])
            # plt.xticks(range(0, len(keysTE)), keysTE, rotation=45)
            plt.xticks(range(len(keysTE)), [f'{next(spaces)}{label}' for label in keysTE])
            plt.xlabel("Number of episodes")
            plt.ylabel("Number of titles")
            plt.title('Number of titles with same amount of episodes')
            plt.show()
        out.write(f'Most common number of episodes: {titleToEpisodes.idxmax().values[0]}\n')
        #   8.c
        sourceToPopular = anime[['source', 'title']].groupby(['source']).count().sort_values(by=['title'], ascending=False)[:3]
        keysSP = sourceToPopular.index.to_list()
        valsSP = sourceToPopular['title'].tolist()
        if(3 in doGraph):
            plt.bar( range(3), valsSP, width=0.9 )
            plt.title('Number of titles by source')
            plt.xticks(range(3), keysSP)
            plt.show()
        out.write(f'Most popular source: "{keysSP[0]}"\n')
        #   8.d
        # counts are already calculated in # 6
        popularThemes = themesTagsCount.sort_values()
        keysPT = popularThemes.index.to_list()
        valsPT = popularThemes.values.tolist()
        if(4 in doGraph):
            plt.bar( range(len(keysPT)), valsPT, align='center', width=0.9)
            plt.title('Number of titles by theme (overlaps)')
            spaces = cycle(['', '\n', '\n\n', '\n\n\n'])
            plt.xlim([-1, len(keysPT) +1])
            plt.xticks(range(len(keysPT)), keysPT, rotation=90)
            plt.show()
        out.write(f'Most popular theme: "{keysSP[-1]}"\n')
        #   8.e
        tempSlice = anime['airdate'].map(lambda x: x.year)
        titlesToYear = tempSlice.value_counts()
        keysTY = titlesToYear.index.to_list()
        valsTY = titlesToYear.values.tolist()
        if(5 in doGraph):
            plt.bar( range(len(keysTY)), valsTY, align='center', width=0.9)
            plt.title('Number of titles by years')
            plt.xlim([-1, len(keysTY) +1])
            plt.xticks(range(len(keysTY)), keysTY, rotation=45)
            plt.show()
        out.write(f'Most releasive year: "{keysTY[0]}"\n')

    if 9 in doTask:
        rMeans = anime[['production', 'rating']].groupby(['production'])['rating'].mean().sort_values(ascending=False)
        keysRM = rMeans.index.to_list()
        valsRM = rMeans.values.tolist()

        if(9 in doGraph):
            plt.bar( range(len(keysRM)), valsRM, align='center', width=0.7)
            plt.title('Average rating for companie\'s amine')
            plt.xticks(range(len(keysRM)), keysRM, rotation=90)
            plt.xlim([-1, len(valsRM) +1])
            plt.show()
        
        out.write(f'''Most popular anime companies: { ', '.join( ['"%s"' % comp for comp in keysRM[:3]] ) } \n''')
    

    if 10 in doTask:
        rIntervals = anime['rating'].groupby( pd.cut( anime["rating"], np.arange(0, 11, 1), right=False) ).count()
        keysRI = rIntervals.index.to_list()
        valsRI = rIntervals.values.tolist()
        if(10 in doGraph):
            plt.bar( range(len(keysRI)), valsRI, align='center', width=0.9)
            plt.title('Average rating for companie\'s amine')
            plt.xticks(range(len(keysRI)), keysRI )
            plt.xlim([-1, len(valsRI) +1])
            plt.show()

        out.write(f'Most often ratings: { rIntervals.idxmax() } \n\n')

    if 11 in doTask:
        slice = anime[["rating", "genre", 'theme']].dropna(axis=0)
        slice['genre'] = slice['genre'].map(lambda x: ', '.join(x))
        slice['theme'] = slice['theme'].map(lambda x: ', '.join(x))

        genres = list(set( sum(anime['genre'].values.tolist(), []) ))
        themes = list(set( sum(anime['theme'].values.tolist(), []) ))

        data = [
            [0] * len(themes)
            for _ in range(len(genres))
        ]
        for g in range(len(genres)):
            for t in range(len(themes)):
                mean = slice.loc[( slice['theme'].str.contains(themes[t]) ) & ( slice['genre'].str.contains(genres[g]) )]['rating'].mean()
                data[g][t] = mean if pd.notna(mean) else 0

        df = pd.DataFrame(data, columns=themes, index=genres)
        out.write('\tMean rating value for each (genre, theme) pair\n')
        out.write(df.to_string())
        
    if 12 in doTask:
        plt.plot(anime['voters'], anime['rating'])
        plt.title('Correlation: Voters/Rating')
        plt.xlabel('Voters')
        plt.ylabel('Rating')

        plt.show()
    out.close()

if __name__ == '__main__':
    main(doTask=[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], doGraph=[1, 2, 3, 4, 5, 9, 10])