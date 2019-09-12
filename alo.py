from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtTest import *
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSignal

"""""""""
font=QtGui.QFont("Times",16)
font2=QtGui.QFont("Century Gothic",14)
uygulama = QtWidgets.QApplication(sys.argv)
pencere=QtWidgets.QWidget()
pencere.setWindowTitle("gladiatus")
dikey=QtWidgets.QVBoxLayout()
yatay=QtWidgets.QHBoxLayout()
buton1=QtWidgets.QPushButton("programa giriş")
buton2=QtWidgets.QPushButton("programdan çıkış")
dikey.addStretch()
yatay.addStretch()
yatay.addWidget(buton1)
yatay.addWidget(buton2)
dikey.addLayout(yatay)

pencere.setLayout(dikey)


icerik1=QtWidgets.QLabel(pencere)
icerik1.setText("ilk botum")
icerik1.move(200,200)
icerik1.setFont(font)


icerik2=QtWidgets.QLabel(pencere)
icerik2.setPixmap(QtGui.QPixmap("gladiatus.jpg"))
icerik2.move(0,0)

dugme1=QtWidgets.QPushButton(pencere)
dugme1.setText("başlat")
dugme1.move(300,400)
dugme1.setFont(font2)
dugme2=QtWidgets.QPushButton(pencere)
dugme2.setText("cikis")
dugme2.setFont(font2)
dugme2.move(400,400)
"""
baslikfont = QFont("Century Gothic", 25)


def ustbolum(mevcutpencere):
    kapatButon = QPushButton("X", mevcutpencere)
    kapatButon.setFont(baslikfont)
    kapatButon.setGeometry(700, 50, 50, 50)
    kapatButon.clicked.connect(Pencere.kapat)


