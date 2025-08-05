def calculate_hello_score(metrics):
    base = (metrics['criteria_passed'] / 7) * 10
    modifier = 0

    # PEG Ratio bonus/penalty
    if metrics['PEG'] < 0.5:
        modifier += 1
    elif metrics['PEG'] > 2:
        modifier -= 1

    # ROE bonus
    if metrics['ROE'] > 50:
        modifier += 1
    elif metrics['ROE'] < 20:
        modifier -= 0.5

    # Free Cash Flow bonus
    if metrics['FCF'] > 10_000_000_000:
        modifier += 1
    elif metrics['FCF'] < 500_000_000:
        modifier -= 0.5

    # Debt to Equity penalty
    if metrics['D/E'] > 0.9:
        modifier -= 0.5

    # Growth bonus
    if metrics['1Y_Earnings'] > 30:
        modifier += 1
    if metrics['5Y_Sales'] > 200:
        modifier += 1

    # Clamp the final score between 1 and 10
    final_score = min(10, max(1, round(base + modifier)))
    return final_score
