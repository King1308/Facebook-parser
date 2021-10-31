from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox
import pandas as pd
import subprocess

from FbParsForMS import Parser
pars = Parser()

app = QtWidgets.QApplication([])
ui = uic.loadUi("ui.ui")


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
    df = pd.DataFrame({'Name': exp["names"], 'ID': exp["ids"], 'Pictures': exp["pictures"], 'Contacts': exp["contacts"], 'Family': exp["family"], 'Place lived': exp["place"],
                      'Work': exp["work"], 'Life Events': exp["events"], 'Basic Info': exp["info"], 'Education': exp["education"], 'Relationship': exp["relationship"]})
    df.to_excel('exports/users.xlsx')


def exel_posts(exp):
    l = {"Shared text": exp["shared_text"], "Post ID": exp["post_id"], "Text": exp["text"], "Posted text": exp["post_text"], "Publication time": exp["time"], "Tine stamp": exp["timestamp"], "Image": exp["image"], "Image lowquality": exp["image_lowquality"], "Images": exp["images"], "Images description": exp["images_description"], "images lowquality": exp["images_lowquality"], "Images lowquality description": exp["images_lowquality_description"], "Video": exp["video"], "Video duration(sec)": exp["video_duration_seconds"], "Video width": exp["video_width"], "Video height": exp["video_height"], "Video ID": exp["video_id"], "Video quality": exp["video_quality"], "Video siza(MB)": exp["video_size_MB"], "Video thumbnail": exp["video_thumbnail"], "Video watches": exp["video_watches"],
         "Likes": exp["likes"], "Comments": exp["comments"], "Shares": exp["shares"], "Post url": exp["post_url"], "Link": exp["link"], "links": exp["links"], "User ID": exp["user_id"], "Username": exp["username"], "User URL": exp["user_url"], "Is live": exp["is_live"], "Fatcheck": exp["factcheck"], "Shared post ID": exp["shared_post_id"], "Shared time": exp["shared_time"], "Shared user ID": exp["shared_user_id"], "Shared username": exp["shared_username"], "Shared post url": exp["shared_post_url"], "Available": exp["available"], "Full comments": exp["comments_full"], "Reactors": exp["reactors"], "W3 fb url": exp["w3_fb_url"], "Reactions": exp["reactions"], "Reactions count": exp["reaction_count"], "With": exp["with"], "Image ID": exp["image_id"], "Image IDs": exp["image_ids"]}
    df = pd.DataFrame(l)
    df.to_excel('exports/post.xlsx')


def exel_group(exp):
    df = pd.DataFrame({'Admins': exp["admins"], 'ID': exp["id"],
                       'Members': exp["members"], 'Name': exp["name"], 'Type': exp["type"]})
    df.to_excel('exports/groupes.xlsx')


def getuser():
    try:
        pars.get_user(get_us_url())
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
            pars.get_user(urls[i])
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
        pars.get_postes(url, il)
        export = pars.export()
        ui.postExL.setText(str(export[1]["text"]))
        exel_posts(export[1])
        compleat()
    except:
        eror()


def getgroup():
    try:
        pars.get_group(get_group_url())
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
