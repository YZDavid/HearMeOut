from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import nltk
from gtts import gTTS

checkpoint = "facebook/bart-large-cnn"
tokenizer = AutoTokenizer.from_pretrained(checkpoint)
model = AutoModelForSeq2SeqLM.from_pretrained(checkpoint)
try:
    nltk.data.find("tokenizers/punkt")
except LookupError:
    nltk.download("punkt")
MAX_LENGTH = tokenizer.max_len_single_sentence

def summary(text):
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
        min_len = int(chunks_len[i]/4)
        max_len = int(min_len*1.1)
        generated = model.generate(**tokens[i], min_length = min_len, max_length = max_len)
        output.append(tokenizer.decode(*generated, skip_special_tokens=True))
    return ' '.join(output)

def make_audio(text, filename):
    tts_file = gTTS(text, lang="en")
    tts_file.save(f"summary_files/{filename}.mp3")




