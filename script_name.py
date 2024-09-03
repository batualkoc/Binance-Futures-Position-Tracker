import ccxt

symbol = 'BTC/USDT' #BTC/USDT, ETH/USDT, SOL/USDT etc.

exchange = ccxt.binance({
    'apiKey': 'API_KEY',
    'secret': 'SECRET_KEY',
    'enableRateLimit': True,
    'options': {
        'defaultType': 'future'
    }
})

balance = exchange.fetchBalance()
positions = balance["info"]["positions"]
startingMoney = float(balance["total"]["USDT"])

output_lines = []

for position in positions:
    if position["symbol"] == symbol:
        amount = float(position["positionAmt"])
        pnl = float(position["unrealizedProfit"])
        isolated_wallet = float(position["isolatedWallet"])
        leverage = int(position["leverage"])
        cross_wallet = float(position['positionInitialMargin'])
        
        # Position
        output_lines.append(f"{position}")
        
        # ROI 
        if cross_wallet != 0:
            roi = (pnl / cross_wallet) * 100
            output_lines.append(f"Avarage ROI: {roi:.2f}%")
        
        # Leverage
        output_lines.append(f"Leverage: {leverage}x")
        
        break
else:
    output_lines.append(f"{symbol} do not have an open position")

# Write output
with open("output.txt", "w") as file:
    for line in output_lines:
        file.write(line + "\n")
