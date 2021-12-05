module="turtles/charset"
rm -f "$module.*"
./run.sh rewrite 'temp' 
temp=`cat temp`
gsed -i -r "s/@/$temp/" "$module.template"
mv "$module.template" "$module.py"
black "$module.py"
gsed -i -r "s/\"(Path[^\"]*)\"/\1/g" "$module.py"
gsed -i -r "s/\"(.*)\"/'\1'/g" "$module.py"
./run.sh news
