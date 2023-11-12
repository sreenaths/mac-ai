from transformers import AutoTokenizer
import transformers
import torch

from yaspin import yaspin

device = "mps"
model = "meta-llama/Llama-2-7b-chat-hf"

print("Loading model: ", model)
tokenizer = AutoTokenizer.from_pretrained(model)
pipeline = transformers.pipeline(
    "text-generation",
    model=model,
    torch_dtype=torch.float16,
    device_map=device,
)

prompt = "My favourite condiment is"
print("Prompt: ", prompt)
with yaspin(text="Generating..."):
  sequences = pipeline(
      prompt,
      do_sample=True,
      top_k=1,
      num_return_sequences=1,
      eos_token_id=tokenizer.eos_token_id,
      max_length=200,
      return_full_text=False
  )
print("Result: ", sequences[0]['generated_text'])
