# Personal-Indic-VLLM

A voice-based conversational AI application that works with Indian languages, specifically Malayalam. The application uses the SarvamAI API to handle speech-to-text, language processing, and text-to-speech conversions.

## Features

- Speech-to-Text conversion in Malayalam
- Natural Language Processing with LLM
- Text-to-Speech conversion in Malayalam
- Web interface using Gradio

## Prerequisites

- Python 3.x
- SarvamAI API key
- Internet connection

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/personal-indic-vllm.git
cd personal-indic-vllm
```

2. Create a `.env` file in the backend directory and add your SarvamAI API key:
```
SARVAM_API_KEY=your_api_key_here
```

3. Install the required dependencies:
```bash
pip install sarvamai python-dotenv gradio
```

## Usage

1. Navigate to the backend directory:
```bash
cd backend
```

2. Run the application:
```bash
python main.py
```

3. Open the provided Gradio interface URL in your web browser
4. Click the microphone button to start recording
5. Speak in Malayalam
6. The application will:
   - Convert your speech to text
   - Process it through an LLM
   - Convert the response back to speech
   - Play the audio response

## Technical Details

- Speech-to-Text: Uses Saarika v2 model
- Language Processing: SarvamAI Chat Completions
- Text-to-Speech: Bulbul v2 model with Manisha voice
- Language Support: Malayalam (ml-IN)

## Contributions

Currently not accepting contributions.