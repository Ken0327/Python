try:
    #嘗試執行的程式
    print('Hello World')

except ArithmeticError as n:
    print("跳至ArithmeticError 區塊")
    print("錯誤原因:",n)
except ZeroDivisionError as n:
    print("跳至ZeroDivisionError 區塊")
    print("錯誤原因:",n)
except KeyboardInterrupt:#例外名稱 as 變數名稱:
    #例外發生時執行的程式
    print('Exception')

else:
    #若try沒產生例外則會執行這裡
    print('Else')
finally:
    #不管有沒有發生例外都會跑到的程式
    print('Finally')


#我們真正想得到的例外是ZeroDivisionError ，但由於ArithmeticError的層級在ZeroDivisionError之上
#使用多個except時會建議把細項(最深層)的擺在最前面

# Python內建的例外層級結構
'''
BaseException 
 +--  SystemExit 
 +--  KeyboardInterrupt 
 +--  GeneratorExit 
 +--  Exception 
      +--  StopIteration 
      +--  ArithmeticError 
      |     +--  FloatingPointError 
      |     +--  OverflowError 
      |     +--  ZeroDivisionError 
      +--  AssertionError 
      +--  AttributeError 
      +--  BufferError 
      +--  EOFError 
      +--  ImportError 
      +--  LookupError 
      |     +--  IndexError 
      |     +--  KeyError 
      +--  MemoryError 
      +--  NameError 
      |     +--  UnboundLocalError 
      +--  OSError 
      |     +--  BlockingIOError 
      |     +--  ChildProcessError 
      |     +--  ConnectionError 
      |     |     +--  BrokenPipeError 
      |     |     +--  ConnectionAbortedError 
      |     |     +--  ConnectionRefusedError 
      |     |     +--  ConnectionResetError 
      |     +--  FileExistsError 
      |     +--  FileNotFoundError 
      |     +--  InterruptedError 
      |     +--  IsADirectoryError 
      |     +--  NotADirectoryError 
      |     +--  PermissionError 
      |     +--  ProcessLookupError 
      |     +--  TimeoutError 
      +--  ReferenceError 
      +--  RuntimeError 
      |     +--  NotImplementedError 
      +--  SyntaxError 
      |     +--  IndentationError 
      |          +--  TabError 
      +--  SystemError 
      +--  TypeError 
      +--  ValueError 
      |     +--  UnicodeError 
      |          +--  UnicodeDecodeError 
      |          +--  UnicodeEncodeError 
      |          +--  UnicodeTranslateError 
      +--  Warning 
           +--  DeprecationWarning 
           +--  PendingDeprecationWarning 
           +--  RuntimeWarning 
           +--  SyntaxWarning 
           +--  UserWarning 
           +--  FutureWarning 
           +--  ImportWarning 
           +--  UnicodeWarning 
           +--  BytesWarning 
           +--  ResourceWarning
'''