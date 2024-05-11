# streamlit run web.py

import streamlit as st

from main import create_chat


###########

@st.cache_resource
def get_gemini_chat():
    print('pop cache')
    return create_chat()

CHAT = get_gemini_chat()


############


st.title("Descubra os cursos da Alura!")

if 'messages' not in st.session_state:
    st.session_state.messages = []
    st.write('Inicializando... um momento.')
    resp = CHAT.send_message('Voce poderia me ajudar a escolher um curso?')
    st.session_state.messages.append({'role': 'assistant', 'content': resp.text})


for message in st.session_state.messages:
    with st.chat_message(message['role']):
        st.markdown(message['content'])

prompt = st.chat_input("Resposta:")
if prompt:
    with st.chat_message("user"): # "assistant"
        st.markdown(prompt)
    st.session_state.messages.append({'role': 'user', 'content': prompt})

    resp = CHAT.send_message(prompt)
    with st.chat_message("assistant"):
        st.markdown(resp.text)
    st.session_state.messages.append(
        {'role': 'assistant', 'content': resp.text})


