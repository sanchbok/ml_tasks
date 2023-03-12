import utils


def test_word_count():
    ''' Simple words counter '''
    texts = ['some random piece of text', 'text']
    count = utils.word_count(texts)
    assert count == {'some': 1, 'random': 1, 'piece': 1, 'of': 1, 'text': 2}


def test_word_count_tricky():
    ''' Tricky words counter '''
    texts = ['some random piece of text', 'text']
    count = utils.word_count(texts)
    assert count == {'some': 1, 'random': 1, 'piece': 1, 'of': 1, 'text': 2}
