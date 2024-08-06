import streamlit as st

options = ['Selection', 'Lead Magnet', 'Unique Selling Proposition (USP)',
           'Warm-up plan for the product for 5 days', 'Sites',
           'Storyteller']
add_selectbox = st.sidebar.selectbox('What would you like to create?', options)

if add_selectbox != 'Selection':
    # st.write(f'Вы выбрали: {add_selectbox}')
    st.sidebar.markdown("# Fill in the fields")
    text_input1 = st.sidebar.text_area("Product Data")
    text_input2 = st.sidebar.text_area("Target Audience Data")

if st.sidebar.button('START'):
    if add_selectbox == 'Selection':
        st.write('Creating Selection...')
    elif add_selectbox == 'Lead Magnet':
        st.write('Creating Lead Magnet...')
    elif add_selectbox == 'Unique Selling Proposition (USP)':
        st.write('Creating USP...')
    elif add_selectbox == 'Warm-up plan for the product for 5 days':
        st.write('Creating Warm-up plan...')
    elif add_selectbox == 'Sites':
        st.write('Creating Sites...')
    elif add_selectbox == 'Storyteller':
        st.write('Creating Storyteller...')

st.title("Echo Bot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = f"Echo: {prompt}"
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
        # st.write_stream(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
