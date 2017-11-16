# -*- coding: utf-8 -*-

sample_text = """11 are directed at achievin;
nf respect”. It must preva
1 running of the enterprise
agreements and judicioL"""

from spellCheck import my_spell_checker as msc

def correct_para(input_text):
    my_text = input_text.split()
    final_string=''
    for item in my_text:
        final_string = final_string+' '+msc.correction(item.strip())+' '
    return final_string
