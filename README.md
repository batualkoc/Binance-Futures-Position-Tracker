# CCXT Binance Futures Position Tracker

This repository contains a Python script that connects to the Binance Futures API using the CCXT library. The script retrieves your account's open positions for a specified trading pair (e.g., `BTC/USDT`, `ETH/USDT`, `SOL/USDT`), calculates important metrics such as the ROI (Return on Investment), and displays leverage information.

## Features

- **Fetch Balance:** Retrieves your Binance Futures account balance.
- **Position Details:** Shows details about your open positions, including the amount, unrealized profit, and isolated/cross wallet balance.
- **ROI Calculation:** Computes the ROI based on your current position and initial margin.
- **Leverage Information:** Displays the leverage used in the position.

## How to Use

1. Clone this repository:
    ```bash
    git clone https://github.com/batualkoc/Binance-Futures-Position-Tracker.git
    ```
2. Navigate to the project directory:
    ```bash
    cd Binance-Futures-Position-Tracker
    ```
3. Install the required dependencies:
    ```bash
    pip install ccxt
    ```
4. Update the `apiKey` and `secret` in the script with your Binance API credentials.
5. Run the script:
    ```bash
    python script_name.py
    ```

## Requirements

- Python 3.x
- CCXT Library

## License

This project is licensed under the MIT License.

## Disclaimer

This script is provided for educational purposes only. Use at your own risk. Trading cryptocurrency involves substantial risk and may result in the loss of all invested capital.
