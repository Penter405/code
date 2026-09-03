import random

# 1. The original source data dictionary
indicators_pool = {
    "外銷訂單動向指數": 1,
    "實質貨幣總計數M1B": 1,
    "股價指數": 1,
    "工業及服務業受僱員工淨進入率": 1,
    "建築物開工樓地板面積": 1,
    "實質半導體設備進口值": 1,
    "製造業營業氣候測驗點": 1,
    
    "工業生產指數": 2,
    "電力（企業）總用電量": 2,
    "製造業銷售量指數": 2,
    "批發、零售及餐飲業營業額": 2,
    "非農業部門就業人數": 2,
    "實質海關出口值": 2,
    "實質機械及電機設備進口值": 2,
    
    "失業率": 3,
    "製造業單位產出勞動成本指數": 3,
    "金融業隔夜拆款利率": 3,
    "全體金融機構放款和投資": 3,
    "製造業存貨價值": 3
}

# Mapping for user input verification and display
category_mapping = {
    1: "領先指標 (Leading Indicator)",
    2: "同時指標 (Coincident Indicator)",
    3: "落後指標 (Lagging Indicator)"
}

# 2. Dictionary to track the questions you got wrong
wrong_answers = {}

print("=== Macroeconomic Indicators Quiz ===")
print("Instructions: Type 1, 2, or 3 to guess the category.")
print("1 = 領先指標 | 2 = 同時指標 | 3 = 落後指標\n")

# 3. Main quiz loop (runs until the pool is empty)
while indicators_pool:
    # Get a random item remaining in the pool
    current_item = random.choice(list(indicators_pool.keys()))
    correct_answer = indicators_pool[current_item]
    
    # Prompt the user with instructions repeated every time
    print(f"Question: Which indicator category does '{current_item}' belong to?")
    print("Reminder: [1] = 領先指標 | [2] = 同時指標 | [3] = 落後指標")
    
    user_input = input("Your answer (1/2/3) or 'q' to quit: ").strip()
    
    # Allow user to quit early
    if user_input.lower() == 'q':
        print("\nQuiz ended early.")
        break
        
    # Validate input format
    if user_input not in ['1', '2', '3']:
        print("❌ Invalid input! Please enter only 1, 2, or 3.\n" + "-"*40)
        continue
    
    user_answer = int(user_input)
    
    # Check if the answer is correct
    if user_answer == correct_answer:
        print("✅ Correct!\n")
    else:
        print(f"❌ Wrong! The correct category was: {category_mapping[correct_answer]}\n")
        # Save the mistake to the wrong_answers dictionary
        wrong_answers[current_item] = {
            "your_guess": category_mapping[user_answer],
            "correct_answer": category_mapping[correct_answer]
        }
    
    # CRITICAL: Remove the item from the pool so it isn't asked again
    del indicators_pool[current_item]
    print(f"Remaining questions: {len(indicators_pool)}")
    print("-" * 40)

# 4. Final Review Section
print("\n=== Quiz Finished! ===")
if wrong_answers:
    print("\nHere is your review dictionary of incorrect answers:")
    import pprint
    pprint.pprint(wrong_answers)
else:
    print("🥇 Perfect score! You didn't miss a single one.")