pelican content -s publishconf.py
cp ../CNAME output/CNAME
ghp-import output -b master
git push origin master
