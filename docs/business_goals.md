# Business Goals    

### **Representing Business Goals in TOGAF**

In TOGAF, business goals are often captured in catalogs, matrices, and diagrams. Specifically, the **Driver/Goal/Objective catalog** is used to document the goals, objectives, and drivers of the organization. This catalog helps in aligning business goals with the enterprise architecture.

#### **Driver/Goal/Objective Catalog Example**

**SQL Database Code Example:**

```sql
CREATE TABLE DriverGoalObjective (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    type VARCHAR(50), -- e.g., Driver, Goal, Objective
    description TEXT,
    related_to INT REFERENCES DriverGoalObjective(id), -- Self-referencing for hierarchical relationships
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### **Tropos Goal-Oriented Modeling**

Tropos is a methodology for agent-oriented software development that focuses on the early requirements analysis phase. It models the goals of stakeholders and the dependencies between them. Here, we provide three examples of goal-oriented modeling using Tropos.

### **Example 1: Online Shopping System**

#### **Code Representation**

```python
class Actor:
    def __init__(self, name):
        self.name = name
        self.goals = []
        self.dependencies = []

class Goal:
    def __init__(self, name, type="hardgoal"):
        self.name = name
        self.type = type  # "hardgoal" or "softgoal"
        self.subgoals = []
        self.plans = []

class Dependency:
    def __init__(self, depender, dependee, dependum):
        self.depender = depender
        self.dependee = dependee
        self.dependum = dependum

class Plan:
    def __init__(self, name):
        self.name = name

# Actors
customer = Actor("Customer")
online_store = Actor("Online Store")

# Goals
browse_products = Goal("Browse Products")
make_purchase = Goal("Make Purchase")
process_order = Goal("Process Order")
deliver_product = Goal("Deliver Product")

# Plans
search_catalog = Plan("Search Catalog")
add_to_cart = Plan("Add to Cart")
checkout = Plan("Checkout")

# Goal structure
customer.goals.extend([browse_products, make_purchase])
online_store.goals.extend([process_order, deliver_product])

browse_products.plans.append(search_catalog)
make_purchase.plans.extend([add_to_cart, checkout])

# Dependencies
product_info = Dependency(customer, online_store, browse_products)
order_placement = Dependency(online_store, customer, make_purchase)
order_fulfillment = Dependency(customer, online_store, deliver_product)

customer.dependencies.extend([product_info, order_fulfillment])
online_store.dependencies.append(order_placement)
```

### **Example 2: Meeting Scheduler**

#### **Code Representation**

```python
# Actors
meeting_initiator = Actor("Meeting Initiator")
meeting_participant = Actor("Meeting Participant")
scheduler_system = Actor("Scheduler System")

# Goals
schedule_meeting = Goal("Schedule Meeting")
find_suitable_slot = Goal("Find Suitable Time Slot")
confirm_attendance = Goal("Confirm Attendance")
send_reminders = Goal("Send Reminders")

# Plans
propose_dates = Plan("Propose Dates")
collect_availability = Plan("Collect Availability")
select_date = Plan("Select Date")
notify_participants = Plan("Notify Participants")

# Goal structure
meeting_initiator.goals.append(schedule_meeting)
meeting_participant.goals.append(confirm_attendance)
scheduler_system.goals.extend([find_suitable_slot, send_reminders])

schedule_meeting.subgoals.extend([find_suitable_slot, confirm_attendance])
schedule_meeting.plans.extend([propose_dates, select_date])
find_suitable_slot.plans.append(collect_availability)
send_reminders.plans.append(notify_participants)

# Dependencies
date_proposals = Dependency(meeting_participant, meeting_initiator, propose_dates)
availability_info = Dependency(scheduler_system, meeting_participant, collect_availability)
meeting_confirmation = Dependency(meeting_initiator, meeting_participant, confirm_attendance)

meeting_initiator.dependencies.extend([availability_info, meeting_confirmation])
meeting_participant.dependencies.append(date_proposals)
scheduler_system.dependencies.append(availability_info)
```

### **Example 3: Smart Home System**

#### **Code Representation**

```python
# Actors
home_owner = Actor("Home Owner")
smart_home_system = Actor("Smart Home System")

# Goals
ensure_home_security = Goal("Ensure Home Security")
optimize_energy_usage = Goal("Optimize Energy Usage", type="softgoal")
control_temperature = Goal("Control Temperature")
monitor_activities = Goal("Monitor Activities")

# Plans
lock_doors = Plan("Lock Doors")
arm_alarm = Plan("Arm Alarm")
adjust_thermostat = Plan("Adjust Thermostat")
turn_off_lights = Plan("Turn Off Unused Lights")
detect_motion = Plan("Detect Motion")

# Goal structure
home_owner.goals.extend([ensure_home_security, optimize_energy_usage])
smart_home_system.goals.extend([control_temperature, monitor_activities])

ensure_home_security.plans.extend([lock_doors, arm_alarm])
optimize_energy_usage.plans.extend([adjust_thermostat, turn_off_lights])
control_temperature.plans.append(adjust_thermostat)
monitor_activities.plans.append(detect_motion)

# Dependencies
security_management = Dependency(home_owner, smart_home_system, ensure_home_security)
energy_efficiency = Dependency(home_owner, smart_home_system, optimize_energy_usage)
temperature_control = Dependency(home_owner, smart_home_system, control_temperature)
activity_monitoring = Dependency(smart_home_system, home_owner, monitor_activities)

home_owner.dependencies.extend([security_management, energy_efficiency, temperature_control])
smart_home_system.dependencies.append(activity_monitoring)
```

### **Conclusion**

These examples demonstrate how to represent business goals and dependencies using the Tropos methodology in Python. The code structures actors, goals, dependencies, and plans, capturing the goal-oriented and agent-oriented aspects of the system. This approach aligns well with TOGAF's Driver/Goal/Objective catalog, providing a comprehensive framework for modeling business goals in enterprise architecture.