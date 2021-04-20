# acik       "border:1px solid;background:#37981A;color:white; border-radius:10px;"
# kapali    "border:1px solid;border-radius:10px;background:white;color:black;"

from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(998, 597)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(690, 10, 41, 21))
        self.label.setStyleSheet("\n""font-size:14px;\n""\n""")
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(690, 40, 51, 21))
        self.label_2.setStyleSheet("\n""font-size:14px;\n""\n""")
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")

        self.line_satir = QtWidgets.QLineEdit(self.centralwidget)
        self.line_satir.setGeometry(QtCore.QRect(750, 10, 45, 24))
        self.line_satir.setStyleSheet("border:1px solid;\n""color:#051161;\n""\n""")
        self.line_satir.setText("")
        self.line_satir.setObjectName("line_satir")

        self.line_sutun = QtWidgets.QLineEdit(self.centralwidget)
        self.line_sutun.setGeometry(QtCore.QRect(750, 40, 45, 24))
        self.line_sutun.setStyleSheet("border:1px solid;\n""")
        self.line_sutun.setObjectName("line_sutun")



        self.lbl_degisenkisim = QtWidgets.QLabel(self.centralwidget)
        self.lbl_degisenkisim.setGeometry(QtCore.QRect(20, 150, 350, 350))
        self.lbl_degisenkisim.setStyleSheet("background:#C3E8B8;\n""border:1px solid;\n""border-radius:3px;\n""border-color:blue;\n""\n""")
        self.lbl_degisenkisim.setText("")
        self.lbl_degisenkisim.setObjectName("lbl_degisenkisim")

        self.lbl_sabitkisim = QtWidgets.QLabel(self.centralwidget)
        self.lbl_sabitkisim.setGeometry(QtCore.QRect(400, 150, 350, 350))
        self.lbl_sabitkisim.setStyleSheet("background:#C3E8B8;\n""border:1px solid;\n""border-radius:3px;\n""border-color:blue;")
        self.lbl_sabitkisim.setText("")
        self.lbl_sabitkisim.setObjectName("lbl_sabitkisim")



        self.cizgi_2 = QtWidgets.QFrame(self.centralwidget)
        self.cizgi_2.setGeometry(QtCore.QRect(20, 30, 461, 20))
        self.cizgi_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.cizgi_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.cizgi_2.setObjectName("cizgi_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 111, 21))
        self.label_3.setStyleSheet("font-size:14px;\n""\n""")
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")

        self.text_yazialani = QtWidgets.QTextBrowser(self.centralwidget)
        self.text_yazialani.setGeometry(QtCore.QRect(760, 150, 231, 351))
        self.text_yazialani.setStyleSheet("background:white;\n""color:black;\n""\n""")
        self.text_yazialani.setObjectName("text_yazialani")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(850, 130, 61, 21))
        self.label_4.setStyleSheet("\n""font-size:14px;\n""")
        self.label_4.setObjectName("label_4")

        self.btn_olustur = QtWidgets.QPushButton(self.centralwidget)
        self.btn_olustur.setGeometry(QtCore.QRect(800, 10, 101, 54))
        self.btn_olustur.setStyleSheet("border:1px solid;border-radius:10px;background:white;color:black;")
        self.btn_olustur.setObjectName("btn_olustur")
        self.btn_olustur.setEnabled(False)


        self.btn_sifirla = QtWidgets.QPushButton(self.centralwidget)
        self.btn_sifirla.setGeometry(QtCore.QRect(20, 510, 161, 45))
        self.btn_sifirla.setStyleSheet("border:1px solid;\n""background:#37981A;\n""color:white;\n""\n""border-radius:10px;\n""")
        self.btn_sifirla.setObjectName("btn_sifirla")

        self.btn_basla = QtWidgets.QPushButton(self.centralwidget)
        self.btn_basla.setGeometry(QtCore.QRect(20, 50, 141, 45))
        self.btn_basla.setStyleSheet("border:1px solid;border-radius:10px;background:white;color:black;")
        self.btn_basla.setObjectName("btn_basla")
        self.btn_basla.setEnabled(False)

        self.btn_secilensatirsil = QtWidgets.QPushButton(self.centralwidget)
        self.btn_secilensatirsil.setGeometry(QtCore.QRect(180, 50, 141, 45))
        self.btn_secilensatirsil.setStyleSheet("border:1px solid;border-radius:10px;background:white;color:black;")
        self.btn_secilensatirsil.setObjectName("btn_secilensatirsil")
        self.btn_secilensatirsil.setEnabled(False)

        self.btn_kapsamlarigor = QtWidgets.QPushButton(self.centralwidget)
        self.btn_kapsamlarigor.setGeometry(QtCore.QRect(340, 50, 141, 45))
        self.btn_kapsamlarigor.setStyleSheet("border:1px solid;border-radius:10px;background:white;color:black;")
        self.btn_kapsamlarigor.setObjectName("btn_kapsamlarigor")
        self.btn_kapsamlarigor.setEnabled(False)

        # TÜM TIKLANMA OLAYLARI
        self.btn_olustur.clicked.connect(ilk_buton_olustur)
        self.btn_basla.clicked.connect(olay_basla)
        self.btn_secilensatirsil.clicked.connect(mutlak_satir_sil)
        self.btn_kapsamlarigor.clicked.connect(kapsananlari_goster)
        self.btn_sifirla.clicked.connect(self.tekrar_basla)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.line_satir.textChanged.connect(self.sayilarkontrol)
        self.line_sutun.textChanged.connect(self.sayilarkontrol)

        # TÜM BTNGRUPLAR
        self.btngrup_normalbuton = QtWidgets.QButtonGroup(MainWindow)
        self.btngrup_normalbuton.setExclusive(True)
        self.btngrup_normalbuton.buttonClicked[int].connect(butontikla)

        self.btngrup_onerilenbuton = QtWidgets.QButtonGroup(MainWindow)
        self.btngrup_onerilenbuton.setExclusive(True)


        # TÜM DEĞİŞKENLER

        self.genel_kapsam = []

        self.satir = 0
        self.sutun = 0

        self.kutu1_bas_x = 20
        self.kutu1_bas_y = 150

        self.kutu2_bas_x = 590
        self.kutu2_bas_y = 150

        self.kutu_genislik = 350
        self.kutu_yukseklik = 350

        self.onerilen_satir_butonu_x = 580
	
        self.kutu1_butonlari = []
        self.kutu2_butonlari = []
        self.kutu2_labelleri = []

        self.kalan_satir_harfleri = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't','u', 'v', 'w', 'x', 'y', 'z']
        self.kalan_satir_idleri = []
        self.kalan_sutun_idleri = []

        self.lbl_satir_harfleri = []
        self.lbl_sutun_sayilari = []

        self.kutu2_satir_harfleri = []
        self.kutu2_sutun_sayilari = []

        self.silinecek_satirlar = []

        self.sabitsatir = 0
        self.sabitsutun = 0

        self.silinmis_butonlar = []


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Kapsama Algoritması"))
        self.label.setText(_translate("MainWindow", "Satır"))
        self.label_2.setText(_translate("MainWindow", "Sütun"))
        self.btn_olustur.setText(_translate("MainWindow", "Oluştur"))
        self.btn_basla.setText(_translate("MainWindow", "Başla"))
        self.btn_secilensatirsil.setText(_translate("MainWindow", "Seçilen Satirlari Sil"))
        self.btn_kapsamlarigor.setText(_translate("MainWindow", "Kapsananları Bul"))
        self.label_3.setText(_translate("MainWindow", "Önerilen Satırlar :"))
        self.text_yazialani.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n""<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n""p, li { white-space: pre-wrap; }\n""</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n""<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "Bildirimler"))
        self.btn_sifirla.setText(_translate("MainWindow", "Sıfırla"))

    def sayilarkontrol(self):
            try:
                no1 = int(ui.line_satir.text())
                no2 = int(ui.line_sutun.text())
                ui.btn_olustur.setEnabled(True)
                ui.btn_olustur.setStyleSheet("border:1px solid;background:#37981A;color:white; border-radius:10px;")
            except Exception:
                pass

    def tekrar_basla(self):

            self.genel_kapsam.clear()

            self.line_satir.clear()
            self.line_satir.setEnabled(True)

            self.line_sutun.clear()
            self.line_sutun.setEnabled(True)

            self.text_yazialani.clear()

            self.satir = 0
            self.sutun = 0

            self.sabitsatir = 0
            self.sabitsutun = 0

            self.silinecek_satirlar.clear()
            self.silinmis_butonlar.clear()

            self.btngrup_normalbuton = QtWidgets.QButtonGroup(MainWindow)
            self.btngrup_normalbuton.setExclusive(True)
            self.btngrup_normalbuton.buttonClicked[int].connect(butontikla)

            self.kalan_satir_harfleri = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                                         'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
            self.kalan_satir_idleri.clear()
            self.kalan_sutun_idleri.clear()

            for i in self.kutu1_butonlari:
                for j in i:
                    j.close()
            self.kutu1_butonlari.clear()

            self.kutu2_butonlari.clear()

            for i in self.lbl_satir_harfleri:
                i.close()
            self.lbl_satir_harfleri.clear()

            for i in self.lbl_sutun_sayilari:
                i.close()

            for i in self.kutu2_labelleri:
                i.close()
            self.kutu2_labelleri.clear()

            for i in self.kutu2_satir_harfleri:
                i.close()
            self.kutu2_satir_harfleri.clear()

            for i in self.kutu2_sutun_sayilari:
                i.close()
            self.kutu2_sutun_sayilari.clear()

