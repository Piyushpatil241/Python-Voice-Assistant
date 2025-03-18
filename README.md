# Voice Assistant

This is a Python-based voice assistant that can recognize speech commands and perform various tasks like opening websites, playing music, fetching news, and performing AI-powered searches.

## Features
- Open popular websites like Google, YouTube, and Facebook using voice commands.
- Search for and play music from a predefined music library.
- Fetch top news headlines using the NewsAPI.
- Perform web searches on Brave Browser.
- AI-powered responses using Groq API (currently non-functional but included in the code).

## Requirements
### Python Libraries
Ensure you have the following Python libraries installed:
```sh
pip install speechrecognition webbrowser pyttsx3 requests python-dotenv groq
```

### API Keys
- Create a `.env` file and add the following environment variables:
```sh
NEWS_API_KEY=your_newsapi_key
GROQ_API_KEY=your_groq_api_key  # Not currently functional
```

## Usage
1. Run the script:
   ```sh
   python voice_assistant.py
   ```
2. Say "Start" or "Jarvis" to activate the assistant.
3. Use commands like:
   - "Open Google"
   - "Play music"
   - "News"
   - "Search [your query]"
   - "Exit" to shut down the assistant.

## Notes
- The Groq AI functionality is included in the code but is currently non-functional.
- Uses Brave Browser for web searches.
- Handles errors for better user experience.

## Future Improvements
- Fix Groq AI integration.
- Add support for more web services.
- Improve voice recognition accuracy.

## License
This project is open-source and free to use.

