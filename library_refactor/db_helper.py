import pymysql


def con():
    return pymysql.connect(
        host="localhost", user="root", password="newPass", database="testing_db"
    )


def create_tables():
    connection = con()
    with connection.cursor() as cursor:
        sql = """CREATE TABLE IF NOT EXISTS `student_data` (
                `id` int(1) NOT NULL AUTO_INCREMENT,
                `user_var` varchar(255) COLLATE utf8_bin NOT NULL,
                `first_name` varchar(255) COLLATE utf8_bin NOT NULL,
                `last_name` varchar(255) COLLATE utf8_bin NOT NULL,
                `study_hours` varchar(255) COLLATE utf8_bin NOT NULL,
                `study_date` varchar(255) COLLATE utf8_bin NOT NULL,
                `course_name` varchar(255) COLLATE utf8_bin NOT NULL,
                `course_module` varchar(255) COLLATE utf8_bin NOT NULL,
                PRIMARY KEY (`id`))
                ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin AUTO_INCREMENT=1;
              """
        cursor.execute(sql)


def write_data_to_db(
    user_var, first_name, last_name, study_hours, study_date, course_name, course_module
):
    connection = con()
    with connection.cursor() as cursor:
        sql = f"""INSERT INTO `student_data` (
        `user_var`, `first_name`, `last_name`, `study_hours`,
        `study_date`, `course_name`, `course_module`) 
         VALUES ( %s, %s, %s, %s, %s, %s, %s); """

        cursor.execute(
            sql,
            (
                user_var,
                first_name,
                last_name,
                study_hours,
                study_date,
                course_name,
                course_module,
            ),
        )
        connection.commit()
