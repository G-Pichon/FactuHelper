import numpy as np
import pandas as pd
import streamlit as st

from helper import filter_dataframe

titre_str = "Assistant de Facturation Datatorii"

st.set_page_config(
    page_title=titre_str,
    page_icon="DtrLogoV2Full_Dark.svg",
    layout="centered",
    initial_sidebar_state="auto",
    menu_items=None,
)

st.image("DtrLogoV2Full_Dark.svg", width=150)

st.title(titre_str)

st.header("Comment tomber juste ?")

st.write("Entrez les valeurs en Euros des TJMs des consultants ainsi que la somme totale à facturer.")

st.text_input("Somme à obtenir :", key="total_sum", value=10000)
st.text_input("TJM numero 1 :", key="TJ_1", value=650)
st.text_input("TJM numero 2 :", key="TJ_2", value=750)
st.text_input("TJM numero 3 :", key="TJ_3", value=800)

TJ_1 = int(st.session_state.TJ_1)
TJ_2 = int(st.session_state.TJ_2)
TJ_3 = int(st.session_state.TJ_3)
total_sum = float(st.session_state.total_sum)

# incremental integer
increment = 0.25

TJ_list = [TJ_1, TJ_2, TJ_3]
max_day_sum = 2 * total_sum / (max(TJ_list))

range_vector = np.arange(0, max_day_sum, increment)

mesh_array = np.array(np.meshgrid(range_vector, range_vector, range_vector)).T.reshape(-1, 3)

df_solutions = pd.DataFrame(mesh_array, columns=[f"TJ1 - {TJ_1} €", f"TJ2 - {TJ_2} €", f"TJ3 - {TJ_3} €"])
df_solutions["Total"] = df_solutions.iloc[:, 0] * TJ_1 + df_solutions.iloc[:, 1] * TJ_2 + df_solutions.iloc[:, 2] * TJ_3


st.header("Solutions")

st.write(
    f"Voici les combinaisons possibles. Les colonnes peuvent êtres triées pour minimiser ou maximiser"
    f" certaines prestations. L'incrément est fixé à {increment} jour."
)

st.dataframe(
    filter_dataframe(df_solutions[df_solutions["Total"] == total_sum]), hide_index=True, use_container_width=True
)
