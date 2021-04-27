from package import *
from function import *

def removeTitleBar(Form):
    Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
def generateID():
    newID = getNewID()
    manager_UI.textEdit.setText(newID)
    manager_UI.textEdit_3.append('New device ID generated!')
def updatePort():
    portlist = serial_ports()
    manager_UI.comboBox.clear()
    for tmp in portlist:
        manager_UI.comboBox.addItem(str(tmp))
def serialConnection():
    selectedPort = str(manager_UI.comboBox.currentText())
    try:
        device = serial.Serial(port=selectedPort, baudrate=115200, timeout=.1)
        manager_UI.textEdit_3.append('<font color="green">Connected</font>')
    except:
        manager_UI.textEdit_3.append('<font color="red">Connect failed</font>')
def write_read(datain):
    selectedPort = str(manager_UI.comboBox.currentText())
    device = serial.Serial(port=selectedPort, baudrate=115200, timeout=.1)
    device.write(bytes(datain, 'utf-8'))
    time.sleep(0.05)
    data = device.readline()
    return str(data.decode("utf-8"))
def writeDeviceData():
    uuid = manager_UI.textEdit.toPlainText()
    data = uuid + '$' + manager_UI.textEdit_4.toPlainText()+'$'+manager_UI.textEdit_5.toPlainText()+'$'

    manager_UI.textEdit_3.append('<font color="green">Successfully override EEPROM Memory!</font>')
    manager_UI.textEdit_3.append('EEPROM DATA:')
    manager_UI.textEdit_3.append(write_read(data))
def getProfile():
    key = manager_UI.textEdit_2.toPlainText()
    if(key =='' or key == None):
        print('none')
    else:
        profileFound = getStudent(key)
        if(len(profileFound)>0):
            manager_UI.textEdit_3.append('<font color="green">Found profile!</font>')
        updateProfile(profileFound[0])
        profileForm.show()
def updateProfile(profileFound):
    profileUI.textEdit.setReadOnly(True)
    profileUI.textEdit_2.setReadOnly(True)
    profileUI.textEdit_3.setReadOnly(True)
    profileUI.textEdit_4.setReadOnly(True)
    profileUI.textEdit_5.setReadOnly(True)
    profileUI.textEdit.setText(profileFound['studentID'])
    profileUI.textEdit_2.setText(profileFound['fullname'])
    profileUI.textEdit_3.setText(profileFound['birthday'])
    profileUI.textEdit_4.setText(profileFound['gender'])
    profileUI.textEdit_5.setText(profileFound['class'])
def readEEPROM():
    print(write_read("read"))
def hideProfile():
    profileForm.hide()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    manager_UI = Manager_Ui_Form()
    manager_UI.setupUi(Form)
    manager_UI.textEdit_3.setReadOnly(True)

    profileForm = QtWidgets.QWidget()
    profileUI = Profile_Ui_Form()
    profileUI.setupUi(profileForm)
    removeTitleBar(profileForm)

    Form.show()
    updatePort()
    manager_UI.pushButton_4.clicked.connect(writeDeviceData)
    manager_UI.pushButton_2.clicked.connect(serialConnection)
    manager_UI.pushButton_3.clicked.connect(updatePort)
    manager_UI.pushButton.clicked.connect(generateID)
    manager_UI.pushButton_5.clicked.connect(getProfile)
    manager_UI.pushButton_6.clicked.connect(readEEPROM)

    profileUI.pushButton.clicked.connect(hideProfile)

    sys.exit(app.exec_())
