from transformers import BertForQuestionAnswering

def load_model(model_path=None):
    if model_path:
        model = BertForQuestionAnswering.from_pretrained(model_path)
    else:
        model = BertForQuestionAnswering.from_pretrained('bert-base-uncased')
    return model

if __name__ == "__main__":
    model = load_model()
    print(model)

