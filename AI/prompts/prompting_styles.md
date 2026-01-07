## Prompting Styles

### 1. ChatML / OpenAI Message Format

**Used by:** OpenAI, Gemini (Your Project Standard), Qwen.
**Structure:**

```python
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello!"},
    {"role": "assistant", "content": "Hi there."}
]
```

### 2. Alpaca Format

**Used by:** Alpaca, older Llama fine-tunes.
**Structure:**

```text
### Instruction:
You are a helpful assistant.

### Input:
Hello!

### Response:
Hi there.
```

### 3. Llama [INST] Format

**Used by:** Llama 2, Llama 3, Mistral.
**Structure:**

```text
<s>[INST] <<SYS>>
You are a helpful assistant.
<</SYS>>

Hello! [/INST] Hi there. </s>
```
