crypto_db = {
    "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sourcing_score": 3, # Changed to an integer for easier comparison
        "sustainability_score": 3/10
    },
    "Ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sourcing_score": 6,
        "sustainability_score": 6/10
    },
    "Cardano": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sourcing_score": 8,
        "sustainability_score": 8/10
    },
    "Solana": { # Added another coin for more variety
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "medium",
        "sourcing_score": 7,
        "sustainability_score": 7/10
    },
    "Polygon": { # Another coin
        "price_trend": "stable",
        "market_cap": "medium",
        "energy_use": "low",
        "sourcing_score": 9,
        "sustainability_score": 9/10
    }
}

def eco_coin_buddy():
    """
    The main function for the EcoCoin Buddy chatbot.
    """
    print("EcoCoin Buddy: Hey there! Let's find you a green and growing crypto!")
    print("EcoCoin Buddy: What are you looking for today? (e.g., 'sustainable', 'long-term growth', 'trending up')")

    while True:
        user_query = input("You: ").lower()

        if "exit" in user_query or "quit" in user_query:
            print("EcoCoin Buddy: Happy investing! May your portfolio bloom green! 🌿 Goodbye!")
            break

        found_recommendation = False

        # Rule 1: Sustainability
        if "sustainable" in user_query or "eco-friendly" in user_query or "green" in user_query:
            best_sustainable_coin = None
            max_sustainability_score = -1

            for coin, data in crypto_db.items():
                if data["energy_use"] == "low" and data["sustainability_score"] > 7/10:
                    if data["sustainability_score"] > max_sustainability_score:
                        max_sustainability_score = data["sustainability_score"]
                        best_sustainable_coin = coin
                elif data["sustainability_score"] >= 6/10 and not best_sustainable_coin: # If no perfect match, find a good one
                     if data["sustainability_score"] > max_sustainability_score:
                        max_sustainability_score = data["sustainability_score"]
                        best_sustainable_coin = coin

            if best_sustainable_coin:
                print(f"EcoCoin Buddy: For a truly green investment, consider {best_sustainable_coin}! 🌱 It's super eco-friendly with a fantastic sustainability score.")
                found_recommendation = True
            else:
                print("EcoCoin Buddy: Hmmm, I couldn't find a perfect match for 'super sustainable' right now, but let's explore other options!")
                found_recommendation = True # Mark as found to avoid the generic message

        # Rule 2: Profitability (Long-term growth)
        if "long-term growth" in user_query or "profitable" in user_query or "invest" in user_query:
            best_profit_coin = None
            
            # Prioritize coins with rising trend and high market cap
            for coin, data in crypto_db.items():
                if data["price_trend"] == "rising" and data["market_cap"] == "high":
                    best_profit_coin = coin
                    break # Found a prime candidate, no need to look further
            
            if not best_profit_coin: # If no "rising" and "high market cap" match, look for just "rising"
                for coin, data in crypto_db.items():
                    if data["price_trend"] == "rising":
                        best_profit_coin = coin
                        break

            if best_profit_coin:
                print(f"EcoCoin Buddy: For long-term growth and potential profits, {best_profit_coin} looks promising! 🚀 It's trending up and has a strong market presence.")
                found_recommendation = True
            elif not found_recommendation: # Only print if no other recommendation was made
                print("EcoCoin Buddy: I'm looking for coins with strong growth potential for you! Currently, I don't have a perfect match for 'high profit' based on my current data, but let's keep an eye out!")
                found_recommendation = True

        # General trends
        if "trending up" in user_query:
            trending_coins = [coin for coin, data in crypto_db.items() if data["price_trend"] == "rising"]
            if trending_coins:
                print(f"EcoCoin Buddy: Coins currently trending up include: {', '.join(trending_coins)}. Keep an eye on them! 👀")
                found_recommendation = True
            else:
                print("EcoCoin Buddy: Currently, no coins are showing a strong 'trending up' signal in my data.")
                found_recommendation = True
        
        if "stable" in user_query:
            stable_coins = [coin for coin, data in crypto_db.items() if data["price_trend"] == "stable"]
            if stable_coins:
                print(f"EcoCoin Buddy: If stability is your game, {', '.join(stable_coins)} are looking stable right now. 🛡️")
                found_recommendation = True
            else:
                print("EcoCoin Buddy: All my listed coins are a bit volatile at the moment!")
                found_recommendation = True

        if not found_recommendation:
            print("EcoCoin Buddy: Hmmm, I'm not sure I understand that query. Can you ask me about 'sustainable', 'long-term growth', or 'trending up' cryptos?")

# Run the chatbot
if __name__ == "__main__":
    eco_coin_buddy()