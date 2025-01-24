# Facebook Messenger Spam Bot script

A Python script that automates sending multiple messages to facebook messenger user using Selenium and WebDriver. The bot interacts with facebook to perform specific actions, such as logging in and sending messages.

## Features
- Automates web interactions using Selenium.
- Configurable through environment variables.
- Supports headless browser operation.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/Typh00ns/FB-Spam-_bot.git
   ```
2. Create and activate a Python virtual environment:
   ```bash
   conda create --name spam_bot_env python=3.12
   conda activate spam_bot_env
   ```
3. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the script:
   ```bash
   python spam_bot.py
   ```

# For people without Anaconda:
```bash
python -m venv spam_bot_env  
spam_bot_env\Scripts\activate  #For Windows
source spam_bot_env/bin/activate  # For Linux/macOS
pip install -r requirements.txt  # Install the dependencies
```
## Usage
The script runs locally on your machine, and no credentials are stored or shared in the repository. When running the script, you'll need to log in with a Facebook account, but this information is handled securely through the browser and is not stored by the script.

Example usage:
```bash
python spam_bot.py

## Acknowledgments

- Selenium for browser automation.
- WebDriver Manager for managing WebDriver binaries.

