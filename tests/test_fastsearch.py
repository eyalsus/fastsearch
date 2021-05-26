import re
from fastsearch import FastSearch

def test_simple_pattern():
    delim_pattern = re.compile(r'\+')
    search = FastSearch(delim_pattern, 3)
    search.add_sentence('1234+56789+abcdefg', {'fun': 1})
    search.add_sentence('bbbb+cccc+ddd', {'fun': 2})
    search.fit()
    assert len(search.lookup('aaaaa12aaaa', one_match=True)) == 0 
    assert len(search.lookup('aaaadefaaa', one_match=True)) == 1 
    assert len(search.lookup('aaaad234aaa', one_match=True)) == 1 
    assert len(search.lookup('aaaad34aaa', one_match=True)) == 0 
    assert len(search.lookup('aaaa89abaa', one_match=True)) == 0 
    assert len(search.lookup('aaaa89ddds', one_match=True)) == 1 