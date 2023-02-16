import streamlit as st;
import Controllers.ClientController as ClientController
import pandas as pd;
import pages.Inserir as Registrar
import pages.select as Selecionar
import pages.excluir as Deletar
import pages.update as Atualizar

st.sidebar.title('BD Tools 1.0')
page = st.sidebar.selectbox('Empregados',['Registrar','Consultar','Alterar','Excluir'])
st.sidebar.markdown('BD Tools escrito por: Igor Santos')
st.sidebar.markdown('Email para comunicação:')
st.sidebar.markdown('igor.seferino@gmail.com')
st.sidebar.markdown('LinkedIn:')
st.sidebar.markdown('https://www.linkedin.com/in/igor-santos-669907b7/')
st.sidebar.markdown('GitHub:')
st.sidebar.markdown('https://github.com/IGOR-SciDATA')


if page == 'Registrar':
   Registrar.Registro()

if page == 'Consultar':
   Selecionar.Search()

if page == 'Alterar':
   Atualizar.alterar()

if page == 'Excluir':
   Deletar.deletar()