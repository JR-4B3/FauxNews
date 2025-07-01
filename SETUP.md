# FauxNews Setup Guide

## Prerequisites

- Python 3.8 or higher
- OpenAI API key

## Installation

1. **Clone or download the repository**
   ```bash
   git clone <repository-url>
   cd FauxNews
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your OpenAI API key**
   
   Create a `.env` file in the project root:
   ```bash
   # .env
   OPENAI_API_KEY=your_openai_api_key_here
   ```
   
   **To get an OpenAI API key:**
   - Go to [OpenAI Platform](https://platform.openai.com/api-keys)
   - Sign up or log in
   - Create a new API key
   - Copy the key and paste it in your `.env` file

## Running the Application

1. **Start the Streamlit app**
   ```bash
   streamlit run app.py
   ```

2. **Open your browser**
   - The app will automatically open at `http://localhost:8501`
   - If it doesn't open automatically, manually navigate to the URL

## Usage

1. **Enter a news topic** in the sidebar (e.g., "Kamala Harris", "Climate Change", "UFOs")
2. **Adjust the absurdity level** using the slider (1-10)
3. **Click "Generate Article"** to create your fake news story
4. **Use the regenerate buttons** to modify specific components:
   - Headline
   - Article body
   - Author name
   - News network
   - Image
   - Beneficiary analysis

## Features

- **AI-Generated Content**: Uses GPT-3.5-turbo for headlines and article text
- **Image Generation**: Uses DALL-E 3 for relevant news images
- **Beneficiary Inference**: Automatically analyzes who would benefit from the fake news
- **Modern UI**: Professional news site layout with Streamlit
- **Component Regeneration**: Regenerate individual parts or the entire article
- **Educational Focus**: Designed for media literacy and AI awareness

## Important Notes

⚠️ **Educational Purpose Only**: This tool is designed for:
- Media literacy education
- Understanding AI capabilities
- Demonstrating the risks of AI-generated content
- Research and experimentation

**Always verify information from reliable sources!**

## Troubleshooting

**"Error generating article"**
- Check that your OpenAI API key is correct
- Ensure you have sufficient API credits
- Verify your internet connection

**"Error generating image"**
- DALL-E 3 requires additional API credits
- The app will show a placeholder if image generation fails

**App won't start**
- Make sure all dependencies are installed: `pip install -r requirements.txt`
- Check that you're using Python 3.8+
- Verify your `.env` file is in the correct location 