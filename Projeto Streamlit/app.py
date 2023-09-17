import pandas as pd  # pip install pandas openpyxl
import streamlit as st  # pip install streamlit
import altair as alt
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(layout="wide")


@st.cache_data
def generate_df():
    df = pd.read_excel(
        io="database.xlsx",
        engine="openpyxl",
        sheet_name=0,
        usecols="A:F",
        nrows=200,
        skiprows=0,
    )
    return df


# def generate_list():
#     df_list = pd.read_excel(
#         io="database.xlsx",
#         engine="openpyxl",
#         sheet_name=1,
#         usecols="A:B",
#         nrows=6,
#     )
#     return df_list


df = generate_df()
# df_list = generate_list()

with st.sidebar:
    st.subheader("Features MVP Overview")
    logo_test = Image.open("ford.ico")
    st.image(logo_test, use_column_width=True)
    st.subheader("Feature Selection")
    fFeature = st.selectbox("Select a feature:", options=df["Feature"].unique())

    user_choice = df.loc[(df["Feature"] == fFeature)]

# user_choice
st.header("Feature Overview")

st.markdown("**Feature Selected:** " + fFeature)

grafOverTarget = (
    alt.Chart(user_choice)
    .mark_line(point=alt.OverlayMarkDef(color="red", size=20))
    .encode(x="Week", y="Overall Target", strokeWidth=alt.value(3))
    .properties(height=720, width=1080)
)

df_user_choice = pd.DataFrame(user_choice)

# The code `# Dados da tabela` is a comment indicating that the following lines of code are related to
# retrieving data from the table.
# Dados da tabela
feature = df_user_choice.loc[:, "Feature"]
overall_target = df_user_choice.loc[:, "Overall Target"]
overall_status = df_user_choice.loc[:, "Overall Status"]
week_target = df_user_choice.loc[:, "Week Target"]
week_status = df_user_choice.loc[:, "Week Status"]
week = df_user_choice.loc[:, "Week"]

# feature
# overall_target
# overall_status
# week_target
# week_status
# week

# Criar o gráfico
# plt.figure(figsize=(12, 6))
# bar_width = 0.2  # Largura das barras
# index = range(len(week))

# plt.plot(
#     week, overall_target, marker="o", label="Overall Target", linestyle="-", color="b"
# )
# plt.plot(
#     week, overall_status, marker="o", label="Overall Status", linestyle="--", color="g"
# )
# plt.bar(week_target, bar_width, label='Week Target', color='r')
# plt.bar(week_status, bar_width, label='Week Status', color='purple')

# plt.title('Progresso da Feature "Automatic Leveling"')
# plt.xlabel("Semana")
# plt.ylabel("Valor")
# plt.legend()
# plt.grid(True)
# plt.xticks([i + 1.5 * bar_width for i in index], week)
# plt.legend()
# plt.grid(True)
# plt.show()
# grafOverStatus = (
#     alt.Chart(user_choice)
#     .mark_bar()
#     .encode(
#         x="Week",
#         y="Overall Status",

#     )
# )

# grafWeekTarget = (
#     alt.Chart(user_choice)
#     .mark_line(point=alt.OverlayMarkDef(color="red", size=20))
#     .encode(x="Week", y="Week Target", strokeWidth=alt.value(3))

#     )

# grafWeekStatus = alt.Chart(user_choice).mark_bar().encode(
#     x="Week",
#     y="Overall Status",

# )
# st.altair_chart(grafOverTarget+grafOverStatus+grafWeekStatus+grafWeekTarget)
# st.altair_chart(grafOverTarget)


# Dados da tabela
# week = ["W_1", "W_2", "W_3", "W_4", "W_5", "W_6", "W_7", "W_8", "W_9", "W_10", "W_11", "W_12", "W_13", "W_14", "W_15", "W_16", "W_17", "W_18", "W_19", "W_20"]
# overall_target = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
# overall_status = [5, 8, 12, 20, 26, 31, 35, 44, 44, 49, 50, 59, 68, 72, 76, 82, 89, 99, 100, 100]
# week_target = [5] * 20
# week_status = [5] * 20

# # Criar o gráfico
# fig, ax1 = plt.subplots(figsize=(12, 6))

# # Configurar o eixo das barras
# bar_width = 0.4
# index = np.arange(week)                   #np.arange(len(week))

# bar1 = ax1.bar(
#     index - bar_width / 2,
#     week_target,
#     bar_width,
#     label="Week Target",
#     color="r",
#     alpha=0.7,
# )
# bar2 = ax1.bar(
#     index + bar_width / 2,
#     week_status,
#     bar_width,
#     label="Week Status",
#     color="purple",
#     alpha=0.7,
# )

# # Configurar o eixo das linhas
# ax2 = ax1.twinx()
# ax2.plot(overall_target, label="Overall Target", marker="o", linestyle="-", color="b")
# ax2.plot(overall_status, label="Overall Status", marker="o", linestyle="--", color="g")

# # Configurar rótulos e legendas
# ax1.set_xlabel("Semana")
# ax1.set_ylabel("Valor (Week)")
# ax2.set_ylabel("Valor (Overall)")
# plt.title(f'Progresso da Feature {fFeature}')
# plt.xticks(index, week)
# ax1.legend(loc="upper left")
# ax2.legend(loc="upper right")

# plt.grid(True)
# st.pyplot(fig)


# import streamlit as st
# import matplotlib.pyplot as plt
# import numpy as np

# Dados da tabela
# week = ["W_1", "W_2", "W_3", "W_4", "W_5", "W_6", "W_7", "W_8", "W_9", "W_10", "W_11", "W_12", "W_13", "W_14", "W_15", "W_16", "W_17", "W_18", "W_19", "W_20"]
# overall_target = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
# overall_status = [5, 8, 12, 20, 26, 31, 35, 44, 44, 49, 50, 59, 68, 72, 76, 82, 89, 99, 100, 100]
# week_target = [5] * 20
# week_status = [5] * 20

# Criar o gráfico
fig, ax1 = plt.subplots(figsize=(12, 6))

# Configurar o eixo das barras
bar_width = 0.4
index = np.arange(len(week))

bar1 = ax1.bar(
    index - bar_width / 2,
    week_target,
    bar_width,
    label="Week Target",
    color="r",
    alpha=0.7,
)
bar2 = ax1.bar(
    index + bar_width / 2,
    week_status,
    bar_width,
    label="Week Status",
    color="purple",
    alpha=0.7,
)

# Configurar o eixo das linhas
ax2 = ax1.twinx()
ax2.plot(
    week, overall_target, label="Overall Target", marker="o", linestyle="-", color="b"
)
ax2.plot(
    week, overall_status, label="Overall Status", marker="o", linestyle="--", color="g"
)

# Configurar rótulos e legendas
ax1.set_xlabel("Semana")
ax1.set_ylabel("Valor (Week)")
ax2.set_ylabel("Valor (Overall)")
plt.title(f'Progresso da Feature {fFeature}')
plt.xticks(index, week)
ax1.legend(loc="upper left")
ax2.legend(loc="upper right")

plt.grid(True)

# Converter o gráfico Matplotlib em um objeto Streamlit
st.pyplot(fig)
df_user_choice