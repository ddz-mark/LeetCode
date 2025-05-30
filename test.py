# tokenizer = BPETokenizer()
#
# corpus = "ab bc bcd ce"
# tokenizer.train(text=corpus, num_merges=3)

# 26个字母+空格

from collections import Counter


def bpe(text, num_merges):

    # 统计词频
    vocab = {}
    word_frep = {}
    for c in text.split():
        if not word_frep.get(c):
            word_frep[c] = 1
        else:
            word_frep[c] += 1

    count = 0
    while count < num_merges:
        # 计算pair对
        pairs = {}
        for word, frep in word_frep.items():
            for i in range(len(word) - 1):
                p = (word[i], word[i+1])
                pairs[p] += frep

        # 合并
        max_pair = max(pairs)
        vocab[max_pair] = len(vocab.keys())

        # 更新词频
        new_word_frep = {}
        for word, frep in word_frep.items():
            new_word_frep[max_pair] = vocab[max_pair]
            index1 = vocab[max_pair[0]]
            index2 = vocab[max_pair[1]]
            del index1, index2

        count += 1


if __name__ == '__main__':
    corpus = "ab bc bcd ce"
    bpe(corpus, 3)
