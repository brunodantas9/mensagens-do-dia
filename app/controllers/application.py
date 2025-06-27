import os
from bottle import TEMPLATE_PATH, template

# Caminho absoluto para a pasta templates
TEMPLATE_PATH.insert(0, os.path.join(
    os.path.dirname(__file__), '../templates'))


def render(tpl, **kwargs):
    return template(tpl, **kwargs)
