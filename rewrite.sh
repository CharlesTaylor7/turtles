module="turtles/charset"

# rewrite character set
./run.sh rewrite 'temp' 
temp=`cat temp`
echo $temp

# expand template
gsed -i -r "s~return~return $temp~g" "$module.template"
echo "$module.template"

# expanded
cat "$module.template"

# replace module
mv "$module.template" "$module.py"

# cleanup formatting
black "$module.py"
gsed -i -r "s/\"(Path[^\"]*)\"/\1/g" "$module.py"
gsed -i -r "s/\"(.*)\"/'\1'/g" "$module.py"

# test new character set
./run.sh news

# cleanup
rm temp
