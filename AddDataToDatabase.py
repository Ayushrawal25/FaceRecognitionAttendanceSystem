import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://faceattendancerealtime-d8fef-default-rtdb.firebaseio.com/"
})
ref = db.reference('Student')

data = {
    "321654":
        {
            "name": "Murtaza",
            "major": "Robotics",
            "starting_year": 2022,
            "total_attendance":18,
            "standing": "G",
            "year":2,
            "last_attendance_time": "2002-12-11 00:54:34"
        },
    "852741":
        {
            "name": "Emily",
            "major": "Economics",
            "starting_year": 2021,
            "total_attendance": 10,
            "standing": "A",
            "year": 3,
            "last_attendance_time": "2002-12-11 00:54:34"
        },
    "963852":
        {
            "name": "Elon Musk",
            "major": "Aeronautics",
            "starting_year": 2020,
            "total_attendance": 15,
            "standing": "V",
            "year": 4,
            "last_attendance_time": "2002-12-11 00:54:34"
        },
    "972508":
        {
            "name": "Ayush Rawal",
            "major": "Information Technology",
            "starting_year": 2021,
            "total_attendance":25,
            "standing": "E",
            "year":3,
            "last_attendance_time": "2002-12-11 00:54:34"
        }

}

for key, value in data.items():
    ref.child(key).set(value)
