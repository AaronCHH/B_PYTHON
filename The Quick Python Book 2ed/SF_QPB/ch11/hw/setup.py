
from distutils.core import setup #引入Distutils
import py2exe #引入py2exe
##視需要引入其它的package(剛剛你記下來的那些package)

setup(
  windows = [{'script': "hw.py"}]
  # console=['hw.py']
) #指定要轉換的程式檔名和程式類型