def ilk_buton_olustur():
    ui.btn_olustur.setEnabled(False)
    ui.btn_olustur.setStyleSheet("border:1px solid;border-radius:10px;background:white;color:black;")
    ui.line_satir.setEnabled(False)
    ui.line_sutun.setEnabled(False)

    ui.satir = int(ui.line_satir.text())
    ui.sutun = int(ui.line_sutun.text())

    ui.sabitsatir = int(ui.satir)
    ui.sabitsutun = int(ui.sutun)

    ui.kalan_satir_harfleri = ui.kalan_satir_harfleri[:ui.satir]
    ui.kalan_satir_idleri = np.arange(ui.satir).tolist()
    ui.kalan_sutun_idleri = np.arange(ui.sutun).tolist()



    butonGenislik  = ( ui.kutu_genislik - ((ui.sutun + 1) * 5)) / ui.sutun
    butonYukseklik = ( ui.kutu_yukseklik - (( ui.satir +1 ) * 5 )) / ui.satir

    kutu1_buton_baslangic_x = ui.kutu1_bas_x + 5
    kutu1_buton_baslangic_y = ui.kutu1_bas_y + 5

    buton_numarasi = 0


    for i in range(0, ui.satir):
        for j in range(0, ui.sutun):

            buton = QtWidgets.QPushButton(MainWindow)
            buton.setGeometry(int(kutu1_buton_baslangic_x), int(kutu1_buton_baslangic_y), int(butonGenislik), int(butonYukseklik))
            buton.setStyleSheet(" border:2px solid; border-color:blue; border-radius:3px; color:black; background:white;")
            ui.btngrup_normalbuton.addButton(buton, buton_numarasi)
            buton.show()
            buton_numarasi += 1
            ui.kutu1_butonlari.append(buton)
            kutu1_buton_baslangic_x += butonGenislik + 5

        kutu1_buton_baslangic_x = int(ui.kutu1_bas_x + 5)
        kutu1_buton_baslangic_y += butonYukseklik + 5



    ui.kutu1_butonlari = np.reshape(ui.kutu1_butonlari, (ui.satir, ui.sutun))
    ui.kutu2_butonlari = np.copy(ui.kutu1_butonlari)

    ui.kutu1_butonlari = ui.kutu1_butonlari.tolist()
    ui.kutu2_butonlari = ui.kutu2_butonlari.tolist()


    labelGenislik = (ui.kutu_genislik - ((ui.sutun + 1) * 5)) / ui.sutun
    labelYukseklik = (ui.kutu_yukseklik - ((ui.satir + 1) * 5)) / ui.satir

    kutu2_label_baslangic_x = 400 + 5
    kutu2_label_baslangic_y = ui.kutu2_bas_y + 5

    label_numarasi = 0

    for i in range(0, ui.satir):
        for j in range(0, ui.sutun):
            label = QtWidgets.QPushButton(MainWindow)
            label.setGeometry(int(kutu2_label_baslangic_x), int(kutu2_label_baslangic_y), int(labelGenislik), int(labelYukseklik))
            label.setStyleSheet("border:1px solid; border-color:white; border-radius:3px; color:black; background:green;")
            label.setEnabled(False)
            label.show()
            label_numarasi += 1
            ui.kutu2_labelleri.append(label)
            kutu2_label_baslangic_x += butonGenislik + 5

        kutu2_label_baslangic_x = int(400 + 5)
        kutu2_label_baslangic_y += labelYukseklik + 5



    ilk_harf_ve_sayi_yaz()



