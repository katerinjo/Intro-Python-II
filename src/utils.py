# printing tools for basically every component

from textwrap import fill

def color(text, shade):
    chosen = {
        'red': '\u001b[31m',
        'green': '\u001b[32m',
        'blue': '\u001b[34m',
        'yellow': '\u001b[33m'
    }[shade]
    return chosen + text + '\u001b[0m'

def log(*paragraphs, shade=None):
    if shade is not None:
        out_text = [color(p, shade) for p in paragraphs]
    else:
        out_text = paragraphs
    print('\n'.join(fill(p) for p in out_text))
