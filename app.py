import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

# Load your cleaned dataset
df = pd.read_csv("data/party_data_cleaned.csv")

# Preprocess dataset the same way
categorical_cols = ['day_of_week', 'event_time', 'weather_condition']
df_encoded = df.copy()

le_dict = {}
for col in categorical_cols:
    le = LabelEncoder()
    df_encoded[col] = le.fit_transform(df_encoded[col])
    le_dict[col] = le

# Encode target
target_le = LabelEncoder()
df_encoded['turnout_level'] = target_le.fit_transform(df_encoded['turnout_level'])

# Features and target
X = df_encoded.drop(columns=['event_name', 'date', 'turnout_level'])
y = df_encoded['turnout_level']

# Train Random Forest
model = RandomForestClassifier(random_state=42)
model.fit(X, y)

# Streamlit app
st.markdown("<h1 style='text-align: center; color: #f63366;'>🎉 Welcome to PartyLens 🎉</h1>", unsafe_allow_html=True)


st.write("Enter event details to predict turnout level!")

# User Inputs
day_of_week = st.selectbox("Day of the Week", le_dict['day_of_week'].classes_)
event_time = st.selectbox("Event Time", le_dict['event_time'].classes_)
weather_condition = st.selectbox("Weather Condition", le_dict['weather_condition'].classes_)
weather_temp = st.slider("Weather Temperature (°F)", 30, 100, 70)
instagram_posts = st.slider("Number of Instagram Posts", 0, 150, 50)
avg_likes = st.slider("Average Likes per Post", 0, 500, 100)
hashtag_count = st.slider("Number of Hashtags Used", 0, 30, 5)
buzz_words = st.slider("Number of Buzz Words in Captions", 0, 20, 3)

# Transform user input to model format
input_data = pd.DataFrame({
    'day_of_week': [le_dict['day_of_week'].transform([day_of_week])[0]],
    'event_time': [le_dict['event_time'].transform([event_time])[0]],
    'weather_condition': [le_dict['weather_condition'].transform([weather_condition])[0]],
    'weather_temp': [weather_temp],
    'instagram_posts': [instagram_posts],
    'avg_likes': [avg_likes],
    'hashtag_count': [hashtag_count],
    'buzz_words_in_caption': [buzz_words]
})
# Ensure the input columns are in the same order as during training
input_data = input_data[X.columns]

# Make prediction
prediction = model.predict(input_data)
predicted_label = target_le.inverse_transform(prediction)[0]


# Display fancier feedback based on prediction
st.subheader("🎯 Predicted Turnout Level:")

if predicted_label == 'High':
    st.success("🔥 High Turnout Expected! Get ready for a packed event!")
    st.balloons()  # 🎈🎈🎈 Party Vibes!
elif predicted_label == 'Medium':
    st.info("😎 Medium Turnout Expected. Should be a good crowd!")
else:
    st.warning("💤 Low Turnout Expected. Might be a smaller vibe.")

