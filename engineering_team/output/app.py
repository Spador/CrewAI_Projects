
import gradio as gr
from accounts import Account

# Create a single demo account
account = Account("demo_user")

def deposit(amount):
    if amount is None or amount <= 0:
        return "Invalid deposit amount."
    success = account.deposit(amount)
    if success:
        return f"Deposited ${amount:.2f}. New cash balance: ${account.balance:.2f}"
    else:
        return "Deposit failed."

def withdraw(amount):
    if amount is None or amount <= 0:
        return "Invalid withdrawal amount."
    success = account.withdraw(amount)
    if success:
        return f"Withdrew ${amount:.2f}. New cash balance: ${account.balance:.2f}"
    else:
        return "Withdrawal failed. Insufficient funds."

def buy(symbol, quantity):
    if symbol is None or quantity is None or quantity <= 0:
        return "Invalid buy parameters."
    success = account.buy_shares(symbol, int(quantity))
    if success:
        return f"Successfully bought {quantity} shares of {symbol}."
    else:
        return "Buy failed. Insufficient funds or invalid quantity."

def sell(symbol, quantity):
    if symbol is None or quantity is None or quantity <= 0:
        return "Invalid sell parameters."
    success = account.sell_shares(symbol, int(quantity))
    if success:
        return f"Successfully sold {quantity} shares of {symbol}."
    else:
        return "Sell failed. Insufficient shares or invalid quantity."

def get_holdings():
    holdings = account.get_holdings()
    if not holdings:
        return "No holdings."
    return str(holdings)

def get_transactions():
    transactions = account.get_transactions()
    if not transactions:
        return "No transactions."
    trans_str = "\n".join([str(t) for t in transactions])
    return trans_str

def get_portfolio_value():
    return account.calculate_portfolio_value()

def get_profit_loss():
    return account.calculate_profit_loss()

def get_cash_balance():
    return account.balance

with gr.Blocks(title="Trading Account Demo") as demo:
    gr.Markdown("# Simple Trading Account Demo")
    gr.Markdown("This demo allows you to manage a single trading account. Supported symbols: AAPL ($150), TSLA ($700), GOOGL ($2500).")

    with gr.Row():
        deposit_amt = gr.Number(label="Deposit Amount ($)", value=100.0, step=10.0)
        deposit_btn = gr.Button("Deposit")
        deposit_out = gr.Textbox(label="Deposit Result", interactive=False)

    with gr.Row():
        withdraw_amt = gr.Number(label="Withdraw Amount ($)", value=50.0, step=10.0)
        withdraw_btn = gr.Button("Withdraw")
        withdraw_out = gr.Textbox(label="Withdraw Result", interactive=False)

    with gr.Row():
        buy_symbol = gr.Dropdown(choices=["AAPL", "TSLA", "GOOGL"], label="Buy Symbol")
        buy_qty = gr.Number(label="Buy Quantity", value=1, step=1, precision=0)
        buy_btn = gr.Button("Buy Shares")
        buy_out = gr.Textbox(label="Buy Result", interactive=False)

    with gr.Row():
        sell_symbol = gr.Dropdown(choices=["AAPL", "TSLA", "GOOGL"], label="Sell Symbol")
        sell_qty = gr.Number(label="Sell Quantity", value=1, step=1, precision=0)
        sell_btn = gr.Button("Sell Shares")
        sell_out = gr.Textbox(label="Sell Result", interactive=False)

    with gr.Row():
        balance_btn = gr.Button("Get Cash Balance")
        balance_out = gr.Number(label="Cash Balance ($)", interactive=False)

    with gr.Row():
        holdings_btn = gr.Button("Get Holdings")
        holdings_out = gr.Textbox(label="Holdings", interactive=False)

    with gr.Row():
        trans_btn = gr.Button("Get Transactions")
        trans_out = gr.Textbox(label="Transaction History", lines=10, interactive=False)

    with gr.Row():
        value_btn = gr.Button("Get Portfolio Value")
        value_out = gr.Number(label="Total Portfolio Value ($)", interactive=False)

    with gr.Row():
        pnl_btn = gr.Button("Get Profit/Loss")
        pnl_out = gr.Number(label="Profit/Loss ($)", interactive=False)

    # Event handlers
    deposit_btn.click(
        fn=deposit,
        inputs=[deposit_amt],
        outputs=[deposit_out]
    )

    withdraw_btn.click(
        fn=withdraw,
        inputs=[withdraw_amt],
        outputs=[withdraw_out]
    )

    buy_btn.click(
        fn=buy,
        inputs=[buy_symbol, buy_qty],
        outputs=[buy_out]
    )

    sell_btn.click(
        fn=sell,
        inputs=[sell_symbol, sell_qty],
        outputs=[sell_out]
    )

    balance_btn.click(
        fn=get_cash_balance,
        outputs=[balance_out]
    )

    holdings_btn.click(
        fn=get_holdings,
        outputs=[holdings_out]
    )

    trans_btn.click(
        fn=get_transactions,
        outputs=[trans_out]
    )

    value_btn.click(
        fn=get_portfolio_value,
        outputs=[value_out]
    )

    pnl_btn.click(
        fn=get_profit_loss,
        outputs=[pnl_out]
    )

if __name__ == "__main__":
    demo.launch()
