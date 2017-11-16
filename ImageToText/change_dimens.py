from difflib import SequenceMatcher

a = [u'THE [ES-GATE ACADEMY has\nbook.\
     In spite of this, if any in;\nACADEMY\
     owes no responsibility\npointed out along with other suggest',

     u'.CADEMY has taken utmost care in\nEMS,\
     if any inaccuracy or printing\n\n:.0 responsibility.\
     THE IES-GATE AC\nth other suggestions for improvement c',
     
     u':ollecting data before publishing thi\n:rror\
     occurs then THE IES-GATE\nADEMY shall be grateful\
     if these ar\nf this book. \u2018']


def change_dimen(input_list):
    temp_list = []

    for i,item in enumerate(input_list):
        temp_list.append(item.split('\n'))
    changed_list = list(zip(*temp_list))
    return changed_list

def words(text):
    return re.findall(r'\w+', text.lower())



def match_two(string1,string2):
    match = SequenceMatcher(None, string1,\
                            string2).find_longest_match\
                            (0, len(string1), 0, len(string2))
    if match.a>len(string1)/2:
        return (string1[: match.a + match.size]+string2[match.b + match.size:]) 
    else:
        return string1 + ' '+ string2



