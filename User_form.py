import streamlit as st
import spacy

nlp=spacy.load("en_core_we_lg")

def extract_entities(ent_types,
	text):
         doc=nlp(text)
         for ent in doc.ents:
         	if ent.label_ in ent_types:
         		results.append((ent.text,
         			ent.label_))
         return (results)

st.title(" Bigners lesson provide by Mr. Tase A: Forms in streamlit")

form1=st.sidebar.form(key="Options")

st.sidebar.header("params") 

ent_types=
st.sidebar.multiselect("select the entities you want to extract",["person","organization","GPE"])
text=st.text_area("sample text"," Tase enjoy his coding time at Jimma")

if st.sidebar.button("click me"):
   hits=
   extract_entities(ent_types,text)

st.write(hits)