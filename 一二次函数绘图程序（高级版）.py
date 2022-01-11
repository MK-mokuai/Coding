#Nakanosan Presents. Functions Drawing software.Copyright.NankaiLiu@2021.11
#From author:我就不写注释哈哈哈
from turtle import *
def my_goto(x,y):
    penup()                 
    goto(x,y)
    pendown()
def my_mov(x,y,my_seth,long):
    my_goto(x,y)
    seth(my_seth)
    fd(long)
def rc():
    scwide=600
    scheight=600
    bgcolor("black")
    pencolor("green")
    pensize("2")
    speed(0)
    my_mov(scwide/2,0,180,scwide)
    my_mov(scwide/2,0,135,scwide/30)
    my_mov(scwide/2,0,225,scwide/30)
    my_mov(0,scheight/2,-90,scheight)     
    my_mov(0,scheight/2,225,scwide/30)
    my_mov(0,scheight/2,315,scwide/30)
    my_goto(scwide/2-10,-40)
    write("X",  font = ("Times", 12,"bold"))
    my_goto(30,scheight/2-30)
    write("Y",  font = ("Times", 12,"bold"))
    my_goto(-40,-40)
    write("O",  font = ("Times", 12,"bold"))
    for i in range(-300,300,50):
        if i==0:
            pass
        else:
            my_mov(i,-5,90,10)
            write(i,font = ("Times", 9,"bold"))
            my_mov(-5,i,0,10)
            my_goto(15,i-5)
            write(i,font = ("Times", 9,"bold"))
tracer(0)
rc()
tracer(1)
hideturtle()
linenum = int(numinput('绘图软件','您要绘制的图像数量',1,1))
for i in range(linenum):
    lineoption = int(numinput('绘图软件','您想要绘制图像的指数 1or2',1,1))
    if lineoption == 1:
        draw_option = int(numinput('绘图软件：一次函数','您想要绘制图像的方式？1.几何画法 2.代数画法',1,1,2))
        if draw_option == 1:
            dx = numinput('绘图软件：一次函数','您要起始的X轴位置',0)
            dy = numinput('绘图软件：一次函数','您要起始的Y轴位置',0)
            dl = numinput('绘图软件：一次函数','您要前进的长度',0)
            dd = numinput('绘图软件：一次函数','您要前进的角度',0)
            penup()
            goto(dx,dy)
            pendown()
            left(dd)
            fd(dl)
            right(dd)
            hideturtle()
        if draw_option == 2:
            dk = numinput('绘图软件：一次函数','直线斜率',0)
            db = numinput('绘图软件：一次函数','直线纵截距',0)
            penup()
            goto(-300,dk*(-300)+db)
            for j in range(-300,301):
                if dk*j+db <= 300 and dk*j+db >= -300:
                    goto(j,dk*j+db)
                    pendown()
            hideturtle()
    if lineoption == 2:
        da = numinput('绘图软件：二次函数','您要绘制的抛物线的二次项系数',0)
        db = numinput('绘图软件：二次函数','您要绘制的抛物线的一次项系数',0)
        dc = numinput('绘图软件：二次函数','您要绘制的抛物线的常数项',0)
        penup()
        goto(-300,da*90000-db*300+dc)
        for j in range(-300,301):
            if da*j*j+db*j+dc <= 300 and da*j*j+db*j+dc >= -300:
                goto(j,da*j*j+db*j+dc)
                pendown()
        hideturtle()
done()