import openai

# Set up your OpenAI API key
openai.api_key = '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'

def chatbot_response(user_input):
    response = openai.Completion.create(
        engine="gpt-3.5-turbo",  # Or "gpt-4" if you have access
        prompt=user_input,
        max_tokens=150,
        temperature=0.7,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.6
    )
    return response.choices[0].text.strip()

if __name__ == "__main__":
    print("Welcome to the AskBanu! Type 'exit' to end the conversation.")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")