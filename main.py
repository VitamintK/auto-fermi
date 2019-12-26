# best fermi problems:
# 
# classics:
# circumference/radius/volume of the Earth
# piano tuners in new york
# energy released at Trinity
#
# from scioly:
# How many atoms of iron are there in a sewing needle?
# How many gas molecules are there in the earth's atmosphere
# How many sodium ions are in one tablespoon of salt?
# How many kilometres of D.N.A. are there in the cells of one human body?
# How much energy does a horse consume in its lifetime?
# How many joules of chemical energy are there in one litre of gasoline?
# How much has the mass of the human population on the earth increased in the last year?
#
# "how many piano tuners" type
# How many bricks are there in (London)?
# 
# "http://www.rain.org/~rcurtis/fermiq.html"
# How many golf balls will fit in a suitcase?
# How many piano tuners are there in Chicago?
# How many cells are there in a human body?
# How many hairs are there on a human head?
# How many individual frames are needed for a feature length motion picture?
# What is the ratio of spacing between gas molecules to molecular diameter in a gas at standard temperature and pressure?
# How many seconds are there in a year?
# If your life earnings were doled out to you by the hour, how much is your time worth per hour?
# What is the weight of solid garbage thrown away by American families each year?
# How many molecules are in a standard classroom?"

# unfortunately, the most interesting problems don't look like they can be generated on wikipedia
# let's try some less-interesting problems anyways - they could still be fun

# from https://www.lesswrong.com/posts/PsEppdvgRisz5xAHG/fermi-estimates:
# how many used cars sold each year?

import re
from mediawiki import MediaWiki
wikipedia = MediaWiki()

def is_numeric(x):
    # https://en.wikipedia.org/wiki/Wikipedia:Manual_of_Style/Dates_and_numbers
    if x != x.strip():
        raise ValueError("{} is not stripped", x)
    numb_re = r'[0-9,]+\.?[0-9]*[MB]?$'
    currencies = ['$','€','£']
    for currency in currencies:
        if currency in x:
            return bool(re.search(numb_re, x))
    return bool(re.match(numb_re, x))

def is_maybe_year(x):
    if not x.isnumeric():
        return False
    return 1600 <= int(x) <= 2025

def get_punctuationless(x):
    return re.sub(r'([^\w]+$)|(^[^\w]+)', '', x)

x = wikipedia.page("Human")
ans = []
for section in x.sections:
    text = x.section(section)
    pars = text.split('\n')
    for par in pars:
        masked = []
        unmasked = []
        for word in par.split():
            clean_word = get_punctuationless(word)
            if is_numeric(clean_word) and not is_maybe_year(clean_word):
                unmasked.append(word)
                masked.append("XXX")
            else:
                masked.append(word)
        if len(unmasked) > 0:
            ans.append(' '.join(masked))
for a in ans:
    print(a)

# running this on "Human" or "Used car" or "Seawater" works OK