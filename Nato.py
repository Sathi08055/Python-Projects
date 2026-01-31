import pandas as pd
path = r"D:\Sources\Courses\Python\26 - List Comprehension and the NATO Alphabet\011 NATO-alphabet-start\NATO-alphabet-start\nato_phonetic_alphabet.csv"
df = pd.read_csv(path)
df_dict= df.set_index("letter").to_dict()
print(df_dict)
alph_list=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
Name="Sathish"
Nato=[df_dict['code'][char.upper()] for char in Name ]
print(Nato)