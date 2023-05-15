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
 st.title ('Easy Control v1.0 | Cadastro')
 with st.form(key='Include_cliente'):
       input_name = st.text_input(label='Insira seu nome completo:')
       input_cpf = st.text_input(label='Insira seu número de CPF:')
       input_tel = st.text_input(label='Insira seu número de telefone:')
       input_email = st.text_input(label='Insira seu email:')
       input_salario = st.text_input(label='Insira o valor de seu salário:')
       input_score = st.text_input(label='Insira seu Score Serasa/Boa Vista:')
       input_submit_button = st.form_submit_button(label='Cadastrar')
       
 if input_submit_button:       
      ClientController.inserir(0,input_name,input_cpf,input_tel,input_email,
                                     input_salario,input_score)
      st.success('Cliente Cadastrado Com Sucesso!')
