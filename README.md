# FauxNews 📰

**AI-Powered Fake News Generator for Media Literacy Education**

FauxNews is a Python application that generates realistic fake news articles using the OpenAI API and Streamlit. Built for experimentation, education, and media literacy awareness, it demonstrates the capabilities—and risks—of AI-powered text and media generation.

## 🎯 Key Features

- **AI-Generated Content**: Uses GPT-3.5-turbo for headlines and article text
- **Image Generation**: DALL-E 3 creates relevant news images
- **Beneficiary Inference**: Automatically analyzes who would benefit from the fake news
- **Modern News Layout**: Professional UI that mimics real news sites
- **Component Regeneration**: Regenerate individual parts or entire articles
- **Educational Focus**: Designed for media literacy and AI awareness

## 🚀 Quick Start

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up OpenAI API key**
   ```bash
   # Create .env file
   echo "OPENAI_API_KEY=your_api_key_here" > .env
   ```

3. **Run the application**
   ```bash
   streamlit run app.py
   ```

4. **Open your browser** to `http://localhost:8501`

## 📋 How It Works

### Article Generation Process

1. **Topic Input**: User specifies a news topic (e.g., "Kamala Harris", "Climate Change")
2. **Absurdity Level**: User sets how outrageous the fake news should be (1-10)
3. **Beneficiary Analysis**: AI infers who would benefit from this narrative
4. **Content Generation**: AI creates:
   - Sensational headline
   - Full article body with fake quotes
   - Author name (randomly generated)
   - News network name (randomly generated)
   - Release date (random date in last 3 months)
   - Relevant image

### Example Output

```
🎯 Likely Beneficiary: Donald Trump

BREAKING: Kamala Harris Caught in Shocking Scandal - 
You Won't Believe What She Did Next!

By Sarah Johnson | Global News Network | December 15, 2024

[AI-Generated Image]

In a stunning revelation that has rocked the political landscape, Vice President Kamala Harris has been implicated in a scandal that could change everything. Sources close to the White House reveal...

[Full article continues with fake quotes and sensational language]
```

## 🎛️ User Interface

### Sidebar Controls
- **Topic Input**: Enter any news topic
- **Absurdity Slider**: Control how outrageous the content is
- **Generate Button**: Create a new article
- **Regenerate Options**: Modify specific components

### Main Display
- **Professional Layout**: Mimics CNN, Reuters, or other news sites
- **Beneficiary Badge**: Shows who benefits from the narrative
- **Article Components**: Headline, byline, image, and body text
- **Metadata Panel**: View all article details

## 🔧 Technical Details

### Dependencies
- `streamlit`: Web interface
- `openai`: AI content generation
- `python-dotenv`: Environment variable management
- `requests`: HTTP requests
- `Pillow`: Image processing

### Architecture
- **Article Class**: Encapsulates all article generation logic
- **Modular Design**: Each component has its own generation method
- **Error Handling**: Graceful fallbacks for API failures
- **Session Management**: Streamlit maintains article state

## ⚠️ Important Disclaimers

**Educational Purpose Only**: This tool is designed for:
- Media literacy education
- Understanding AI capabilities
- Demonstrating the risks of AI-generated content
- Research and experimentation

**Always verify information from reliable sources!**

## 📚 Use Cases

### Educational
- **Media Literacy**: Show students how AI can create convincing fake news
- **Critical Thinking**: Demonstrate the importance of fact-checking
- **AI Awareness**: Understand the capabilities and limitations of AI

### Research
- **Content Analysis**: Study patterns in AI-generated misinformation
- **Detection Methods**: Develop tools to identify AI-generated content
- **Policy Development**: Inform discussions about AI regulation

## 🛠️ Development

### Project Structure
```
FauxNews/
├── main.py          # Article class and generation logic
├── app.py           # Streamlit interface
├── requirements.txt # Python dependencies
├── SETUP.md         # Detailed setup instructions
└── README.md        # This file
```

### Contributing
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📖 Documentation

- **[Setup Guide](SETUP.md)**: Detailed installation and configuration
- **Code Comments**: Inline documentation in source files
- **Error Messages**: Helpful troubleshooting information

## 🤝 License

This project is for educational purposes. Please use responsibly and in accordance with OpenAI's terms of service.

## 🔗 Links

- [OpenAI Platform](https://platform.openai.com/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Media Literacy Resources](https://medialiteracynow.org/)

---

**Built with ❤️ for media literacy education**
