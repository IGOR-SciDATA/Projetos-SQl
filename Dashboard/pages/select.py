import Controllers.ClientController as ClientController
import streamlit as st;

def Search():
  
 st.title('Select Tool v1.4')

 colunas = st.columns((1,2,1,2,1))
 campos = ['ID','Nome','Idade','Profissão','Excluir']
 for coluna, campo in zip(colunas,campos):
        coluna.write(campo)

 for item in ClientController.SelectTodos():
        col1,col2,col3,col4,col5 = st.columns((1,2,1,2,1))
        col1.write(item[0])
        col2.write(item[1])
        col3.write(item[2])
        col4.write(item[3])
        button_excluir = col5.empty()
        on_click_excluir = button_excluir.button('Excluir', 'btnExcluir' + str(item[0]))

        if on_click_excluir:
            ClientController.excluir(item[0])
            st.success('Empregado deletado com sucesso!!!')