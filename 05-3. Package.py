import sys
sys.path.append("/Users/songjaehyeok/Documents/Python/Jump to Python/game")

# 모듈이 포함되도록 import

#import game.sound.echo
#game.sound.echo.echo_test()

#from game.sound import echo
#echo.echo_test()

#from game.sound.echo import echo_test
#echo_test()

from game.sound import *   # sound 폴더에 있는 __init__.py 파일에 __all__ = ['echo'] 추가
echo.echo_test()


from game.graphic.render import render_test
render_test()