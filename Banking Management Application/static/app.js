
async function createAccount() {
    const accountNumber = document.getElementById('accountNumber').value;
    const accountHolderName = document.getElementById('accountHolderName').value;
    const password = document.getElementById('password').value;

    const response = await fetch('/create_account', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            accountNumber: accountNumber,
            accountHolderName: accountHolderName,
            password: password,
        }),
    });

    const data = await response.json();
    alert(data.message || data.error);
}

async function deposit() {
    const accountNumber = document.getElementById('depositAccountNumber').value;
    const password = document.getElementById('depositPassword').value;
    const depositAmount = document.getElementById('depositAmount').value;

    const response = await fetch('/deposit', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            accountNumber: accountNumber,
            password: password,
            depositAmount: depositAmount,
        }),
    });

    const data = await response.json();
    alert(data.message || data.error);
}


async function deposit() {
    const accountNumber = document.getElementById('depositAccountNumber').value;
    const password = document.getElementById('depositPassword').value;
    const depositAmount = document.getElementById('depositAmount').value;

    const response = await fetch('/deposit', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            accountNumber: accountNumber,
            password: password,
            depositAmount: depositAmount,
        }),
    });

    const data = await response.json();
    alert(data.message || data.error);
}

async function withdraw() {
    const accountNumber = document.getElementById('withdrawAccountNumber').value;
    const password = document.getElementById('withdrawPassword').value;
    const withdrawalAmount = document.getElementById('withdrawalAmount').value;

    const response = await fetch('/withdraw', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            accountNumber: accountNumber,
            password: password,
            withdrawalAmount: withdrawalAmount,
        }),
    });

    const data = await response.json();
    alert(data.message || data.error);
}

async function viewBalance() {
    const accountNumber = document.getElementById('balanceAccountNumber').value;
    const password = document.getElementById('balancePassword').value;

    const response = await fetch('/view_balance', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            accountNumber: accountNumber,
            password: password,
        }),
    });

    const data = await response.json();
    alert(data.message || data.error);
}

async function viewAllAccounts() {
    const response = await fetch('/view_all_accounts', {
        method: 'GET',
    });

    const data = await response.json();
    alert(JSON.stringify(data, null, 2));
}

