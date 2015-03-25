#!/usr/bin/env python3
__author__ = 'Administrator'

from reportlab.pdfgen import canvas


def hello():
    c = canvas.Canvas('helloworld.pdf')
    c.drawString(100, 100, 'Hello World')
    c.showPage()
    c.save()

hello()