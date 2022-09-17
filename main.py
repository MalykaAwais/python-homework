#!/usr/bin/env python
# coding: utf-8

# ## Task no. 1
# 
# <font color='green'>PyBank</font>

# In[4]:


#import modules
import pandas as pd
from pathlib import Path

#set path for file
csvpath = Path("budget_data.csv")

# Read in the CSV as a DataFrame
data_csv = pd.read_csv(csvpath)
data_csv.head()


# In[5]:


#1The total number of months included in the dataset.
data_csv["Profit/Losses"].count()


# In[21]:


Total_Months= data_csv["Profit/Losses"].count()
Total_Months


# In[7]:


#2 The net total amount of Profit/Losses over the entire period.
data_csv["Profit/Losses"].sum()


# In[8]:


NetPnl = data_csv["Profit/Losses"].sum()


# In[9]:


#3 The average of the changes in Profit/Losses over the entire period.
data_csv["Profit/Losses"].mean()


# In[10]:


data_csv["Profit/Losses"].sum()
data_csv['pnl_changes']=data_csv["Profit/Losses"]- data_csv["Profit/Losses"].shift()
data_csv


# In[11]:


Mean_PL= data_csv["pnl_changes"].mean()
Mean_PL


# In[12]:


data_csv["pnl_changes"].max()


# In[32]:


max_difference= data_csv["pnl_changes"].max()
max_difference


# In[13]:


data_csv.loc[data_csv["pnl_changes"] == data_csv["pnl_changes"].max(),'Date']


# In[14]:


data_csv["pnl_changes"].min()


# In[15]:


min_difference= data_csv["pnl_changes"].min()
min_difference


# In[16]:


data_csv.loc[data_csv["pnl_changes"] == data_csv["pnl_changes"].min(),'Date']


# In[34]:


print("Financial Analysis")
print("----------------------")
Total_Months= data_csv["Profit/Losses"].count()
print("Total Months: ",Total_Months)
print(f"Total: ${NetPnl}")
print(f"Average Change: ${Mean_PL}")
print("Greatest Increase in Profits: Feb-2012 $ (", max_difference,")")
print("Greatest Decrease in Profits: Sep-2013 $ (", min_difference,")")


# ## To install the Pretty Table:
# 
# <font color='violet'>python -m pip install -U prettytable</font>

# In[40]:


from prettytable import PrettyTable
myTable = PrettyTable(["Financial Analysis", "Values"])

myTable.add_row(["Total Months", Total_Months])
myTable.add_row(["Net Total Amount", NetPnl])
myTable.add_row(["Average Change", Mean_PL])
myTable.add_row(["Greatest Increase in Profits", max_difference])
myTable.add_row(["Greatest Decrease in Profits", min_difference])

print(myTable)