def ilk_harf_ve_sayi_yaz():


    for i in ui.lbl_satir_harfleri:
        i.close()

    for j in ui.lbl_sutun_sayilari:
        j.close()

    ui.lbl_satir_harfleri.clear()
    ui.lbl_sutun_sayilari.clear()


    kutu1_sayi_genislik =  (ui.kutu_genislik - ((ui.sutun + 1)* 5)) / ui.sutun
    kutu1_harf_yukseklik = (ui.kutu_yukseklik - ((ui.satir + 1) * 5)) / ui.satir


    solkosey = 150



    for i in range(0, ui.satir):
        lbl= QtWidgets.QLabel(MainWindow)
        lbl.setText(str(ui.kalan_satir_harfleri[i]))
        lbl.setAlignment(QtCore.Qt.AlignVCenter)
        lbl.setGeometry(7, int(solkosey) , 10, int(kutu1_harf_yukseklik))
        lbl.show()
        ui.lbl_satir_harfleri.append(lbl)
        solkosey += kutu1_harf_yukseklik + 5

    solkosex = 20

    for i in range(0, ui.sutun):
        lbl= QtWidgets.QLabel(MainWindow)
        lbl.setText(str(ui.kalan_sutun_idleri[i]))
        lbl.setAlignment(QtCore.Qt.AlignHCenter)
        lbl.setGeometry(int(solkosex), 130, int(kutu1_sayi_genislik),13)
        lbl.show()
        ui.lbl_sutun_sayilari.append(lbl)
        solkosex += kutu1_sayi_genislik + 5

    solkosey = 150


    for i in range(0, ui.satir):
        lbl = QtWidgets.QLabel(MainWindow)
        lbl.setText(str(ui.kalan_satir_harfleri[i]))
        lbl.setAlignment(QtCore.Qt.AlignVCenter)
        lbl.setGeometry(390, int(solkosey), 10, int(kutu1_harf_yukseklik))
        lbl.show()
        ui.kutu2_satir_harfleri.append(lbl)
        solkosey += kutu1_harf_yukseklik + 5

    solkosex = 405

    for i in range(0, ui.sutun):
        lbl = QtWidgets.QLabel(MainWindow)
        lbl.setText(str(ui.kalan_sutun_idleri[i]))
        lbl.setAlignment(QtCore.Qt.AlignHCenter)
        lbl.setGeometry(int(solkosex), 130, int(kutu1_sayi_genislik), 13)
        lbl.show()
        ui.kutu2_sutun_sayilari.append(lbl)
        solkosex += kutu1_sayi_genislik + 5


