import pandas as pd
import time
import os
import gc
os.system("cls")
path = os.getcwd()

subpath = path + "/csv/sub"
sublist = []
for file in os.listdir(subpath):
    if os.path.isfile(os.path.join(subpath, file)):
        sublist.append(subpath + "/" + file)

for f in sublist:   
    os.remove(f)

csvpath = path+"/csv"

filelist = []
for file in os.listdir(csvpath):
    if os.path.isfile(os.path.join(csvpath, file)):
        filelist.append(csvpath + "/" + file)


# for f in filelist:
#     print(f)

# print("--------------------------------------------")

df0 = pd.read_csv(filelist[0])
for i in range(len(filelist)):
    if (i >= 1):
        df1 = pd.read_csv(filelist[i])        
        df0 = pd.concat([df0, df1])

df = df0.sort_values('Ticker')
df[~df.duplicated(subset=['Ticker'])].to_csv(
    path+'/csv/merge.csv', index=False)

df1 = df[~df.duplicated(subset=['Ticker'])]

length = df1.shape[0]
inc = 100
q = length//inc      # quotient   5//3 =1
r = length % inc     # remainder  5%3  =2
for i in range(q):
    f = path + "/csv/sub/" + str(i) + ".csv"
    print(f)
    df1.iloc[0+inc*i:inc*(i+1), :].to_csv(f, index=False)  # print(df1.iloc[0:  10,  :])

f = path + "/csv/sub/" + str(q) + ".csv"
df1.iloc[inc*q:inc*q+r, :].to_csv(f, index=False)        # print(df1.iloc[10: 20,  :])
print(f)

gc.collect()
del df0
del df1
del df
print("-----Merge Finished------")
print("wait for 2 seconds")
time.sleep(2)
