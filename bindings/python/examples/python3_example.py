#!/usr/bin/env python3
import gpod
import sys

if len(sys.argv) > 1:
    db = gpod.Database(sys.argv[1])
else:
    db = gpod.Database()

print(db)

for track in db:
    #print("%(artist)s, %(album)s, %(title)s" % track)
    print(track)

