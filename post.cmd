python zh_to_en.py
hugo --gc --minify --cleanDestinationDir
git add .
git commit -m "modify posts"
git push