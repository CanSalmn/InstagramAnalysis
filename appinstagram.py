import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from selenium import webdriver
import time
from  INTERFACEAPP import *
from loginandgetper import *
from ABOUT import *


"---------------------------------------------------------------------------------------------------------"

app = QtWidgets.QApplication(sys.argv)
main_screen =QtWidgets.QMainWindow()
pagetool = Ui_MainWindow()
pagetool.setupUi(main_screen)
main_screen.show()
user_name=""
password=""
global boolValu
boolValu=False
"---------------------------------------------ABOUT PENCERESI----------------------------------------------------"


about_screen=QtWidgets.QDialog()
pagetool2=Ui_ABOUT()
pagetool2.setupUi(about_screen)

def showAbout():
    about_screen.show()


pagetool.menubar.triggered.connect(showAbout)








"---------------------------------------------GİRİS BİLGİLERİ ALMA---------------------------------------------"

def show():
    global user_name
    global password
    user_name= pagetool.USERNAMEIN.text()
    password= pagetool.PASSWORDIN.text()
    print(user_name)
    print(password)
    if (user_name and password) == "":
        QtWidgets.QMessageBox.information(main_screen, "ERROR", "Boşlukları eksiksiz doldurunuz.",
                                          QtWidgets.QMessageBox.Ok)



pagetool.LOGINBUTTON.clicked.connect(show)

"--------------------------------------------ISLEM----------------------------------------------------"
def hesap_cekme():
    global boolValu
    global liste
    if (user_name and password) != "":
        QtWidgets.QMessageBox.information(main_screen, "INFO",
                                          "Açılan Tarayıcıda herhangi bir İşlem yapmayınız.İşlem hızınız takipçi sayısına ve internet hızınıza göre değişiklik gösterebilir.",
                                          QtWidgets.QMessageBox.Ok)
        account = Getfollowers()
        liste=account.usercon(user_name,password)
        print(liste)
        boolValu=liste[3]
        return boolValu
    elif (user_name and password) != "" and (boolValu == False):
        print("hesap_cekme de hata var.")
        QtWidgets.QMessageBox.information(main_screen, "ERROR", "Tekrar Deneyiniz.",   QtWidgets.QMessageBox.Ok)
        boolValu=False
        return boolValu



pagetool.LOGINBUTTON.clicked.connect(hesap_cekme)

"--------------------------------------------KİSİLERİ LİSTELEME---------------------------------------------------------------"

def kisi_gonderme():
    
    try:
        print("kişilere listes",liste[0])
        if (user_name and password) != "" and boolValu:

            pagetool.listWidget.addItems(liste[0])
            print(liste[0])
            QtWidgets.QMessageBox.information(main_screen, "INFO",
                                              "İŞLEMİNİZ BAŞARIYLA TAMAMLANDI.(TARAYICIYI KAPATMAYIN !!!)",
                                              QtWidgets.QMessageBox.Ok)
        elif (user_name and password) != "" and (boolValu == False):
            QtWidgets.QMessageBox.information(main_screen, "ERROR",
                                              "Kullanıcı adınız veya parolanız hatalı lüften tekrar deneyiniz.",
                                              QtWidgets.QMessageBox.Ok)
    except:
        print("kisi_gonderme de hata var")

pagetool.LOGINBUTTON.clicked.connect(kisi_gonderme)


"--------------------------------------------Hesaplara erişim-------------------------------------------------"
def hesaplara_erisim():
    global response
    try:
        print("listenin ikinci elemanı sessions id:", liste[1])
        print("listenin üçüncü elemanı execute url:", liste[2])

        if (user_name and password) != ""and boolValu:
            hesap_id = pagetool.listWidget.selectedItems()
            i = hesap_id[0]
            id=i.text()
            lastid=id
            print("i nin değeri ",i.text)
            print("id nin değeri ",lastid)
            account1=Getfollowers()
            response=account1.other_page(lastid,liste[1],liste[2])
            print(response)
            if response == True:
                print("HERE")
                QtWidgets.QMessageBox.information(main_screen, "ERROR", "Tekrar giriş yapmalısınız tarayıcınız kapatılmış.",
                                            QtWidgets.QMessageBox.Ok)

    except:
        QtWidgets.QMessageBox.information(main_screen, "ERROR", "Önce Giriş yapmalısınız.",
                                              QtWidgets.QMessageBox.Ok)
        print("hesaplara_erisim de hata var.")
pagetool.SHOWITEM.clicked.connect(hesaplara_erisim)



"--------------------------------------------INFO Sağda üst button--------------------------------------------"
def topinfo():
    QtWidgets.QMessageBox.information(main_screen, "How Does It Work","1.Belirtilen Alanlara kullanıcı adı ve şifreninizi giriniz.\n2.Eksiksiz doldurduktan sonra LOGIN butonuna basınız.\n3.Bir süre bekledikten sonra sayfanın alt kısmında hesapları göreceksiniz.",
                                      QtWidgets.QMessageBox.Ok)


pagetool.toolButton.clicked.connect(topinfo)


"--------------------------------------------Çıkış----------------------------------------------------"

def shut_down():
    main_screen.close()
    close_up = Getfollowers()
    close_up.close_upwindows(liste[1],liste[2])




pagetool.LOGOUT.clicked.connect(shut_down)








sys.exit(app.exec_())



































































