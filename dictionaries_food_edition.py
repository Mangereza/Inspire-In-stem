#!/usr/bin/python

mary_fav_food=['ugali','chicken','managu']
jane_fav_food=['chapo','chilli beef','soda']
#dictionary containing the above
Food={
    'mary':['ugali','chicken','managu'],
    'jane':['chapo','chilli beef','soda'],
}
for key, value in Food.items():
    print(f"{key}:{value}")


