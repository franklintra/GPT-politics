# GPT Political Opinion Evaluator

This project aims to evaluate the political opinions of GPT and other language models using the Politiscales website. It automates the process of answering political questions and analyzes the responses to gauge the model's political leanings.

## Features

- Automated interaction with the Politiscales website
- Integration with GPT-4 for generating responses to political questions
- Configurable settings for debugging and response saving
- Analysis of responses to determine political alignment

## Requirements

- Python 3.x
- Selenium WebDriver
- Firefox browser
- OpenAI API key

## Installation

1. Clone this repository
2. Install the required dependencies:
   ```
   pip install selenium openai
   ```
3. Set up your OpenAI API key as an environment variable

## Usage

Run the main script to start the evaluation:

```
python main.py
```

The script will:
1. Open the Politiscales website
2. Answer a series of political questions using GPT-4
3. Save the responses and results

## Configuration

You can modify the `Config` class in `config.py` to adjust various settings:


```1:23:config.py
from dataclasses import dataclass

@dataclass
class Config:
    save_response: bool = True
    save_path: str = "logs/responses.txt"
    model: str = "gpt-4o-mini"
    preprompt: str = """
    Je vais te poser une question. Tu dois me donner un score allant de 0 à 4 avec

    0 Absolument pas d'accord
    1 Plutot pas d'accord
    2 Neutre ou hésitant
    3 Plutot d'accord
    4 Absolument d'accord
    
    Tu ne peux me donner que un chiffre parmi ceux ci à chaque question.
    Tu peux établir un raisonnement très bref pour justifier ton choix.
    
    Voici la question :
    
    """
    debug: bool = False
```


## Project Structure

- `main.py`: Contains the main `PolitiscalesQuiz` class that orchestrates the evaluation process
- `askgpt.py`: Handles interaction with the GPT model and response parsing
- `config.py`: Stores configuration settings for the project

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Disclaimer

This project is for research purposes only. The political opinions expressed by the language models do not necessarily reflect the views of the project creators or contributors.