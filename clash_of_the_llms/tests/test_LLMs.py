import os
from dotenv import load_dotenv
import litellm

load_dotenv()

for model in ["openai/gpt-4o-mini", "gemini/gemini-1.5-flash", "xai/grok-4-fast"]:
    try:
        print(f"\nTesting {model} ...")
        resp = litellm.completion(
            model=model,
            messages=[{"role": "user", "content": "Say 'ok'."}]
        )
        print("OK:", resp.choices[0].message["content"])
    except Exception as e:
        print("ERR:", e)