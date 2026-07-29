# Projeto Luco IA Coder - Assistante de programação em Python

# Importa módulo para interagir com o sistema operacional
import os

# Importa a biblioteca Streamlit para criar a interface web interativa 
import streamlit as st

# Importa a classe Groq para se conectar à API da plataforma Groq e acessar o LLM
from groq import Groq

# Configura a página do Streamlit com título, ícone e layout e estado inicial de sidebar 
st.set_page_config(
    page_title="Luco IA Coder", page_icon=":robot_face:", layout="wide", initial_sidebar_state="expanded"

)

# Define um prompt de sistema que descreve o comportamento do assistente de programação Luco IA Coder
CUSTOM_SYSTEM_PROMPT = """
Você é o Luco IA Coder, um assistente de programação especializado em Python. 

REGRAS DE OPERAÇÃO:

1. **Foco em Programação**: Responda apenas perguntas relacionadas à programação, algortimos, estruturas de dados, depuração de código e boas práticas de desenvolvimento em Python. Evite fornecer informações irrelevantes ou fora do contexto da programação.
2. **Estrutura de Resposta**: Sempre forneça respostas detalhadas, incluindo explicações passo a passo, exemplos de código e referências a documentação oficial quando apropriado. Evite respostas vagas ou superficiais.
3. **Boas Práticas de Programação**: Incentive o uso de boas práticas de programação, como modularidade, legibilidade, testes e documentação. Evite sugerir soluções que comprometam a qualidade do código.
4. **Segurança e Ética**: Não forneça instruções para atividades ilegais, antiéticas ou prejudiciais. Evite compartilhar informações sensíveis ou privadas.
5. **Limitações do Modelo**: Reconheça suas limitações e evite fornecer informações que possam ser imprecisas ou desatualizadas. Sempre que possível, sugira a verificação de fontes confiáveis.
6. **Interatividade**: Incentive o usuário a fornecer detalhes adicionais sobre seu problema ou contexto, para que você possa fornecer respostas mais precisas e úteis. Evite respostas genéricas sem solicitar informações adicionais quando necessário.
7. **Atualização de Conhecimento**: Informe ao usuário que seu conhecimento é baseado em informações disponíveis até setembro de 2021 e que ele deve verificar fontes atualizadas para obter informações mais recentes.
8. **Respeito e Cortesia**: Mantenha um tom respeitoso e cortês em todas as interações. Evite linguagem ofensiva, sarcástica ou desrespeitosa.
9. **Exemplos de Código**: Sempre que possível, forneça exemplos de código claros e funcionais em Python para ilustrar conceitos ou soluções. Evite fornecer exemplos incompletos ou confusos.
10. **Documentação e Referências**: Sempre que possível, forneça links para documentação oficial, tutoriais ou recursos adicionais que possam ajudar o usuário a aprofundar seu conhecimento. Evite fornecer informações sem referências confiáveis.
11. **Feedback e Aprendizado**: Incentive o usuário a fornecer feedback sobre suas respostas e a compartilhar suas experiências de aprendizado. Evite desconsiderar o feedback do usuário ou não reconhecer suas contribuições.
12. **Limite de Resposta**: Evite respostas excessivamente longas ou detalhadas que possam sobrecarregar o usuário. Forneça informações de forma concisa e organizada, destacando os pontos mais importantes.

"""

# Cria uma barra lateral no Streamlit para exibir informações sobre o projeto e o assistente de programação Luco IA Coder
with st.sidebar:

    # Define o título da barra lateral
    st.title("Luco IA Coder")

    # Mostra um texto de boas-vindas e instruções sobre como usar o assistente de programação Luco IA Coder
    st.markdown(
        """
        **Bem-vindo ao Luco IA Coder!** :robot_face:

        Este é um assistente de programação especializado em Python, projetado para ajudá-lo a resolver problemas de codificação, fornecer exemplos de código e compartilhar boas práticas de desenvolvimento.

        **Como usar:**
        1. Digite sua pergunta ou problema relacionado à programação em Python na caixa de entrada.
        2. Clique no botão "Enviar" para receber uma resposta detalhada do Luco IA Coder.
        3. Explore os exemplos de código fornecidos e consulte a documentação oficial quando necessário.

        **Observação:** O conhecimento do Luco IA Coder é baseado em informações disponíveis até setembro de 2021. Verifique fontes atualizadas para obter informações mais recentes.

        **Divirta-se programando!** :sparkles:
        """
    )
    # Campo para inserir a chave de API da Groq, que é necessária para se conectar à API da plataforma Groq e acessar o LLM
    groq_api_key = st.text_input("Insira sua chave de API da Groq", type="password", help="Você pode obter sua chave de API na plataforma Groq. Esta chave é necessária para se conectar à API e acessar o modelo de linguagem. https://platform.groq.com/")

    

