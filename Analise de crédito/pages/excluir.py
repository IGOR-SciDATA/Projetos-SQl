import Controllers.ClientController as ClientController
import streamlit as st;


#Função que estrutura pagina para delete de dados no BD
def deletar():
    if "dele" not in st.session_state:
        st.session_state.dele = False

    st.title('Easy Control v1.0 | Deletar')

    if button_delete_select:
        st.session_state.dele = True

    if st.session_state.dele == True:
        item = ClientController.selecionar_id(delete_id)[0]
        st.write(item)
        button_delete = st.button('Deletar')

        if button_delete:
            ClientController.excluir(item[0])
            st.success('Cliente deletado com sucesso!!!')
            st.session_state.dele = False