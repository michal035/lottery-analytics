import pandas as pd 


main = pd.DataFrame(columns=["a","b"])

a = pd.DataFrame({"a" : [2]})
b = pd.DataFrame({"b" : [3]})


main = pd.concat([main,a])
main = pd.concat([main,b], axis=1)

print(main.columns)