def butontikla(id):

    ui.btn_basla.setStyleSheet("border:1px solid;background:#37981A;color:white; border-radius:10px;")
    ui.btn_basla.setEnabled(True)

    for buton in ui.btngrup_normalbuton.buttons():
        if buton == ui.btngrup_normalbuton.button(id):
            if buton.text() == "":
                buton.setText("1")
                ui.kutu2_labelleri[id].setText("1")
            else:
                buton.setText("")
                ui.kutu2_labelleri[id].setText("")


def olay_basla():

    ui.btn_kapsamlarigor.setEnabled(False)
    ui.btn_kapsamlarigor.setStyleSheet("border:1px solid;border-radius:10px;background:white;color:black;")
    sutun_agirligi = sutun_agirlik_bul()

    if 0 in sutun_agirligi:
        ui.text_yazialani.append("Kapsam YOK..\n")
        ui.tekrar_basla()
        ui.btn_basla.setEnabled(False)
        ui.btn_basla.setStyleSheet("border:1px solid;border-radius:10px;background:white;color:black;")
    else:
        ui.btn_basla.setText("İleri")

        if len(mutlak_bul()) != 0:
            ui.text_yazialani.append("Mutlak Satır Bulundu. Öneriliyor.")
            onerilen_satir_diz(mutlak_bul())
        else:
            ui.text_yazialani.append("Mutlak Yok.Sezgisel Deneniyor.")
            ui.text_yazialani.append("Minimum Ağırlıklı Satırlar..")
            min_agirlikli_satir = sezgisel()
            onerilen_satir_diz(min_agirlikli_satir)

