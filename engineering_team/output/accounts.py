
# accounts.py

def get_share_price(symbol):
    """
    Test implementation of share price lookup.
    
    :param symbol: The stock symbol
    :return: The current price of the share
    """
    prices = {
        'AAPL': 150.0,
        'TSLA': 700.0,
        'GOOGL': 2500.0
    }
    return prices.get(symbol.upper(), 0.0)

class Account:
    def __init__(self, user_id: str):
        """
        Initializes a new account for a user.
        
        :param user_id: Unique identifier for the user
        """
        self.user_id = user_id
        self.balance = 0.0
        self.portfolio = {}  # Dictionary to hold the number of shares of each symbol
        self.transactions = []  # List to hold history of transactions
        self.initial_deposit = 0.0

    def deposit(self, amount: float) -> bool:
        """
        Deposit funds into the user's account.
        
        :param amount: The amount to deposit
        :return: True if deposit is successful, False otherwise
        """
        if amount > 0:
            self.balance += amount
            self.initial_deposit += amount
            self.transactions.append(('DEPOSIT', amount))
            return True
        return False

    def withdraw(self, amount: float) -> bool:
        """
        Withdraw funds from the user's account.
        
        :param amount: The amount to withdraw
        :return: True if withdrawal is successful, False otherwise
        """
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transactions.append(('WITHDRAW', amount))
            return True
        return False

    def buy_shares(self, symbol: str, quantity: int, get_share_price_func = get_share_price) -> bool:
        """
        Record the purchase of shares.
        
        :param symbol: The stock symbol
        :param quantity: The number of shares to buy
        :param get_share_price_func: Function to get current share price
        :return: True if purchase is successful, False otherwise
        """
        if quantity <= 0:
            return False
        share_price = get_share_price_func(symbol)
        total_price = share_price * quantity
        if self.balance >= total_price:
            self.balance -= total_price
            self.portfolio[symbol] = self.portfolio.get(symbol, 0) + quantity
            self.transactions.append(('BUY', symbol, quantity, share_price))
            return True
        return False

    def sell_shares(self, symbol: str, quantity: int, get_share_price_func = get_share_price) -> bool:
        """
        Record the sale of shares.
        
        :param symbol: The stock symbol
        :param quantity: The number of shares to sell
        :param get_share_price_func: Function to get current share price
        :return: True if sale is successful, False otherwise
        """
        if quantity <= 0:
            return False
        current_quantity = self.portfolio.get(symbol, 0)
        if current_quantity >= quantity:
            share_price = get_share_price_func(symbol)
            total_price = share_price * quantity
            self.balance += total_price
            self.portfolio[symbol] = current_quantity - quantity
            if self.portfolio[symbol] == 0:
                del self.portfolio[symbol]  # Remove symbol from portfolio if quantity is zero
            self.transactions.append(('SELL', symbol, quantity, share_price))
            return True
        return False

    def calculate_portfolio_value(self, get_share_price_func = get_share_price) -> float:
        """
        Calculate the total value of a user's portfolio.
        
        :param get_share_price_func: Function to get current share price
        :return: The total value of the portfolio
        """
        total_value = self.balance
        for symbol, quantity in self.portfolio.items():
            total_value += get_share_price_func(symbol) * quantity
        return total_value

    def calculate_profit_loss(self, get_share_price_func = get_share_price) -> float:
        """
        Calculate the profit or loss from the initial deposit.
        
        :param get_share_price_func: Function to get current share price
        :return: The profit or loss amount
        """
        current_value = self.calculate_portfolio_value(get_share_price_func)
        return current_value - self.initial_deposit

    def get_holdings(self) -> dict:
        """
        Get the current holdings of shares.
        
        :return: A dictionary of the share holdings
        """
        return self.portfolio.copy()

    def get_transactions(self) -> list:
        """
        List all the transactions made by the user.
        
        :return: A list of transactions
        """
        return self.transactions.copy()
