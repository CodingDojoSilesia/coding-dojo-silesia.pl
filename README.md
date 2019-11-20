# Coding Dojo Silesia Website

## General Project Description

We are working on Coding Dojo Silesia website to spread the information about greatest event in Upper Silesia. If you want to contribute you are warmly welcomed, all details you can find at [CONTRIBUTING.md file](https://github.com/CodingDojoSilesia/coding-dojo-silesia.pl/blob/master/CONTRIBUTING.md).

## install

```bash
# venv or sth (python mastah)
git submodule update --init
pip install -r requirements.txt
pelican content  # tada - your content is in output dir
```

## What is editable?

* `content` dir
* `pelicanconf.py` file

## Still confused?

* https://docs.getpelican.com/en/stable/
* https://docs.getpelican.com/en/stable/content.html

## Dev mode

```
pelican --listen
```

This command create a devserver on localhost:8000

Warning: you still need `pelican content` command to generate content
