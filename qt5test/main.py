#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/26 17:59
# @Author  : qiubin
# @File    : main.py
# @Software: PyCharm

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from qt5test import uitest
from PyQt5.QtGui import QIcon
from Day_001 import Test

app = QApplication(sys.argv)
widget = QWidget()
ui = uitest.Ui_From()
ui.setupUi(widget)
widget.setWindowIcon(QIcon('f1.ico'))  # 增加icon图标，如果没有图片可以没有这句
widget.show()
sys.exit(app.exec_())
