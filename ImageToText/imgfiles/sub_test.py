from difflib import SequenceMatcher



def match_two(string1,string2):
    match = SequenceMatcher(None, string1,\
                            string2).find_longest_match\
                            (0, len(string1), 0, len(string2))
    print(match)
    if match.size>1:
        s= string1[: match.a + match.size]+string2[match.b + match.size:]
        print(s)
        return (s) 
    else:
        return string1+' '+string2


def change_dimen(input_list):
    temp_list = []

    for i,item in enumerate(input_list):
        temp_list.append(item.split('\n'))
    b = list(zip(*temp_list))
    return b
    

def accuracy_1(az):
    for item in az:
        #print(item)
        final_string=''
        for i,sub_item in enumerate(item):
            #print(i,sub_item)
            if i==0:
                final_string=sub_item
            else:
                final_string = match_two(final_string,sub_item)
        print(final_string)

