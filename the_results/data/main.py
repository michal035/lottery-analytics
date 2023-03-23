import pandas as pd


df = pd.read_csv("the_results/re.csv",sep=';', dtype=str)
df =  df[df['date'].isnull() == False]

duplicated_date = df.duplicated()
df = df[duplicated_date==False]

df.to_csv("the_results/re2.csv")


def a(df):
    #there is 49 numbers
    #for i in range(48):
    
    counter = 0
    for i in df.columns:
        temp_df = df.loc[df[i] == '24']

        if len(temp_df) != 0:
            print(f"{temp_df} \n")
            print(f"{len(temp_df)} {i} \n")

        counter += len(temp_df)


    print(counter)
   

def b(df):
     for i in df.columns:
         print(df[i])


lotto = (df["lotto"]).to_frame()


lotto["numbers"] =  df["lotto"].str.split(" ")



# each number is it's own collumn - I don't think this will be that useful
lotto2 = pd.DataFrame(lotto.lotto.str.split(' ').tolist(),columns = ['1','2','3','4','5','6'])



a(lotto2)



#Alternative might be useful later ig 
#b(lotto2)

