#%%
import locale as lc
import pandas as pd

lc.setlocale(category=lc.LC_ALL, locale="pt_BR.UTF-8")
# pd.set_option("display.max_columns", None)

df_acessos = pd.read_csv("./bases/acessos.csv.zip", delimiter=";", compression="zip")
df_acessos["hora_acesso"] = pd.to_datetime(df_acessos["hora_acesso"])
#  #   Column                Non-Null Count    Dtype
# ---  ------                --------------    -----
#  0   hash_usuario          1048575 non-null  object
#  1   pagina_acessada       1048575 non-null  object
#  2   hora_acesso           1048575 non-null  datetime64[ns]
#  3   info_dispositivo      1048575 non-null  object
#  4   cidade                1048575 non-null  object
#  5   pais                  1048575 non-null  object
#  6   identificador_visita  1048575 non-null  object

df_matriculas = pd.read_csv("./bases/consulta_matriculas.csv")
#  #   Column        Non-Null Count  Dtype
# ---  ------        --------------  -----
#  0   matricula     90499 non-null  object
#  1   hash_usuario  90499 non-null  object
#  2   produto       90499 non-null  object

#%%
respostas: dict[str: list[int | float | str]] = {"id_resposta": [], "resposta": []}

resposta01: str = df_matriculas[df_matriculas["matricula"].eq("F8719981")]["hash_usuario"].values[0]
respostas["id_resposta"].append("resposta01")
respostas["resposta"].append(resposta01)

#%%
resposta02: int = df_acessos[df_acessos["hash_usuario"].eq(resposta01)]["hash_usuario"].value_counts().values[0]
respostas["id_resposta"].append("resposta02")
respostas["resposta"].append(resposta02)

#%%
resposta03: str = (df_acessos[df_acessos["hash_usuario"].eq(resposta01)]["hora_acesso"].iloc[0]).strftime("%x")
respostas["id_resposta"].append("resposta03")
respostas["resposta"].append(resposta03)

#%%
resposta04: str = (df_acessos[df_acessos["hash_usuario"].eq(resposta01)]["hora_acesso"].iloc[-1]).strftime("%x")
respostas["id_resposta"].append("resposta04")
respostas["resposta"].append(resposta04)

#%%
resposta05: int = df_acessos[df_acessos["hash_usuario"].eq(resposta01)]["pagina_acessada"].value_counts().reset_index()["index"].iloc[0]
respostas["id_resposta"].append("resposta05")
respostas["resposta"].append(resposta05)

#%%
resposta06: int = df_acessos[df_acessos["hash_usuario"].eq(resposta01)]["info_dispositivo"].value_counts().reset_index()["index"].iloc[0]
respostas["id_resposta"].append("resposta06")
respostas["resposta"].append(resposta06)

#%%
resposta07: int = df_acessos[df_acessos["hash_usuario"].eq(resposta01)]["cidade"].value_counts().reset_index()["index"].iloc[0]
respostas["id_resposta"].append("resposta07")
respostas["resposta"].append(resposta07)

#%%
resposta08: int = df_acessos[df_acessos["hash_usuario"].eq(resposta01)]["pais"].value_counts().reset_index()["index"].iloc[0]
respostas["id_resposta"].append("resposta08")
respostas["resposta"].append(resposta08)

#%%
resposta09 = df_acessos[df_acessos["hash_usuario"].eq(resposta01)].copy()
resposta09["hora_acesso"] = pd.to_datetime(resposta09["hora_acesso"].dt.strftime("%x"), format="%x")
resposta09 = resposta09[["hora_acesso", "pais"]].value_counts().reset_index().iloc[0,-1]
respostas["id_resposta"].append("resposta09")
respostas["resposta"].append(resposta09)

#%%
df = pd.DataFrame(respostas)
print(df)
# df.to_csv("./bases/F8719981_v1_wa.csv", header=True, index=False)
