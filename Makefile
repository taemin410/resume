# Makefile for LaTeX Resume

LATEX = pdflatex
RESUME = resume

.PHONY: all clean view help

all: $(RESUME).pdf

$(RESUME).pdf: $(RESUME).tex
	$(LATEX) $(RESUME).tex
	$(LATEX) $(RESUME).tex  # Run twice to ensure proper formatting

clean:
	rm -f $(RESUME).aux $(RESUME).log $(RESUME).out $(RESUME).fdb_latexmk $(RESUME).fls

clean-all: clean
	rm -f $(RESUME).pdf

view: $(RESUME).pdf
	xdg-open $(RESUME).pdf 2>/dev/null || open $(RESUME).pdf 2>/dev/null || start $(RESUME).pdf

help:
	@echo "Available targets:"
	@echo "  all        - Build the resume PDF (default)"
	@echo "  clean      - Remove auxiliary files"
	@echo "  clean-all  - Remove all generated files including PDF"
	@echo "  view       - Open the PDF after building"
	@echo "  help       - Show this help message"

# Default target
.DEFAULT_GOAL := all