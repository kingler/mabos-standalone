# Dynamic Business Model Examples

Based on the information provided, here are some examples of how to implement dynamic and executable business models using Python code structures:

1. Retail Store Business Model

```python
import random

class RetailStore:
    def __init__(self, name, initial_capital):
        self.name = name
        self.capital = initial_capital
        self.inventory = {}
        self.revenue = 0
        self.expenses = 0
        
    def purchase_inventory(self, item, quantity, cost_per_unit):
        total_cost = quantity * cost_per_unit
        if self.capital >= total_cost:
            self.capital -= total_cost
            self.expenses += total_cost
            self.inventory[item] = self.inventory.get(item, 0) + quantity
            print(f"Purchased {quantity} units of {item}")
        else:
            print(f"Not enough capital to purchase {item}")
    
    def set_price(self, item, price):
        if item in self.inventory:
            self.inventory[item] = {"quantity": self.inventory[item], "price": price}
            print(f"Set price of {item} to ${price}")
        else:
            print(f"No inventory for {item}")
    
    def simulate_sales(self):
        for item, details in self.inventory.items():
            quantity = details["quantity"]
            price = details["price"]
            sales = min(quantity, random.randint(0, 10))
            self.inventory[item]["quantity"] -= sales
            self.revenue += sales * price
            print(f"Sold {sales} units of {item}")
    
    def calculate_profit(self):
        profit = self.revenue - self.expenses
        print(f"Revenue: ${self.revenue}")
        print(f"Expenses: ${self.expenses}")
        print(f"Profit: ${profit}")
        self.capital += profit
        self.revenue = 0
        self.expenses = 0
    
    def run_month(self):
        self.simulate_sales()
        self.calculate_profit()
        print(f"Capital at end of month: ${self.capital}")
        print("---")

# Usage
store = RetailStore("MyStore", 10000)
store.purchase_inventory("Shirts", 100, 10)
store.purchase_inventory("Pants", 50, 20)
store.set_price("Shirts", 20)
store.set_price("Pants", 40)

for month in range(1, 4):
    print(f"Month {month}")
    store.run_month()

print(f"Final capital: ${store.capital}")
print(f"Remaining inventory: {store.inventory}")
```

2. SaaS Business Model

```python
import random

class SaaSBusiness:
    def __init__(self, name, initial_capital):
        self.name = name
        self.capital = initial_capital
        self.customers = 0
        self.churn_rate = 0.05
        self.subscription_price = 50
        self.customer_acquisition_cost = 100
        self.monthly_operating_cost = 5000
        
    def acquire_customers(self):
        new_customers = random.randint(5, 20)
        acquisition_cost = new_customers * self.customer_acquisition_cost
        if self.capital >= acquisition_cost:
            self.capital -= acquisition_cost
            self.customers += new_customers
            print(f"Acquired {new_customers} new customers")
        else:
            print("Not enough capital for customer acquisition")
    
    def calculate_churn(self):
        churned_customers = int(self.customers * self.churn_rate)
        self.customers -= churned_customers
        print(f"Lost {churned_customers} customers to churn")
    
    def collect_revenue(self):
        revenue = self.customers * self.subscription_price
        self.capital += revenue
        print(f"Collected ${revenue} in subscription revenue")
    
    def pay_operating_costs(self):
        self.capital -= self.monthly_operating_cost
        print(f"Paid ${self.monthly_operating_cost} in operating costs")
    
    def calculate_profit(self):
        revenue = self.customers * self.subscription_price
        expenses = self.monthly_operating_cost
        profit = revenue - expenses
        print(f"Revenue: ${revenue}")
        print(f"Expenses: ${expenses}")
        print(f"Profit: ${profit}")
    
    def run_month(self):
        self.acquire_customers()
        self.calculate_churn()
        self.collect_revenue()
        self.pay_operating_costs()
        self.calculate_profit()
        print(f"Capital at end of month: ${self.capital}")
        print(f"Total customers: {self.customers}")
        print("---")

# Usage
saas = SaaSBusiness("MySaaS", 50000)

for month in range(1, 13):
    print(f"Month {month}")
    saas.run_month()

print(f"Final capital: ${saas.capital}")
print(f"Final customer count: {saas.customers}")
```

3. Freelance Consulting Business Model

```python
import random

class FreelanceConsulting:
    def __init__(self, name, initial_capital):
        self.name = name
        self.capital = initial_capital
        self.clients = []
        self.hourly_rate = 100
        self.monthly_expenses = 2000
        
    def acquire_client(self):
        if random.random() < 0.3:  # 30% chance of getting a new client
            project_size = random.randint(10, 100)  # hours
            self.clients.append(project_size)
            print(f"Acquired new client with {project_size} hour project")
    
    def do_client_work(self):
        revenue = 0
        for i, hours_left in enumerate(self.clients):
            hours_worked = min(hours_left, random.randint(10, 40))
            self.clients[i] -= hours_worked
            revenue += hours_worked * self.hourly_rate
        
        self.capital += revenue
        print(f"Earned ${revenue} from client work")
        
        # Remove completed projects
        self.clients = [hours for hours in self.clients if hours > 0]
    
    def pay_expenses(self):
        self.capital -= self.monthly_expenses
        print(f"Paid ${self.monthly_expenses} in monthly expenses")
    
    def calculate_profit(self):
        revenue = sum(self.clients) * self.hourly_rate
        profit = revenue - self.monthly_expenses
        print(f"Projected Revenue: ${revenue}")
        print(f"Expenses: ${self.monthly_expenses}")
        print(f"Projected Profit: ${profit}")
    
    def run_month(self):
        self.acquire_client()
        self.do_client_work()
        self.pay_expenses()
        self.calculate_profit()
        print(f"Capital at end of month: ${self.capital}")
        print(f"Active clients: {len(self.clients)}")
        print("---")

# Usage
consulting = FreelanceConsulting("MyConsulting", 10000)

for month in range(1, 13):
    print(f"Month {month}")
    consulting.run_month()

print(f"Final capital: ${consulting.capital}")
print(f"Final client count: {len(consulting.clients)}")
```

These examples demonstrate how to create dynamic and executable business models using Python classes. Each model encapsulates the core logic of a specific business type, allowing for easy simulation and analysis of different scenarios. The models can be further extended with additional methods and attributes to capture more complex business dynamics.
