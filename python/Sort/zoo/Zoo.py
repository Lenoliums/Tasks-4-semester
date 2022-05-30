import pandas as pd

if __name__ == '__main__':
    headersSM = ["ID","type", "gender", "nickname", "date_of_birth", "date_to_zoo"]
    animals = pd.read_csv('./input.txt', names=headersSM, sep=' ')
    animals_male = animals.loc[(animals["gender"] == "male"), ["type"]].drop_duplicates()
    animals_female = animals.loc[(animals["gender"] == "female"), ["type"]].drop_duplicates()
    anim_pair = pd.merge(animals_male, animals_female, on="type", how='inner')
    if anim_pair.empty:
        print(0)
    else:
        print(*[x[0] for x in anim_pair.reindex(anim_pair.type.str.len().sort_values().index).values], sep='\n')
    
    animals_amount = animals["type"].value_counts().rename_axis("type").reset_index(name='Amount')
    print(*[f'{x[0]} - {x[1]}' for x in animals_amount.values], sep='\n')