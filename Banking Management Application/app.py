from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

class BankAccount:
    def __init__(self, account_number, account_holder_name, password):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.balance = 0.0
        self.password = password

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount} into {self.account_holder_name}'s account successfully.\nNew balance: ${self.balance}"
        else:
            return "Invalid deposit amount."

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Withdrawn ${amount} from {self.account_holder_name}'s account successfully.\nNew balance: ${self.balance}"
        else:
            return "Invalid withdrawal amount or insufficient balance."

    def get_balance(self):
        return self.balance

accounts = {}

def validate_account_exists(account_number):
    return account_number in accounts

def validate_password(account_number, password):
    return accounts[account_number].password == password

def validate_positive_amount(amount):
    return amount > 0

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create_account', methods=['POST'])
def create_account():
    data = request.get_json()
    account_number = data.get('accountNumber')
    account_holder_name = data.get('accountHolderName')
    password = data.get('password')

    if not account_number or not account_holder_name or not password:
        return jsonify({'error': 'All fields are required'}), 400

    if account_number in accounts:
        return jsonify({'error': 'Account number already exists'}), 400

    accounts[account_number] = BankAccount(account_number, account_holder_name, password)
    return jsonify({'message': 'Account created successfully'})

@app.route('/deposit', methods=['POST'])
def deposit():
    data = request.get_json()
    account_number = data.get('accountNumber')
    password = data.get('password')
    deposit_amount = data.get('depositAmount')

    if not account_number or not password or not deposit_amount:
        return jsonify({'error': 'All fields are required'}), 400

    if not validate_account_exists(account_number) or not validate_password(account_number, password):
        return jsonify({'error': 'Authentication failed or account not found'}), 401

    if not validate_positive_amount(deposit_amount):
        return jsonify({'error': 'Deposit amount must be positive'}), 400

    result = accounts[account_number].deposit(deposit_amount)
    return jsonify({'message': result})

@app.route('/withdraw', methods=['POST'])
def withdraw():
    data = request.get_json()
    account_number = data.get('accountNumber')
    password = data.get('password')
    withdrawal_amount = data.get('withdrawalAmount')

    if not account_number or not password or not withdrawal_amount:
        return jsonify({'error': 'All fields are required'}), 400

    if not validate_account_exists(account_number) or not validate_password(account_number, password):
        return jsonify({'error': 'Authentication failed or account not found'}), 401

    if not validate_positive_amount(withdrawal_amount):
        return jsonify({'error': 'Withdrawal amount must be positive'}), 400

    result = accounts[account_number].withdraw(withdrawal_amount)
    return jsonify({'message': result})

@app.route('/view_balance', methods=['POST'])
def view_balance():
    data = request.get_json()
    account_number = data.get('accountNumber')
    password = data.get('password')

    if not account_number or not password:
        return jsonify({'error': 'All fields are required'}), 400

    if not validate_account_exists(account_number) or not validate_password(account_number, password):
        return jsonify({'error': 'Authentication failed or account not found'}), 401

    balance = accounts[account_number].get_balance()
    return jsonify({'balance': balance})

@app.route('/view_all_accounts', methods=['GET'])
def view_all_accounts():
    account_details = []
    for account_number, account in accounts.items():
        account_details.append({
            'accountNumber': account_number,
            'accountHolderName': account.account_holder_name,
            'balance': account.balance
        })
    return jsonify({'accounts': account_details})

if __name__ == '__main__':
    app.run(debug=True)
