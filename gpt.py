from g4f.client import Client
from g4f.Provider import You

client = Client()
response = client.images.generate(
  model="gemini",
  prompt="a white siamese cat",
)
image_url = response.data[0].url