from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()

while True:
    x,y,z = mc.player.getPos()
    mc.setBlock(x,y-1,z,30)
    time.sleep(0)