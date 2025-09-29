chai_prices_inr = {
    "Masala Chai": 40,
    "Green Tea": 50,
    "Herbal Tea": 80
}
chai_prices_usd= {tea:price / 80 for tea,price in chai_prices_inr.items()}
print("Chai ke prices in INR: ",chai_prices_inr)
print("Chai ke prices in USD: ",chai_prices_usd)