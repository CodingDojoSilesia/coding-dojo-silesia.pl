from markdown.preprocessors import Preprocessor
from markdown import Extension
import re


class SectionPreprocessor(Preprocessor):
    END_SECTION_LINES = ['</div>', '</section>']
    section_pattern = re.compile(r'### +([\w-]+ +)?SECTION +###', re.IGNORECASE)

    def run(self, lines):
        state = 'START'
        new_lines = []
        for line in lines:
            match = self.section_pattern.match(line.strip())
            if not match:
                new_lines.append(line) 
                continue
            section_name = (match.group(1) or '').strip()
            state, additional_lines = self.get_next_line(state, section_name)
            new_lines += additional_lines
        if state is not None:  # close sections
            new_lines += self.END_SECTION_LINES
        return new_lines

    def get_next_line(self, state, section_name):
        prefix = self.END_SECTION_LINES if state != 'START' else []

        def section(classes=None):
            if classes is None:
                lines = ['<section markdown="1">', '<div>']
            else:
                lines = [f'<section class="{classes}" markdown="1">', '<div>']
            return prefix + lines

        if section_name:
            if section_name == 'RED':
                return 'RED', section('red')
            if section_name in 'RED-PATTERN':
                return 'RED', section('red pattern')
            if section_name in 'RED-PATTERN-2':
                return 'RED', section('red pattern-2')
            if section_name == 'WHITE':
                return 'WHITE', section()
            if section_name == 'END':
                return 'END', prefix
        else:
            if state == 'RED':
                return 'WHITE', section()
            if state in ['WHITE', 'START']:
                return 'RED', section('red')
        return 'END', []  # fallback


class DojoExtension(Extension):
    def extendMarkdown(self, md):
        md.preprocessors.register(SectionPreprocessor(md), 'section-preprocessor', 175)


makeExtension = DojoExtension # need to register extension
