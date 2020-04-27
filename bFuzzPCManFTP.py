#!/usr/bin/python3

# reference: https://github.com/jtpereyda/boofuzz
# Here I fuzz PCManFTPD2.exe

from boofuzz import *

host = '192.168.1.6'    # Host IP
port = 21               # Server port

def main():
 # setting the restart threshold we will stop fuzzing after 5 attempts without response
 ses = Session(target = Target(connection = SocketConnection(host, port, proto='tcp')),restart_threshold = 5)
 s_initialize("PCMan_FTPS")        # the session name
 
 s_string("FUZZ")                  # please holder for the fuzzing string
 
 ses.connect(s_get("PCMan_FTPS")) # having our 'session' connected
 ses.fuzz()                       # calling this function actually performs the fuzzing

if __name__ == "__main__":
    main()
