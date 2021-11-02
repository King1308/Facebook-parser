from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox
import pandas as pd
import subprocess

from FbParsForMS import Parser, Setings, Cookies
pars = Parser()
settings = Setings().get()
cook = Cookies(settings)
cook.get()

app = QtWidgets.QApplication([])
if settings["language"] == "Ua":
    ui = uic.loadUi("ua.ui")
elif settings["language"] == "Eng":
    ui = uic.loadUi("eng.ui")


def compleat():
    ret = QMessageBox.question(ui, 'MessageBox', "Дані зпарсені\n\nВідкрити папку з файлами результату,",
                               QMessageBox.Yes, QMessageBox.No)

    if ret == QMessageBox.Yes:
        subprocess.call("explorer exports", shell=True)


def eror():
    msg = QMessageBox()
    msg.setWindowTitle("Eror")
    msg.setText("Силка не існує або неправильно написана або інший збій")
    msg.setIcon(QMessageBox.Warning)
    msg.exec_()


def get_us_url():
    text = ui.usUrlInp.text()
    short = ui.usUrlS.isChecked()
    if short:
        url = text
    else:
        url = str(text)[25:]
    return(url)


def get_us_urls():
    text = ui.usersUrlInp.toPlainText()
    short = ui.usersUrlS.isChecked()
    urls = []
    urls_inp = text.split('\n')
    for url in urls_inp:
        if short:
            url = url
        else:
            url = str(url)[25:]
        urls.append(url)
    return(urls)


def get_post_urls():
    text = ui.postUrlInp.text()
    short = ui.postUrlS.isChecked()
    if short:
        url = text
    else:
        url = str(text)[25:]
    return(url)


def get_group_url():
    text = ui.groupUrlInp.text()
    short = ui.groupUrlS.isChecked()
    if short:
        url = text
    else:
        url = str(text)[32:]
    return(url)


def exel_users(exp):
    l = {}
    for k, v in exp.items():
        l[k.title()] = v
    df = pd.DataFrame(l)
    df.to_excel('exports/users.xlsx')


def exel_posts(exp):
    l = {}
    for k, v in exp.items():
        l[k.title()] = v
    df = pd.DataFrame(l)
    df.to_excel('exports/post.xlsx')


def exel_group(exp):
    l = {}
    for k, v in exp.items():
        l[k.title()] = v
    df = pd.DataFrame(l)
    df.to_excel('exports/groupes.xlsx')


def getuser():
    try:
        pars.get_user(get_us_url(), settings["collect_cookies"])
        export = pars.export()
        ui.usExL.setText(str(export[0]))
        exel_users(export[0])
        compleat()
    except:
        eror()


def getusers():
    try:
        urls = get_us_urls()
        for i in range(len(urls)):
            pars.get_user(urls[i], settings["collect_cookies"])
        export = pars.export()
        exel_users(export[0])
        compleat()
    except:
        eror()


def getpost():
    try:
        pars = Parser()
        url = get_post_urls()
        il = ui.postPInp.value()
        pars.get_postes(url, il, settings["collect_cookies"])
        export = pars.export()
        ui.postExL.setText(str(export[1]["text"]))
        exel_posts(export[1])
        compleat()
    except:
        eror()


def getgroup():
    try:
        pars.get_group(get_group_url(), settings["collect_cookies"])
        export = pars.export()
        ui.groupExL.setText(str(export[2]))
        exel_group(export[2])
        compleat()
    except:
        eror()


def conwertUs():
    text = ui.conUsI.text()
    if ui.conUsRS.isChecked():
        url = str(text)[25:]
    elif ui.conUsRF.isChecked():
        url = f"https://www.facebook.com/{text}"
    ui.conUsE.setText(url)


def conwertPost():
    text = ui.conPoI.text()
    if ui.conPoRS.isChecked():
        url = str(text)[25:]
    elif ui.conPoRF.isChecked():
        url = f"https://www.facebook.com/{text}"
    ui.conPoE.setText(url)


def conwertGroup():
    text = ui.conGrI.text()
    ToI = ui.conGrTo.currentIndex()
    ToWI = ui.conGrToW.currentIndex()
    FrW = ui.conGrFrW.currentIndex()
    L = [ToI, ToWI, FrW]
    if L[0] == 0:
        if L[1] == 0:
            if L[2] == 0:
                url = f"https://www.facebook.com/{text}"
                ui.conGrE.setText(url)
            elif L[2] == 1:
                url = f"https://www.facebook.com/{text[7:]}"
                ui.conGrE.setText(url)
        elif L[1] == 1:
            if L[2] == 0:
                url = f"https://www.facebook.com/groups/{text}"
                ui.conGrE.setText(url)
            elif L[2] == 1:
                url = f"https://www.facebook.com/{text}"
                ui.conGrE.setText(url)
    elif L[0] == 1:
        if L[1] == 0:
            if L[2] == 0:
                url = f"{text[25:]}"
                ui.conGrE.setText(url)
            elif L[2] == 1:
                url = f"{text[32:]}"
                ui.conGrE.setText(url)
        elif L[1] == 1:
            if L[2] == 0:
                url = f"groups/{text[25:]}"
                ui.conGrE.setText(url)
            elif L[2] == 1:
                url = f"{text[25:]}"
                ui.conGrE.setText(url)


ui.usGetB.clicked.connect(getuser)
ui.usersGetB.clicked.connect(getusers)
ui.postGetB.clicked.connect(getpost)
ui.groupGetB.clicked.connect(getgroup)

ui.conUsB.clicked.connect(conwertUs)
ui.conPoB.clicked.connect(conwertPost)
ui.conGrB.clicked.connect(conwertGroup)

if __name__ == "__main__":
    try:
        pars.get_group(" ")
    except:
        pass
    ui.show()
    app.exec()
