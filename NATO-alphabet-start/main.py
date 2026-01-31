import pandas as pd
path=r"D:\Sources\Obsidian\Python\Projects\NATO-alphabet-start\nato_phonetic_alphabet.csv"
df=pd.read_csv(path)
new_df=df.set_index("letter")
name=str(input("What is your name?\n")).upper()
name_list=list(name)
c=df["letter"].to_list()
nato_list=[]
for n in name_list:
    if n in c:
        a=new_df.loc[n,"code"]
        nato_list.append(a)
    else:
        raise TypeError(f"{n} is not a alphabet")
print(nato_list)
