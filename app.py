import streamlit as st
from deep_translator import MyMemoryTranslator
st.title("Language Translator Tool")
st.write("Translator text from one language to another.")
text = st.text_area("Enter text  to translate")
source = st.selectbox("Translate from",["English", "Hindi", "French", "spanish"])
target = st.selectbox("translate to", ["Hindi", "English", "French", "Spanish" ])
if st.button("Translate"):
    if text.strip():
        result = MyMemoryTranslator(source=source.lower(),target=target.lower()).translate(text)
        st.subheader("Translation")
        st.write(result)
    else:
        st.write("please enter some text to translate.")