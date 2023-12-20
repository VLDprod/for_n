import firebase_admin
from firebase_admin import db, credentials
import os


try:
    cred = credentials.Certificate("Update_N/credentials.json")
    firebase_admin.initialize_app(cred, {"databaseURL": "https://updane-n-default-rtdb.europe-west1.firebasedatabase.app"})
    
except Exception as ero:
    print(ero)

#a = fb.db.reference(f"/auto-connect-lessons/schedule/{today}/{which_less}").get()
#fb.db.reference(f"/auto-connect-lessons/schedule/{x}").set(less_arr)