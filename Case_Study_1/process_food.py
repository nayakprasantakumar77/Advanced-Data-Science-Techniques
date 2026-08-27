
print("Enter Order Details")

order_amount = float(input("Enter Order Amount (e.g., 650.0): "))
delivery_distance = float(input("Enter Delivery Distance in km (e.g., 5.2): "))
customer_type = input("Enter Customer Type (VIP / Gold / Regular): ").strip()
customer_rating = float(input("Enter Customer Rating (1.0 - 5.0): "))
restaurant_rating = float(input("Enter Restaurant Rating (1.0 - 5.0): "))
prep_time = int(input("Enter Preparation Time in minutes: "))
payment_method = input("Enter Payment Method (Online / COD): ").strip()
weather = input("Enter Weather Condition (Clear / Rainy / Stormy): ").strip()
demand_level = input("Enter Demand Level (Low / Medium / High): ").strip()

peak_input = input("Is it Peak Hour? (yes / no): ").strip().lower()
if peak_input == "yes":
    is_peak_hour = True
else:
    is_peak_hour = False

previous_cancellations = int(input("Enter Previous Cancellations Count: "))



if restaurant_rating >= 4.0:
    restaurant_status = "Top Rated"
elif restaurant_rating >= 3.0:
    restaurant_status = "Standard"
else:
    restaurant_status = "Low Rating Warning"



if previous_cancellations >= 3:
    cancellation_risk = "High Risk"
elif previous_cancellations >= 1 and payment_method == "COD":
    cancellation_risk = "High Risk"
elif previous_cancellations > 0:
    cancellation_risk = "Medium Risk"
else:
    cancellation_risk = "Low Risk"



manual_review_status = "Not Required"

if restaurant_rating < 2.5 or delivery_distance > 20 or weather == "Stormy":
    order_status = "Rejected"
elif (
    cancellation_risk == "High Risk"
    or prep_time > 45
    or (order_amount > 3000 and payment_method == "COD")
):
    order_status = "Manual Review"
    manual_review_status = "Flagged for Verification"
else:
    order_status = "Accepted"



if delivery_distance <= 3:
    delivery_charge = 25.0
elif delivery_distance <= 8:
    delivery_charge = 50.0
else:
    delivery_charge = 80.0


if weather == "Rainy":
    delivery_charge = delivery_charge + 20.0


if is_peak_hour and demand_level == "High":
    delivery_charge = delivery_charge + 25.0


if customer_type == "VIP" or (
    customer_type == "Gold" and delivery_distance <= 5
):
    delivery_charge = 0.0



if customer_type == "VIP":
    discount = order_amount * 0.15
elif customer_type == "Gold":
    discount = order_amount * 0.10
elif order_amount >= 500:
    discount = order_amount * 0.05
else:
    discount = 0.0



if customer_type == "VIP" or customer_type == "Gold":
    if prep_time <= 30:
        priority_status = "High Priority"
    else:
        priority_status = "Standard Priority"
else:
    priority_status = "Standard Priority"



if order_amount >= 1500:
    final_order_category = "Bulk / Large Order"
elif customer_type == "VIP" or customer_type == "Gold":
    final_order_category = "Loyalty Member Order"
else:
    final_order_category = "Standard Order"



final_payable_amount = order_amount - discount + delivery_charge



print(" ORDER AUTOMATION REPORT ")
print("Order Status           :", order_status)
print("Manual Review Status   :", manual_review_status)
print("Restaurant Status      :", restaurant_status)
print("Cancellation Risk      :", cancellation_risk)
print("Final Order Category   :", final_order_category)
print("Priority Status        :", priority_status)
print("Order Amount           :", order_amount)
print("Discount Applied       :", discount)
print("Delivery Charge        :", delivery_charge)
print("Final Payable Amount   :", final_payable_amount)
