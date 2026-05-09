from transformers import AutoTokenizer

# Download original tokenizer from HuggingFace
tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen2.5-3B-Instruct")

# Save missing tokenizer files into your merged folder
tokenizer.save_pretrained(r"C:\Users\omsaw\OneDrive\Desktop\College Documents\MajorProject\TechStart\fastapi_slm\SLM_MERGED")

print("Tokenizer restored successfully!")