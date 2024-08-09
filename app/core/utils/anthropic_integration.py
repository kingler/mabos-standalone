
import anthropic

client = anthropic.Anthropic(
  # defaults to os.environ.get("ANTHROPIC_API_KEY")
  api_key="my_api_key",
  base_url="https://anthropic.helicone.ai/",
  default_headers={
    "Helicone-Auth": "Bearer pk-helicone-wsxikyq-blbuhya-rq67izi-43nhjla",
  }
)
  
message = client.messages.create(
  model="claude-3-opus-20240229",
  max_tokens=1024,
  messages=[
    {"role": "user", "content": "Hello, Claude"}
  ]
)
  
print(message.content)
