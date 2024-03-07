from PyQt5.QtWidgets import *
import sys
from PyQt5.uic import loadUiType
import mysql.connector
from fpdf import FPDF
import os

hass,_=loadUiType('untitled.ui')
class hassan(QMainWindow,hass):
    def __init__(self):
        super(hassan,self).__init__()
        QMainWindow.__init__(self)
        self.setupUi(self)

        self.les_button()
        self.db_connecte()
        self.showclient()
        self.showfournisseur()
        self.comclient()
        self.wilaya()
        self.region()
        self.wilayafo()
        self.regionfo()





    def db_connecte(self):
        self.db =mysql.connector.connect(user='root',password='root',
                                        host='localhost',port=3306,db='hassan')
        self.cur= self.db.cursor()
        print('hassan')

    def les_button(self):

        self.pushButton.clicked.connect(self.open_mesclient)
        self.pushButton_2.clicked.connect(self.open_fournisseur)
        self.pushButton_5.clicked.connect(self.open_facture)
        self.pushButton_6.clicked.connect(self.open_caisse)

        self.pushButton_9.clicked.connect(self.openlistedeproduit)
        self.pushButton_13.clicked.connect(self.lesachats)
        self.pushButton_19.clicked.connect(self.lesventes)

        self.pushButton_82.clicked.connect(self.acceuil)
        self.pushButton_83.clicked.connect(self.acceuil)
        self.pushButton_3.clicked.connect(self.client)
        self.pushButton_4.clicked.connect(self.client)
        self.pushButton_31.clicked.connect(self.lesclient)
        self.pushButton_28.clicked.connect(self.acceuil)
        self.pushButton_34.clicked.connect(self.fournisseur)
        self.pushButton_35.clicked.connect(self.fournisseur)
        self.pushButton_39.clicked.connect(self.lesfournisseur)
        self.pushButton_40.clicked.connect(self.fecture)
        self.pushButton_48.clicked.connect(self.lesfacture)
        self.pushButton_30.clicked.connect(self.insereclient)
        self.pushButton_38.clicked.connect(self.insertfournisseur)
        self.pushButton_89.clicked.connect(self.searshfourniseurtab)
        self.pushButton_90.clicked.connect(self.searshfourniseur)
        self.pushButton_92.clicked.connect(self.modifiefournisseur)

        self.pushButton_154.clicked.connect(self.ajouteproduit)
        self.pushButton_85.clicked.connect(self.modifieclient)
        self.pushButton_87.clicked.connect(self.searshclient)
        self.pushButton_86.clicked.connect(self.deletclient)
        self.pushButton_88.clicked.connect(self.searshclienttab)
        self.pushButton_27.clicked.connect(self.pdfclient)

    def insereclient(self):


        code=self.lineEdit_3.text()
        nom=self.lineEdit_4.text()
        activit=self.lineEdit_5.text()
        nature=self.comboBox_5.currentText()
        wilaya=self.lineEdit_78.text()
        region=self.lineEdit_77.text()
        adresse=self.lineEdit_9.text()
        telephon=self.lineEdit_6.text()
        mobil=self.lineEdit_8.text()
        mail=self.lineEdit_11.text()
        regcom=self.lineEdit_12.text()
        matfisco=self.lineEdit_13.text()
        artimpo=self.lineEdit_14.text()
        nis=self.lineEdit_15.text()
        soldeini=self.lineEdit_16.text()
        reglement=self.comboBox_8.currentText()
        soldemax=self.lineEdit_17.text()
        soldeactuel=self.lineEdit_18.text()
        note=self.lineEdit_7.text()

        tarif=45
        solde=12


        self.cur.execute('''
        INSERT INTO client
        (code,nom,tarif,adresse,telephon,region,wilaya,mail,solde,activite,nature,mobile,regcom,matfisco,artimpo,nis,soldeinitial,soldemax,reglement,soldeactuel,note)
        VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        ''',(code,nom,tarif,adresse,telephon,region,wilaya,mail,solde,activit,nature,mobil,regcom,matfisco,artimpo,nis,soldeini,soldemax,reglement,soldeactuel,note))
        self.db.commit()


        self.showclient()

    def modifieclient(self):
        code=self.lineEdit_3.text()
        nom=self.lineEdit_4.text()
        activit=self.lineEdit_5.text()
        nature=self.comboBox_5.currentText()
        wilaya=self.lineEdit_78.text()
        region=self.lineEdit_77.text()
        adresse=self.lineEdit_9.text()
        telephon=self.lineEdit_6.text()
        mobil=self.lineEdit_8.text()
        mail=self.lineEdit_11.text()
        regcom=self.lineEdit_12.text()
        matfisco=self.lineEdit_13.text()
        artimpo=self.lineEdit_14.text()
        nis=self.lineEdit_15.text()
        soldeini=self.lineEdit_16.text()
        reglement=self.comboBox_8.currentText()
        soldemax=self.lineEdit_17.text()
        soldeactuel=self.lineEdit_18.text()
        note=self.lineEdit_7.text()

        tarif=45
        solde=12

        self.cur.execute('''
        UPDATE client SET  nom=%s,tarif=%s,adresse=%s,telephon=%s,region=%s,wilaya=%s,mail=%s,solde=%s,activite=%s,nature=%s,mobile=%s,regcom=%s,matfisco=%s,artimpo=%s,nis=%s,soldeinitial=%s,soldemax=%s,reglement=%s,soldeactuel=%s,note=%s 
        WHERE  code=%s''',(nom,tarif,adresse,telephon,region,wilaya,mail,solde,activit,nature,mobil,regcom,matfisco,artimpo,nis,soldeini,soldemax,reglement,soldeactuel,note,code))
        self.db.commit()

    def showclient(self):

        self.tableWidget.clear()
        self.tableWidget.insertRow(0)
        self.cur.execute('''

                SELECT code,nom,tarif,adresse,telephon,region,wilaya,mail,solde FROM client 
                ''')
        data = self.cur.fetchall()


        for row, fo in enumerate(data):

            for col, item in enumerate(fo):
                self.tableWidget.setItem(row, col, QTableWidgetItem(str(item)))
                col += 1

            pos = self.tableWidget.rowCount()
            self.tableWidget.insertRow(pos)


    def searshclienttab(self):

        nom = self.lineEdit_2.text()
        code = self.lineEdit.text()
        self.tableWidget.clear()
        self.tableWidget.insertRow(0)
        self.cur.execute('''

                SELECT code,nom,tarif,adresse,telephon,region,wilaya,mail,solde FROM client 
                WHERE code=%s OR nom=%s''',(code,nom))
        data = self.cur.fetchall()

        for row, fo in enumerate(data):

            for col, item in enumerate(fo):
                self.tableWidget.setItem(row, col, QTableWidgetItem(str(item)))
                col += 1

            pos = self.tableWidget.rowCount()
            self.tableWidget.insertRow(pos)



    def searshclient(self):
        code = self.lineEdit_3.text()
        self.cur.execute('''
        SELECT * FROM   client WHERE  code=%s
        ''',(code,))
        data=self.cur.fetchone()
        print(data)
        self.lineEdit_4.setText(data[2])
        self.lineEdit_9.setText(data[4])
        self.lineEdit_6.setText(data[5])

        self.lineEdit_78.setText(data[7])
        self.lineEdit_77.setText(data[6])
        self.lineEdit_11.setText(data[8])

        self.lineEdit_5.setText(data[10])
        self.comboBox_5.setCurrentText(data[11])
        self.lineEdit_8.setText(str(data[12]))

        self.lineEdit_12.setText(data[13])
        self.lineEdit_13.setText(data[14])
        self.lineEdit_14.setText(data[15])
        self.lineEdit_15.setText(data[16])

        self.lineEdit_16.setText(str(data[17]))
        self.comboBox_8.setCurrentText(data[19])
        self.lineEdit_17.setText(str(data[18]))
        self.lineEdit_18.setText(str(data[20]))
        self.lineEdit_7.setText(data[21])


    def deletclient(self):

        code = self.lineEdit_3.text()

        self.cur.execute('''
        DELETE FROM client WHERE code=%s
        ''',(code,))

        self.db.commit()

    def wilaya(self):
        self.cur.execute('''
        SELECT wilaya FROM client 
        ''')
        data=self.cur.fetchall()
        dat =set(data)
        for wilaya in dat :
            self.comboBox.addItem(wilaya[0])

    def region(self):
        self.cur.execute('''
                SELECT region FROM client 
                ''')
        data = self.cur.fetchall()
        dat = set(data)
        for region in dat:
            self.comboBox_2.addItem(region[0])
    def pdfclient(self):
        cod=self.lineEdit.text()
        self.cur.execute('''

                    SELECT code,nom,tarif,adresse,telephon,region,wilaya,mail,solde FROM client WHERE code=%s
                    ''',(cod,))
        da = self.cur.fetchall()
        data=[(1,2,3,4,5,6,7,8,9)]
        data.extend(da)
        print(data)
        pdf = FPDF()
        pdf.add_page()

        pdf.set_font("Times", size=20)
        pdf.cell(40, 10, 'liste de client', ln=True)
        pdf.cell(40, 10, 'nom')
        pdf.cell(40, 10, data[1][1], ln=True)

        pdf.set_font("Times", size=10)
        line_height = pdf.font_size * 2.5
        col_width = pdf.epw / 9  # distribute content evenly
        for row in data:
            for datum in row:
                pdf.multi_cell(col_width, line_height, str(datum), border=1, ln=3, max_line_height=pdf.font_size)
            pdf.ln()
        pdf.output('hassan.pdf')

        path = 'hassan.pdf'
        os.system(path)



    def insertfournisseur(self):


        code=self.lineEdit_21.text()
        nom=self.lineEdit_110.text()
        wilaya=self.lineEdit_26.text()
        region=self.lineEdit_111.text()
        adresse=self.lineEdit_31.text()
        telephon=self.lineEdit_25.text()
        mobile=self.lineEdit_27.text()
        mail=self.lineEdit_29.text()
        regcom=self.lineEdit_22.text()
        matfisco=self.lineEdit_23.text()
        artimpo=self.lineEdit_24.text()
        reglement=self.comboBox_13.currentText()
        soldeinitial=self.lineEdit_30.text()
        self.cur.execute('''
        INSERT INTO fournisseur (code,nom,adresse,telephon,mobil,region,wilaya,mail,soldeinitial,regcom,matfisco,artimpo,reglement)
        VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        ''',(code,nom,adresse,telephon,mobile,region,wilaya,mail,soldeinitial,regcom,matfisco,artimpo,reglement))
        self.db.commit()

        self.showfournisseur()

    def modifiefournisseur(self):
        code = self.lineEdit_21.text()
        nom = self.lineEdit_110.text()
        wilaya = self.lineEdit_26.text()
        region = self.lineEdit_111.text()
        adresse = self.lineEdit_31.text()
        telephon = self.lineEdit_25.text()
        mobile = self.lineEdit_27.text()
        mail = self.lineEdit_29.text()
        regcom = self.lineEdit_22.text()
        matfisco = self.lineEdit_23.text()
        artimpo = self.lineEdit_24.text()
        reglement = self.comboBox_13.currentText()
        soldeinitial = self.lineEdit_30.text()

        self.cur.execute('''
        UPDATE fournisseur SET nom=%s,adresse=%s,telephon=%s,mobil=%s,region=%s,wilaya=%s,mail=%s,soldeinitial=%s,regcom=%s,matfisco=%s,artimpo=%s,reglement=%s
        WHERE code=%s''',(nom,adresse,telephon,mobile,region,wilaya,mail,soldeinitial,regcom,matfisco,artimpo,reglement,code))
        self.db.commit()

    def searshfourniseur(self):


        code = self.lineEdit_21.text()

        self.cur.execute('''
        SELECT * FROM fournisseur
        WHERE code=%s
        ''',(code,))
        data=self.cur.fetchone()
        self.lineEdit_110.setText(data[2])
        self.lineEdit_31.setText(data[3])
        self.lineEdit_25.setText(str(data[4]))
        self.lineEdit_27.setText(str(data[5]))

        self.lineEdit_111.setText(data[6])
        self.lineEdit_26.setText(data[7])

        self.lineEdit_29.setText(data[8])
        self.lineEdit_30.setText(str(data[9]))
        self.lineEdit_22.setText(str(data[10]))
        self.lineEdit_23.setText(str(data[11]))
        self.lineEdit_24.setText(str(data[12]))
        self.comboBox_13.setCurrentText(str(data[13]))



    def showfournisseur(self):
        self.tableWidget_2.insertRow(0)

        self.cur.execute('''
        SELECT code,nom,adresse,telephon,mobil,mail,wilaya,region FROM fournisseur 
        ''')

        data= self.cur.fetchall()

        for row , form in enumerate(data):
            for col , item in enumerate(form):
                self.tableWidget_2.setItem(row,col,QTableWidgetItem(str(item)))

                col+=1

            pos=self.tableWidget_2.rowCount()
            self.tableWidget_2.insertRow(pos)

    def searshfourniseurtab(self):

        code=self.lineEdit_19.text()
        nom = self.lineEdit_20.text()
        self.tableWidget_2.clear()

        self.tableWidget_2.insertRow(0)

        self.cur.execute('''
        SELECT code,nom,adresse,telephon,mobil,mail,wilaya,region FROM fournisseur 
        WHERE code=%s OR nom=%s ''',(code,nom))

        data= self.cur.fetchall()

        for row , form in enumerate(data):
            for col , item in enumerate(form):
                self.tableWidget_2.setItem(row,col,QTableWidgetItem(str(item)))

                col+=1

            pos=self.tableWidget_2.rowCount()
            self.tableWidget_2.insertRow(pos)

    def comclient(self):
        self.comboBox_19.clear()
        self.cur.execute('''
        SELECT  nom FROM client 
        ''')

        data=self.cur.fetchall()

        for name in data :
            self.comboBox_19.addItem(str(name[0]))

    def wilayafo(self):
        self.comboBox_10.clear()
        self.cur.execute('''
                SELECT  wilaya FROM fournisseur 
                ''')

        data = self.cur.fetchall()
        data=set(data)
        for wilaya in data:
            self.comboBox_10.addItem(str(wilaya[0]))
    def regionfo(self):
        self.comboBox_9.clear()
        self.cur.execute('''
                        SELECT  region FROM fournisseur 
                        ''')

        data = self.cur.fetchall()
        data = set(data)
        for region in data:
            self.comboBox_9.addItem(str(region[0]))

    def ajouteproduit(self):

        reference=self.lineEdit_46.text()
        nom=self.lineEdit_47.text()
        code=self.lineEdit_48.text()
        unite=self.lineEdit_49.text()
        cond=self.lineEdit_51.text()
        tva=self.lineEdit_50.text()
        famille=self.lineEdit_79.text()
        marque=self.lineEdit_80.text()
        etat=self.comboBox_28.currentText()
        image='hassan'
        prixht=self.lineEdit_53.text()
        prixttc=self.lineEdit_54.text()
        pmp=self.lineEdit_55.text()
        dernierprix=self.lineEdit_56.text()
        fournisser=self.comboBox_29.currentText()
        initial=self.lineEdit_72.text()
        alert=self.lineEdit_73.text()
        localisation=self.lineEdit_81.text()

        detailht=self.lineEdit_57.text()
        revendeurht=self.lineEdit_58.text()
        grosht=self.lineEdit_59.text()
        autre1ht=self.lineEdit_60.text()
        autre2ht=self.lineEdit_61.text()

        detailttc =self.lineEdit_63.text()
        revendeurttc =self.lineEdit_63.text()
        grosttc =self.lineEdit_63.text()
        autre1ttc =self.lineEdit_63.text()
        autre2ttc =self.lineEdit_62.text()

        detailmarge = self.lineEdit_68.text()
        revendeurmarge =self.lineEdit_69.text()
        grosmarge =self.lineEdit_70.text()
        autre1marge =self.lineEdit_71.text()
        autre2marge =self.lineEdit_67.text()

        pack=self.lineEdit_76.text()
        prixdepack=self.lineEdit_75.text()
        prixunitair=self.lineEdit_76.text()

        observation=self.lineEdit_10.text()


        self.cur.execute('''
        INSERT INTO produit ( reference, nom, code, unite, conde, tva, famille, marque, etat, image, prixht, prixttc, pmp, dernierprix, fournisseur, initial, alert, localisation, detailht, revendeurht, grosht, autre1ht, autre2ht, detailttc, revendeurttc, grosttc, autre1ttc, autre2ttc, detailmarge, revendeurmarge, grosmarge, autre1marge, autre2marge, pack, prixdepack, prixunitair, observation )
        VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        ''',(reference, nom, code, unite, cond, tva, famille, marque, etat, image, prixht, prixttc, pmp, dernierprix, fournisser, initial, alert, localisation, detailht, revendeurht, grosht, autre1ht, autre2ht, detailttc, revendeurttc, grosttc, autre1ttc, autre2ttc, detailmarge, revendeurmarge, grosmarge, autre1marge, autre2marge, pack, prixdepack, prixunitair, observation))
        print(reference, nom, code, unite, cond, tva, famille, marque,etat,image,prixht,prixttc,pmp,dernierprix,fournisser,initial,alert,localisation)
        self.db.commit()







    def openlistedeproduit(self):
        self.tabWidget.setCurrentIndex(5)
    def fournisseur(self):
        self.tabWidget_4.setCurrentIndex(1)

    def lesfournisseur(self):
        self.tabWidget_4.setCurrentIndex(0)

    def fecture(self):
        self.tabWidget_5.setCurrentIndex(1)

    def lesfacture(self):
        self.tabWidget_5.setCurrentIndex(0)

    def lesclient(self):
        self.tabWidget_2.setCurrentIndex(0)

    def lesachats(self):
        self.tabWidget.setCurrentIndex(6)

    def lesventes(self):
        self.tabWidget.setCurrentIndex(7)

    def open_mesclient(self):
        self.tabWidget.setCurrentIndex(1)

    def open_fournisseur(self):
        self.tabWidget.setCurrentIndex(2)

    def open_facture(self):
        self.tabWidget.setCurrentIndex(3)

    def open_caisse(self):
        self.tabWidget.setCurrentIndex(4)

    def acceuil(self):
        self.tabWidget.setCurrentIndex(0)

    def client(self):
        self.tabWidget_2.setCurrentIndex(1)

if __name__ == '__main__':
    app=QApplication(sys.argv)
    win = hassan()
    win.show()
    app.exec_()