def kapsananlari_bul():
    ui.btn_kapsamlarigor.setEnabled(False)
    ui.btn_kapsamlarigor.setStyleSheet("border:1px solid;border-radius:10px;background:white;color:black;")


    kapsananlar = []
    satir_agirliklari = []

    for i in range(ui.satir):
        satir_agirliklari.append(int(0))

    for i in range(0, ui.satir):
        for j in range(0, ui.sutun):
            if ui.kutu1_butonlari[i][j].text() == "1":
                satir_agirliklari[i] += 1


    for denedigim_satir in range(ui.satir):
        for su_anki_satir in range(0,ui.satir):
            if denedigim_satir != su_anki_satir and denedigim_satir not in kapsananlar:
                ayni_sayi = 0
                for j in range(ui.sutun):
                    if ui.kutu1_butonlari[denedigim_satir][j].text() == "1" and ui.kutu1_butonlari[su_anki_satir][j].text() == "1":
                        ayni_sayi += 1

                if ayni_sayi == satir_agirliklari[denedigim_satir]:
                    kapsananlar.append(denedigim_satir)
                else:
                    ayni_sayi == 0

    return kapsananlar



def sezgisel():

    a = sutun_agirlik_bul()                                  # TÜM SÜTUNLARIN AĞIRLIKLARI BULUNDU
    b = min(a)                                            # MİNİMUM AĞIRLIK DEĞERİ BULUNDU

    min_agirlikli_satir_indis=[]
    hesaplanacak_satirlar=[]
    satir_agirliklar=[]
    min_sutunlar_id=[]

    for i in range(0,len(a)):                           # MİNİMUM AĞIRLIĞA SAHİP OLAN SÜTUNLARIN İD Sİ BULUNDU
        if a[i]==b:
            min_sutunlar_id.append(i)


    for i in range(0,ui.satir):                                                 # ağırlığı hesaplanması gereken satırların indisleri tutuldu
        for j in range(0,ui.sutun):
            if j in min_sutunlar_id and ui.kutu1_butonlari[i][j].text()=="1" and i not in hesaplanacak_satirlar:
                hesaplanacak_satirlar.append(i)




    toplam=0

    for i in hesaplanacak_satirlar:
        for j in range(0,ui.sutun):
            if ui.kutu1_butonlari[i][j].text() == "1":
                toplam += (1 / a[j])

        satir_agirliklar.append(toplam)
        toplam=0

    minagirlik = min(satir_agirliklar)


    for i in range(0,len(hesaplanacak_satirlar)):
        if satir_agirliklar[i] == minagirlik:
            min_agirlikli_satir_indis.append(hesaplanacak_satirlar[i])

    return min_agirlikli_satir_indis


def mutlak_satir_sil():
    ui.btn_secilensatirsil.setEnabled(False)
    ui.btn_secilensatirsil.setStyleSheet("border:1px solid;border-radius:10px;background:white;color:black;")

    for i in ui.btngrup_onerilenbuton.buttons():
        i.close()

    mutlak_mi = mutlak_bul()

    if len(mutlak_mi) != 0:

        silinecek_sutunlar = satir_sutun_kesisme(ui.silinecek_satirlar)
        sutun_sil(silinecek_sutunlar)

        for i in ui.silinecek_satirlar:
            a = ui.kalan_satir_harfleri[i]
            ui.genel_kapsam.append(str(a))

        satir_sil(ui.silinecek_satirlar)

        if ui.satir == 0:
            ui.text_yazialani.append(str("Genel Kapsam Bulunmuştur.."))
            ui.text_yazialani.append(str(ui.genel_kapsam))
            ui.btn_basla.setEnabled(False)
            ui.btn_kapsamlarigor.setEnabled(False)
            ui.btn_secilensatirsil.setEnabled(False)

            ui.btn_basla.setStyleSheet("border:1px solid;border-radius:10px;background:white;color:black;")
            ui.btn_kapsamlarigor.setStyleSheet("border:1px solid;border-radius:10px;background:white;color:black;")
            ui.btn_secilensatirsil.setStyleSheet("border:1px solid;border-radius:10px;background:white;color:black;")
        else:

            bos_satir = bos_satir_varmi()
            bos_satir.sort()

            if len(bos_satir) > 0:
                ui.text_yazialani.append("Bos satırlar bulundu")
                satir_sil(bos_satir)

            kapsananlar = kapsananlari_bul()
            if len(kapsananlar) > 0:
                ui.text_yazialani.append("Kapsanan Satırlar Var")
                ui.btn_kapsamlarigor.setEnabled(True)
                ui.btn_kapsamlarigor.setStyleSheet("border:1px solid;background:#37981A;color:white; border-radius:10px;")




    else:
        satir_sil(ui.silinecek_satirlar)

    if ui.satir != 0:
        butonlari_ve_harfleri_yinele()

        for i in range(0,len(ui.silinecek_satirlar)):
            for buton in ui.btngrup_onerilenbuton.buttons():
                if buton == ui.btngrup_onerilenbuton.button(ui.silinecek_satirlar[i]):
                    buton.close()
                    ui.btngrup_onerilenbuton.removeButton(buton)

        ui.silinecek_satirlar.clear()
    else:
        for i in ui.silinmis_butonlar:
            i.close()

        for i in ui.lbl_satir_harfleri:
            i.close()

        for i in ui.lbl_sutun_sayilari:
            i.close()


