# Banking Management Application

This is a simple web application for banking management. Users can create accounts, deposit and withdraw money, view balances, and see all accounts.

## Project Structure

- **app.py:** Flask application containing server-side logic.
- **static/:** Folder for static assets like JavaScript and CSS files.
  - **app.js:** Frontend logic for interacting with the backend.
  - **styles.css:** CSS file for styling the application.
- **templates/:** HTML templates for different pages/views.
  - **index.html:** Main page with forms for creating accounts, depositing, withdrawing, and viewing balances.

## Dependencies

- Flask: Web framework for the backend.
- Bootstrap: Frontend framework for styling.

## Setup

1. Install dependencies: `pip install Flask`
2. Run the application: `python app.py`
3. Access the application at `http://127.0.0.1:5000` in your browser.

## Usage

- **Create New Account:** Enter account details and click "Create Account."
- **Deposit:** Enter account details and deposit amount, then click "Deposit."
- **Withdraw:** Enter account details and withdrawal amount, then click "Withdraw."
- **View Balance:** Enter account details and click "View Balance."
- **View All Accounts:** Click "View All Accounts" to see a list of all accounts.

## Additional Notes

- The project uses Bootstrap for a simple and responsive design.
- Ensure that the background image is placed in the `assets/` folder.

## License

This project is licensed under the [MIT License](LICENSE).
