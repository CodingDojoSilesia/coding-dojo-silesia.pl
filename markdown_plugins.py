from markdown.preprocessors import Preprocessor
from markdown import Extension
import re


class DojoPreprocessor(Preprocessor):
    END_LINES = []
    pattern = re.compile(r'---', re.IGNORECASE)

    def run(self, lines):
        state = 'START'
        new_lines = []
        for line in lines:
            match = self.pattern.match(line.strip())
            if not match:
                new_lines.append(line) 
                continue
            section_name = match.group(1)
            state, additional_lines = self.get_next_line(state, section_name)
            new_lines += additional_lines
        if state is not None:  # close sections
            new_lines += self.END_LINES
        return new_lines

class SectionPreprocessor(DojoPreprocessor):
    END_LINES = ['</div>', '</section>']
    pattern = re.compile(r'### +([\w-]+ +)?SECTION +###', re.IGNORECASE)

    def get_next_line(self, state, section_name):
        prefix = self.END_LINES if state != 'START' else []

        def section(classes=None):
            if classes is None:
                lines = ['<section markdown="1">', '<div>']
            else:
                lines = [f'<section class="{classes}" markdown="1">', '<div>']
            return prefix + [''] + lines

        if section_name:
            section_name = section_name.strip().upper()
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


class ColPreprocessor(DojoPreprocessor):
    END_LINES = ['</div>']
    pattern = re.compile(r'### +([\w-]+) +COL +###', re.IGNORECASE)

    def get_next_line(self, state, section_name):
        section_name = section_name.lower()
        prefix = self.END_LINES if state != 'START' else []
        if section_name == 'end':
            return 'START', prefix
        return 'SET', prefix + [''] + [f'<div class="col-{section_name}" markdown="1">']


class DojoExtension(Extension):
    def extendMarkdown(self, md):
        md.preprocessors.register(SectionPreprocessor(md), 'section-preprocessor', 175)
        md.preprocessors.register(ColPreprocessor(md), 'col-preprocessor', 170)


makeExtension = DojoExtension # need to register extension