def kapsananlari_goster():
    ui.text_yazialani.append("Kapsananlar Gösteriliyor")
    onerilen_satir_diz(kapsananlari_bul())
    ui.btn_kapsamlarigor.setEnabled(False)
    ui.btn_kapsamlarigor.setStyleSheet("border:1px solid;border-radius:10px;background:white;color:black;")


def onceki_butonlari_yok_et():
    for i in ui.silinmis_butonlar:
        i.close()

def butonlari_ve_harfleri_yinele():

    onceki_butonlari_yok_et()
    genislik = (int(ui.kutu_genislik) - int(((ui.sutun + 1) * 5))) / int(ui.sutun)
    yukseklik = int((ui.kutu_yukseklik - ((ui.satir + 1) * 5)) / ui.satir)

    solkosex = int(ui.kutu1_bas_x + 5)
    solkosey = int(ui.kutu1_bas_y + 5)



    for i in range(0, ui.satir):
            for j in range(0, ui.sutun):
                    ui.kutu1_butonlari[i][j].show()
                    ui.kutu1_butonlari[i][j].setGeometry(int(solkosex), int(solkosey), int(genislik), int(yukseklik))
                    ui.kutu1_butonlari[i][j].setEnabled(False)
                    solkosex += genislik + 5
            solkosex = int(ui.kutu1_bas_x + 5)
            solkosey += yukseklik + 5


    for i in ui.lbl_satir_harfleri:
        i.close()

    for j in ui.lbl_sutun_sayilari:
        j.close()

    ui.lbl_satir_harfleri.clear()
    ui.lbl_sutun_sayilari.clear()

    genislik = (int(ui.kutu_genislik) - int((ui.sutun + 1) * 5)) / int(ui.sutun)
    yukseklik = int((ui.kutu_yukseklik - ((ui.satir + 1) * 5)) / ui.satir)

    solkosex = int(ui.kutu1_bas_x + 5)
    solkosey = int(ui.kutu1_bas_y + 5)



    for i in range(0, ui.satir):
        lblsatir = QtWidgets.QLabel(MainWindow)
        lblsatir.setText(str(ui.kalan_satir_harfleri[i]))
        lblsatir.setAlignment(QtCore.Qt.AlignVCenter)
        lblsatir.setGeometry(7, int(solkosey) , 10, int(yukseklik))
        lblsatir.show()
        ui.lbl_satir_harfleri.append(lblsatir)
        solkosey += yukseklik + 5

    for i in range(0, ui.sutun):
        lblsutun = QtWidgets.QLabel(MainWindow)
        lblsutun.setText(str(ui.kalan_sutun_idleri[i]))
        lblsutun.setAlignment(QtCore.Qt.AlignCenter)
        lblsutun.setGeometry(int(solkosex), 130, int(genislik), 13)
        lblsutun.show()
        ui.lbl_sutun_sayilari.append(lblsutun)
        solkosex += genislik + 5


def bos_satir_varmi():
    bossatirlar=[]
    t=0
    for i in range(ui.satir-1,-1,-1):
        for j in range(0,ui.sutun):
            if ui.kutu1_butonlari[i][j].text()=="1":
                t+=1

        if t==0:
            bossatirlar.append(i)
        t=0
    return bossatirlar


