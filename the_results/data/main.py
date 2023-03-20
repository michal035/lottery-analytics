import pandas as pd


df = pd.read_csv("the_results/re.csv",sep=';', dtype=str)
df =  df[df['date'].isnull() == False]

duplicated_date = df.duplicated()
df = df[duplicated_date==False]




def duplicates(df):
    collumn_name = list(df.columns)[0]
    for i in df[collumn_name]:
        pass
        


lotto = (df["lotto"]).to_frame()
#duplicates(lotto)

lotto["numbers"] =  df["lotto"].str.split(" ")
print(lotto)


# each number is it's own collumn - I don't think this will be that useful
#lotto = pd.DataFrame(lotto.lotto.str.split(' ').tolist(),columns = ['1','2','3','4','5','6'])

