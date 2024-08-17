import os
from together import Together
import base64
import PIL
from PIL import Image
import io
print("=========================================")
print("welcome to Zainab's Model")
print("you want to chat or create image?")
UserInput=input("Enter \'C\' for chat and\'I\' for image: ").strip()
print("=========================================")

import ApiKey as key

client = Together(api_key=key.key)

def chat(query):
        response = client.chat.completions.create(
        model="meta-llama/Meta-Llama-3.1-405B-Instruct-Turbo",
        messages=[
              {
                  "role":"user",
                  "content":query
              }
        ],
        max_tokens=512,
        temperature=0.7,
        top_p=0.7,
        top_k=50,
        repetition_penalty=1,
        stop=["<|eot_id|>","<|eom_id|>"],
        #stream=True
        )
        print(f" AI: {response.choices[0].message.content}")


def image(description):
      
        client = Together(api_key=key.key)
        response = client.images.generate(
           prompt=description,
           model="stabilityai/stable-diffusion-xl-base-1.0",
           width=512,
           height=512,
           steps=40,
           n=2,
           seed=4685
        )
        image_data = base64.b64decode(response.data[0].b64_json)
        image = Image.open(io.BytesIO(image_data))
        image.show()
        image.save("image.png")

if UserInput=='C' or UserInput=='c':
   while True:
        q=input("enter query: ")
        chat(q)       
elif UserInput=='I'or UserInput=='i':
   while True:
          prompt=input("enter prompt to generate image: ")
          image(prompt)
else:
      print("Invalid Choice")     