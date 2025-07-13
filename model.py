import numpy as np

def predict_days_to_zero(stock_list):
    if len(stock_list) < 2:
        return 999  # Not enough data

    daily_usage = []
    for i in range(1, len(stock_list)):
        diff = stock_list[i - 1] - stock_list[i]
        if diff >= 0:
            daily_usage.append(diff)

    if not daily_usage:
        return 999  # No consumption

    avg_daily_use = np.mean(daily_usage)
    if avg_daily_use <= 0:
        return 999

    current_stock = stock_list[-1]
    days_left = current_stock / avg_daily_use
    return round(days_left, 1)
