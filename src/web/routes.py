from flask import Blueprint, render_template, request, redirect, url_for

# Blueprint Web_routen definieren
main_bp = Blueprint('main', __name__)

@main_bp.route('/', methods=['GET'])
def index():
    # Dummy Dev A (Models) Bev B (DB)
    dummy_transactions = [
        {'id': 1, 'title': 'Gehalt', 'amount': 2500.0, 'type': 'income', 'category': 'Job'},
        {'id': 2, 'title': 'Miete', 'amount': 800.0, 'type': 'expense', 'category': 'Wohnen'}
    ]
    
    total_income = 2500.0
    total_expense = 800.0
    balance = total_income - total_expense
    
    return render_template(
        'index.html',
        transactions=dummy_transactions,
        total_income=total_income,
        total_expense=total_expense,
        balance=balance
    )
    
@main_bp.route('/add', methods=['POST'])
def add_transaction():
    # entgegennehmen Formulardaten (später ans Repo übergeben)
    title = request.form.get('title')
    amount = request.form.get('amount')
    trans_type = request.form.get('type')
    category = request.form.get('category')
    
    print(f"[DEBUG POST /add] Neue Buchung: {title}, {amount}€, {trans_type}, {category}")
    
    # zurück zur Startseite
    return redirect(url_for('main.index'))