def satir_sil(dizi):
    cumle = []

    for i in dizi:
        cumle.append(ui.kalan_satir_harfleri[i])

    ui.text_yazialani.append(str(cumle) + " satırları silindi ")

    for i in range(len(dizi)-1,-1,-1):
        for a in ui.kutu1_butonlari[dizi[i]]:
            ui.silinmis_butonlar.append(a)

        del ui.kutu1_butonlari[dizi[i]]
        del ui.kalan_satir_harfleri[dizi[i]]
        del ui.kalan_satir_idleri[dizi[i]]

    ui.satir-=len(dizi)
    bos_butonlari_sil()

    ui.btn_basla.setEnabled(True)
    ui.btn_basla.setStyleSheet("border:1px solid;background:#37981A;color:white; border-radius:10px;")



def sutun_sil(dizi):

    cumle = []
    for i in dizi:
        cumle.append(str(ui.kalan_sutun_idleri[i]))

    ui.text_yazialani.append(str(cumle) + " sütunları silindi")

    for i in range(ui.satir):
        for j in range(ui.sutun-1,-1,-1):
            if j in dizi:
                ui.silinmis_butonlar.append(ui.kutu1_butonlari[i][j])
                del ui.kutu1_butonlari[i][j]

    for i in range(len(dizi)-1,-1,-1):
        del ui.kalan_sutun_idleri[dizi[i]]


    ui.sutun -= len(dizi)
    bos_butonlari_sil()


def bos_butonlari_sil():
    kutu1_toplam_butonu = 0
    for i in ui.kutu1_butonlari:
        for j in i:
            kutu1_toplam_butonu += 1

    kutu1_butonlari = np.reshape(ui.kutu1_butonlari,(1,kutu1_toplam_butonu))
    kutu2_labelleri = np.reshape(ui.kutu2_labelleri,(ui.sabitsatir,ui.sabitsutun))


    for i in range(ui.sabitsatir):
        for j in range(ui.sabitsutun):
            if ui.kutu2_butonlari[i][j] not in kutu1_butonlari:
                kutu2_labelleri[i][j].setStyleSheet("background:#18110C;")






def satir_sutun_kesisme(dizi):
    kesisensutunindis=[]

    for i in range(0,ui.satir):
        if i in dizi:
            for j in range(0,ui.sutun):
                if ui.kutu1_butonlari[i][j].text()=="1" and j not in kesisensutunindis:
                    kesisensutunindis.append(j)

    kesisensutunindis.sort()
    return kesisensutunindis





def silinecek_satir_dizisine_ekle(id):

    if id not in ui.silinecek_satirlar:
        ui.silinecek_satirlar.append(int(id))

    ui.btn_secilensatirsil.setEnabled(True)
    ui.btn_secilensatirsil.setStyleSheet("border:1px solid;background:#37981A;color:white; border-radius:10px;")

def onerilen_satir_diz(dizi):

    ui.btngrup_onerilenbuton = QtWidgets.QButtonGroup(MainWindow)
    ui.btngrup_onerilenbuton.setExclusive(True)
    ui.btngrup_onerilenbuton.buttonClicked[int].connect(silinecek_satir_dizisine_ekle)

    baslax = 130
    genislik = 60

    for i in range(0, len(dizi)):
        buton = QtWidgets.QPushButton(MainWindow)
        buton.setGeometry(int(baslax), 11, int(genislik), 20)
        buton.setText(str(ui.kalan_satir_harfleri[dizi[i]]))
        buton.setStyleSheet("background:green;border-radius:5px;color:white;font-size:13px;")
        ui.btngrup_onerilenbuton.addButton(buton, dizi[i])
        buton.show()
        baslax += 70



def mutlak_bul():
    sutun_agirliklari = sutun_agirlik_bul()

    mutlak_satirlar_indis = []
    mutlak_sutunlarin_indisi = []

    for i in range(0,len(sutun_agirliklari)):
        if sutun_agirliklari[i] == 1 :
            mutlak_sutunlarin_indisi.append(i)

    for i in range(0, ui.satir):
        for j in range(0, ui.sutun):
            if j in mutlak_sutunlarin_indisi and ui.kutu1_butonlari[i][j].text() == "1" and i not in mutlak_satirlar_indis:
                mutlak_satirlar_indis.append(int(i))

    return mutlak_satirlar_indis




def sutun_agirlik_bul():
    stnagirlik = []

    for i in range(0, ui.sutun):
        stnagirlik.append(int(0))

    for i in range(0, ui.satir):
        for j in range(0, ui.sutun):
            if ui.kutu1_butonlari[i][j].text() == "1":
                 stnagirlik[j] += 1

    return stnagirlik


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
