from django import template


register = template.Library()

CENSORED_WORDS = [
   "The", "of",
]

@register.filter()
def censor(value):
    censored = ""
    for word in value.split():
        if word in CENSORED_WORDS:
            cens = "*"*(len(word)-1)
            word = f'{word[0]}{cens}'
        
        censored += f"{word} "
       

    return censored.rstrip()