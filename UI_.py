from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QPushButton, QComboBox, QMenuBar, QAction, QMessageBox, QLabel, QFileDialog, QLineEdit, QCheckBox
from PyQt5.QtGui import QIcon, QFont
from json import load, dump

from text_2_speech import create_audio

from Json_Manip import json_manip


class UI(QWidget):

    font_textbox = QFont("Roboto", 11, weight=97)
    font_combobox = QFont("Tahoma", 12)
    font_menubar = QFont("Acknowledgement", 11, weight=97)
    font_menu = QFont("Verdana", 9, weight=87)
    font_label = QFont("Cascadia Mono", 10, weight=97)

    def __init__(this, *args, **kwargs):

        json_manip.OS_detected()

        this.app = QApplication([])

        this.icon = QIcon("icon.png")

        super().__init__(*args, **kwargs)

        this.setWindowTitle("Text-to-Speech")
        this.setWindowIcon(this.icon)
        this.setStyleSheet(open("CSS_files/QWidget.css").read())
        this.setFixedSize(this.app.primaryScreen().size().width()//3, this.app.primaryScreen().size().height()//2-this.app.primaryScreen().size().height()//11)

        this.menubar = QMenuBar(this)
        this.__menubar_setup()

        this.textbox = QTextEdit(this)
        this.textbox.setPlaceholderText("Enter your text here ...")
        this.textbox.setFont(this.font_textbox)
        this.textbox.setStyleSheet(open("CSS_files/QTextEdit.css").read())
        this.textbox.setGeometry(25, 30, this.width()-50, 150)

        label_lang = QLabel("Language", this)
        label_lang.setGeometry(30, this.textbox.y() + this.textbox.height()+20, this.width()//3, 30)
        label_lang.setFont(this.font_label)
        label_lang.setStyleSheet(open("CSS_files/QLabel.css").read())

        this.language = QComboBox(this)
        this.language.addItems(load(open("_config_.json"))["languages"])
        this.language.setGeometry(30, label_lang.y()+label_lang.height(), this.width()//3, 30)
        this.language.setStyleSheet(open("CSS_files/QComboBox.css").read())
        this.language.setFont(this.font_combobox)
        this.language.setCurrentText(json_manip.get_value("current_language"))
        this.language.currentTextChanged.connect(lambda: json_manip.update_config("current_language", this.language.currentText()))

        label_speed = QLabel("Fast", this)
        label_speed.setGeometry(this.language.x()+this.language.width()+50,this.textbox.y()+this.textbox.height()+20, this.width()//3, 30)
        label_speed.setFont(this.font_label)
        label_speed.setStyleSheet(open("CSS_files/QLabel.css").read())

        this.speed_checkbox = QCheckBox(this)
        this.speed_checkbox.setGeometry(label_speed.x()+15, label_lang.y()+label_lang.height(), 40, 40)
        this.speed_checkbox.setStyleSheet("background-color:transparent")

        label_accent = QLabel("Accent", this)
        label_accent.setGeometry(this.textbox.x()+this.textbox.width()-this.language.width(), this.textbox.y()+this.textbox.height()+20, this.width()//3, 30)
        label_accent.setFont(this.font_label)
        label_accent.setStyleSheet(open("CSS_files/QLabel.css").read())

        this.accent = QComboBox(this)
        this.accent.addItems(json_manip.get_value("accent"))
        this.accent.setGeometry(label_accent.x(), this.language.y(), this.language.width(), this.language.height())
        this.accent.setStyleSheet(open("CSS_files/QComboBox.css").read())
        this.accent.setFont(this.font_combobox)
        this.accent.setCurrentText(json_manip.get_value("current_accent"))
        this.accent.currentTextChanged.connect(lambda: json_manip.update_config("current_accent", this.accent.currentText()))

        this.play = QPushButton("Play", this)
        this.play.setGeometry(this.width()//2-50, this.language.y()+this.language.height()+30, 100, 50)
        this.play.setFont(this.font_menubar)
        this.play.setStyleSheet(open("CSS_files/QPushButton.css").read())
        this.play.pressed.connect(this.__play_pressed)

        label_save = QLabel("Save Location :", this)
        label_save.setFont(this.font_label)
        label_save.setGeometry(this.textbox.x(), this.play.y()+this.play.height()+35, this.width()//4, 30)
        label_save.setStyleSheet(open("CSS_files/QLabel.css").read())

        this.save_loc_box = QLineEdit(this)
        this.save_loc_box.setGeometry(label_save.x()+label_save.width(), label_save.y(), this.width()//2, label_save.height())
        this.save_loc_box.setStyleSheet(open("CSS_files/QLineEdit.css").read())
        this.save_loc_box.setFont(QFont("Times new Roman", 10, weight=97))
        this.save_loc_box.setDisabled(True)
        this.save_loc_box.setPlaceholderText("Default Location")
        this.save_loc_box.setText(json_manip.get_value("save_location"))
        this.save_loc_box.textChanged.connect(lambda: json_manip.update_config("save_location", this.save_loc_box.text()))

        this.choose_directory = QPushButton("Choose", this)
        this.choose_directory.setGeometry(this.save_loc_box.x() + this.save_loc_box.width()+10, this.save_loc_box.y(), this.save_loc_box.width()//4, this.save_loc_box.height())
        this.choose_directory.setFont(this.font_textbox)
        this.choose_directory.setStyleSheet(open("CSS_files/choose_dir.css").read())
        this.choose_directory.pressed.connect(lambda: this.save_loc_box.setText(str(QFileDialog.getExistingDirectory(this, "Select file location"))+"/"))

        this.show()
        exit(this.app.exec())

    def __menubar_setup(this):
        this.menubar.setGeometry(0, 0, 110, 24)
        this.menubar.setFont(this.font_menubar)
        this.menubar.setFont(this.font_menubar)
        this.menubar.setStyleSheet(open("CSS_files/QMenuBar.css").read())

        about = QAction("About", this.menubar)
        about.setFont(this.font_menu)
        about.triggered.connect(lambda : this.__message_display("About" ,json_manip.get_value("about_message") ))

        this.menubar.addAction(about)
        this.menubar.show()

    def __message_display(this, title: str, messsage: str):
        qm = QMessageBox()
        qm.setWindowTitle(title)
        qm.setWindowIcon(this.icon)
        qm.setFont(QFont("Bahnschrift", pointSize=10, weight=97))
        qm.setText(messsage)
        qm.setStyleSheet(open("CSS_files/QMessageBox.css").read())
        qm.exec()

    def __play_pressed(this):
        x = create_audio(this.textbox.toPlainText(), this.language.currentText(
        ), this.accent.currentText(), this.save_loc_box.text(), this.speed_checkbox.isChecked())
        if x.__len__() != 0:
            this.__message_display("Text-to-Speech", x)


if __name__ == "__main__":
    UI()
