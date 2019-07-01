# perpared ttf
    cd fonts
    mv *.ttf /usr/share/fonts/truetype
    cd /usr/share/fonts/truetype
    mkfontscale
    mkfontdir
    fc-cache
    xset fp rehash
    https://gist.github.com/matthewhartman/7b1661dbe6ff26a231e4