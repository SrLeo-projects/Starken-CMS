from django.shortcuts import render

# models.TextField value convert to p tags with class="text-muted", last one with class="text-primary"
def text_to_p(text):
    return ''.join(['<p class="text-muted">{}</p>'.format(p) for p in text.splitlines()[:-1]]) + '<p class="text-primary">{}</p>'.format(text.splitlines()[-1])