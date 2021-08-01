import sys
from pathlib import Path

from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
from data_connection.h1pos import db1
from presentation.Themes.Special_StyleSheet import label_num, desc_5



class CL_printCoupon(QtWidgets.QDialog):

    def __init__(self):
        super(CL_printCoupon, self).__init__()
        cwd = Path.cwd()
        mod_path = Path(__file__).parent.parent.parent
        self.dirname = mod_path.__str__() + '/presentation/coupon_ui'
        self.conn = db1.connect()

    # Todo: method load ui of printCoupon
    def FN_LOADUI(self):
        filename = self.dirname + '/printCoupon.ui'
        loadUi(filename, self)

        css_path = Path(__file__).parent.parent.parent
        path = css_path.__str__() + '/presentation/Themes/Style.css'
        self.setStyleSheet(open(path).read())
        self.FN_getData()



    # Todo: method to get all coupons
    def FN_getData(self):
        try:
            self.conn = db1.connect()
            mycursor = self.conn.cursor()
            mycursor.execute("SELECT COP_DESC,COP_ID FROM COUPON where COP_STATUS = 1 and COP_VALID_TO >= COP_VALID_FROM")
            records = mycursor.fetchall()
            for row, val in records:
                self.CMB_CouponDes.addItem(row, val)
            mycursor.close()
        except:
            print(sys.exc_info())