# AI Autonomous Agent Prototype
import random

def analyze_market():
    return {
        "product": "Lipstick AZTK",
        "sentiment": random.randint(70, 90)
    }

def generate_content(product):
    return f"{product} đang là xu hướng, giá tốt, màu đẹp!"

def simulate_customer_response():
    responses = [
        "Còn hàng không?",
        "Có freeship không?",
        "Màu này hợp da ngăm không?"
    ]
    return random.choice(responses)

def evaluate():
    return round(random.uniform(7.0, 9.5), 1)

def optimize():
    return "Adjust tone to emotional + urgency"

def run_agent():
    data = analyze_market()
    content = generate_content(data["product"])
    response = simulate_customer_response()
    score = evaluate()
    action = optimize()

    print("=== AI AGENT CYCLE ===")
    print("Product:", data["product"])
    print("Sentiment:", data["sentiment"], "%")
    print("Content:", content)
    print("Customer:", response)
    print("Score:", score)
    print("Optimization:", action)

if __name__ == "__main__":
    run_agent()