class yenimenu(QWidget):
    zindanblogu = 0

    def __init__(self, driver):
        self.driver = driver
        super().__init__()

        # ustbolum(self)
        dikey = QVBoxLayout()
        yatay = QHBoxLayout()
        yatay.addLayout(dikey)
        baslik = QLabel("yeni menumuze hoşgeldiniz")
        yazi = QLabel("istediğiniz keşif yerine tıklayınız ")
        kesifseferi = QPushButton("kesifseferiyap")
        self.kombobox = QComboBox()
        self.kombobox.addItem("karanlık orman")
        self.kombobox.addItem("korsan limanı")
        self.kombobox.addItem("mist dağları")
        self.kombobox.addItem("kurt ini")
        self.kombobox.addItem("antik tapınak")
        self.kombobox.addItem("barbar köyü")
        self.kombobox.addItem("haydut kampı")
        self.kombobox.addItem("voodoo tapınağı")
        self.kombobox.addItem("köprü")
        self.kombobox.addItem("kan mağarası")
        self.kombobox.addItem("kayıp liman")
        self.kombobox.addItem("umpokta klanı")
        self.kombobox.addItem("kervan")
        self.kombobox.addItem("mesoai vahası")
        self.kombobox.addItem("kaya antilobu")

        self.tik = QCheckBox()
        self.tik2 = QCheckBox()
        self.tik3 = QCheckBox("zindan")

        self.kombobox.activated.connect(self.secildi)

        baslat = QPushButton("baslat")
        self.zindanliste = QComboBox()
        sirkturma = QPushButton("sirkturma yap")
        arena = QPushButton("arena yap")
        zindan = QPushButton("zindan yap")
        self.zindanliste.addItem("Gustavo nun köy evi")
        self.zindanliste.addItem("Firarda")
        self.zindanliste.addItem("Ejder Hazinesi")
        self.zindanliste.addItem("Karanlık Çetelerin Mağarası")
        self.zindanliste.addItem("Cehennem Azabı Tapınağı")
        self.zindanliste.addItem("Sürüklendi")
        self.zindanliste.addItem("Kayıp Liman")
        baslik.setFont(baslikfont)

        dikey.addWidget(baslik)
        dikey.addWidget(yazi)
        dikey.addWidget(self.kombobox)
        yatay.addWidget(arena)
        yatay.addWidget(self.tik2)
        yatay.addWidget(sirkturma)
        yatay.addWidget(self.tik)
        dikey.addWidget(zindan)
        dikey.addWidget(self.zindanliste)
        yatay.addWidget(self.tik3)
        dikey.addStretch()
        dikey.addWidget(baslat)
        baslat.clicked.connect(self.baslat)
        self.tik.clicked.connect(self.secildi)
        self.tik2.clicked.connect(self.secildi)
        self.tik3.clicked.connect(self.secildi)
        ustbolum(self)

        self.thread = ThreadClass()
        self.thread.start()

        self.setLayout(yatay)
        self.setGeometry(0, 0, 800, 600)

    def secildi(self):
        secilenkesif = self.kombobox.currentText()

        tik1incheki = self.tik.isChecked()
        tik2ninchecki = self.tik2.isChecked()
        tik3ninchecki = self.tik3.isChecked()

    def saldir(self, secilen):
        driver = self.driver

        try:
            lvlatlama = driver.find_element_by_xpath("""//*[@id="linknotification"]""")

            lvlatlama.click()
            time.sleep(2)
        except:
            pass
        if secilen == "karanlık orman":

            try:
                time.sleep(2)
                kesif_puanı = driver.find_element_by_id("expeditionpoints_value_point").text
                kesif_yapilirmi = driver.find_element_by_id("cooldown_bar_text_expedition").text

            except:

                driver.refresh()
                time.sleep(2)

            if (int(kesif_puanı) != 0 and kesif_yapilirmi == "Keşif Seferi`ne geç"):
                a = driver.find_element_by_xpath("""//*[@id="cooldown_bar_expedition"]/a""")
                a.click()
                time.sleep(2)
                secme = driver.find_element_by_xpath("""//*[@id="submenu2"]/a[2]""")
                secme.click()
                time.sleep(2)
                a = driver.find_element_by_xpath("""//*[@id="expedition_list"]/div[1]/div[2]/button""")
                a.click()
                time.sleep(2)


        elif secilen == "korsan limanı":

            kesif_puanı = driver.find_element_by_id("expeditionpoints_value_point").text
            kesif_yapilirmi = driver.find_element_by_id("cooldown_bar_text_expedition").text

            if (int(kesif_puanı) != 0 and kesif_yapilirmi == "Keşif Seferi`ne geç"):
                a = driver.find_element_by_xpath("""//*[@id="cooldown_bar_expedition"]/a""")
                a.click()
                time.sleep(2)
                secme = driver.find_element_by_xpath("""//*[@id="submenu2"]/a[3]""")  # korsanlimanı
                secme.click()
                time.sleep(2)
                a = driver.find_element_by_xpath("""//*[@id="expedition_list"]/div[1]/div[2]/button""")  # kaçakköle
                a.click()
                time.sleep(2)


        elif secilen == "mist dağları":

            kesif_puanı = driver.find_element_by_id("expeditionpoints_value_point").text
            kesif_yapilirmi = driver.find_element_by_id("cooldown_bar_text_expedition").text

            if (int(kesif_puanı) != 0 and kesif_yapilirmi == "Keşif Seferi`ne geç"):
                a = driver.find_element_by_xpath("""//*[@id="cooldown_bar_expedition"]/a""")
                a.click()
                time.sleep(2)
                secme = driver.find_element_by_xpath("""//*[@id="submenu2"]/a[4]""")
                secme.click()
                time.sleep(2)
                a = driver.find_element_by_xpath("""//*[@id="expedition_list"]/div[1]/div[2]/button""")
                a.click()
                time.sleep(2)



        elif secilen == "kurt ini":

            kesif_yapilirmi = driver.find_element_by_id("cooldown_bar_text_expedition").text

            kesif_puanı = driver.find_element_by_id("expeditionpoints_value_point").text

            if (int(kesif_puanı) != 0 and kesif_yapilirmi == "Keşif Seferi`ne geç"):
                a = driver.find_element_by_xpath("""//*[@id="cooldown_bar_expedition"]/a""")
                a.click()
                time.sleep(2)

                secme = driver.find_element_by_xpath("""//*[@id="submenu2"]/a[5]""")
                secme.click()
                time.sleep(2)

                a = driver.find_element_by_xpath("""//*[@id="expedition_list"]/div[1]/div[2]/button""")
                a.click()
                time.sleep(3)
        elif secilen == "antik tapınak":

            kesif_yapilirmi = driver.find_element_by_id("cooldown_bar_text_expedition").text

            kesif_puanı = driver.find_element_by_id("expeditionpoints_value_point").text

            if (int(kesif_puanı) != 0 and kesif_yapilirmi == "Keşif Seferi`ne geç"):
                a = driver.find_element_by_xpath("""//*[@id="cooldown_bar_expedition"]/a""")
                a.click()
                time.sleep(2)

                secme = driver.find_element_by_xpath("""//*[@id="submenu2"]/a[6]""")
                secme.click()
                time.sleep(2)

                a = driver.find_element_by_xpath("""//*[@id="expedition_list"]/div[1]/div[2]/button""")
                a.click()
                time.sleep(3)
        elif secilen == "barbar köyü":

            kesif_yapilirmi = driver.find_element_by_id("cooldown_bar_text_expedition").text

            kesif_puanı = driver.find_element_by_id("expeditionpoints_value_point").text

            if (int(kesif_puanı) != 0 and kesif_yapilirmi == "Keşif Seferi`ne geç"):
                a = driver.find_element_by_xpath("""//*[@id="cooldown_bar_expedition"]/a""")
                a.click()
                time.sleep(2)

                secme = driver.find_element_by_xpath("""//*[@id="submenu2"]/a[7]""")
                secme.click()
                time.sleep(2)

                a = driver.find_element_by_xpath("""//*[@id="expedition_list"]/div[1]/div[2]/button""")
                a.click()
                time.sleep(3)
        elif secilen == "haydut kampı":

            kesif_yapilirmi = driver.find_element_by_id("cooldown_bar_text_expedition").text

            kesif_puanı = driver.find_element_by_id("expeditionpoints_value_point").text

            if (int(kesif_puanı) != 0 and kesif_yapilirmi == "Keşif Seferi`ne geç"):
                a = driver.find_element_by_xpath("""//*[@id="cooldown_bar_expedition"]/a""")
                a.click()
                time.sleep(2)

                secme = driver.find_element_by_xpath("""//*[@id="submenu2"]/a[8]""")
                secme.click()
                time.sleep(2)

                a = driver.find_element_by_xpath("""//*[@id="expedition_list"]/div[1]/div[2]/button""")
                a.click()
                time.sleep(3)
        if secilen == "voodoo tapınağı":

            try:
                time.sleep(2)
                kesif_puanı = driver.find_element_by_id("expeditionpoints_value_point").text
                kesif_yapilirmi = driver.find_element_by_id("cooldown_bar_text_expedition").text

            except:

                driver.refresh()
                time.sleep(2)

            if (int(kesif_puanı) != 0 and kesif_yapilirmi == "Keşif Seferi`ne geç"):
                a = driver.find_element_by_xpath("""//*[@id="cooldown_bar_expedition"]/a""")
                a.click()
                time.sleep(2)

                secme = driver.find_element_by_xpath("""//*[@id="submenu2"]/a[2]""")
                secme.click()
                time.sleep(2)
                a = driver.find_element_by_xpath("""//*[@id="expedition_list"]/div[1]/div[2]/button""")

                a.click()
                time.sleep(2)
        if secilen == "köprü":

            try:
                time.sleep(2)
                kesif_puanı = driver.find_element_by_id("expeditionpoints_value_point").text
                kesif_yapilirmi = driver.find_element_by_id("cooldown_bar_text_expedition").text

            except:

                driver.refresh()
                time.sleep(2)

            if (int(kesif_puanı) != 0 and kesif_yapilirmi == "Keşif Seferi`ne geç"):
                a = driver.find_element_by_xpath("""//*[@id="cooldown_bar_expedition"]/a""")
                a.click()
                time.sleep(2)

                secme = driver.find_element_by_xpath("""//*[@id="submenu2"]/a[3]""")
                secme.click()
                time.sleep(2)
                a = driver.find_element_by_xpath("""//*[@id="expedition_list"]/div[1]/div[2]/button""")

                a.click()
                time.sleep(2)
        if secilen == "kan mağarası":

            try:
                time.sleep(2)
                kesif_puanı = driver.find_element_by_id("expeditionpoints_value_point").text
                kesif_yapilirmi = driver.find_element_by_id("cooldown_bar_text_expedition").text

            except:

                driver.refresh()
                time.sleep(2)

            if (int(kesif_puanı) != 0 and kesif_yapilirmi == "Keşif Seferi`ne geç"):
                a = driver.find_element_by_xpath("""//*[@id="cooldown_bar_expedition"]/a""")
                a.click()
                time.sleep(2)

                secme = driver.find_element_by_xpath("""//*[@id="submenu2"]/a[4]""")
                secme.click()
                time.sleep(2)
                a = driver.find_element_by_xpath("""//*[@id="expedition_list"]/div[1]/div[2]/button""")

                a.click()
                time.sleep(2)
        if secilen == "kayıp liman":

            try:
                time.sleep(2)
                kesif_puanı = driver.find_element_by_id("expeditionpoints_value_point").text
                kesif_yapilirmi = driver.find_element_by_id("cooldown_bar_text_expedition").text

            except:

                driver.refresh()
                time.sleep(2)

            if (int(kesif_puanı) != 0 and kesif_yapilirmi == "Keşif Seferi`ne geç"):
                a = driver.find_element_by_xpath("""//*[@id="cooldown_bar_expedition"]/a""")
                a.click()
                time.sleep(2)

                secme = driver.find_element_by_xpath("""//*[@id="submenu2"]/a[5]""")
                secme.click()
                time.sleep(2)
                a = driver.find_element_by_xpath("""//*[@id="expedition_list"]/div[1]/div[2]/button""")

                a.click()
                time.sleep(2)
    def sirkyap(self):
        driver = self.driver

        try:
            sirkyapılırmı = driver.find_element_by_xpath("""//*[@id="cooldown_bar_text_ct"]""").text

        except NoSuchElementException:

            driver.refresh()
            time.sleep(2)
        sirkyapılırmı = driver.find_element_by_xpath("""//*[@id="cooldown_bar_text_ct"]""").text
        if sirkyapılırmı == "Sirk Turma`ya geç":
            tıkla = driver.find_element_by_xpath("""//*[@id="cooldown_bar_ct"]/a""")
            tıkla.click()
            time.sleep(2)

            provenc = driver.find_element_by_xpath("""//*[@id="mainnav"]/li/table/tbody/tr/td[4]/a""")
            provenc.click()
            time.sleep(2)

            dovus = driver.find_element_by_xpath("""//*[@id="own3"]/table/tbody/tr[5]/td[4]/div""")
            dovus.click()
            time.sleep(2)

    def arenayap(self):

        driver = self.driver

        try:
            arena_yapılırmı = driver.find_element_by_xpath(""" //*[@id="cooldown_bar_text_arena"]""").text

        except NoSuchElementException:

            driver.refresh()
            time.sleep(2)
        arena_yapılırmı = driver.find_element_by_xpath(""" //*[@id="cooldown_bar_text_arena"]""").text

        if (arena_yapılırmı == "Arena`ya geç"):
            arenatık = driver.find_element_by_xpath("""//*[@id="cooldown_bar_arena"]/a""")

            arenatık.click()

            time.sleep(2)
            proarena = driver.find_element_by_xpath("""//*[@id="mainnav"]/li/table/tbody/tr/td[2]/a""")

            proarena.click()
            time.sleep(2)

            arenasavas = driver.find_element_by_xpath("""//*[@id="own2"]/table/tbody/tr[6]/td[4]/div""")

            arenasavas.click()
            time.sleep(2)

    def zindanyap(self):

        driver = self.driver

        secilenzindan = self.zindanliste.currentText()

        time.sleep(2)
        try:
            zindanagir = driver.find_element_by_xpath("""//*[@id="cooldown_bar_text_dungeon"]""").text

            zindanvarmı = driver.find_element_by_xpath("""//*[@id="dungeonpoints_value_point"]""").text

        except:

            driver.refresh()
            time.sleep(2)
            zindanagir = driver.find_element_by_xpath("""//*[@id="cooldown_bar_text_dungeon"]""").text
            zindanvarmı = driver.find_element_by_xpath("""//*[@id="dungeonpoints_value_point"]""").text

        if secilenzindan == "Gustavo nun köy evi" and zindanvarmı != 0 and zindanagir == "Zindan`a geç":

            try:
                zindantık = driver.find_element_by_xpath("""//*[@id="cooldown_bar_dungeon"]/a""")
                zindantık.click()
                time.sleep(2)
            except:

                eksepgecme = driver.find_element_by_xpath("""//*[@id="breakDiv"]""")
                eksepgecme.click()
                time.sleep(2)

            karanlıkorman = driver.find_element_by_xpath("""//*[@id="submenu2"]/a[2]""")
            karanlıkorman.click()
            time.sleep(2)
            zindanagec = driver.find_element_by_xpath("""//*[@id="mainnav"]/li/table/tbody/tr/td[2]/a""")
            zindanagec.click()

            time.sleep(2)

            if yenimenu.zindanblogu == 0:
                try:
                    zindanagir = driver.find_element_by_xpath(
                        """//*[@id="content"]/div[2]/div/form/table/tbody/tr/td[1]/input""")
                    zindanagir.click()
                    time.sleep(2)
                except NoSuchElementException:
                    pass

            ilksaldiri = driver.find_element_by_xpath("""//*[@id="content"]/div[3]/div/div[1]/span[2]""").text

            ikincisaldiri = driver.find_element_by_xpath("""//*[@id="content"]/div[3]/div/div[2]/span[2]""").text

            if (ilksaldiri == "Başarılamadı"):

                yenimenu.zindanblogu = 1

                savas = driver.find_element_by_xpath("""//*[@id="content"]/div[2]/div/img[7]""")

                savas.click()
                time.sleep(2)

            elif (ikincisaldiri == "Başarılamadı"):
                yenimenu.zindanblogu = 1
                savas = driver.find_element_by_xpath("""//*[@id="content"]/div[2]/div/div[2]""")
                savas.click()
                time.sleep(2)
            else:

                yenimenu.zindanblogu = 0
                savas = driver.find_element_by_xpath("""//*[@id="content"]/div[2]/div/div[3]""")
                savas.click()
                time.sleep(2)
        elif secilenzindan == "Firarda" and zindanvarmı != 0 and zindanagir == "Zindan`a geç":

            try:
                zindantık = driver.find_element_by_xpath("""//*[@id="cooldown_bar_dungeon"]/a""")
                zindantık.click()
                time.sleep(2)
            except:

                eksepgecme = driver.find_element_by_xpath("""//*[@id="breakDiv"]""")
                eksepgecme.click()
                time.sleep(2)

            korsanlimanı = driver.find_element_by_xpath("""//*[@id="submenu2"]/a[3]""")
            korsanlimanı.click()
            time.sleep(2)

            korsanlimanızindanı = driver.find_element_by_xpath("""//*[@id="mainnav"]/li/table/tbody/tr/td[2]/a""")
            korsanlimanızindanı.click()
            time.sleep(2)

            if yenimenu.zindanblogu == 0:
                try:
                    zindanagir = driver.find_element_by_xpath(
                        """//*[@id="content"]/div[2]/div/form/table/tbody/tr/td[1]/input""")
                    zindanagir.click()
                    time.sleep(2)
                except NoSuchElementException:
                    pass

            ilksaldiri = driver.find_element_by_xpath("""//*[@id="content"]/div[3]/div/div[2]/span[2]""").text

            if (ilksaldiri == "Başarılamadı"):

                try:
                    yenimenu.zindanblogu = 1
                    savas = driver.find_element_by_xpath("""//*[@id="content"]/div[2]/div/img[9]""")
                    savas.click()
                    time.sleep(1)
                except:
                    try:
                        yenimenu.zindanblogu = 1
                        savas1 = driver.find_element_by_xpath("""//*[@id="content"]/div[2]/div/img[7]""")

                        savas1.click()
                        time.sleep(1)
                    except:
                        yenimenu.zindanblogu = 1
                        savas2 = driver.find_element_by_xpath("""//*[@id="content"]/div[2]/div/img[11]""")
                        savas2.click()
                        time.sleep(1)



            elif ilksaldiri == "Yerine getirildi":

                ikincisaldiri = driver.find_element_by_xpath("""//*[@id="content"]/div[3]/div/div[3]/span[2]""").text
                if ikincisaldiri == "Başarılamadı":
                    try:
                        yenimenu.zindanblogu = 1
                        savas = driver.find_element_by_xpath("""//*[@id="content"]/div[2]/div/img[6]""")
                        savas.click()
                        time.sleep(2)
                    except:
                        try:
                            yenimenu.zindanblogu = 1
                            savas1 = driver.find_element_by_xpath("""//*[@id="content"]/div[2]/div/img[5]""")
                            savas1.click()
                            time.sleep(1)
                        except:
                            yenimenu.zindanblogu = 1
                            savas2 = driver.find_element_by_xpath("""//*[@id="content"]/div[2]/div/img[6]""")
                            savas2.click()
                            time.sleep(1)
                elif ikincisaldiri == "Yerine getirildi":
                    saldiri3 = driver.find_element_by_xpath("""//*[@id="content"]/div[3]/div/div[5]/span[2]""").text
                    if saldiri3 == "Başarılamadı":
                        savas3 = driver.find_element_by_xpath("""//*[@id="content"]/div[2]/div/img[7]""")
                        savas3.click()
                        time.sleep(1)
                    else:
                        yenimenu.zindanblogu = 0
                        boslasavas = driver.find_element_by_xpath("""//*[@id="content"]/div[2]/div/img[5]""")
                        boslasavas.click()
                        time.sleep(2)
        elif secilenzindan == "Ejder Hazinesi" and zindanvarmı != 0 and zindanagir == "Zindan`a geç":

            try:
                zindantık = driver.find_element_by_xpath("""//*[@id="cooldown_bar_dungeon"]/a""")
                zindantık.click()
                time.sleep(2)
            except:

                eksepgecme = driver.find_element_by_xpath("""//*[@id="breakDiv"]""")
                eksepgecme.click()
                time.sleep(2)

            mistdaglari = driver.find_element_by_xpath("""//*[@id="submenu2"]/a[4]""")
            mistdaglari.click()
            time.sleep(2)
            zindanagec = driver.find_element_by_xpath("""//*[@id="mainnav"]/li/table/tbody/tr/td[2]/a""")
            zindanagec.click()

            time.sleep(2)

            if yenimenu.zindanblogu == 0:
                try:
                    zindanagir = driver.find_element_by_xpath(
                        """//*[@id="content"]/div[2]/div/form/table/tbody/tr/td[1]/input""")
                    zindanagir.click()
                    time.sleep(2)
                except NoSuchElementException:
                    pass

            ilksaldiri = driver.find_element_by_xpath("""//*[@id="content"]/div[3]/div/div[1]/span[2]""").text

            ikincisaldiri = driver.find_element_by_xpath("""//*[@id="content"]/div[3]/div/div[2]/span[2]""").text

            ucuncusaldiri = driver.find_element_by_xpath("""//*[@id="content"]/div[3]/div/div[3]/span[2]""").text

            if ilksaldiri == "Başarılamadı" and ikincisaldiri == "Başarılamadı" and ucuncusaldiri == "Başarılamadı":
                yenimenu.zindanblogu = 1

                kerberos = driver.find_element_by_xpath("""//*[@id="content"]/div[2]/div/img[6]""")
                kerberos.click()
                time.sleep(2)
            elif ilksaldiri == "Yerine getirildi" and ikincisaldiri == "Başarılamadı" and ucuncusaldiri == "Başarılamadı":
                yenimenu.zindanblogu = 1

                yarısyuzucusu = driver.find_element_by_xpath("""//*[@id="content"]/div[2]/div/img[5]""")
                yarısyuzucusu.click()
                time.sleep(2)
            elif ilksaldiri == "Yerine getirildi" and ikincisaldiri == "Yerine getirildi" and ucuncusaldiri == "Başarılamadı":
                yenimenu.zindanblogu = 1

                minator = driver.find_element_by_xpath("""//*[@id="content"]/div[2]/div/img[4]""")
                minator.click()
                time.sleep(2)
            elif ilksaldiri == "Yerine getirildi" and ikincisaldiri == "Yerine getirildi" and ucuncusaldiri == "Yerine getirildi":
                yenimenu.zindanblogu = 0

                boss = driver.find_element_by_xpath("""//*[@id="content"]/div[2]/div/img[3]""")
                boss.click()
                time.sleep(2)
        #############################################################3
        elif secilenzindan == "Karanlık Çetelerin Mağarası" and zindanvarmı != 0 and zindanagir == "Zindan`a geç":

            try:
                zindantık = driver.find_element_by_xpath("""//*[@id="cooldown_bar_dungeon"]/a""")
                zindantık.click()
                time.sleep(2)
            except:

                eksepgecme = driver.find_element_by_xpath("""//*[@id="breakDiv"]""")
                eksepgecme.click()
                time.sleep(2)

            kurtini = driver.find_element_by_xpath("""//*[@id="submenu2"]/a[5]""")
            kurtini.click()
            time.sleep(2)
            zindanagec = driver.find_element_by_xpath("""//*[@id="mainnav"]/li/table/tbody/tr/td[2]/a""")
            zindanagec.click()

            time.sleep(2)

            if yenimenu.zindanblogu == 0:
                try:
                    zindanagir = driver.find_element_by_xpath(
                        """//*[@id="content"]/div[2]/div/form/table/tbody/tr/td[1]/input""")
                    zindanagir.click()
                    time.sleep(2)
                except NoSuchElementException:
                    pass

            ilksaldiri = driver.find_element_by_xpath("""//*[@id="content"]/div[3]/div/div[1]/span[2]""").text

            ikincisaldiri = driver.find_element_by_xpath("""//*[@id="content"]/div[3]/div/div[2]/span[2]""").text

            ucuncusaldiri = driver.find_element_by_xpath("""//*[@id="content"]/div[3]/div/div[3]/span[2]""").text

            if ilksaldiri == "Başarılamadı" and ikincisaldiri == "Başarılamadı" and ucuncusaldiri == "Başarılamadı":
                yenimenu.zindanblogu = 1

                kurt = driver.find_element_by_xpath("""//*[@id="content"]/div[2]/div/img[7]""")
                kurt.click()
                time.sleep(2)
            elif ilksaldiri == "Yerine getirildi" and ikincisaldiri == "Başarılamadı" and ucuncusaldiri == "Başarılamadı":
                yenimenu.zindanblogu = 1

                cuce = driver.find_element_by_xpath("""//*[@id="content"]/div[2]/div/img[6]""")
                cuce.click()
                time.sleep(2)
            elif ilksaldiri == "Yerine getirildi" and ikincisaldiri == "Yerine getirildi" and ucuncusaldiri == "Başarılamadı":
                yenimenu.zindanblogu = 1

                iskelet = driver.find_element_by_xpath("""//*[@id="content"]/div[2]/div/img[5]""")
                iskelet.click()
                time.sleep(2)
            elif ilksaldiri == "Yerine getirildi" and ikincisaldiri == "Yerine getirildi" and ucuncusaldiri == "Yerine getirildi":
                yenimenu.zindanblogu = 0

                boss = driver.find_element_by_xpath("""//*[@id="content"]/div[2]/div/img[4]""")
                boss.click()
                time.sleep(2)
        elif secilenzindan == "Cehennem Azabı Tapınağı" and zindanvarmı != 0 and zindanagir == "Zindan`a geç":

            try:
                zindantık = driver.find_element_by_xpath("""//*[@id="cooldown_bar_dungeon"]/a""")
                zindantık.click()
                time.sleep(2)
            except:

                eksepgecme = driver.find_element_by_xpath("""//*[@id="breakDiv"]""")
                eksepgecme.click()
                time.sleep(2)

            voodooo = driver.find_element_by_xpath("""//*[@id="submenu2"]/a[2]""")

            voodooo.click()
            time.sleep(2)
            zindanagec = driver.find_element_by_xpath("""//*[@id="mainnav"]/li/table/tbody/tr/td[2]/a""")
            zindanagec.click()

            time.sleep(2)

            if yenimenu.zindanblogu == 0:
                try:
                    zindanagir = driver.find_element_by_xpath("""//*[@id="content"]/div[2]/div/form/table/tbody/tr/td[1]/input""")
                    zindanagir.click()
                    time.sleep(2)
                except NoSuchElementException:
                    pass

            ilksaldiri = driver.find_element_by_xpath("""//*[@id="content"]/div[3]/div/div[1]/span[2]""").text

            ikincisaldiri = driver.find_element_by_xpath("""//*[@id="content"]/div[3]/div/div[2]/span[2]""").text
            ucuncusaldiri = driver.find_element_by_xpath("""//*[@id="content"]/div[3]/div/div[3]/span[2]""").text

            if (ilksaldiri == "Başarılamadı" and ikincisaldiri =="Başarılamadı" and ucuncusaldiri =="Başarılamadı"):

                yenimenu.zindanblogu = 1

                savas = driver.find_element_by_xpath("""//*[@id="content"]/div[2]/div/img[10]""")

                savas.click()
                time.sleep(2)

            elif (ilksaldiri=="Yerine getirildi" and ikincisaldiri == "Başarılamadı" and ucuncusaldiri =="Başarılamadı"):
                yenimenu.zindanblogu = 1
                print("aloo buraya geldim mi")
                savas = driver.find_element_by_xpath("""//*[@id="content"]/div[2]/div/img[10]""")
                print("dafuq")
                savas.click()
                time.sleep(2)

            elif (ilksaldiri == "Yerine getirildi" and ikincisaldiri == "Yerine getirildi" and ucuncusaldiri == "Başarılamadı"):
                yenimenu.zindanblogu = 1
                try :
                    yenimenu.zindanblogu = 1
                    savas = driver.find_element_by_xpath("""//*[@id="content"]/div[2]/div/img[12]""")
                    savas.click()
                    time.sleep(2)
                except:
                    try :
                        yenimenu.zindanblogu = 1
                        savas = driver.find_element_by_xpath("""// *[ @ id = "content"] / div[2] / div / img[10]""")
                        savas.click()
                        time.sleep(2)
                    except:
                        try:
                            yenimenu.zindanblogu = 1
                            savas = driver.find_element_by_xpath("""//*[@id="content"]/div[2]/div/img[8]""")
                            savas.click()
                            time.sleep(2)

                        except:
                            yenimenu.zindanblogu = 1
                            savas = driver.find_element_by_xpath("""//*[@id="content"]/div[2]/div/img[6]""")
                            savas.click()
                            time.sleep(2)
            else :
                yenimenu.zindanblogu=0
                boslasavas=driver.find_element_by_xpath("""//*[@id="content"]/div[2]/div/div""")
                boslasavas.click()
                time.sleep(2)

        elif secilenzindan == "Sürüklendi" and zindanvarmı != 0 and zindanagir == "Zindan`a geç":

            try:
                zindantık = driver.find_element_by_xpath("""//*[@id="cooldown_bar_dungeon"]/a""")
                zindantık.click()
                time.sleep(2)
            except:

                eksepgecme = driver.find_element_by_xpath("""//*[@id="breakDiv"]""")
                eksepgecme.click()
                time.sleep(2)

            kopru = driver.find_element_by_xpath("""//*[@id="submenu2"]/a[3]""")

            kopru.click()
            time.sleep(2)
            zindanagec = driver.find_element_by_xpath("""//*[@id="mainnav"]/li/table/tbody/tr/td[2]/a""")
            zindanagec.click()

            time.sleep(2)

            if yenimenu.zindanblogu == 0:
                try:
                    zindanagir = driver.find_element_by_xpath("""//*[@id="content"]/div[2]/div/form/table/tbody/tr/td[1]/input""")
                    zindanagir.click()
                    time.sleep(2)
                except NoSuchElementException:
                    pass

            ilksaldiri = driver.find_element_by_xpath("""//*[@id="content"]/div[3]/div/div[1]/span[2]""").text
            print(ilksaldiri)
            ikincisaldiri = driver.find_element_by_xpath("""//*[@id="content"]/div[3]/div/div[3]/span[2]""").text
            print(ikincisaldiri)
            ucuncusaldiri = driver.find_element_by_xpath("""//*[@id="content"]/div[3]/div/div[4]/span[2]""").text
            print(ucuncusaldiri)
            dort= driver.find_element_by_xpath("""//*[@id="content"]/div[3]/div/div[6]/span[2]""").text
            print(dort)

            if (ilksaldiri == "Başarılamadı" and ikincisaldiri =="Başarılamadı" and ucuncusaldiri =="Başarılamadı" and dort=="Başarılamadı"):

                yenimenu.zindanblogu = 1
                try:
                    yenimenu.zindanblogu = 1
                    savas = driver.find_element_by_xpath("""//*[@id="content"]/div[2]/div/img[11]""")
                    savas.click()
                    time.sleep(2)
                except:
                    try:
                        yenimenu.zindanblogu = 1
                        savas = driver.find_element_by_xpath("""//*[@id="content"]/div[2]/div/img[10]""")
                        savas.click()
                        time.sleep(2)
                    except:
                        try:
                            yenimenu.zindanblogu = 1
                            savas = driver.find_element_by_xpath("""//*[@id="content"]/div[2]/div/img[9]""")
                            savas.click()
                            time.sleep(2)
                        except:
                            yenimenu.zindanblogu = 1
                            savas = driver.find_element_by_xpath("""//*[@id="content"]/div[2]/div/img[8]""")
                            savas.click()
                            time.sleep(2)


            elif (ilksaldiri=="Yerine getirildi" and ikincisaldiri == "Başarılamadı" and ucuncusaldiri =="Başarılamadı" and dort =="Başarılamadı"):
                yenimenu.zindanblogu = 1
                print("aloo buraya geldim mi")
                savas = driver.find_element_by_xpath("""//*[@id="content"]/div[2]/div/img[7]""")
                print("dafuq")
                savas.click()
                time.sleep(2)

            elif (ilksaldiri == "Yerine getirildi" and ikincisaldiri == "Yerine getirildi" and ucuncusaldiri == "Başarılamadı" and dort =="Başarılamadı"):
                yenimenu.zindanblogu = 1
                savas2=driver.find_element_by_xpath("""//*[@id="content"]/div[2]/div/img[6]""")
                savas2.click()
                time.sleep(2)
            elif (ilksaldiri == "Yerine getirildi" and ikincisaldiri == "Yerine getirildi" and ucuncusaldiri == "Yerine getirildi" and dort =="Başarılamadı"):
                yenimenu.zindanblogu = 1
                savas2=driver.find_element_by_xpath("""//*[@id="content"]/div[2]/div/img[5]""")
                savas2.click()
                time.sleep(2)
            elif (ilksaldiri == "Yerine getirildi" and ikincisaldiri == "Yerine getirildi" and ucuncusaldiri == "Yerine getirildi" and dort=="Yerine getirildi") :

                print("burda mı sıkıntı var ")
                yenimenu.zindanblogu=0
                boslasavas=driver.find_element_by_xpath("""//*[@id="content"]/div[2]/div/div""")
                boslasavas.click()
                time.sleep(2)
        elif secilenzindan == "Kayıp Liman" and zindanvarmı != 0 and zindanagir == "Zindan`a geç":

            try:
                zindantık = driver.find_element_by_xpath("""//*[@id="cooldown_bar_dungeon"]/a""")
                zindantık.click()
                time.sleep(2)
            except:

                eksepgecme = driver.find_element_by_xpath("""//*[@id="breakDiv"]""")
                eksepgecme.click()
                time.sleep(2)

            kayıpliman = driver.find_element_by_xpath("""//*[@id="submenu2"]/a[5]""")
            kayıpliman.click()
            time.sleep(2)

            korsanlimanızindanı = driver.find_element_by_xpath("""//*[@id="mainnav"]/li/table/tbody/tr/td[2]/a""")
            korsanlimanızindanı.click()
            time.sleep(2)

            if yenimenu.zindanblogu == 0:
                try:
                    zindanagir = driver.find_element_by_xpath("""//*[@id="content"]/div[2]/div/form/table/tbody/tr/td[1]/input""")
                    zindanagir.click()
                    time.sleep(2)
                except NoSuchElementException:
                    pass

            ilksaldiri = driver.find_element_by_xpath("""//*[@id="content"]/div[3]/div/div[2]/span[2]""").text

            if (ilksaldiri == "Başarılamadı"):

                try:
                    yenimenu.zindanblogu = 1
                    savas = driver.find_element_by_xpath("""//*[@id="content"]/div[2]/div/img[7]""")
                    savas.click()
                    time.sleep(1)
                except:
                    try:
                        yenimenu.zindanblogu = 1
                        savas1 = driver.find_element_by_xpath("""//*[@id="content"]/div[2]/div/img[7]""")

                        savas1.click()
                        time.sleep(1)
                    except:
                        try:
                            yenimenu.zindanblogu = 1
                            savas2 = driver.find_element_by_xpath("""//*[@id="content"]/div[2]/div/img[7]""")
                            savas2.click()
                            time.sleep(1)
                        except:
                            yenimenu.zindanblogu=1
                            savas3=driver.find_element_by_xpath("""//*[@id="content"]/div[2]/div/img[7]""")
                            savas3.click()
                            time.sleep(1)




            elif ilksaldiri == "Yerine getirildi":

                ikincisaldiri = driver.find_element_by_xpath("""//*[@id="content"]/div[3]/div/div[4]/span[2]""").text
                if ikincisaldiri == "Başarılamadı":
                    try:
                        yenimenu.zindanblogu = 1
                        savas = driver.find_element_by_xpath("""//*[@id="content"]/div[2]/div/img[7]""")
                        savas.click()
                        time.sleep(2)
                    except:
                        try:

                            yenimenu.zindanblogu = 1
                            savas1 = driver.find_element_by_xpath("""//*[@id="content"]/div[2]/div/img[6]""")
                            savas1.click()
                            time.sleep(1)
                        except:
                            yenimenu.zindanblogu = 1
                            savas2 = driver.find_element_by_xpath("""//*[@id="content"]/div[2]/div/img[5]""")
                            savas2.click()
                            time.sleep(1)
                elif ikincisaldiri == "Yerine getirildi":
                    saldiri3 = driver.find_element_by_xpath("""//*[@id="content"]/div[3]/div/div[5]/span[2]""").text
                    if saldiri3 == "Başarılamadı":
                        savas3 = driver.find_element_by_xpath("""//*[@id="content"]/div[2]/div/img[4]""")
                        savas3.click()
                        time.sleep(1)
                    else:
                        yenimenu.zindanblogu = 0
                        boslasavas = driver.find_element_by_xpath("""//*[@id="content"]/div[2]/div/img[4]""")
                        boslasavas.click()
                        time.sleep(2)


    def canbas(self):
        driver = self.driver
        can = driver.find_element_by_xpath("""//*[@id="header_values_hp_percent"]""").text
        can = can.replace("%", "")
        if int(can) < 30:
            geneldurum = driver.find_element_by_xpath("""//*[@id="mainmenu"]/a[1]""")
            geneldurum.click()
            time.sleep(2)

            dropable = driver.find_element_by_xpath("""//*[@id="avatar"]/div[4]""")
            envanter = driver.find_element_by_xpath("""//*[@id="inv"]""")
            icerik=envanter.find_elements_by_tag_name("div")


            print(envanter)
            print("alo")
            print(icerik)
            for i in icerik:
                print(icerik)
                ActionChains(driver).drag_and_drop(i, dropable).perform()
                time.sleep(2)
                can = driver.find_element_by_xpath("""//*[@id="header_values_hp_percent"]""").text
                can = can.replace("%", "")
                if int(can) > 70:
                    break

    def baslat(self):
        secilenkesif = self.kombobox.currentText()
        tik1incheki = self.tik.isChecked()  # sirk
        tik2ninchecki = self.tik2.isChecked()  # arena
        zindantiki = self.tik3.isChecked()  # zindan
        secilenzindan = self.zindanliste.currentText()

        a = True
        if tik1incheki == True and tik2ninchecki == True and zindantiki == True:  # kesif zindan arena sirk
            while True:
                self.canbas()
                time.sleep(2)
                self.saldir(secilenkesif)
                time.sleep(2)
                self.zindanyap()
                time.sleep(2)
                self.arenayap()
                time.sleep(2)
                self.sirkyap()
                time.sleep(2)



        elif tik1incheki == True and tik2ninchecki == False and zindantiki == True:  # kesif zindan sirk
            while True:
                self.canbas()
                time.sleep(2)
                self.saldir(secilenkesif)
                time.sleep(2)
                self.zindanyap()
                time.sleep(2)
                self.sirkyap()
                time.sleep(2)


        elif tik1incheki == False and tik2ninchecki == True and zindantiki == True:  # kesif zindan arena
            while True:
                self.canbas()
                time.sleep(2)
                self.saldir(secilenkesif)
                time.sleep(2)
                self.zindanyap()
                time.sleep(2)
                self.arenayap()
                time.sleep(2)


        elif zindantiki == False and tik1incheki == False and tik2ninchecki == True:  # arena ve kesif
            while True:
                self.canbas()
                time.sleep(2)
                self.saldir(secilenkesif)
                time.sleep(2)
                self.arenayap()
                time.sleep(2)


        elif tik2ninchecki == True and tik1incheki == True:  # kesif arena sirk
            while True:
                self.canbas()
                time.sleep(2)
                self.saldir(secilenkesif)
                time.sleep(2)
                self.arenayap()
                time.sleep(2)
                self.sirkyap()
                time.sleep(2)

        elif tik1incheki == False and tik2ninchecki == False and zindantiki == False:  # kesif
            while True:
                self.canbas()
                self.saldir(secilenkesif)

        elif zindantiki == True:
            while True:
                self.zindanyap()


