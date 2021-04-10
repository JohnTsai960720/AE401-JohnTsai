from mcpi.minecraft import Minecraft

mc = Minecraft.create()
x,y,z=mc.player.getTilePos()
width=10
height=10
length=10
mc.setBlocks(x,y,z,x+width,y+height,z+length,20)
mc.setBlocks(x+1,y+1,z+1,x+width-1,y+height-1,z+length-1,9)
