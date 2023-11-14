from lib.grammar_stats import *
def test_grammar_stats():
    grammar_stats = GrammarStats()
    pass

def test_check_true():
    grammar_stats=GrammarStats()
    result = grammar_stats.check('Hello world!')
    assert result == True

def test_check_false():
    grammar_stats=GrammarStats()
    result = grammar_stats.check('hello world,')
    assert result == False

def test_percentage_good():
    grammar_stats=GrammarStats()
    result_wrong = grammar_stats.check('hello world,')
    result_right = grammar_stats.check('Hello world!')
    percentage = grammar_stats.percentage_good()
    assert percentage == 50
