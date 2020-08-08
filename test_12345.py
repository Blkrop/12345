import unittest
import 12345


def test_sample_single_word():
    list_ = ('foo', 'bar', 'foobar')
    word = 12345.sample(list_)
    assert word in list_


def test_sample_multiple_words():
    list_ = ('foo', 'bar', 'foobar')
    words = 12345.sample(list_, 2)
    assert len(words) == 2
    assert words[0] in list_
    assert words[1] in list_
    assert words[0] is not words[1]


def test_generate_buzz_of_at_least_five_words():
    phrase = 12345.generate_buzz()
    assert len(phrase.split()) >= 5
