import pandas as pd
import numpy


df = pd.read_csv("the_results/re.csv",sep=';', dtype=str)
df =  df[df['date'].isnull() == False]

duplicated_date = df.duplicated()
df = df[duplicated_date==False]

#df.to_csv("the_results/re2.csv")


def main(df):

    #Just df to save evrything in one place 
    df_results = pd.DataFrame({"number" : [], "occurences" : []})

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

        df_result = pd.DataFrame({"number" : [number], "occurences":[counter]})

        df_results = pd.concat([df_results, df_result])

    return df_results


from time import sleep

def how_other_numbers_are_repeated(df):
    
    #Just df to save evrything in one place 
    df_results = pd.DataFrame({"number" : [], "occurences" : []})

    #there is 49 different numbers in the actuallt lottery 
    numbers = [ str(i+1) for i in range(49)]
    

    # we need to loop through those numbers
    col = list(df.columns)
    
    

    for number in numbers:
        counter = 0
        dates_df = pd.DataFrame({"info": []})
        

        for i in col:
            
            temp_df = df.loc[df[i] == number]
            #print(temp_df)
            #dates_df = pd.concat(dates_df,)

            counter += len(temp_df)

        df_result = pd.DataFrame({"number" : [number], "occurences":[counter]})

        df_results = pd.concat([df_results, df_result])

    return df_results



overall_number_of_draws = len(df)
lotto = (df["lotto"]).to_frame()


# each number is it's own collumn - I don't think this will be that useful

list_lotto = df.lotto.str.split(' ').tolist()

for i,j in enumerate(df.date):

    j = (j.split(","))[1]
    list_lotto[i].append(j)



lotto2 = pd.DataFrame(list_lotto,columns = ["date",'1','2','3','4','5','6'])
lotto3 = pd.DataFrame(lotto.lotto.str.split(' ').tolist(), columns = ['1', '2','3','4', '5', '6'])

df = main(lotto3)
sorted = df.sort_values(by=['occurences'], ascending=False)


df2 = how_other_numbers_are_repeated(lotto2)

# Just so i can call this function from another file and get current results 
def data_for_further_processing():
    return overall_number_of_draws, sorted


#print(o_df)

