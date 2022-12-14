from models.Bert import BERT as Bert
from models.Roberta import ROBERTA as Roberta
from models.Electra import ELECTRA as Electra
def load_model(type: str):
    if type=='bert':
        return Bert
    elif type == 'roberta':
        return Roberta
    elif type == 'electra':
        return Electra
    else:
        raise Exception('Select the correct model type. Currently supporting only T5 and GPT2.')