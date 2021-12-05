module="turtles/charset"
rm -f "$module.*"

# rewrite character set
./run.sh rewrite 'temp' 
temp=`cat temp`

# expand template
gsed -i -r "s/@/$temp/" "$module.template"

# replace module
mv "$module.template" "$module.py"

# cleanup formatting
black "$module.py"
gsed -i -r "s/\"(Path[^\"]*)\"/\1/g" "$module.py"
gsed -i -r "s/\"(.*)\"/'\1'/g" "$module.py"

# test new character set
./run.sh news
