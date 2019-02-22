import sys
import math
import random

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

awal=[]
akhir=[]

# player_count: the amount of players (always 2)
# my_id: my player ID (0 or 1)
# zone_count: the amount of zones on the map
# link_count: the amount of links between all zones
player_count, my_id, zone_count, link_count = [int(i) for i in input().split()]
for i in range(zone_count):
    # zone_id: this zone's ID (between 0 and zoneCount-1)
    # platinum_source: Because of the fog, will always be 0
    zone_id, platinum_source = [int(j) for j in input().split()]
for i in range(link_count):
    zone_1, zone_2 = [int(j) for j in input().split()]
    awal.extend([zone_1])
    akhir.extend([zone_2])
#print(awal)
#print(akhir)

# game loop
while True:
    my_platinum = int(input())  # your available Platinum
    zid=[]
    oid=[]
    pods0=[]
    pods1=[]
    visibli=[]
    fplatinum=[]
    originid=[]
    originpods=[]
    target=[]
    a=[]
    b=[]
    
    for i in range(zone_count):
        # z_id: this zone's ID
        # owner_id: the player who owns this zone (-1 otherwise)
        # pods_p0: player 0's PODs on this zone
        # pods_p1: player 1's PODs on this zone
        # visible: 1 if one of your units can see this tile, else 0
        # platinum: the amount of Platinum this zone can provide (0 if hidden by fog)
        z_id, owner_id, pods_p0, pods_p1, visible, platinum = [int(j) for j in input().split()]

        zid.extend([z_id])
        oid.extend([owner_id])
        pods0.extend([pods_p0])
        pods1.extend([pods_p1])
        visibli.extend([visible])
        fplatinum.extend([platinum])
        

        b=[]
        if ((my_id==0 and pods_p0>0) or (my_id==1 and pods_p1>0)):
            if (my_id==0):
                originid.extend([z_id])
                originpods.extend([pods_p0])
                for j in range(link_count):
                    if (awal[j]==z_id):
                        b.extend([akhir[j]])
                    if (akhir[j]==z_id):
                        b.extend([awal[j]])
                target.append(b)
                        
            else:
                originid.extend([z_id])
                originpods.extend([pods_p1])
                for j in range(link_count):
                    if (awal[j]==z_id):
                        b.extend([akhir[j]])
                    if (akhir[j]==z_id):
                        b.extend([awal[j]])
                target.append(b)
                
    
    for i in range(len(originid)):
        a = target[i]
        for j in a:
            if (oid[j]!=my_id):
                target[i]=j
                break
            else:
                target[i]=random.choice(a)
                
        
    
    # Write an action using print       
    #print("Debug messages...", file=sys.stderr)

    #print(originpods,originid,target)
    for i in range(len(originid)):
        if (i==(len(originid)-1)):
            print(originpods[i],originid[i],target[i])
        else:
            print(originpods[i],originid[i],target[i],end=" ")


    # first line for movement commands, second line no longer used (see the protocol in the statement for details)
    
    print("WAIT")
