# MaskMix

This is the script used in Montinaro et al. 2016 *"Complex Ancient Genetic Structure and Cultural Transitions in Southern African Populations"* (Genetics).

Basically, the program takes beagle file and PCAdmix output and return a masked Beagle in which only one ancestry is kept.

### Requirements
The software is written following the python 3.5+ syntax.
the argparse and sys python modules must be installed.

### Usage (See TEST files for examples)
python MaskMix --viterbi [filename] --markers [filename] --beagle [filename] --ancestry [number of the ancestry to keep] --out [name of the output]


Please be aware that this script has not be fully tested, therefore there may be bugs or inconsistencies. Moreover, it will not give you error messages if the files are poorly formatted.

### Future development

Considering that beagle 3.x is not longer commonly used, I will soon develop a similar tool using VCF inputs and RFMIX outputs. For any enquiries please contact francesco.montinaro[at].gmail.com  
