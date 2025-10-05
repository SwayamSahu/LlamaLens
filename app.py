import streamlit as st
from llama_client import call_llama, extract_text_from_response
from utils import format_json

st.set_page_config(page_title="LlamaLens - AI API Debugger", page_icon="🦙", layout="wide")

st.title("🦙 LlamaLens – AI-Powered API Debugger")
st.write("Paste your API response, log, or error message below. LlamaLens will explain it in plain English and suggest fixes.")

input_data = st.text_area("🔍 Paste your API response or log snippet here:", height=200)

if st.button("Analyze with Llama 🧠"):
    if not input_data.strip():
        st.warning("Please enter a valid API response or log.")
    else:
        with st.spinner("Analyzing..."):
            messages = [
                {"role": "system", "content": "You are an expert API debugger."},
                {"role": "user", "content": f"Explain this API response or error and suggest fixes:\n\n{input_data}"}
            ]
            try:
                response = call_llama(messages)
                output_text = extract_text_from_response(response)
                st.subheader("🧾 Explanation & Suggested Fixes")
                st.write(output_text)
            except Exception as e:
                st.error(f"Error: {e}")
else:
    st.info("Enter your API response above and click **Analyze**.")
