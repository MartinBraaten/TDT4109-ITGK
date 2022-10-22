__author__ = 'Martinskole'
# -*- coding: utf-8 -*-
n=1

def log(melding, klokkeslett, avsender):
    global n
    print(n ,klokkeslett, "sendte ",avsender, "foelgende melding: ",melding)
    n=n+1
def main():
    log("hodor", "12:01", "atle")
    log("hodor", "12:01", "atle")
    log("hodor", "12:01", "atle")
    log("hodor", "12:01", "atle")
    log("hodor", "12:01", "atle")
main()
