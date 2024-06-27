# Alexa Voice Assistant

This project is a simple voice-activated assistant using Python, capable of performing various tasks such as playing songs on YouTube, providing the current date and time, fetching weather information, and retrieving summaries from Wikipedia.

## Features

- **Voice Recognition**: Listens for voice commands and responds accordingly.
- **Text-to-Speech**: Converts text responses into spoken words.
- **YouTube Integration**: Plays songs on YouTube.
- **Date and Time**: Provides the current date and time.
- **Weather Information**: Fetches and announces the current weather conditions.
- **Wikipedia Integration**: Retrieves and reads out summaries from Wikipedia.
- **Exit Command**: Stops the assistant on voice command.

## Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/your_username/alexa-voice-assistant.git
   cd alexa-voice-assistant
   ```

2. **Install the required packages:**
   ```sh
   pip install speechrecognition pyttsx3 pywhatkit wikipedia requests beautifulsoup4
   ```

3. **Run the script:**
   ```sh
   python script.py
   ```

## Usage

1. **Start the assistant:**
   When you run the script, the assistant will start and announce its readiness.

2. **Give commands:**
   - To play a song: `Alexa, play [song name]`
   - To get the current date: `Alexa, what is the date?`
   - To get the current time: `Alexa, what is the time?`
   - To get the weather: `Alexa, what is the weather in [city]?`
   - To get information from Wikipedia: `Alexa, who is [person's name]?`
   - To stop the assistant: `Alexa, stop` or `Alexa, exit`

## Note

- Ensure your microphone is properly set up and working.
- Replace `"your_username"` in the clone URL with your actual GitHub username.
- For weather information, replace the city in the `get_weather` function URL as per your requirement.

## Contributing

Contributions are welcome! Please create a pull request with your enhancements.

## License

This project is licensed under the MIT License.
