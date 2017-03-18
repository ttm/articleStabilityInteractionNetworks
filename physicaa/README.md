# Source files
Of the article 'Stability of human interaction networks' for Physica A

## Obtaining the PDF file from these sources
Execute the following commands:
  $ pdflatex elsarticle-template.tex
  $ bibtex elsarticle-template.aux
  $ pdflatex elsarticle-template.tex
  $ pdflatex elsarticle-template.tex

The resulting PDF is elsarticle-template.pdf
## Figures
Are at the figs/ directory

## Tables
Are either on elsarticle-template.tex or on the tables/ directory

## Producing a zip file
Use the following command: 
  $ zip -r sources.zip elsarticle-template.tex supportingInformation.aux tables/tab1Overview.tex figs/criaRede3_.png figs/fser___.png tables/tab2TimeLAD___.tex tables/tabHoursCPP_.tex tables/tabWeekdays.tex tables/tabMonthdaysMET.tex tables/tabMonthsLAU.tex figs/InText-WLAU-S1000__.png tables/userTab.tex tables/tabPCA3CPP.tex figs/im13PCAPLOT___.png figs/mpgamma2__.png paper.bib README.md
