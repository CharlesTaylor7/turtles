git clean -f && ./run.sh rewrite && black new_char_set.py && gsed -i -r "s/'(Path.*)'/\1/g" && cat new_char_set.py
