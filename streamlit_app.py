from openai import OpenAI
import streamlit as st
import time

client = OpenAI(api_key=st.secrets.OPENAI_API_KEY)
if 'message_thread' not in st.session_state:
    st.session_state['assistant_id'] = st.secrets.assistant_id_3


text_input1 = ""
text_input2 = ""

options = ['Selection', 'Lead Magnet', 'Funnel MARATHON / WEBINAR',
           'Warm-up plan for the product for 5 days', 'Sites',
           'Storyteller']
add_selectbox = st.sidebar.selectbox('What would you like to create?', options)

if add_selectbox != 'Selection':
    # st.write(f'Вы выбрали: {add_selectbox}')
    st.sidebar.markdown("# Fill in the fields")
    text_input1 = st.sidebar.text_area("Product Data")
    text_input2 = st.sidebar.text_area("Target Audience Data")

    if add_selectbox == 'Lead Magnet':
        st.write('Creating Lead Magnet...')
        st.session_state['assistant_id'] = st.secrets.assistant_id_1
    elif add_selectbox == 'Funnel MARATHON / WEBINAR':
        st.write('Creating WEBINAR...')
        st.session_state['assistant_id'] = st.secrets.assistant_id_3
    elif add_selectbox == 'Warm-up plan for the product for 5 days':
        st.write('Creating Warm-up plan...')
        st.session_state['assistant_id'] = st.secrets.assistant_id_3
    elif add_selectbox == 'Sites':
        st.write('Creating Sites...')
        st.session_state['assistant_id'] = st.secrets.assistant_id_4
    elif add_selectbox == 'Storyteller':
        st.write('Creating Storyteller...')
        st.session_state['assistant_id'] = st.secrets.assistant_id_5

prompt = f"Product Data: {text_input1}, Target Audience Data: {text_input2}"

if st.sidebar.button('START'):
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        msg = ""
        if 'message_thread' not in st.session_state:
            st.session_state['message_thread'] = client.beta.threads.create()

        with client.beta.threads.runs.stream(
                thread_id=st.session_state.message_thread.id,
                assistant_id=st.session_state['assistant_id']
        ) as stream:

            for event in stream:
                # Print the text from text delta events
                if event.event == "thread.message.delta" and event.data.delta.content:
                    msg = msg + str(event.data.delta.content[0].text.value)
            response = st.write(msg)

    st.session_state.messages.append({"role": "assistant", "content": response})


# if "openai_model" not in st.session_state:
#     st.session_state["openai_model"] = "gpt-3.5-turbo"

if prompt2 := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt2})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        msg = ""
        with client.beta.threads.runs.stream(
                thread_id=st.session_state.message_thread.id,
                assistant_id=st.session_state['assistant_id']
        ) as stream:
            for event in stream:
                # Print the text from text delta events
                if event.event == "thread.message.delta" and event.data.delta.content:
                    msg = msg + str(event.data.delta.content[0].text.value)
            response2 = st.write(msg)
    st.session_state.messages.append({"role": "assistant", "content": response2})

