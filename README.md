# Requirements
	git submodule update --init
	git clone git@github.com:makinacorpus/makina-slides.git -b gh-pages www
	pip install landslide

# Slide generation

	lanslide maconfig.cfg

# Publishing

Place your HTML output in the www directory, commit and push to the gh-pages branch.
It will get served under http://makinacorpus.github.io/makina-slides/
