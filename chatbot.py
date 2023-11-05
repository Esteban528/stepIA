import os
import openai

# Configura la clave de la API de OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")

def process_user_input(user_input):
    # Lógica de OpenAI para procesar la entrada del usuario
    # Ejemplo simple de uso de OpenAI
    # response = openai.Completion.create(
    #     engine="text-davinci-003",
    #     prompt=user_input,
    #     max_tokens=50
    #)
    # response = openai.Completion.create(
    #     engine="davinci",
    #     prompt="Translate the following English text to French: '{}'".format("Hello, how are you?"),
    #     max_tokens=100
    # )
    
    completion = openai.Completion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": "Hello!"}
        ]
    )

    return (completion.choices[0].message)
