
import pygame,random,sys

# the final zoom factor of the screen
ZOOM=4

# the screen size. Taken from the original gameboy (20*8=160 and 18*8=144)
ARENAW=20
ARENAH=16

# the indices of different tiles
APPLE=28
HEAD=4
TAIL=6
CORP=16
TURN=2
SEP=15
GRASS=1

# the indices of the text
TEXT="0123456789*:+-/` ABCDEFGHIJKLMNOPQRSTUVWXYZ'.,?!"

# the data for the different levels
ARENAS=[[
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
  ],[
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
  0, 0, 0, 0, 2, 4, 4, 1, 0, 0, 0, 0, 1, 4, 4, 3, 0, 0, 0, 0,
  0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0,
  0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0,
  0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0,
  0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0,
  0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0,
  0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0,
  0, 0, 0, 0, 6, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 7, 0, 0, 0, 0,
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
  ],[
  2, 4, 4, 4, 4, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 4, 4, 4, 4, 3,
  5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5,
  5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5,
  5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5,
  5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5,
  1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
  1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
  5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5,
  5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5,
  5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5,
  5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5,
  6, 4, 4, 4, 4, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 4, 4, 4, 4, 7,
  ],[
  2, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3,
  5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5,
  5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5,
  5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5,
  5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5,
  5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5,
  5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5,
  5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5,
  5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5,
  5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5,
  5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5,
  5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5,
  5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5,
  5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5,
  5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5,
  6, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 7,
  ],[
  2, 4, 4, 4, 4, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 4, 4, 4, 4, 3,
  5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5,
  5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5,
  5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5,
  5, 0, 0, 0, 2, 4, 4, 1, 0, 0, 0, 0, 1, 4, 4, 3, 0, 0, 0, 5,
  1, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 1,
  0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0,
  0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0,
  0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0,
  0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0,
  1, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 1,
  5, 0, 0, 0, 6, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 7, 0, 0, 0, 5,
  5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5,
  5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5,
  5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5,
  6, 4, 4, 4, 4, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 4, 4, 4, 4, 7,
  ],[
  2, 4, 4, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 2, 4, 4, 3,
  5, 2, 3, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5, 2, 3, 5,
  5, 6, 7, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5, 6, 7, 5,
  6, 4, 4, 7, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 6, 4, 4, 7,
  5, 1, 1, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 1, 1, 5,
  5, 1, 1, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 1, 1, 5,
  5, 1, 1, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 1, 1, 5,
  5, 1, 1, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 1, 1, 5,
  5, 1, 1, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 1, 1, 5,
  5, 1, 1, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 1, 1, 5,
  5, 1, 1, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 1, 1, 5,
  5, 1, 1, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 1, 1, 5,
  2, 4, 4, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 2, 4, 4, 3,
  5, 2, 3, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5, 2, 3, 5,
  5, 6, 7, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5, 6, 7, 5,
  6, 4, 4, 7, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 6, 4, 4, 7,
  ],[
  2, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3,
  5, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5,
  5, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5,
  5, 0, 0, 0, 1, 4, 4, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5,
  5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5,
  5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5,
  5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5,
  5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5,
  5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 4, 4, 1, 0, 0, 5,
  5, 0, 0, 0, 1, 4, 4, 4, 4, 1, 0, 0, 0, 5, 0, 0, 0, 0, 0, 5,
  5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 5,
  5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 5,
  5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 5,
  5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 5,
  5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 5,
  6, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 7,
  ],
  [
  2, 4, 4, 4, 4, 4, 4, 4, 4, 3, 2, 4, 4, 4, 4, 4, 4, 4, 4, 3,
  1, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 0, 0, 0, 0, 0, 0, 0, 0, 1,
  0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0,
  0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0,
  0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0,
  1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1,
  5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5,
  6, 4, 4, 4, 4, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 4, 4, 4, 4, 7,
  2, 4, 4, 4, 4, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 4, 4, 4, 4, 3,
  5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5,
  1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1,
  0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0,
  0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0,
  0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0,
  1, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 0, 0, 0, 0, 0, 0, 0, 0, 1,
  6, 4, 4, 4, 4, 4, 4, 4, 4, 7, 6, 4, 4, 4, 4, 4, 4, 4, 4, 7,
  ],
 ]
def drap(val):
 if val==ARENAW-1:
  val=-1
 if val==-ARENAW+1:
  val=1
 if val==ARENAH-1:
  val=-1
 if val==-ARENAH+1:
  val=1
 return val

