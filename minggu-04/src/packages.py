#import permodul
import sound.effects.echo
#load modul sound.effecs.echo
sound.effectcs.echo.echofilter(input, output, delay=0.7, atten=4)
#alternatif import sub modul
from sound.effects import echo
echo.echofilter(input, outpur, delay=0.7, atten=4)
#bentuk lain import fungsi atau variabel scr langsung
from sound.effects.echo import echofilter
#bisa panggil langsung echofilter()
echofilter(input, output, delay=0.7, attend=4)
