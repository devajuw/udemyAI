import tiktoken
enc= tiktoken.encoding_for_model("gpt-4o")

text = "Hello, how are you?"
tokens = enc.encode(text)
print("Tokens:", tokens)

decoded_text = enc.decode([13225, 11, 1495, 553, 481, 30])
print("Decoded text:", decoded_text)