def write(text,surface,letters,x=0,y=ARENAH+1):
  for letter in text:
   if letter in letters:
    tile=tiles[32+letters.index(letter)]
    surface.blit(tile,(x*8,y*8))
    x+=1
   if letter=="\n":
    x=0
    y+=1


if __name__=="__main__":
 tiles=[]
 highscore=[]
 highfile=open("snake.hsc","rb")
 for i in ARENAS:
  val=ord(highfile.read(1))
  val+=ord(highfile.read(1))<<8
  highscore.append(val)
 img=pygame.image.load("snake.png")
 for y in range(6):
  for x in range(16):
   s=pygame.Surface((8,8))
   s.blit(img,(-8*x,-8*y))
   if len(tiles) in (HEAD,HEAD+1,HEAD+16,HEAD+17):
    s.set_colorkey((255,255,255))
   tiles.append(s)
 display=pygame.display.set_mode((8*ARENAW*ZOOM,8*(ARENAH+2)*ZOOM))
 surface=pygame.Surface((8*ARENAW,8*ARENAH+16))
 clock=pygame.time.Clock()
 x=ARENAW/2
 y=ARENAH/2
 arraypos=[(x-1,y),(x,y)]
 applepos=[x+1,y]
 direction=(1,0)
 olddirection=(1,0)
 score=0
 grass=[]
 arena=0
 gameover=True
 for i in range(ARENAW*ARENAH/4):
  grass.append([random.randint(0,ARENAW-1),random.randint(0,ARENAH-1)])
 lasttime=pygame.time.get_ticks()
 while 1:
  for event in pygame.event.get():
   if event.type==pygame.QUIT:
    pygame.quit()
    sys.exit()
   if event.type==pygame.KEYUP and event.key==pygame.K_SPACE:
    gameover=False
    lasttime=pygame.time.get_ticks()
    score=0
   if event.type==pygame.KEYDOWN:
    if event.key==pygame.K_ESCAPE:
     pygame.quit()
     sys.exit() 
    if gameover:
     if event.key==pygame.K_DOWN:
      arena+=1
      arena%=len(ARENAS)
      x=ARENAW/2
      y=ARENAH/2
      arraypos=[(x-1,y),(x,y)]
      applepos=[x+1,y]
      grass=[]
      score=highscore[arena]
      for i in range(ARENAW*ARENAH/4):
       grass.append([random.randint(0,ARENAW-1),random.randint(0,ARENAH-1)])
     if event.key==pygame.K_UP:
      arena-=1
      arena%=len(ARENAS)
      x=ARENAW/2
      y=ARENAH/2
      arraypos=[(x-1,y),(x,y)]
      applepos=[x+1,y]
      grass=[]
      score=highscore[arena]
      for i in range(ARENAW*ARENAH/4):
       grass.append([random.randint(0,ARENAW-1),random.randint(0,ARENAH-1)])
    else:
     if event.key==pygame.K_LEFT and olddirection!=(1,0):
      direction=(-1,0)
     if event.key==pygame.K_RIGHT and olddirection!=(-1,0):
      direction=(1,0)
     if event.key==pygame.K_UP and olddirection!=(0,-1):
      direction=(0,-1)
     if event.key==pygame.K_DOWN and olddirection!=(0,1):
      direction=(0,1)
    if event.key==pygame.K_SPACE:
      gameover=True
      x=ARENAW/2
      y=ARENAH/2
      arraypos=[(x-1,y),(x,y)]
      applepos=[x+1,y]
      direction=(1,0)
      olddirection=(1,0)
  surface.fill((255,255,255))
  for x in range(ARENAW):
   surface.blit(tiles[SEP],(x*8,ARENAH*8))
  for x,y in grass:
   surface.blit(tiles[GRASS],(x*8,y*8))
   
  x,y=arraypos[-1]
  if pygame.time.get_ticks()-lasttime>250-score*4 and not gameover:
   if direction[0]==-olddirection[0] and direction[1]==-olddirection[1]:
    direction=olddirection
   x+=direction[0]
   y+=direction[1]
   olddirection=direction
   lasttime+=250-score*4
   x%=ARENAW
   y%=ARENAH
   if [x,y] in arraypos[1:] or ARENAS[arena][x+y*ARENAW]!=0:
    gameover=True
   arraypos.append([x,y])
   if applepos in arraypos:
    score+=1
    x=random.randint(0,ARENAW-1)
    y=random.randint(0,ARENAH-1)
    while [x,y] in arraypos or ARENAS[arena][x+y*ARENAW]:
     x=random.randint(0,ARENAW-1)
     y=random.randint(0,ARENAH-1)
    applepos=[x,y]
   else:
    arraypos.pop(0)
  for y in range(ARENAH):
   for x in range(ARENAW):
    val=ARENAS[arena][x+y*ARENAW]
    if 1<=val<=3:
     val=val+8
    if 4<=val<=7:
     val=val+20
    if val:
     surface.blit(tiles[val],(x*8,y*8))
  for i in range(len(arraypos)):
   if i==len(arraypos)-1:
    dirx=drap(arraypos[i][0]-arraypos[i-1][0])
    diry=drap(arraypos[i][1]-arraypos[i-1][1])
    if dirx<0:
     surface.blit(tiles[HEAD],(arraypos[i][0]*8,arraypos[i][1]*8))
    if dirx>0:
     surface.blit(tiles[HEAD+1],(arraypos[i][0]*8,arraypos[i][1]*8))
    if diry<0:
     surface.blit(tiles[HEAD+16],(arraypos[i][0]*8,arraypos[i][1]*8))
    if diry>0:
     surface.blit(tiles[HEAD+17],(arraypos[i][0]*8,arraypos[i][1]*8))
   elif i==0:
    dirx=drap(arraypos[i+1][0]-arraypos[i][0])
    diry=drap(arraypos[i+1][1]-arraypos[i][1])
    if dirx<0:
     surface.blit(tiles[TAIL+1],(arraypos[i][0]*8,arraypos[i][1]*8))
    if dirx>0:
     surface.blit(tiles[TAIL],(arraypos[i][0]*8,arraypos[i][1]*8))
    if diry<0:
     surface.blit(tiles[TAIL+17],(arraypos[i][0]*8,arraypos[i][1]*8))
    if diry>0:
     surface.blit(tiles[TAIL+16],(arraypos[i][0]*8,arraypos[i][1]*8))
   else:
    dirx=drap(arraypos[i][0]-arraypos[i-1][0])
    diry=drap(arraypos[i][1]-arraypos[i-1][1])
    dirx2=drap(arraypos[i+1][0]-arraypos[i][0])
    diry2=drap(arraypos[i+1][1]-arraypos[i][1])
    if dirx2==dirx and diry2==diry:
     if dirx<0:
      surface.blit(tiles[CORP],(arraypos[i][0]*8,arraypos[i][1]*8))
     if dirx>0:
      surface.blit(tiles[CORP],(arraypos[i][0]*8,arraypos[i][1]*8))
     if diry<0:
      surface.blit(tiles[CORP+1],(arraypos[i][0]*8,arraypos[i][1]*8))
     if diry>0:
      surface.blit(tiles[CORP+1],(arraypos[i][0]*8,arraypos[i][1]*8))
    else:
     if dirx2<0 and diry>0:
      surface.blit(tiles[TURN+17],(arraypos[i][0]*8,arraypos[i][1]*8))
     if dirx2>0 and diry>0:
      surface.blit(tiles[TURN+16],(arraypos[i][0]*8,arraypos[i][1]*8))
     if dirx2<0 and diry<0:
      surface.blit(tiles[TURN+1],(arraypos[i][0]*8,arraypos[i][1]*8))
     if dirx2>0 and diry<0:
      surface.blit(tiles[TURN],(arraypos[i][0]*8,arraypos[i][1]*8))
     if dirx>0 and diry2<0:
      surface.blit(tiles[TURN+17],(arraypos[i][0]*8,arraypos[i][1]*8))
     if dirx<0 and diry2<0:
      surface.blit(tiles[TURN+16],(arraypos[i][0]*8,arraypos[i][1]*8))
     if dirx>0 and diry2>0:
      surface.blit(tiles[TURN+1],(arraypos[i][0]*8,arraypos[i][1]*8))
     if dirx<0 and diry2>0:
      surface.blit(tiles[TURN],(arraypos[i][0]*8,arraypos[i][1]*8))
  surface.blit(tiles[APPLE],(applepos[0]*8,applepos[1]*8))
  if gameover:
   if score>=highscore[arena]:
    write("SCORE:"+str(score).rjust(2,"0")+" * HIGHSCORE",surface,TEXT)
    highscore[arena]=score
    highfile=open("snake.hsc","wb")
    for ele in highscore:
     highfile.write(chr(ele&255))
     highfile.write(chr(ele>>8))
    highfile.close()
   else:
    write("SCORE:"+str(score).rjust(2,"0")+" * GAME OVER",surface,TEXT)
  else:
   write("SCORE:"+str(score).rjust(2,"0")+" * HIGH:"+str(highscore[arena]).rjust(2,"0"),surface,TEXT)
  pygame.transform.scale(surface,display.get_size(),display)
  pygame.display.flip()
  pygame.display.set_caption("score:"+str(score))