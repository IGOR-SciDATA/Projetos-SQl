import streamlit as st;
import Controllers.ClientController as ClientController
import pandas as pd;
import pages.Inserir as Registrar
import pages.select as Consultar
import pages.update as Atualizar

st.sidebar.title('EZ Control System')
page = st.sidebar.selectbox('Clientes',['Registrar','Consultar','Alterar'])
st.sidebar.markdown('EZ Control System escrito por: Igor Santos')
st.sidebar.markdown('LinkedIn:https://www.linkedin.com/in/igor-santos-669907b7/')
st.sidebar.markdown('GitHub:https://github.com/IGOR-SciDATA')


if page == 'Registrar':
   Registrar.Registro()

if page == 'Consultar':
   Consultar.Search()

if page == 'Alterar':
   Atualizar.alterar()