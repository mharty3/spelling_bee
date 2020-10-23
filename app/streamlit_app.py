import streamlit as st
import word_finder

st.title('NYT Spelling Bee Cheater')

letters = st.text_input("What are today's letters?")

if letters:
    key_letter = st.selectbox('Which is the middle letter? This is the one that must be included in all words.', letters.upper())

    letters = key_letter.lower() + letters.lower() # key letter must be the first in the string

if letters:
    good_words = word_finder.word_finder(letters)
    pangrams = word_finder.find_pangrams(good_words)
    data = dict(pangrams=pangrams, all_words=good_words)

    pangram_expander = st.beta_expander("Pangrams")
    with pangram_expander:

        for w in data['pangrams']:
            st.write(w.upper())

    other_word_expander = st.beta_expander("All Words")
    with other_word_expander:

        for w in data['all_words']:
            st.write(w.upper())