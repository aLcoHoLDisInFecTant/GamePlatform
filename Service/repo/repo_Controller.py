import pymysql

class DatabaseRepo:
    def __init__(self, host, user, password, dbname):
        self.host = host
        self.user = user
        self.password = password
        self.dbname = dbname
        self.connection = self.connect_to_database()

    def connect_to_database(self):
        try:
            connection = pymysql.connect(host=self.host, user=self.user, password=self.password, db=self.dbname)
            print("Database connection established.")
            return connection
        except pymysql.MySQLError as e:
            print("Error connecting to MySQL Platform: ", e)
            return None

    def check_and_create_tables(self):
        tables_sql = {
            'Patients': """
                CREATE TABLE IF NOT EXISTS Patients (
                    patient_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(100),
                    age INT,
                    gender CHAR(1),
                    contact_info VARCHAR(255),
                    emergency_contact VARCHAR(255),
                    medical_history TEXT
                );
            """,
            # Add the rest of your table creation SQL statements here
            # ...
            'GameSessions': '''
            CREATE TABLE GameSessions (
                session_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
                patient_id INT UNSIGNED,
                game_id INT UNSIGNED,
                start_time DATETIME,
                end_time DATETIME,
                performance_metrics TEXT,
                FOREIGN KEY (patient_id) REFERENCES Patients(patient_id),
                FOREIGN KEY (game_id) REFERENCES Games(game_id)
            );
            CREATE INDEX idx_patient_id ON GameSessions(patient_id);
            CREATE INDEX idx_game_id ON GameSessions(game_id);
            ''',
            'Games': '''
            CREATE TABLE Games (
                game_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
                game_name VARCHAR(100),
                description TEXT,
                type VARCHAR(50)
            );
            CREATE FULLTEXT INDEX idx_game_details ON Games(game_name, description);
            ''',
            'ProgressTracking': '''
            CREATE TABLE ProgressTracking (
                track_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
                patient_id INT UNSIGNED,
                session_id INT UNSIGNED,
                date DATE,
                score DECIMAL(5,2),
                physician_notes TEXT,
                FOREIGN KEY (patient_id) REFERENCES Patients(patient_id),
                FOREIGN KEY (session_id) REFERENCES GameSessions(session_id)
            );
            CREATE INDEX idx_progress_patient_id ON ProgressTracking(patient_id);
            CREATE INDEX idx_progress_session_id ON ProgressTracking(session_id);
            ''',
            'Therapists': '''
            CREATE TABLE Therapists (
                therapist_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100),
                specialization VARCHAR(100),
                contact_info VARCHAR(255),
                username VARCHAR(100) UNIQUE,
                password VARCHAR(100)
            );
            CREATE UNIQUE INDEX idx_username ON Therapists(username);
            ''',
            'PatientsTherapistRelation': '''
                CREATE TABLE PatientsTherapistRelation (
                relation_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
                therapist_id INT UNSIGNED,
                patient_id INT UNSIGNED,
                FOREIGN KEY (therapist_id) REFERENCES Therapists(therapist_id),
                FOREIGN KEY (patient_id) REFERENCES Patients(patient_id)
            );
            CREATE INDEX idx_therapist_patient ON PatientsTherapistRelation(therapist_id, patient_id);
                ''',


        }

        with self.connection.cursor() as cursor:
            for table_name, create_sql in tables_sql.items():
                cursor.execute(f"SHOW TABLES LIKE '{table_name}';")
                result = cursor.fetchone()
                if not result:
                    cursor.execute(create_sql)
                    print(f"Created table {table_name}.")
                else:
                    print(f"Table {table_name} already exists.")
            self.connection.commit()

    def close_connection(self):
        if self.connection:
            self.connection.close()
            print("Database connection closed.")

# Example usage:
# Replace 'host', 'user', 'password', and 'dbname' with your database information
repo = DatabaseRepo('host', 'user', 'password', 'dbname')
repo.check_and_create_tables()
# Do other database operations...
repo.close_connection()
