# Customer Complaint Analyzer

print("======================================")
print("     CUSTOMER COMPLAINT ANALYZER")
print("======================================")

complaint = input("Enter customer complaint: ").lower()

# Sentiment words
positive_words = ["good", "happy", "satisfied", "excellent", "thank"]
negative_words = [
    "bad", "worst", "poor", "angry", "problem", "issue",
    "late", "delay", "failed", "broken", "terrible",
    "disappointed", "refund", "complaint"
]

# Count sentiment words
positive_count = sum(word in complaint for word in positive_words)
negative_count = sum(word in complaint for word in negative_words)

# Sentiment
if negative_count > positive_count:
    sentiment = "Negative"
elif positive_count > negative_count:
    sentiment = "Positive"
else:
    sentiment = "Neutral"

# Complaint category
if any(word in complaint for word in ["payment", "money", "refund", "transaction", "billing"]):
    category = "Payment/Billing"

elif any(word in complaint for word in ["delivery", "order", "late", "shipping"]):
    category = "Delivery"

elif any(word in complaint for word in ["login", "password", "account", "website", "app"]):
    category = "Account/Technical"

elif any(word in complaint for word in ["product", "damaged", "broken", "quality"]):
    category = "Product"

else:
    category = "General Complaint"

# Priority
if any(word in complaint for word in ["urgent", "immediately", "fraud", "scam", "security"]):
    priority = "High"

elif negative_count >= 2:
    priority = "Medium"

else:
    priority = "Low"

# Display result
print("\n========== ANALYSIS RESULT ==========")
print("Complaint :", complaint)
print("Sentiment  :", sentiment)
print("Category   :", category)
print("Priority   :", priority)

print("\nKeywords detected:")

keywords = []

for word in negative_words + ["payment", "refund", "delivery",
                               "product", "login", "account"]:
    if word in complaint:
        keywords.append(word)

if keywords:
    print(", ".join(keywords))
else:
    print("No important keywords found")

print("=====================================")