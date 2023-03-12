def word_count(batch, count={}):
    ''' Words counter '''
    count_copy = count.copy()
    for text in batch:
        for word in text.split():
            count_copy[word] = count_copy.get(word, 0) + 1
    return count_copy
