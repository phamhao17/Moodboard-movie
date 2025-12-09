import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd
import requests
from io import BytesIO
from sklearn.metrics.pairwise import cosine_similarity
import os
import random

st.set_page_config(page_title="Movie Moodboard", layout="wide")
st.title("🎬 Movie Moodboard")

# -------------------------
# Section 1: Upload an image
# -------------------------
uploaded_file = st.file_uploader("Upload a scene image:", type=["png", "jpg", "jpeg"])

# Placeholder movie dataset
# Normally this would be movie_vectors.npy + movie_files.npy
# For simplicity, we simulate with small dummy dataset
movie_dataset = {
    "movie1.jpg": np.random.rand(512),
    "movie2.jpg": np.random.rand(512),
    "movie3.jpg": np.random.rand(512)
}

movie_files = list(movie_dataset.keys())
movie_vectors = np.array(list(movie_dataset.values()))

if uploaded_file:
    st.subheader("🔍 Finding similar movie images...")
    input_image = Image.open(uploaded_file).convert("RGB")
    st.image(input_image, caption="Uploaded Image", use_column_width=True)

    # Simulate embedding for uploaded image
    input_vector = np.random.rand(512).reshape(1, -1)

    similarities = cosine_similarity(input_vector, movie_vectors)[0]
    top_idx = similarities.argsort()[::-1][:3]

    st.subheader("✅ Top similar movie images")
    for idx in top_idx:
        movie_img_path = movie_files[idx]
        st.image(movie_img_path, caption=f"Movie: {movie_img_path}", use_column_width=True)
else:
    st.info("Upload an image to find similar movie scenes, or use keywords below.")

# -------------------------
# Section 2: Keyword fallback
# -------------------------
st.subheader("📝 Search by keywords")
character = st.text_input("Character")
genre = st.text_input("Genre")
setting = st.text_input("Setting")
dialogue = st.text_input("Dialogue")

if st.button("Search by keywords"):
    st.write(f"Searching for movies with: Character={character}, Genre={genre}, Setting={setting}, Dialogue={dialogue}")
    # Simulate search result
    dummy_results = ["movie1.jpg", "movie2.jpg"]
    for m in dummy_results:
        st.image(m, caption=f"Movie: {m}", use_column_width=True)

# -------------------------
# Section 3: Music suggestions
# -------------------------
st.subheader("🎵 Suggested Movie Music")
mood = st.selectbox("Select mood:", ["Happy", "Sad", "Romantic", "Suspense"])
# Dummy playlist links
playlists = {
    "Happy": ["https://open.spotify.com/playlist/37i9dQZF1DXdPec7aLTmlC"],
    "Sad": ["https://open.spotify.com/playlist/37i9dQZF1DX7qK8ma5wgG1"],
    "Romantic": ["https://open.spotify.com/playlist/37i9dQZF1DX5EkyRFIV92g"],
    "Suspense": ["https://open.spotify.com/playlist/37i9dQZF1DX8Uebhn9wzrS"]
}
st.markdown(f"[{mood} Playlist]({playlists[mood]})")

# -------------------------
# Section 4: Movie recommendations
# -------------------------
st.subheader("🎬 Recommended Movies")
st.write("Movies with similar genre or mood:")
# Dummy recommendations
recommended_movies = ["Movie A", "Movie B", "Movie C"]
st.write(recommended_movies)
