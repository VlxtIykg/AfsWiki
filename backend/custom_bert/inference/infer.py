from transformers import BertTokenizer
import torch
import sys
sys.path.append('../models')
from model import load_model

def answer_question(question, context, model, tokenizer):
    inputs = tokenizer.encode_plus(question, context, add_special_tokens=True, return_tensors='pt')
    input_ids = inputs['input_ids'].tolist()[0]

    text_tokens = tokenizer.convert_ids_to_tokens(input_ids)
    model.eval()
    with torch.no_grad():
        outputs = model(**inputs)

    answer_start = torch.argmax(outputs.start_logits)
    answer_end = torch.argmax(outputs.end_logits)

    answer = tokenizer.convert_tokens_to_string(tokenizer.convert_ids_to_tokens(input_ids[answer_start:answer_end+1]))
    return answer

if __name__ == "__main__":
    model_path = '../training/results'
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    model = load_model(model_path)

    # Example question
    question = "What are demonic fruits for?"
    context = "Demonic fruits are used to create demonic avatar, demonic units, shinying demonic units, talenting demonic units, and evolving demonic units."
    print(answer_question(question, context, model, tokenizer))

