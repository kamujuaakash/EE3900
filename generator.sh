#!/bin/bash
echo "Enter your Name"
read name
echo "Enter your Github Profile Name"
read gitname
echo "Enter Roll No."
read roll
mkdir charger
cd charger
mkdir codes
mkdir figs
cd codes
wget https://raw.githubusercontent.com/LokeshBadisa/EE3900-Linear-Systems-and-Signal-Processing/main/charger/codes/1.1.py
wget https://raw.githubusercontent.com/LokeshBadisa/EE3900-Linear-Systems-and-Signal-Processing/main/charger/codes/2.3.py
wget https://raw.githubusercontent.com/LokeshBadisa/EE3900-Linear-Systems-and-Signal-Processing/main/charger/codes/2.6.py
python3 1.1.py
python3 2.3.py
python3 2.6.py
cd ..
wget https://raw.githubusercontent.com/LokeshBadisa/EE3900-Linear-Systems-and-Signal-Processing/main/charger/main.tex
sed -i -e s/LokeshBadisa/"$gitname"/g main.tex
sed -i -e s/Lokesh Badisa\\/"$name"/ main.tex
sed -i -e s/AI21BTECH11005 \\/"$roll"/g main.tex
latexmk main.tex -f
evince main.pdf
