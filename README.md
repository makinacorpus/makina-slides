# Contributing

## Installation

    virtualenv venv
    source venv/bin/activate
    git clone https://github.com/makinacorpus/makina-slides.git
    cd makina-slides
    pip install landslide
    pip install watchdog

## Good practice

* Please create your `*.cfg` and source files in an appropriate directory
(it may already exist)
* Always make your path is relative to root directory and thus run `landslide`
from it
* If applicable, update `index.html` with the link to you new slides

## Example config file

Let's take an example `mydomain/myconfig.cfg`

    [landslide]
    theme = assets/theme
    source = mydomain/myslides.md
    destination = docs/1-initiation-django.html
    relative = True
    embed = True
    linenos = no
    css = mydomain/css/mycustom.css
    js = mydomain/js/mycustom.js

* _theme_: must always be the same
* _source_: can be one or mutliple Markdown or RestructuredText files, relative
to root
* _destination_: relative to root, always generate in `docs/` directory
* _relative_: keep this option
* _embed_: this option will embed images (recommended)
* _linenos_: display line numbers in code blocks
* _js_ and _css_: you can add your own files here in addition to theme,
these will be embed

More documentation at <https://github.com/adamzap/landslide>

Next, just run:

	  lanslide mydomain/myconfig.cfg

## Publishing

Presentation are served under http://makinacorpus.github.io/makina-slides/

## Theming

If you need to change the style of all slides (on screen and print), edit
`assets/lanslide_theme/css/makina.css`.
If you need to change the style of all slides (on screen only), edit
`assets/lanslide_theme/css/screen.css`.
If you need to change the style of all slides (on print only), edit
`assets/lanslide_theme/css/print.css`.

## Structure

    ├── assets          --> symbolic link to docs/assets, for generation purposes
    ├── docs            --> Github delivery root
    │   ├── assets      --> Assets directory
    │   │   └── theme   --> landslide theme root
    │   │       ├── js
    │   │       └── css
    │   ├── index.html  --> home page, not generated
    │   └── *.html      --> presentation files
    └── *               --> any other directory containing *.cfg files

# Usage

## Notes

Add notes to your slides using the `.notes:` keyword, eg.:

    # My Slide Title

    .notes: These are my notes, hidden by default

    My visible content goes here

You can toggle display of notes by pressing the `2` key.

You can also add presenter notes to each slide by following the slide content
with a heading entitled "Presenter Notes". Press the 'p' key to open the
presenter view.

## Shortcuts while viewing

- Press `h` to toggle display of help
- Press `left arrow` and `right arrow` to navigate
- Press `t` to toggle a table of contents for your presentation. Slide titles
  are links
- Press `ESC` to display the presentation overview (Exposé)
- Press `n` to toggle slide number visibility
- Press `b` to toggle screen blanking
- Press `c` to toggle current slide context (previous and next slides)
- Press `e` to make slides filling the whole available space within the
  document body
- Press `S` to toggle display of link to the source file for each slide
- Press '2' to toggle notes in your slides (specify with the .notes macro)
- Press '3' to toggle pseudo-3D display (experimental)
- Browser zooming is supported


## Exporting to PDF

## Slide styles

Some slide styles are also available using `.fx: foo bar` will add the
`foo` and `bar` classes to the corresponding slide `<div>` element.

Available classes for makina theme are:

* `quoteslide`: slide with a single quote
* `alternate`: pink title, useful for subparts or exercices
* `titleslide`: h1 + h2 on same slide, centered
* `smaller`: smaller text (not title)
* `larger`: larger text (not title)
* `imageslide`: single image covering all slide
