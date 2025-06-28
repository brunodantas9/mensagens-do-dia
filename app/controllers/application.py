from bottle import template

def render(tpl, **kwargs):
    return template('base', tpl=tpl, **kwargs)

