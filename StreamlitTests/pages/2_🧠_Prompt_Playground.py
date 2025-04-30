import streamlit as st
from openai import OpenAI
import os

st.set_page_config(
    page_title="Prompt Playground",
    page_icon="🧠",
)

client = OpenAI(api_key="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")

st.title("🧠 Prompt Playground")
st.divider()
st.sidebar.title("Prompt Playground")
st.sidebar.markdown("Simple OpenAI API key web app for generating images or completing text prompts")
st.sidebar.divider()
# Input fields
prompt = st.text_area("Enter your prompt:", height=75)
temperature = st.slider("Temperature:", 0.0, 1.0, 0.7)
max_tokens = st.slider("Max tokens,", 10, 1000, 350)

task_type = st.radio("Select task type:", ["Text Completion", "Image Generation"])

if st.button("Run Prompt"):
    if not prompt.strip():
        st.warning("Please enter a prompt.")
    else:
        with st.spinner("Processings..."):
            try:
                if task_type == "Text Completion":
                    response = client.chat.completions.create(
                        model = "gpt-3.5-turbo",
                        messages = [
                            {"role": "user", "content": prompt}
                        ],
                        temperature = temperature,
                        max_tokens = max_tokens,
                    )
                    st.divider()
                    st.subheader("Response:")
                    st.write(response.choices[0].message.content.strip())
                elif task_type == "Image Generation":
                    response = client.images.generate(
                        model = "dall-e-2",
                        prompt=prompt,
                        n=1,
                        size="256x256",
                    )
                    st.divider()
                    st.subheader("Generated Image:")
                    st.image(response.data[0].url, caption="Generated Image", use_container_width=True)
            except Exception as e:
                st.error(f"Error: {e}")