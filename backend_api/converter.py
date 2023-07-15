from transformers import pipeline
import math

MODELS = {
    'news': ('ccdv/lsg-bart-base-16384-mediasum', 16384),
    'book': ('pszemraj/led-base-book-summary', 16384),
    'general': ('google/bigbird-pegasus-large-bigpatent', 4096),
    'scientific': ('google/bigbird-pegasus-large-arxiv', 4096)
}

def summary(text, type):
    summarizer = pipeline('summarization', model=MODELS[type][0])
    max_characters = 4 * (MODELS[type][1] - 2)
    split_amt = math.ceil(len(text)/max_characters)
    input_arr = [text[(i-1)*max_characters:i*max_characters] for i in range(1, split_amt + 1)]
    output_arr = []
    for chunk in input_arr:
        min_len = int((len(chunk)/4)*0.25)
        max_len = int(min_len*1.1)
        output_arr.append(summarizer(chunk, min_length = min_len, max_length = max_len)[0]['summary_text'])
    return ' '.join(output_arr)


def summary2(text, type):
    summarizer = pipeline('summarization', model=MODELS[type][0])
    min_len = int(len(text)/16)
    max_len = int(min_len*1.1)
    output = summarizer(text, min_length=min_len, max_length=max_len)[0]['summary_text']
    return output

        



    
