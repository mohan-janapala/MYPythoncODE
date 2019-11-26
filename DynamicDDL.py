import pandas as pd
import sys

#commenting these two for now
#inputfile_name = input('please enter input file name with complete path')
#oututfile_name = input('please enter output file name with complete path')

tablesdf =  pd.read_csv('C:\\Users\\mrj000f\\Desktop\\HRODS\\tbstructure.txt', sep='|'  , engine='python')
outputfile = open('C:\\Users\\mrj000f\\Desktop\\HRODS\\output.sql', "w")

tables_to_create = tablesdf["ENTITY"].unique()

arr_size = len(tables_to_create)

for x in range(arr_size):
    curr_table_name = tables_to_create[x]
    required_columns = tablesdf[tablesdf.ENTITY == curr_table_name][['ATTRIBUTE','DATA_TYPE']]
    curr_col_len = len(required_columns)
    ret_col = "("
    for y in range(curr_col_len):
        col_nam = required_columns['ATTRIBUTE'].iloc[y]
        dat_typ = required_columns['DATA_TYPE'].iloc[y]
        fin_col = col_nam + "   " + dat_typ + ","
        ret_col = ret_col + " " + fin_col
    ret_col = ret_col[:-1] + ")" + ";"
    ret_col = "create table" + " " +curr_table_name + " " + ret_col
    outputfile.write(ret_col + "\n")
    outputfile.flush()
outputfile.close()