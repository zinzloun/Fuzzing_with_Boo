#!/usr/bin/python3

# Fuzzing Vulnserver.exe

from boofuzz import *

host = '192.168.1.2'      # Host IP
port = 9999               # Server port

def main():
 
 # setting the restart threshold we will stop fuzzing after 5 attempts without response
 session = Session(target = Target(connection = SocketConnection(host, port, proto='tcp')),restart_threshold = 5)
 s_initialize("Vulnsrv-TRUN") # just giving our session a name
 # the trun command is BOF vulnerable
 s_string("TRUN", fuzzable = False) # we pass the command name, not to be fuzzed
 s_delim(" ", fuzzable = False) # of course we don't fuzz the delimeter 
 s_string("FUZZ") # fuzzing placeholder
 
 session.connect(s_get("Vulnsrv-TRUN")) # connect to the session
 session.fuzz() # performs the fuzzing
 

if __name__ == "__main__":
    main()
