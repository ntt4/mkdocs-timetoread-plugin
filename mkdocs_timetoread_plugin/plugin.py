import math
import re

from mkdocs.config import config_options, Config
from mkdocs.plugins import BasePlugin

class TimeToRead(BasePlugin):

    page_time_dict = {}
    page_skip_dict = {}


    config_scheme = (
        ('wpm', config_options.Type(int, default=255)),
        ('allPages', config_options.Type(bool, default=True)),
        ('textColor', config_options.Type(str, default="bdbdbd")),
        ('substitute', config_options.Type(str, default="</h1>")),

    )


    def time(self, text, wpm):
        time = int(math.ceil(len(re.split(re.compile(r'\W+'), text.strip())) / wpm))
        return time


    def on_page_markdown(self, markdown, page, config, files):
        wpm = self.config['wpm']
        all_pages = self.config['allPages']            

        if 'timetoread' in page.meta.keys() and False in page.meta.values():
            key_value = {page.url : False}
            self.page_time_dict.update(key_value)
            return markdown

        if all_pages == True or 'timetoread' in page.meta.keys() and True in page.meta.values():
            self.result = self.time(markdown, wpm)
            key_value = {page.url : self.result}
            self.page_time_dict.update(key_value)
            return markdown

        else:
            return markdown


    def on_post_page(self, output: str, page, config: Config):
        text_color = self.config['textColor']
        sub = self.config['substitute']

        for key, value in self.page_time_dict.items():
            if key == page.url:
                if value > 1:
                    wanted = f'</h1><p style="color:#{text_color}"><i>Estimated time to read: {value} minutes</i></p>\n'
                elif value == 1:
                    wanted = f'</h1><p style="color:#{text_color}"><i>Estimated time to read: {value} minute</i></p>\n'
                elif value == False:
                    return output
                else: 
                    return output

                if sub in output:
                    where = [m.start() for m in re.finditer(sub, output)][0]
                    before = output[:where]
                    after = output[where:]
                    after = after.replace(sub, wanted, 1)
                    output = before + after
        
                return output
