#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: xxx
import turtle

def main():
  #设置一个画面
  windows = turtle.Screen()
  #设置背景
  windows.bgcolor('blue')
  #生成一个黄色乌龟
  bran = turtle.Turtle()
  bran.shape('turtle')
  bran.color('yellow')
  #开始你的表演
  bran.penup()
  bran.goto(0,-200)
  bran.pendown()
  bran.circle(200)

  bran.penup()
  bran.goto(0,-150)
  bran.pendown()
  bran.circle(150)

  bran.penup()
  bran.goto(0,-100)
  bran.pendown()
  bran.circle(100)
  
  bran.penup()
  bran.goto(0,-50)
  bran.pendown()
  bran.circle(50)







if __name__ == '__main__':
  main()