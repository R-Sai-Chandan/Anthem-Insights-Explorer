# Anthem Insights Explorer

Discover the hidden themes in national anthems! 🌍 This project uses Natural Language Processing (NLP) and Machine Learning to cluster national anthems based on their semantic themes. Through thematic clustering and visualization, it provides unique insights into the interplay of culture, language, and identity.

## Features

- **Clustering with Word2Vec**: Identifies thematic clusters based on semantic similarities.
- **Interactive Visualization**: Generates word clouds and t-SNE plots for thematic differentiation.
- **Streamlit App**: Explore country-specific clusters, view colormaps, and read national anthems interactively.

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/R-Sai-Chandan/Anthem-Insights-Explorer
    ```

2. **Navigate to the project folder:**

    ```bash
    cd Anthem-Insights-Explorer
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Streamlit app:**

    ```bash
    streamlit run streamlitapp/app.py
    ```

## Project Structure

```plaintext
Anthem-Insights-Explorer/
├── datasets/                   # Contains datasets (e.g., national_anthems.csv)
├── images/                     # Contains word cloud images for clusters
├── CountryTrainer/             # Jupyter notebook for preprocessing and clustering
│   ├── CountryTrainer.ipynb
├── streamlitapp/               # Streamlit app for dynamic exploration
│   ├── app.py
├── .gitignore                  # Specifies files and directories to ignore
└── README.md                   # Project overview and instructions


How It Works
1. Data Preprocessing
Cleans and tokenizes anthem text.

Removes stopwords.

Generates sentence embeddings using Word2Vec.

2. Clustering
Applies KMeans clustering to group anthems based on semantic themes.

3. Visualization
Creates dynamic word clouds and t-SNE plots to represent thematic clusters.

4. Interactive Exploration
The Streamlit app enables users to explore clusters, word clouds, and country-specific insights.

Tech Stack
Python: Data preprocessing and analysis.

NLTK & Word2Vec: For tokenization and semantic embeddings.

KMeans & t-SNE: For clustering and dimensionality reduction.

Streamlit: To build an interactive and user-friendly app.

Future Work
Incorporate sentiment analysis for deeper thematic insights.

Experiment with advanced embeddings like BERT or FastText for better clustering accuracy.

Add more languages to cover a broader spectrum of national anthems.

Contributing
Contributions are welcome! Feel free to fork this repository and open a pull request with your improvements or suggestions.

License
This project is open-source and available under the MIT License. Feel free to use, modify, and share as needed.


### Changes Made:
- Added headers like `#`, `##`, `###` to define the structure more clearly.
- Formatted the code blocks and commands using backticks (```) for better clarity.
- Broke up long paragraphs into smaller, more digestible sections.
