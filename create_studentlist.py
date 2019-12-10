#!/usr/bin/python3


import psycopg2


def create_studentlist():
    query = "COPY (select auth_user.last_name, auth_user.first_name, accounts_user.mat_number, count(solutions_solution.author_id) as tasks_completed, ((select count(*) from tasks_task where title like 'H%' and submission_date < now()) - count(solutions_solution.author_id)) as tasks_failed from accounts_user, auth_user, solutions_solution, tasks_task where accounts_user.user_ptr_id=solutions_solution.author_id and tasks_task.id=solutions_solution.task_id and auth_user.id = accounts_user.user_ptr_id and auth_user.is_staff='f' and solutions_solution.final='t' and solutions_solution.accepted='t' and tasks_task.title like 'H%' and tasks_task.submission_date < now() group by accounts_user.mat_number, auth_user.last_name, auth_user.first_name)TO STDOUT WITH CSV HEADER"
    ps_conn = psycopg2.connect("host=DB_HOST port=DB_PORT dbname=DB_NAME user=DB_USER password=DB_PASS")
    cursor = ps_conn.cursor()
    file = open('/student_list.csv', 'w')
    cursor.copy_expert(query, file, size=8192)  
    cursor.close()
    ps_conn.close()
    file.close()


create_studentlist()
