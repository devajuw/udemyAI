# running this is supposed to be downloading this AI model locally if you dont have the model downloaded yet.. from second time it parses result.
from transformers import pipeline

pipe = pipeline("image-text-to-text", model="google/gemma-3-4b-it")
messages = [
    {
        "role": "user",
        "content": [
            {"type": "image", "url": "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/p-blog/candy.JPG"},
            {"type": "text", "text": "What animal is on the candy?"}
        ]
    },
]
pipe(text=messages)