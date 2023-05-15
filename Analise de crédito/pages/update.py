import Controllers.ClientController as ClientController
import streamlit as st;


# função para a página de alterar dados
def alterar():
    if "upda" not in st.session_state:
        st.session_state.upda = False

    st.title('Easy Control v1.0 | Atualizar')

    update_id = st.number_input(label='Insira o ID do Cliente', format='%d', step=1)
    button_update_select = st.button('Consultar')

    if button_update_select:
        st.session_state.upda = True

    if st.session_state.upda == True:
        item = ClientController.selecionar_id(update_id)[0]
        with st.form(key='update'):
            update_name = st.text_input(label='Insira o Nome', value=item[1])
            update_cpf = st.text_input(label='Insira o CPF', value=item[2])
            update_tel = st.text_input(label='Insira o novo Telefone', value=item[3])
            update_email = st.text_input(label='Insira o novo Email', value=item[4])
            update_sal = st.number_input(label='Insira o novo Salario', value=item[5])
            update_sc = st.text_input(label='Insira o novo Score', value=item[6])
            button_update = st.form_submit_button('Alterar')

            if button_update:
                ClientController.alterar(update_name, update_cpf, update_tel,update_email,update_sal,update_sc, item[0])
                st.success('Cliente alterado com sucesso!!!')
                st.session_state.upda = False