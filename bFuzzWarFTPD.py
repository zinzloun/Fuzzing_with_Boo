#!/usr/bin/python3

# Here I fuzz the FTP  Server war-ftpd.ex

from boofuzz import *

host = '192.168.1.3'    # Host IP
port = 21               # Server port

def main():
 # setting the restart threshold we will stop fuzzing after 5 attempts without response
 ses = Session(target = Target(connection = SocketConnection(host, port, proto='tcp')),restart_threshold = 5)
 
 s_initialize("WarFTPD") #just giving our session a name, "TRUN"
 
 s_string("USER", fuzzable = False)        #the FTP parameter to fuzz
 s_delim(" ")            # the delimeter
 s_string("FUZZ")        # the fuzz string placeholder
 s_static("\r\n")        # carriage return
 
 ses.connect(s_get("WarFTPD")) # having our 'session' connected
 ses.fuzz()                    # calling this function actually performs the fuzzing

if __name__ == "__main__":
    main()
