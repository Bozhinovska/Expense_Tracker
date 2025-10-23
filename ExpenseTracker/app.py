from flask import Flask, render_template, request, url_for, redirect
import sqlite3

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/expenses', methods=['GET', 'POST'])
def expenses():
    if request.method == 'GET':
        conn = get_db_connection()

        expenses = conn.execute('SELECT * FROM expenses').fetchall()

        total = conn.execute('SELECT SUM(amount) FROM expenses').fetchone()[0]
        conn.close()
        return render_template('expenses.html', expenses=expenses, total=total)

    if request.method == 'POST':
        print("Form submitted!")
        conn = get_db_connection()

        expense_date = request.form['date']
        method_of_payment = request.form['method_of_payment']
        paid_to = request.form['paid_to']
        description = request.form['description']
        amount = request.form['amount']



        conn.execute('''
        INSERT INTO expenses (date, method_of_payment, paid_to, description, amount)
        VALUES (?, ?, ?, ?, ?);
        ''', (expense_date,method_of_payment, paid_to, description,amount))

        conn.commit()
        conn.close()
        return redirect(url_for('expenses'))

@app.route('/delete_expense/<int:expense_id>', methods=['POST'])
def delete_expense(expense_id):
    conn = get_db_connection()
    conn.execute('DELETE FROM expenses WHERE id=?', (expense_id,))
    conn.commit()
    conn.close()
    print('Removed expense', expense_id)
    return redirect(url_for('expenses'))
if __name__ == '__main__':
    app.run()
