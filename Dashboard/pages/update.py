import Controllers.ClientController as ClientController
import streamlit as st;


# função para a página de alterar dados
def alterar():
    if "upda" not in st.session_state:
        st.session_state.upda = False

    st.title('Update Tool v1.0')
    emprego = ['Estagiario','Analista Junior','Analista Senior','Analista Pleno']

    update_id = st.number_input(label='Insira o ID do Empregado', format='%d', step=1)
    button_update_select = st.button('Consultar')

    if button_update_select:
        st.session_state.upda = True

    if st.session_state.upda == True:
        item = ClientController.selecionar_id(update_id)[0]
        with st.form(key='update'):
            update_name = st.text_input(label='Insira o nome', value=item[1])
            update_age = st.number_input(label='Insira a idade', format='%d', step=1, value=item[2])
            update_job = st.selectbox(label='Insira o emprego',
                                     options=emprego,
                                     index=emprego.index(item[3]))
            button_update = st.form_submit_button('Alterar')

            if button_update:
                ClientController.alterar(update_name, update_age, update_job, item[0])
                st.success('Empregado alterado com sucesso!!!')
                st.session_state.upda = False