import Controllers.ClientController as ClientController
import streamlit as st;
import string
import random

#função que gera strings aleatoriamente
def random_generator(size=20, chars=string.ascii_uppercase + string.digits):
 return ''.join(random.choice(chars) for _ in range(size))
value = random_generator()

#Função que cria pagina para Registrar os dados dos campos
def Registro():
 st.title ('ADD Tool v1.5')
 with st.form(key='Include_cliente'):
       input_name = st.text_input(label='Insira o nome do empregado:')
       input_age = st.number_input(label='Idade:',format='%d',step=1)
       input_occupation = st.selectbox(label="Selecione seu emprego",options=('Estagiario','Analista Junior','Analista Senior','Analista Pleno'))
       input_submit_button = st.form_submit_button(label='Cadastrar')
       
 if input_submit_button:       
      ClientController.inserir(0,input_name,input_age,input_occupation)
      st.success('Empregado Cadastrado Com Sucesso!')
