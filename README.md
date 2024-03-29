AI Chatbot for Qigong Assistance

This repository contains the code for an AI-powered chatbot designed to provide assistance and information on Qigong, a traditional Chinese exercise and healing technique. The chatbot utilizes OpenAI's GPT-3.5 model, embedded within the LangChain framework, and offers a Streamlit-based user interface for easy interaction.
Features

- Personalized responses based on user queries about Qigong.
- Integration with OpenAI's powerful language models.
- Streamlit interface for a user-friendly experience.
- Data-driven responses with context awareness.

Getting Started
Prerequisites:

```bash
    Python 3.8+
    OpenAI API Key
    Streamlit
```
Installation:

Clone the repository:

```bash
git clone https://github.com/[your-username]/qigong-chatbot.git

Navigate to the project directory:

cd qigong-chatbot

Install the required packages:

pip install -r requirements.txt
```

Setting Up

Create a .env file in the root directory with your OpenAI API key

```bash

OPENAI_API_KEY='your_api_key_here'
```

Load and preprocess your Qigong-related data. Place the data file in the data directory.

Run the Streamlit app:

```bash
streamlit run app/main.py
```

Project Structure

```bash

chatbot_project/
│
├── app/                       # Application code
│   ├── main.py                # Entry point
│   ├── chatbot.py             # Chatbot logic
│   └── ...
│
├── data/                      # Data files
│   └── ...
│
├── requirements.txt           # Dependencies
└── README.md                  # Project documentation
```

Usage

Interact with the chatbot via the Streamlit interface. Input your queries related to Qigong, and the chatbot will respond based on the context provided by the preprocessed data.
Contributing

Contributions to enhance the chatbot's functionality or to extend its dataset are welcome. Please feel free to fork the repository and submit a pull request with your improvements.