#Título principal do app 
st.title("Luco IA Coder") 

# Subtítulo explicativo do app            
st.subheader("Assistente de Programação em Python")

# Inicializa o histórico de mensagens na sessão, caso ainda não exista, para armazenar as interações entre o usuário e o assistente de programação Luco IA Coder
if "messages" not in st.session_state:
    st.session_state.messages = []            

# Exibe o histórico de mensagens anteiriores entre o usuário e o assistente de programação Luco IA Coder, mostrando as mensagens do usuário e as respostas do assistente em ordem cronológica
for message in st.session_state.messages:
    if message["role"] == "user":
        st.markdown(f"**Você:** {message['content']}")
    elif message["role"] == "assistant":
        st.markdown(f"**Luco IA Coder:** {message['content']}")

# Inicializa a variável de entrada do Cliente Groq como None
client = None

# Verifica se a chave de API da Groq foi fornecida pelo usuário e, em caso afirmativo, cria uma instância do cliente Groq usando a chave de API fornecida. Caso contrário, exibe uma mensagem de aviso solicitando que o usuário insira a chave de API para se conectar à API da plataforma Groq e acessar o LLM
if groq_api_key:

    try:
        # Cria cliente groq com a chave de API fornecida pelo usuário, permitindo que o assistente de programação Luco IA Coder se conecte à API da plataforma Groq e acesse o modelo de linguagem para fornecer respostas detalhadas e exemplos de código em Python
        client = Groq(api_key=groq_api_key)

    except Exception as e:
    # Exibe uma mensagem de erro caso ocorra algum problema ao criar o cliente Groq, informando ao usuário que houve um erro ao tentar se conectar à API da plataforma Groq e fornecendo detalhes sobre o erro ocorrido
        st.error(f"Erro ao criar cliente Groq: {e}")    
        st.stop()

# Caso não tenha chave, mas já existam mensagens no histórico, exibe uma mensagem de aviso solicitando que o usuário insira a chave de API para se conectar à API da plataforma Groq e acessar o LLM
elif not groq_api_key and st.session_state.messages:
    st.warning("Por favor, insira sua chave de API da Groq para se conectar à API e acessar o modelo de linguagem.")
    st.stop()

# Captura a entrada do usuário em uma caixa de texto, permitindo que o usuário digite sua pergunta ou problema relacionado à programação em Python para que o assistente de programação Luco IA Coder possa fornecer uma resposta detalhada e exemplos de código
user_input = st.text_area("Digite sua pergunta ou problema relacionado à programação em Python:", height=150)

# Se não houver Cliente válido, exibe uma mensagem de aviso solicitando que o usuário insira a chave de API da Groq para se conectar à API da plataforma Groq e acessar o LLM.
if not client:
    st.warning("Por favor, insira sua chave de API da Groq para se conectar à API e acessar o modelo de linguagem.")
    st.stop()

# Armazena a mensagem do usuário no estado na sessão, permitindo que o histórico de mensagens seja atualizado com a nova entrada do usuário e que o assistente de programação Luco IA Coder possa fornecer uma resposta detalhada e exemplos de código em Python com base na pergunta ou problema fornecido pelo usuário
    st.session_state.messages.append({"role": "user", "content": CUSTOM_SYSTEM_PROMPT})
    for msg in st.session_state.messages:
        messages_for_api.append(msg)

# Cria uma resposta do assistente de programação Luco IA Coder no chat 
with st.chat_message("assistant"):

    with st.spinner("Analisando sua pergunta..."):

        try:
            # Chama a API da plataforma Groq para gerar uma resposta detalhada do assistente de programação Luco IA Coder com base na pergunta ou problema fornecido pelo usuário, incluindo explicações passo a passo, exemplos de código em Python e referências à documentação oficial quando apropriado
            chat_completion = client.chat_completion.create(
                messages = messages_for_api,
                model = "groq-code-llm-v1",
                temperature = 0.2,
                max_tokens = 500,

            )

            # Extrai a resposta gerada pela IA
            assistant_response = chat_completion.choices[0].message.content

            # Exibe a resposta do assistente 
