from __future__ import print_function
import Utils
import config


# print(read_file("C:\\Users\\yodeb\\Desktop\\haptik-assignments\\data\\chats.txt"))

# test_str = ("<John>: its the next big thing\n"
# 	"<Adam>: yea, and the backend building for chatbots is super exicting\n"
# 	"<Steve>: who all are in the chatbot space today\n"
# 	"<Ram>: Haptik is the one I know")

# matches = re.finditer(regex, test_str, re.MULTILINE)

# for matchNum, match in enumerate(matches, start=1):
    
#     print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
    
#     for groupNum in range(0, len(match.groups())):
#         groupNum = groupNum + 1
        
#         print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))


def most_active_person(assertvalue=None, test=False):
    # Question 1
    content = Utils.Utils.read_file(config.CHATFILEPATH)
    regex = config.REGEX
    count = config.COUNT
    
    names = Utils.Haptik.get_namedict(chat_lines=content, regex=regex)
    most_active = Utils.Haptik.maxValuefromDict(names=names, ncount=count)
    print(most_active)

    if test==True and len(assertvalue):
        try:
            assert most_active == assertvalue
        except AssertionError as e:
            print(e)
            print("test_failed!")


def test():
    most_active_person()





test()