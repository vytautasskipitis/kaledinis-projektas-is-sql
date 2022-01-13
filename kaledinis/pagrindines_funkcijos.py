
import sqlite3
conn = sqlite3.connect(':memory:')
c = conn.cursor()

c.execute("""CREATE TABLE employees (
            first text,
            last text,
            pay integer
            )""")


# def get_emps_count_by_name(first, last):
#     c.execute(f"SELECT COUNT(*) FROM employees WHERE last=:{last} and first=:{first}")
#     return c.fetchall()
#     """0,1,2"""


def insert_emp(emp):
    with conn:
        c.execute("INSERT INTO employees VALUES (:first, :last, :pay)",
                  {'first': emp.first, 'last': emp.last, 'pay': emp.pay})


def get_emps_by_name(lastname):
    c.execute("SELECT * FROM employees WHERE last=:last", {'last': lastname})
    return c.fetchall()


# nostalgijai palikau
# def update_pay(emp, pay):
#     with conn:
#         c.execute("""UPDATE employees SET pay = :pay
#                     WHERE first = :first AND last = :last""",
#                   {'first': emp.first, 'last': emp.last, 'pay': pay})


def remove_emp(firstname, lastname):
    with conn:
        c.execute("DELETE from employees WHERE first=:first AND last=:last",
                  {'first': firstname, 'last': lastname})


if __name__ == "__main__":
    print("mainas veikia ")





