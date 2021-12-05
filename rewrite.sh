module="turtles/charset.py"
rm -f $module 
./run.sh rewrite 'temp' 
temp=`cat temp`
gsed -i -r "s/@/$temp/" $module 
black $module 
gsed -i -r "s/\"(Path[^\"]*)\"/\1/g" $module 
gsed -i -r "s/\"(.*)\"/'\1'/g" $module 
./run.sh news
