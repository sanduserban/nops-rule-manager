vpath %.css public/static/css
vpath %.styl stylus
vpath %.plim src

.css:
	mkdir -p .css

public/%.html: src/%.plim src/defs.plim
	@echo Compiling $< to $@
ifeq ($(DEBUG),1)
	@pudb3 $$(which plimc) -H -p extensions:svg -o $@ $<
else
	@plimc -H -p extensions:svg -o $@ $<
endif

app.css: stylus/*.styl

css: public/static/css/app.css
html: public/index.html
all: html css

build: export NODE_ENV=production
build: export PYTHONWARNINGS=ignore
build: all

dev: export SHELL=$$(which fish)
dev: export NODE_ENV=development
dev: export TAILWIND_MODE=build
dev: export PYTHONWARNINGS=ignore
dev:
	@trap "pkill -9 -f -l 'netlify|livereload|/bin/sh -c livereload'" INT EXIT && \
		livereload --wait 1 --host 0.0.0.0 -t public & \
		rg --files --type-add 'plim:*.plim' -t plim -t stylus | entr ${ENTR_ARGS} -s 'make all'

watch: export NODE_ENV=development
watch: export TAILWIND_MODE=build
watch: export PYTHONWARNINGS=ignore
watch:
	rg --files --type-add 'plim:*.plim' -t plim -t stylus | entr ${ENTR_ARGS} -s 'make all'

server: export NODE_ENV=development
server: export TAILWIND_MODE=build
server: export PYTHONWARNINGS=ignore
server:
	hug -f server.py

clean:
	rm public/*.html public/static/css/*

python-deps:
	pip install -r requirements.txt
netlify-deps:
	npm i -g netlify-cli
node-deps:
	yarn add postcss-cli@latest tailwindcss@latest postcss@latest autoprefixer@latest stylus@latest
deps: python-deps node-deps netlify-deps

public/static/css/%.css: export TAILWIND_MODE=build
public/static/css/%.css: %.styl $(wildcard stylus/*.styl) .css tailwind.config.js $(wildcard public/*.html)
	@echo Compiling $< to $@
	@npx stylus -u rupture -c -m -o .css/ $<
	@npx postcss --map -o $@ .css/$*.css
	cp $@ public/static/css/$*.$$(python -c "import hashlib; print(hashlib.sha256(open('$@', 'rb').read()).hexdigest());").css
