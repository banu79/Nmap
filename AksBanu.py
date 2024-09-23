import openai

openai.api_key = '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'


def generate_response(prompt):
    response = openai.Completion.create(
        engine="gpt-3.5-turbo",  # Use GPT-4 or gpt-3.5-turbo
        prompt=prompt,
        max_tokens=150,
        temperature=0.7
    )
    return response.choices[0].text.strip()

# Test the chatbot
if __name__ == "__main__":
    user_input = "Hello, how are you?"
    response = generate_response(user_input)
    print(f"Chatbot: {response}")