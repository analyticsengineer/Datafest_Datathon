import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud, STOPWORDS
from collections import Counter
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import string

# Download NLTK resources if not already available
nltk.download('punkt', quiet=True)
nltk.download('wordnet', quiet=True)
nltk.download('stopwords', quiet=True)

# Set up Streamlit app title
st.title("Student Response Analysis")

# Load dataset
online_review = pd.read_excel('Datafest_Hackathon.xlsx')
online_review = online_review.iloc[:, 1:]

# Display dataset overview
st.subheader("Dataset Overview")
st.write(online_review.head())
st.write("Shape of dataset:", online_review.shape)
st.write("Data types:", online_review.dtypes)

# Convert ordinal columns to categorical
ordinal_var_dict = {
    'Exam readiness': ['Not well prepared', 'Somewhat prepared', 'Very well prepared'],
    'Exam preparation': ['Not stressful', 'Moderately stressful', 'Extremely stressful'],
    'Exam confidence': ['Not confident', 'Somewhat confident', 'Very confident'],
    'Family support': ['Not supportive', 'Somewhat supportive', 'Very supportive']
}

for var in ordinal_var_dict:
    ordered_var = pd.api.types.CategoricalDtype(ordered=True, categories=ordinal_var_dict[var])
    online_review[var] = online_review[var].astype(ordered_var)

# Univariate Exploration
st.subheader("Univariate Exploration")
fig, ax = plt.subplots(nrows=4, figsize=(16, 12))
sns.countplot(data=online_review, x='Exam readiness', ax=ax[0]).set(title='Exam Readiness for Online Education')
sns.countplot(data=online_review, x='Exam preparation', ax=ax[1]).set(title='Exam Preparation for Online Education')
sns.countplot(data=online_review, x='Exam confidence', ax=ax[2]).set(title='Exam Confidence for Online Education')
sns.countplot(data=online_review, x='Family support', ax=ax[3]).set(title='Family Support for Online Education')
st.pyplot(fig)

# Age Distribution
st.write(online_review['Age'].value_counts(normalize=True) * 100)
fig_age = plt.figure()
sns.countplot(data=online_review, x='Age').set(title='Distribution of Age')
st.pyplot(fig_age)

# Gender Distribution
gendercount = round(online_review['Gender'].value_counts(normalize=True) * 100, 2)
fig_gender = plt.figure()
plt.pie(gendercount, labels=[f"{str(x)}%" for x in gendercount.values], startangle=90, counterclock=False, wedgeprops={'width': 0.5})
plt.title('Gender Distribution')
plt.legend(gendercount.index)
st.pyplot(fig_gender)

# Function to generate word cloud
def generate_wordcloud(df, column_name, title="Word Cloud"):
    def preprocess_text(text):
        text = text.lower().translate(str.maketrans('', '', string.punctuation))
        tokens = word_tokenize(text)
        tokens = [word for word in tokens if word not in stopwords.words('english')]
        lemmatizer = WordNetLemmatizer()
        return [lemmatizer.lemmatize(word) for word in tokens]

    df['processed_text'] = df[column_name].apply(lambda x: preprocess_text(str(x)))
    all_words = [word for text in df['processed_text'] for word in text]
    word_freq = Counter(all_words)
    wordcloud = WordCloud(width=600, height=300, background_color='white', max_words=100, contour_color='black', colormap='viridis', stopwords=STOPWORDS).generate_from_frequencies(word_freq)

    plt.figure(figsize=(10, 4))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title(title)
    st.pyplot()

# Generate word clouds for specified columns
for column in ['Main academy challenge', 'Education resources', 'Recommendation', 'Non-primary academy challenge']:
    st.subheader(f"{column} Word Cloud")
    generate_wordcloud(online_review, column, title=f"{column} Word Cloud")

# Bivariate Exploration
st.subheader("Bivariate Exploration")
fig, ax = plt.subplots(nrows=3, figsize=(12, 8))
sns.countplot(data=online_review, x='Exam readiness', hue='Exam confidence', ax=ax[0])
sns.countplot(data=online_review, x='Exam preparation', hue='Exam confidence', ax=ax[1])
sns.countplot(data=online_review, x='Family support', hue='Exam confidence', ax=ax[2])
plt.tight_layout()
st.pyplot(fig)

# Clustering
st.subheader("Model Building with K-Modes Clustering")
from kmodes.kmodes import KModes

categorical_cols = ['Gender', 'Age', 'School', 'Exam', 'Location', 'Education',
                    'Guardians Education', 'Main academy challenge', 'Non-primary academy challenge', 
                    'Exam readiness', 'Education resources', 'CBT technical issues', 
                    'Exam preparation', 'Exam malpractice', 'After school study', 
                    'Exam guidance', 'Exam confidence', 'Health issues', 'Family support']

online_review[categorical_cols] = online_review[categorical_cols].astype('category')

for col in categorical_cols:
    online_review[col] = online_review[col].cat.codes

kmodes = KModes(n_clusters=3, init='Cao', n_init=5, verbose=1, random_state=42)
online_review['Cluster'] = kmodes.fit_predict(online_review[categorical_cols])

# Visualization of clusters
def visualize_clusters(x_feature, y_feature):
    plt.figure(figsize=(10, 7))
    sns.scatterplot(x=online_review[x_feature], y=online_review[y_feature],
                    hue=online_review['Cluster'], palette='viridis', s=100)
    plt.title(f'K-Modes Clustering: {x_feature} vs {y_feature}')
    plt.xlabel(x_feature)
    plt.ylabel(y_feature)
    st.pyplot()
    st.write("Cluster Centroids:\n", kmodes.cluster_centroids_)

x_feature = st.selectbox("Select Y-axis feature:", categorical_cols)
y_feature = st.selectbox("Select X-axis feature:", ['Exam readiness', 'Exam preparation', 'Exam confidence'])
if st.button('Visualize Clusters'):
    visualize_clusters(x_feature, y_feature)
