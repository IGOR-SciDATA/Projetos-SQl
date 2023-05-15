import Controllers.ClientController as ClientController
import streamlit as st;

def Search():
  
 st.title('Easy Control v1.0 | Consulta')

 colunas = st.columns((1,2,1,2,1,2,1))
 campos = ['ID','Nome','CPF','Email','Salario','Score','Excluir']
 for coluna, campo in zip(colunas,campos):
        coluna.write(campo)

 for item in ClientController.SelectTodos():
        col1,col2,col3,col4,col5,col6,col7 = st.columns((1,2,1,2,1,2,1))
        col1.write(item[0])
        col2.write(item[1])
        col3.write(item[2])
        col4.write(item[4])
        col5.write(item[5])
        col6.write(item[6])
        button_excluir = col7.empty()
        on_click_excluir = button_excluir.button('X', 'btnExcluir' + str(item[0]))

        if on_click_excluir:
            ClientController.excluir(item[0])
            st.success('Cliente deletado com sucesso!!!')