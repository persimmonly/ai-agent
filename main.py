import sys
import os
from google import genai
from dotenv import load_dotenv
from google.genai import types

def main():
    load_dotenv()
    
    #definitions
    args = sys.argv[1:]
    verbose_flag = '--verbose' in args

    #parse args
    if not args:
        print("AI Code Assistant")
        print('\nUsage: python main.py "your prompt here"')
        print('Example: python main.py "How do I build a calculator app?"')
        sys.exit(1)

    #user prompt
    cleaned_args = [arg for arg in args if arg != '--verbose']
    user_prompt = " ".join(cleaned_args)

    #build messages
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    #call api to get response
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
    )
    print("Response:")
    print(response.text)

    #verbose addons
    if verbose_flag:
        pt = getattr(response.usage_metadata, "prompt_token_count", None)
        rt = getattr(response.usage_metadata, "candidates_token_count", None)
        print("User prompt:", user_prompt)
        print("Prompt tokens:", pt)
        print("Response tokens:", rt)

if __name__ == "__main__":
    main()

