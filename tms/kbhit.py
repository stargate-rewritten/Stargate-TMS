'''
A Python class implementing KBHIT, the standard keyboard-interrupt poller.
Works transparently on Windows and Posix (Linux, Mac OS X).  Doesn't work
with IDLE.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as 
published by the Free Software Foundation, either version 3 of the 
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

'''

import os
import sys
import time
# Windows
if os.name == 'nt':
    import msvcrt

# Posix (Linux, OS X)
else:
    import termios
    import atexit
    from select import select


class KBHit:
    
    def __init__(self):
        '''Creates a KBHit object that you can call to do various keyboard things.
        '''

        self._enabled = True
        if os.name == 'nt':
            pass
        
        else:
    
            # Save the terminal settings
            self._fd = sys.stdin.fileno()
            self._new_term = termios.tcgetattr(self.fd)
            self._old_term = termios.tcgetattr(self.fd)
    
            # New terminal setting unbuffered
            self._new_term[3] = (self._new_term[3] & ~termios.ICANON & ~termios.ECHO)
            termios.tcsetattr(self._fd, termios.TCSAFLUSH, self._new_term)
    
            # Support normal-terminal reset at exit
            atexit.register(self.setNormalTerm)
    
    
    def setNormalTerm(self):
        ''' Resets to normal terminal.  On Windows this is a no-op.
        '''
        
        if os.name == 'nt':
            pass
        
        else:
            termios.tcsetattr(self._fd, termios.TCSAFLUSH, self._old_term)


    def getChar(self):
        ''' Returns a keyboard character after kbhit() has been called.
            Should not be called in the same program as getarrow().
        '''
        
        s = ''
        
        if os.name == 'nt':
            return msvcrt.getch().decode('utf-8')
        
        else:
            return sys.stdin.read(1)
                        

    def getArrow(self):
        ''' Returns an arrow-key code after kbhit() has been called. Codes are
        0 : up
        1 : right
        2 : down
        3 : left
        Should not be called in the same program as getch().
        '''
        
        if os.name == 'nt':
            msvcrt.getch() # skip 0xE0
            c = msvcrt.getch()
            vals = [72, 77, 80, 75]
            
        else:
            c = sys.stdin.read(3)[2]
            vals = [65, 67, 66, 68]
        
        return vals.index(ord(c.decode('utf-8')))
        

    def kbhit(self):
        ''' Returns True if keyboard character was hit, False otherwise.
        '''
        if os.name == 'nt':
            return msvcrt.kbhit()
        
        else:
            dr,dw,de = select([sys.stdin], [], [], 0)
            return dr != []
    
    def readLine(self) -> str:
        line = ""
        while self._enabled:
            if not self.kbhit():
                time.sleep(0.01)
                continue
            try:
                aChar = self.getChar()
                if ord(aChar) == 13:
                    break
                sys.stdout.write(aChar)
                sys.stdout.flush()
                line = line + aChar
            except UnicodeDecodeError:
                pass
        
        if not self._enabled:
            raise EOFError("Reader is disabled.")
        sys.stdout.write("\n")
        sys.stdout.flush()
        return line
    
    def getExit(self):
        while self._enabled:
            if not self.kbhit():
                time.sleep(0.01)
                continue
            try:
                aChar = self.getChar()
                if ord(aChar) == 13:
                    break
            except UnicodeDecodeError:
                pass
        if not self._enabled:
            raise EOFError("Reader is disabled")
        
    def disable(self):
        self._enabled = False