from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()

x,y,z=mc.player.getTilePos()

while True:
    mc.setBlocks(x+2,y,z+2,x-2,y,z-2,9)
    time.sleep(30)    