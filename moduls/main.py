import myModule
myModule.do1()

from myModule import do2
do2()

from myModule import *
do1()
do2()
do3()