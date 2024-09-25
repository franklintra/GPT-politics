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