# Business Plan

Create business plans in code that are programmatically dynamic and executable using Python to define classes and methods that represent different aspects of a business plan. These classes can include dynamic elements such as revenue generation, expense management, hiring employees, and customer acquisition. The plans can then be executed to simulate business operations and analyze outcomes.

Here are three examples of business plans implemented in Python:

### **Example 1: Tech Startup Business Plan**

This example simulates a tech startup's business plan, including hiring employees, acquiring customers, generating revenue, and calculating profit.

```python
import random

class TechStartup:
    def __init__(self, name, initial_capital):
        self.name = name
        self.capital = initial_capital
        self.revenue = 0
        self.expenses = 0
        self.profit = 0
        self.customers = 0
        self.employees = 0
        
    def hire_employees(self, num):
        cost_per_employee = 50000
        if self.capital >= num * cost_per_employee:
            self.employees += num
            self.capital -= num * cost_per_employee
            self.expenses += num * cost_per_employee
            print(f"Hired {num} employees. Total employees: {self.employees}")
        else:
            print("Not enough capital to hire employees")
    
    def acquire_customers(self):
        new_customers = random.randint(0, 10) * self.employees
        self.customers += new_customers
        print(f"Acquired {new_customers} new customers. Total customers: {self.customers}")
    
    def generate_revenue(self):
        revenue_per_customer = 1000
        self.revenue = self.customers * revenue_per_customer
        print(f"Generated ${self.revenue} in revenue")
    
    def calculate_profit(self):
        self.profit = self.revenue - self.expenses
        print(f"Profit: ${self.profit}")
        self.capital += self.profit
    
    def run_quarter(self):
        self.acquire_customers()
        self.generate_revenue()
        self.calculate_profit()
        print(f"Capital at end of quarter: ${self.capital}")
        print("---")

# Example usage:
tech_startup = TechStartup("TechCo", 1000000)

for quarter in range(1, 5):
    print(f"Quarter {quarter}")
    if quarter == 1:
        tech_startup.hire_employees(5)
    tech_startup.run_quarter()

print(f"Final capital: ${tech_startup.capital}")
print(f"Total employees: {tech_startup.employees}")
print(f"Total customers: {tech_startup.customers}")
```

### **Example 2: Retail Store Business Plan**

This example simulates a retail store's business plan, including purchasing inventory, setting prices, simulating sales, and calculating profit.

```python
import random

class RetailStore:
    def __init__(self, name, initial_capital):
        self.name = name
        self.capital = initial_capital
        self.revenue = 0
        self.expenses = 0
        self.profit = 0
        self.inventory = {}
        self.sales = {}
    
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
            self.sales[item] = {"price": price, "quantity": 0}
            print(f"Set price of {item} to ${price}")
        else:
            print(f"No inventory for {item}")
    
    def simulate_sales(self):
        for item in self.inventory:
            if item in self.sales:
                max_sales = min(self.inventory[item], random.randint(0, 100))
                self.sales[item]["quantity"] += max_sales
                self.inventory[item] -= max_sales
                self.revenue += max_sales * self.sales[item]["price"]
                print(f"Sold {max_sales} units of {item}")
    
    def calculate_profit(self):
        self.profit = self.revenue - self.expenses
        print(f"Revenue: ${self.revenue}")
        print(f"Expenses: ${self.expenses}")
        print(f"Profit: ${self.profit}")
        self.capital += self.profit
    
    def run_month(self):
        self.simulate_sales()
        self.calculate_profit()
        print(f"Capital at end of month: ${self.capital}")
        print("---")

# Example usage:
retail_store = RetailStore("MyStore", 100000)

retail_store.purchase_inventory("Shirts", 100, 10)
retail_store.purchase_inventory("Pants", 50, 20)

retail_store.set_price("Shirts", 20)
retail_store.set_price("Pants", 40)

for month in range(1, 4):
    print(f"Month {month}")
    retail_store.run_month()

print(f"Final capital: ${retail_store.capital}")
print(f"Remaining inventory: {retail_store.inventory}")
```

### **Example 3: Consulting Firm Business Plan**

This example simulates a consulting firm's business plan, including hiring consultants, acquiring clients, generating revenue, and calculating profit.

```python
import random

class ConsultingFirm:
    def __init__(self, name, initial_capital):
        self.name = name
        self.capital = initial_capital
        self.revenue = 0
        self.expenses = 0
        self.profit = 0
        self.clients = 0
        self.consultants = 0
        
    def hire_consultants(self, num):
        cost_per_consultant = 80000
        if self.capital >= num * cost_per_consultant:
            self.consultants += num
            self.capital -= num * cost_per_consultant
            self.expenses += num * cost_per_consultant
            print(f"Hired {num} consultants. Total consultants: {self.consultants}")
        else:
            print("Not enough capital to hire consultants")
    
    def acquire_clients(self):
        new_clients = random.randint(0, 5) * self.consultants
        self.clients += new_clients
        print(f"Acquired {new_clients} new clients. Total clients: {self.clients}")
    
    def generate_revenue(self):
        revenue_per_client = 15000
        self.revenue = self.clients * revenue_per_client
        print(f"Generated ${self.revenue} in revenue")
    
    def calculate_profit(self):
        self.profit = self.revenue - self.expenses
        print(f"Profit: ${self.profit}")
        self.capital += self.profit
    
    def run_quarter(self):
        self.acquire_clients()
        self.generate_revenue()
        self.calculate_profit()
        print(f"Capital at end of quarter: ${self.capital}")
        print("---")

# Example usage:
consulting_firm = ConsultingFirm("ConsultCo", 500000)

for quarter in range(1, 5):
    print(f"Quarter {quarter}")
    if quarter == 1:
        consulting_firm.hire_consultants(3)
    consulting_firm.run_quarter()

print(f"Final capital: ${consulting_firm.capital}")
print(f"Total consultants: {consulting_firm.consultants}")
print(f"Total clients: {consulting_firm.clients}")
```

### **Conclusion**

These examples demonstrate how to create dynamic and executable business plans in Python. Each example includes methods for hiring employees or consultants, acquiring customers or clients, generating revenue, and calculating profit. The business plans can be run over multiple periods (quarters or months) to simulate business operations and analyze outcomes. This approach allows for easy testing of different scenarios and sensitivity analysis, making it a powerful tool for business planning and decision-making.