class Pencere(QWidget):

    def __init__(self):
        super().__init__()

        ustbolum(self)
        self.yazi = QLabel("welcome")
        self.dugme1 = QPushButton("start")
        self.dugme2 = QPushButton("stop")
        self.input1 = QLineEdit("")
        self.input1.setPlaceholderText("Username")
        self.input2 = QLineEdit("")
        self.input2.setPlaceholderText("password")
        self.input3 = QLineEdit()
        self.input3.setPlaceholderText("server giriniz")
        self.dugme1.clicked.connect(self.giris)
        self.dugme2.clicked.connect(self.cikis)
        self.dikey = QVBoxLayout()
        self.yatay = QHBoxLayout()
        self.yatay.addStretch()
        self.dikey.addStretch()
        self.dikey.addWidget(self.input1)
        self.dikey.addWidget(self.input2)
        self.dikey.addWidget(self.input3)
        self.dikey.addWidget(self.yazi)
        self.dikey.addWidget(self.dugme1)
        self.dikey.addWidget(self.dugme2)
        self.dikey.addStretch()
        self.yatay.addLayout(self.dikey)
        self.yatay.addStretch()

        self.setLayout(self.yatay)
        self.setGeometry(0, 0, 800, 600)
        self.show()

    def giris(self):
        self.driver = webdriver.Chrome()

        isim = self.input1.text()

        password = self.input2.text()

        server = self.input3.text()

        driver = self.driver
        driver.get("https://lobby.gladiatus.gameforge.com/tr_TR/")
        QTest.qWait(3000)
        time.sleep(2)
        girisegit = driver.find_element_by_xpath("""//*[@id="loginRegisterTabs"]/ul/li[1]/span""")
        girisegit.click()
        elem = driver.find_element_by_xpath("""//*[@id="loginForm"]/div[1]/div/input""")
        elem.send_keys(isim)
        elem = driver.find_element_by_xpath("""//*[@id="loginForm"]/div[2]/div/input""")
        elem.send_keys(password)
        a = driver.find_element_by_xpath("""//*[@id="loginForm"]/p/button[1]""")
        a.click()
        QTest.qWait(2000)
        time.sleep(1)
        girisebas = driver.find_element_by_xpath("""//*[@id="joinGame"]/a/button/span""")
        girisebas.click()
        time.sleep(1)
        oyna = driver.find_element_by_xpath(
            """//*[@id="accountlist"]/div/div[1]/div[2]/div[1]/div/div[11]/button""").click()
        time.sleep(2)
        driver.close()
        driver.switch_to.window((driver.window_handles[0]))

        self.yazi.setText("bot başlıyor")
        self.yazi.setText("hoş geldin " + isim)
        QTest.qWait(2000)
        self.yazi.setText("bot acildi")

        self.ikinci = yenimenu(driver)
        self.ikinci.show()
        self.close()

    def cikis(self):
        self.yazi.setText("bot cikiliyor")
        QtTest.QTest.qWait(2000)
        self.yazi.setText("bot durdu")

        self.close()

    def kapat(self):
        qApp.quit()


class ThreadClass(QtCore.QThread):
    def __init__(self, parent=None):
        super(ThreadClass, self).__init__(parent)

    def run(self):
        a = 0


uygulama = QApplication(sys.argv)
pencere = Pencere()
sys.exit(uygulama.exec_())

