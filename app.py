import sys
import numpy as np
import pandas as pd
import streamlit as st

st.text_input("TJM numero 1", key="TJ_1",value=650)
st.text_input("TJM numero 2", key="TJ_2",value=750)
st.text_input("TJM numero 3", key="TJ_3",value=800)
#st.text_input("Somme totale à moduler", key="total_sum",value=1500)

total_sum = st.slider("Somme totale à moduler", min_value=0, max_value=100000,step=25)

TJ_1 = int(st.session_state.TJ_1)
TJ_2 = int(st.session_state.TJ_2)
TJ_3 = int(st.session_state.TJ_3)

# incremental integer 
increment = 0.25

TJ_list = [TJ_1,TJ_2,TJ_3]
max_day_sum = 2*total_sum/(max(TJ_list))

range_vector = np.arange(0,max_day_sum,increment)

mesh_array = np.array(np.meshgrid(range_vector,range_vector,range_vector)).T.reshape(-1,3)

df_solutions = pd.DataFrame(mesh_array,columns=[f"TJ1 - {TJ_1} €",f"TJ2 - {TJ_2} €",f"TJ3 - {TJ_3} €"])
df_solutions["Total"]=df_solutions.iloc[:, 0]*TJ_1 + df_solutions.iloc[:, 1]*TJ_2 + df_solutions.iloc[:, 2]*TJ_3

st.dataframe(df_solutions[df_solutions["Total"]==total_sum])



# # Intput
# TJ_1 = 675
# TJ_2 = 1000
# TJ_3 = 900
# total_sum = 4200

#total_sum = int(st.session_state.total_sum)

# df_solutions[df_solutions["NUM_Solution"]==total_sum].sort_values(by = ["NUM_Range_1","NUM_Range_2","NUM_Range_3"]).iloc[0]


# raw_order_one = df_solutions[df_solutions["NUM_Solution"]==total_sum].sort_values(by = ["NUM_Range_1","NUM_Range_2","NUM_Range_3"]).iloc[0]
# raw_order_two = df_solutions[df_solutions["NUM_Solution"]==total_sum].sort_values(by = ["NUM_Range_2","NUM_Range_1","NUM_Range_3"]).iloc[0]
# raw_order_three = df_solutions[df_solutions["NUM_Solution"]==total_sum].sort_values(by = ["NUM_Range_3","NUM_Range_2","NUM_Range_1"]).iloc[0]


# st.write(f"Solution 1 : {TJ_1}x{raw_order_one.NUM_Range_1} + {TJ_2}x{raw_order_one.NUM_Range_2} + {TJ_3}x{raw_order_one.NUM_Range_3} = {total_sum}")
# st.write(f"Solution 2 : {TJ_1}x{raw_order_two.NUM_Range_1} + {TJ_2}x{raw_order_two.NUM_Range_2} + {TJ_3}x{raw_order_two.NUM_Range_3} = {total_sum}")
# st.write(f"Solution 2 : {TJ_1}x{raw_order_three.NUM_Range_1} + {TJ_2}x{raw_order_three.NUM_Range_2} + {TJ_3}x{raw_order_three.NUM_Range_3} = {total_sum}")

# st.write(df_solutions[df_solutions["NUM_Solution"]==total_sum].iloc[0])


