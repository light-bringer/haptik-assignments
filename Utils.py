import re
import operator
from heapq import nlargest
import Types



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