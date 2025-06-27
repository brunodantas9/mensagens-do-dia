from bottle import template, TEMPLATE_PATH
import os


class Application:
    def render(self, tpl, **kwargs):
        base_path = os.path.dirname(os.path.abspath(__file__))
        templates_path = os.path.join(base_path, '../templates')
        if templates_path not in TEMPLATE_PATH:
            TEMPLATE_PATH.insert(0, templates_path)
        return template(tpl, **kwargs)
