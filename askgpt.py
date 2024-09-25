import json
from openai import OpenAI
from config import Config

class GPTResponseParser:
    SCORES = {
        0: "strong-disagree",
        1: "disagree",
        2: "neutral",
        3: "agree",
        4: "strong-agree"
    }

    def __init__(self):
        self.config = Config()
        self.client = OpenAI()
        self.qa_history = []

    def parse_gpt_response(self, prompt: str, retries: int = 3) -> str:
        if self.config.debug:
            print(f"Entering parse_gpt_response with prompt: {prompt}, retries: {retries}")
        
        if retries == 0:
            raise Exception("Aucune réponse trouvée")
        
        full_prompt = self.config.preprompt + prompt
        
        response = self._get_gpt_response(full_prompt)
        predicted_score = self._extract_score(response)

        self.qa_history.append({
            "question": prompt,
            "response": response,
            "predicted_score": predicted_score
        })

        print(f"Question: {prompt} and predicted score: {self.SCORES.get(predicted_score, 'Unknown')}")
        
        if predicted_score is not None:
            return self.SCORES[predicted_score]
        
        print("Aucune réponse trouvée, réessayons")
        return self.parse_gpt_response(prompt, retries - 1)

    def _get_gpt_response(self, prompt: str) -> str:
        response = self.client.chat.completions.create(
            model=self.config.model,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content

    def _extract_score(self, response: str) -> int | None:
        for score in self.SCORES.keys():
            if str(score) in response:
                return score
        return None

    def save_qa_history(self):
        if self.config.debug:
            print(f"Saving QA history to file: {self.config.save_path}")
        with open(self.config.save_path, "w", encoding="utf-8") as f:
            json.dump(self.qa_history, f, ensure_ascii=False, indent=2)
        if self.config.debug:
            print("QA history saved successfully")

# Modify the main execution
if __name__ == "__main__":
    if self.config.debug:
        print("Starting main execution")
    print(parse_gpt_response("Est-ce que tu aimes les pommes ? sur une echelle de 0 à 4"))
    
    save_qa_history()
    if self.config.debug:
        print("Main execution completed")