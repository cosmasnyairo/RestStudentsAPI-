import mysql.connector

from secrets import DB_SECRETS
from students import STUDENTS


class Database:
    def __init__(self):
        self.secrets = DB_SECRETS()
        self.db = mysql.connector.connect(
            host=self.secrets.host,
            user=self.secrets.username,
            password=self.secrets.password,
            database=self.secrets.database
        )

    def fetch_all(self):
        self. mycursor = self.db.cursor(dictionary=True)
        self.mycursor.execute(
            "SELECT * FROM {} ".format(self.secrets.table)
        )
        self.myresult = self.mycursor.fetchall()
        self.fetched_student = []
        for row in self.myresult:
            self.fetched_student.append(
                STUDENTS(
                    student_id=row['studentid'],
                    student_name=row['student_name'],
                    email=row['email'],
                    phone_number=row['phonenumber'],
                    student_address=row['student_address'],
                    entry_points=row['entrypoints']
                ).__dict__
            )
        return self.fetched_student

    def fetch_records(self, admission_number):
        self. mycursor = self.db.cursor(dictionary=True)
        self.mycursor.execute(
            "SELECT * FROM {} WHERE studentid={}".format(
                self.secrets.table, admission_number)
        )
        self.myresult = self.mycursor.fetchall()
        for row in self.myresult:
            print(row)
            self.fetched_student = STUDENTS(
                student_id=row['studentid'],
                student_name=row['student_name'],
                email=row['email'],
                phone_number=row['phonenumber'],
                student_address=row['student_address'],
                entry_points=row['entrypoints']
            )
        return self.fetched_student

    def insert_records(self, student_name, email, phone_number, student_address, entry_points):
        self.mycursor = self.db.cursor()
        self.sql = "INSERT INTO {} (student_name,email,phonenumber,student_address,entrypoints)  VALUES ({},{},{},{},{})".format(
            self.secrets.table,
            student_name,
            email,
            phone_number,
            student_address,
            entry_points
        )
        self.mycursor.execute(self.sql)
        self.db.commit()
