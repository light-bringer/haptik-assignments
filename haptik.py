from __future__ import print_function
import Utils
import config



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
            print("Test passed")
        except AssertionError as e:
            print(e)
            print("test_failed!")


def test():
    # Question 1 
    most_active_person()
    most_active_person(assertvalue=['John', 'Ram', 'Adam'], test=True)
    most_active_person(assertvalue=['John', 'Ram'], test=True)





test()