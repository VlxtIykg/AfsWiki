import json
import torch
from transformers import BertTokenizer

def load_dataset(path):
    with open(path) as f:
        return json.load(f)

def preprocess_data(qa_data, tokenizer, max_len=128):
    inputs = {'input_ids': [], 'attention_mask': [], 'start_positions': [], 'end_positions': []}
    for item in qa_data:
        question = item['question']
        answer = item['answer']
        
        # Encode the question and answer
        encoding = tokenizer.encode_plus(
            question,
            answer,
            add_special_tokens=True,
            max_length=max_len,
            return_token_type_ids=False,
            padding='max_length',
            truncation=True,
            return_attention_mask=True,
            return_tensors='pt'
        )
        
        # Find start and end positions of the answer within the encoded tokens
        input_ids = encoding['input_ids'].flatten()
        answer_ids = tokenizer.encode(answer, add_special_tokens=False, return_tensors='pt').flatten()

        # Find the start and end index of the answer within the input_ids
        start_idx = (input_ids == answer_ids[0]).nonzero(as_tuple=True)[0].item()
        end_idx = start_idx + len(answer_ids) - 1

        inputs['input_ids'].append(input_ids)
        inputs['attention_mask'].append(encoding['attention_mask'].flatten())
        inputs['start_positions'].append(torch.tensor(start_idx))
        inputs['end_positions'].append(torch.tensor(end_idx))
    
    inputs = {key: torch.stack(val) for key, val in inputs.items()}
    return inputs

if __name__ == "__main__":
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    qa_data = load_dataset('../data/qa_dataset.json')
    inputs = preprocess_data(qa_data, tokenizer)
    print(inputs)