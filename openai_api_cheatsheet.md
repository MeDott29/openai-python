Sure, here's a cheat sheet based on the information in the @README.md file:

## OpenAI Python API Cheat Sheet

### Installation
```sh
pip install openai
```

### Usage
```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Say this is a test",
        }
    ],
    model="gpt-3.5-turbo",
)
```

### Async Usage
```python
import os
import asyncio
from openai import AsyncOpenAI

client = AsyncOpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

async def main() -> None:
    chat_completion = await client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "Say this is a test",
            }
        ],
        model="gpt-3.5-turbo",
    )

asyncio.run(main())
```

### Streaming Responses
```python
from openai import OpenAI

client = OpenAI()

stream = client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": "Say this is a test"}],
    stream=True,
)
for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content)
```

### Module-level client
```python
import openai

openai.api_key = '...'

completion = openai.chat.completions.create(
    model="gpt-4",
    messages=[
        {
            "role": "user",
            "content": "How do I output all files in a directory using Python?",
        },
    ],
)
print(completion.choices[0].message.content)
```

### Handling errors
```python
import openai
from openai import OpenAI

client = OpenAI()

try:
    client.fine_tunes.create(
        training_file="file-XGinujblHPwGLSztz8cPS8XY",
    )
except openai.APIConnectionError as e:
    print("The server could not be reached")
    print(e.__cause__)
except openai.RateLimitError as e:
    print("A 429 status code was received; we should back off a bit.")
except openai.APIStatusError as e:
    print("Another non-200-range status code was received")
    print(e.status_code)
    print(e.response)
```

### Microsoft Azure OpenAI
```python
from openai import AzureOpenAI

client = AzureOpenAI(
    api_version="2023-07-01-preview"
    azure_endpoint="https://example-endpoint.openai.azure.com",
)

completion = client.chat.completions.create(
    model="deployment-name",
    messages=[
        {
            "role": "user",
            "content": "How do I output all files in a directory using Python?",
        },
    ],
)
print(completion.model_dump_json(indent=2))
```
