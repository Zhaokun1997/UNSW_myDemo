import sys
import re


def isroman(string):
    for i in len(string):
        if string[i] not in ['I', 'V', 'X', 'L', 'C', 'D', 'M']:
            return False
    return True


feedback_str = ["I don't get what you want, sorry mate!", \
                "Hey, ask me something that's not impossible to do! ", \
                "Sure! It is "]
while 1:
    user_input = input('How can I help you?')
    match_obj = re.match(r'Please convert (.*)', user_input)  # 匹配输入的字符串是否符合条件

    try:
        if match_obj:  # 测试输入的字符串是否符合基本条件
            group = match_obj.group(1)
            print(group)
            match_obj_second = re.search(r'(.*) using (.*)', group)
            match_obj_third = re.search(r'(.*) minimally', group)
            if match_obj_second:  # 满足第二种输入条件
                print(match_obj_second.group(), \
                      match_obj_second.group(1), \
                      match_obj_second.group(2))
            elif match_obj_third:  # 满足第三种输入条件
                print(match_obj_second.group(1))
            else:  # 只满足第一种输入条件
                try:
                    if group.isnumeric() or isroman(group):
                        print(group)
                    else:
                        print(feedback_str[1])
                except TypeError:
                    print(feedback_str[1])
        else:
            print(feedback_str[0])
    except ValueError:
        print("Invaild input!")
        sys.exit()
