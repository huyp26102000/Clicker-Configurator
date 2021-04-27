from package import *

cred = credentials.Certificate("./inspiration/serviceAccountKey.json")
default_app = firebase_admin.initialize_app(cred)
db = firestore.client()

def getNewID():
    id = uuid.uuid4()
    return str(id)
def serial_ports():
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')
    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result
def getStudent(studentID):
    docs = db.collection(u'student').where(u'studentID', u'==', studentID).stream()
    allDoc = list(docs)
    for i in range(0, len(allDoc)):
        allDoc[i] = allDoc[i].to_dict()
    return allDoc
# getStudent('HE140610')