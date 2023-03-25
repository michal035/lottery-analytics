import pandas as pd
import numpy

df = pd.read_csv("the_results/re.csv",sep=';', dtype=str)
df =  df[df['date'].isnull() == False]

duplicated_date = df.duplicated()
df = df[duplicated_date==False]

#df.to_csv("the_results/re2.csv")






def a(df):

    #Just df to save evrything in one place 
    df_results = pd.DataFrame()

    #there is 49 different numbers in the actuallt lottery 
    numbers = [ str(i+1) for i in range(49)]
    

    # we need to loop through those numbers
    for number in numbers:
        counter = 0
        for i in df.columns:
            temp_df = df.loc[df[i] == number]

            """
            if len(temp_df) != 0:
                print(f"{temp_df} \n")
                print(f"{len(temp_df)} {i} \n")
            """

            counter += len(temp_df)

        df_result = pd.DataFrame({number : [counter]})

        df_results = pd.concat([df_results, df_result], axis=1)

    return df_results

        
   




lotto = (df["lotto"]).to_frame()


lotto["numbers"] =  df["lotto"].str.split(" ")



# each number is it's own collumn - I don't think this will be that useful
lotto2 = pd.DataFrame(lotto.lotto.str.split(' ').tolist(),columns = ['1','2','3','4','5','6'])



a(lotto2).to_csv('result.csv')


