import re
import operator
from heapq import nlargest
import Types
from itertools import chain
import collections
from functools import lru_cache








class Utils(object):
    '''
    # Utility Class with few static methods to do useful work.

    '''

    @staticmethod
    def read_file(filename:str)-> str:
        '''
        Description : takes filename -> str as inut and returns the file contents separated by \n
        Input       : filename-> str
        Output      : filecontent -> str
        
        '''
        
        with open(filename, 'r') as file: 
            data = file.read()
        
        return data


class Haptik(object):

    @staticmethod
    def maxValuefromDict(names: Types.nameDict, ncount: int = 1)->str:
        '''
        Description : Takes a dictionary of name and count and returns back the person with max chats
        Input       : names -> nameDict -> dict {str, int}
        Output      : name -> str

        '''
        # 3key = max(names.items(), key=operator.itemgetter(1))
        keys = nlargest(ncount, names, key=names.get)
        return keys


    @staticmethod
    def get_namedict(chat_lines:str, regex:str)->Types.nameDict:
        '''
        Description : Takes chat content and returns back the count of each person's messages.
        Input       : chat_lines -> str,  regex -> str
        Output      : names -> nameDict -> dict {str, int}

        '''
        names = {}
        matches = re.finditer(regex, chat_lines, re.MULTILINE)
        for matchnum, match in enumerate(matches, start=0):
            name = match.group(1)
            if name not in names.keys():
                names[name] = 1
            else:
                names[name] += 1
        
        return names
    

class Haptik2(object):

    @staticmethod        
    def validate_all_chars(text, words):
        all_chars = set(chain.from_iterable(words))
        return all_chars.issuperset(text)
    
    @staticmethod
    def find_occurrences(pattern: str, text: str):
        idx = 0
        while True:
            idx = text.find(pattern, idx)
            if idx == -1:
                return
            yield idx, idx + len(pattern)
            idx += 1
    

    @staticmethod
    def build_span_graph(text, words):
        all_spans = collections.defaultdict(set)
        spans = (Haptik2.find_occurrences(word, text) for word in words)
        for span in spans:
            for begin, end in span:
                all_spans[begin].add(end)
        return all_spans
    
    
    @staticmethod
    def find_path(spans, length, begin=0, visited=None):
        visited = set() if visited is None else visited
        visited.add(begin)
        ends = spans[begin]
        return length in ends or any(
            Haptik2.find_path(spans, length=length, begin=new_begin, visited=visited)
            for new_begin in ends
            if new_begin not in visited and new_begin in spans
        )
    
    @staticmethod
    def wordBreak(s: str, wordDict:list)-> bool:
        '''
        Description : Takes string and a wordlist to construct the words from the wordlist
        Input       : s -> str,  wordDict -> [str]
        Output      : bool

        '''
        wordDict = set(wordDict)
        if not s or not wordDict:
            return False
        
        @lru_cache(None)
        def check(s):
            if s in wordDict:
                return True
            for i, _ in enumerate(s[1:], 1):
                if s[:i] in wordDict and check(s[i:]):
                    return True
            return False
        
        return check(s)

