import re
import jieba
import pynlpir

pynlpir.open()

# 设置使用古文分词库

def read_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

confucian_text = read_text('Analects.txt')
daoist_text = read_text('daodejing.txt')


def clean_text(text):
    # 移除非中文字符
    text = re.sub(r'[^\u4e00-\u9fff]', '', text)
    # 移除多余的空白
    text = re.sub(r'\s+', ' ', text).strip()
    return text

confucian_text_clean = clean_text(confucian_text)
daoist_text_clean = clean_text(daoist_text)

def tokenize(text):
    return list(jieba.cut(text))

confucian_tokens = tokenize(confucian_text_clean)
daoist_tokens = tokenize(daoist_text_clean)

def save_cleaned_text(text, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(text)

# 保存清理后的儒家文本
save_cleaned_text(confucian_text_clean， 'confucian_cleaned.txt')

# 保存清理后的道家文本
save_cleaned_text(daoist_text_clean, 'daoist_cleaned.txt')

def tokenize_with_pynlpir(text):
    # 使用 pynlpir 进行分词，只保留词语而不保留词性标注
    return [word for word, pos in pynlpir.segment(text) if word.strip()]

confucian_tokens = tokenize_with_pynlpir(confucian_text_clean)
daoist_tokens = tokenize_with_pynlpir(daoist_text_clean)

def save_tokenized_text(tokens, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(' '.join(tokens))

# 保存分词后的儒家文本
save_tokenized_text(confucian_tokens,  'confucian_tokenized.txt')

# 保存分词后的道家文本
save_tokenized_text(daoist_tokens,  'daoist_tokenized.txt')

pynlpir.close()
