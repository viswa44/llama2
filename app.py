import streamlit as st
form langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

def getllamaresponse(input_text,no_words,blog_style):
    


st.set_page_config(page_title="Generate Blogs",
                   page_icon ='**V***',
                   layout='centered',
                   initial_sidebar_state='collapsed')

st.head("Generate Blogs ")

input_text = st.text_input("Enter the blog topic")

col1,col2 = st.columns([5,5])
with col1:
    no_words = st.text_input("No os words")
with col2:
    blog_style = st.selectbox('Writing the blog for', ('Researchers','people'),index=0)
    
submit= st.button("Generate")

if submit:
    st.write(getLLamarespo )