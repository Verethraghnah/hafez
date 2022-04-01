import markovify
import streamlit as st

# Get raw text as string.
st.title("What would Hafez say?")
data = open("hafez.txt", mode="r", encoding='utf-8').read()


@st.cache  # cache the result of the hafez.txt file
def get_model():
    tex = markovify.Text(data)
    return tex


model = get_model()

# ask user how many sentences to generate
st.sidebar.markdown("How many sentences would you like to generate?")
num_sentences = st.sidebar.slider("Sentences", min_value=1, max_value=4)
st.sidebar.markdown("How many characters would you like to generate for each sentence?")
num_words = st.sidebar.slider("Sentences", min_value=20, max_value=280)


# Generate a sentence.
@st.cache
def generate_sentence():
    for i in range(num_sentences):
        sentence = model.make_sentence()
        sentece2 = model.make_short_sentence(num_words)
        return sentence, sentece2


# show the generated sentence
st.write("Hafez wants to tell you: ", generate_sentence())
