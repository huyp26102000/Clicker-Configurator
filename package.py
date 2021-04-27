import sys
import glob
import serial
import time
import uuid

import firebase_admin
from firebase_admin import credentials, firestore
from firebase_admin import credentials

from model.login import *
from model.Manager_UI import *
from model.profile_UI import *