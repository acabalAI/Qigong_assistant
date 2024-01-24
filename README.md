# Qigong-Assistant

Qigong-Assistant is a cutting-edge, multilingual AI assistant, a collaborative effort with the Shanghai University of Traditional Chinese Medicine and the Institute of Qigong Research of Shanghai, designed for international Qigong practitioners.
It implements a customized knowledge-base and a multiagent framework for hallucination mitigation and reasoning capabilities enhancement.

## Features

- Multilingual Support: Accessible to a global audience.
- AI-Powered Responses: Advanced AI for accurate, context-aware interactions.
- Expert Knowledge Integration: Insights from Qigong experts.
- Multiagent framework.
- Conference Recognition: Featured at a conference in October 2023.

## Project Structure

```bash
qigong-assistant/
├── app/                       # Application code
│   ├── agents/                # Different agents for chatbot
│   │   ├── __init__.py
│   │   ├── memory_agent.py
│   │   ├── dialogue_agent.py
│   │   └── revision_agent.py
│   ├── models/                # Models and embeddings
│   │   ├── __init__.py
│   │   ├── embeddings.py
│   │   └── vector_base.py
│   ├── utils/                 # Utility functions
│   │   ├── __init__.py
│   │   ├── data_utils.py
│   │   └── text_utils.py
│   ├── services/              # External service integrations
│   │   ├── __init__.py
│   │   └── openai_service.py
│   ├── chatbot.py
│   ├── config.py
│   ├── data_loader.py
│   └── main.py
├── data/                      # Data files and resources
│   └── Database.xlsx
├── tests/                     # Unit and integration tests
│   ├── __init__.py
│   ├── test_agents.py
│   ├── test_data_loader.py
│   └── test_utils.py
├── web/                       # Web interface (e.g., Streamlit files)
│   ├── __init__.py
│   ├── app.py
│   └── streamlit_utils.py
├── documents/                 # Documentation and reference materials
├── .env                       # Environment variables file
├── .gitignore                 # List of files to be ignored by version control
├── requirements.txt           # Project dependencies
└── README.md                  # Project overview and instructions

```

## Prerequisites

```bash
    Python 3.8+
    OpenAI API Key
    Streamlit
```

## Installation

```bash
git clone https://github.com/acabalAI/qigong-assistant.git
cd qigong-assistant
pip install -r requirements.txt
```

## Configuration

Set up your OpenAI API key in the .env file.

## Running the Application

```bash
python - m streamlit run web/main.py
```

## Usage

Engage with the chatbot via Streamlit, providing queries about Qigong.

## Next Steps

In the following iteractions of the system the plan to work on the following features:

    -Speech to Text & Text to Speech: Enhance user interaction with voice commands and responses.
    -Customization: Personalize user experience based on individual preferences and history.
    -Expanding Knowledge Base: Continuously update the AI with new data, research, and insights about Qigong.

## Contributing

We welcome contributions! Fork the repo and submit your enhancements.

## License

MIT License - LICENSE.

## Acknowledgments

OpenAI, LangChain community, Shanghai University of Traditional Chinese Medicine, Institute of Qigong Research.
