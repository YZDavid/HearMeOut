from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import nltk
from gtts import gTTS
from newspaper import Article

checkpoint = "facebook/bart-large-cnn"
tokenizer = AutoTokenizer.from_pretrained(checkpoint)
model = AutoModelForSeq2SeqLM.from_pretrained(checkpoint)
try:
    nltk.data.find("tokenizers/punkt")
except LookupError:
    nltk.download("punkt")
MAX_LENGTH = tokenizer.max_len_single_sentence

def summary(text, percentage=None):
    # If percentage was passed in, set it as a floating value from 0.05 to 0.95
    if percentage:
        percentage = percentage / 100
    sentences = nltk.tokenize.sent_tokenize(text)
    length = 0
    chunk = ""
    chunks = []
    chunks_len = []
    count = -1
    for sentence in sentences:
        count += 1
        combined_length = len(tokenizer.tokenize(sentence)) + length
        if combined_length <= MAX_LENGTH:
            chunk += sentence + " "
            length = combined_length
            if count == len(sentences) - 1:
                chunks.append(chunk.strip())
                chunks_len.append(combined_length)
        
        else:
            chunks.append(chunk.strip())
            chunks_len.append(combined_length)
            length = 0
            chunk = sentence + " "
            length = len(tokenizer.tokenize(sentence))

    tokens = [tokenizer(chunk, return_tensors="pt") for chunk in chunks]
    output = []
    
    for i in range(len(tokens)):
        if percentage:
            min_len = int(chunks_len[i]*percentage)
            max_len = int(min_len*1.1)
            generated = model.generate(**tokens[i], min_length = min_len, max_length = max_len)
        else:
            generated = model.generate(**tokens[i])
        output.append(tokenizer.decode(*generated, skip_special_tokens=True))
    return ' '.join(output)

def url_summary(url):
    article = Article(url)
    article.download()
    article.parse()
    original_length = len(article.text)
    article.nlp()
    return (original_length, article.summary)

def make_audio(text, filepath):
    tts_file = gTTS(text, lang="en")
    tts_file.save(filepath)




