
## TOGAF Catalog | Matrix | Diagram

### Diagrams
1. Value Chain diagram
2. Solution Concept diagram
3. Business Footprint diagram
4. Business Service/Information diagram
5. Functional Decomposition diagram
6. Product Lifecycle diagram
7. Goal/Objective/Service diagram
8. Business Use-Case diagram
9. Organization Decomposition diagram
10. Process Flow diagram
11. Event diagram
12. Class diagram
13. Data Dissemination diagram
14. Data Security diagram
15. Class Hierarchy diagram
16. Data Migration diagram
17. Data Lifecycle diagram
18. Application Communication diagram
19. Application and User Location diagram
20. System Use-Case diagram
21. Enterprise Manageability diagram
22. Process/System Realization diagram
23. Software Engineering diagram
24. Application Migration diagram
25. Software Distribution diagram
26. Environments and Locations diagram
27. Platform Decomposition diagram
28. Processing diagram
29. Networked Computing/Hardware diagram
30. Communications Engineering diagram
31. Project Context diagram
32. Benefits diagram

___

### Catalogs
1. Organization/Actor catalog
2. Driver/Goal/Objective catalog
3. Role catalog
4. Business Service/Function catalog
5. Location catalog
6. Process/Event/Control/Product catalog
7. Contract/Measure catalog
8. Data Entity/Data Component catalog
9. Application Portfolio catalog
10. Interface catalog
11. Technology Standards catalog
12. Technology Portfolio catalog
13. Requirements catalog

**SQL Database Code Examples for Each Catalog**

**1. Organization/Actor Catalog**
```sql
CREATE TABLE OrganizationActor (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    type VARCHAR(50), -- e.g., Organization, Actor
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

**2. Driver/Goal/Objective Catalog**
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

**3. Role Catalog**
```sql
CREATE TABLE Role (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

**4. Business Service/Function Catalog**
```sql
CREATE TABLE BusinessServiceFunction (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    type VARCHAR(50), -- e.g., Service, Function
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

**5. Location Catalog**
```sql
CREATE TABLE Location (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    address TEXT,
    city VARCHAR(100),
    state VARCHAR(100),
    country VARCHAR(100),
    postal_code VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

**6. Process/Event/Control/Product Catalog**
```sql
CREATE TABLE ProcessEventControlProduct (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    type VARCHAR(50), -- e.g., Process, Event, Control, Product
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

**7. Contract/Measure Catalog**
```sql
CREATE TABLE ContractMeasure (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    type VARCHAR(50), -- e.g., Contract, Measure
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

**8. Data Entity/Data Component Catalog**
```sql
CREATE TABLE DataEntityComponent (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    type VARCHAR(50), -- e.g., Data Entity, Data Component
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

**9. Application Portfolio Catalog**
```sql
CREATE TABLE ApplicationPortfolio (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    version VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

**10. Interface Catalog**
```sql
CREATE TABLE Interface (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    protocol VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

**11. Technology Standards Catalog**
```sql
CREATE TABLE TechnologyStandards (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    version VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

**12. Technology Portfolio Catalog**
```sql
CREATE TABLE TechnologyPortfolio (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    version VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

**13. Requirements Catalog**
```sql
CREATE TABLE Requirements (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    priority VARCHAR(50),
    status VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

___

### Matrix

1. Stakeholder Map matrix
2. Business Interaction matrix
3. Actor/Role matrix
4. Data Entity/Business Function matrix
5. System/Data matrix
6. System/Organization matrix
7. Role/System matrix
8. System/Function matrix
9. Application Interaction matrix
10. System/Technology matrix


```python
import numpy as np

# 1. Stakeholder Map matrix
stakeholder_map = np.array([
    ['Stakeholder', 'Interest', 'Influence', 'Impact'],
    ['CEO', 'High', 'High', 'High'],
    ['IT Manager', 'High', 'Medium', 'High'],
    ['End Users', 'Medium', 'Low', 'Medium'],
    ['Vendors', 'Low', 'Low', 'Low']
])

# 2. Business Interaction matrix
business_interaction = np.array([
    ['', 'Sales', 'Marketing', 'Finance', 'HR'],
    ['Sales', 'X', 'High', 'Medium', 'Low'],
    ['Marketing', 'High', 'X', 'Low', 'Low'],
    ['Finance', 'Medium', 'Low', 'X', 'Medium'],
    ['HR', 'Low', 'Low', 'Medium', 'X']
])

# 3. Actor/Role matrix
actor_role = np.array([
    ['', 'Manager', 'Developer', 'Tester', 'Support'],
    ['John', 'X', '', '', ''],
    ['Alice', '', 'X', '', ''],
    ['Bob', '', '', 'X', ''],
    ['Eve', '', '', '', 'X']
])

# 4. Data Entity/Business Function matrix
data_entity_business_function = np.array([
    ['', 'Sales', 'Marketing', 'Finance', 'HR'],
    ['Customer Data', 'C', 'R', 'R', ''],
    ['Product Data', 'R', 'C', '', ''],
    ['Financial Data', '', '', 'C', 'R'],
    ['Employee Data', '', '', 'R', 'C']
])

# 5. System/Data matrix
system_data = np.array([
    ['', 'Customer Data', 'Product Data', 'Financial Data', 'Employee Data'],
    ['CRM System', 'C', 'R', '', ''],
    ['ERP System', 'R', 'C', 'C', 'R'],
    ['HR System', '', '', '', 'C'],
    ['Analytics System', 'R', 'R', 'R', 'R']
])

# 6. System/Organization matrix
system_organization = np.array([
    ['', 'Sales', 'Marketing', 'Finance', 'HR'],
    ['CRM System', 'X', 'X', '', ''],
    ['ERP System', 'X', '', 'X', 'X'],
    ['HR System', '', '', '', 'X'],
    ['Analytics System', 'X', 'X', 'X', 'X']
])

# 7. Role/System matrix
role_system = np.array([
    ['', 'CRM System', 'ERP System', 'HR System', 'Analytics System'],
    ['Manager', 'R', 'R', 'R', 'R'],
    ['Developer', 'R', 'R', '', 'R'],
    ['Tester', 'R', 'R', 'R', 'R'],
    ['Support', 'R', 'R', 'R', '']
])

# 8. System/Function matrix
system_function = np.array([
    ['', 'Sales Management', 'Inventory Management', 'Financial Reporting', 'Employee Management'],
    ['CRM System', 'X', '', '', ''],
    ['ERP System', 'X', 'X', 'X', ''],
    ['HR System', '', '', '', 'X'],
    ['Analytics System', 'X', 'X', 'X', 'X']
])

# 9. Application Interaction matrix
application_interaction = np.array([
    ['', 'CRM System', 'ERP System', 'HR System', 'Analytics System'],
    ['CRM System', 'X', 'High', 'Low', 'Medium'],
    ['ERP System', 'High', 'X', 'Medium', 'High'],
    ['HR System', 'Low', 'Medium', 'X', 'Low'],
    ['Analytics System', 'Medium', 'High', 'Low', 'X']
])

# 10. System/Technology matrix
system_technology = np.array([
    ['', 'Cloud', 'On-Premise', 'Mobile', 'AI/ML'],
    ['CRM System', 'X', '', 'X', ''],
    ['ERP System', 'X', 'X', '', ''],
    ['HR System', 'X', '', 'X', ''],
    ['Analytics System', 'X', '', '', 'X']
])

# Function to print matrices in a more readable format
def print_matrix(matrix, title):
    print(f"\n{title}:")
    for row in matrix:
        print(" | ".join(str(cell).ljust(20) for cell in row))
    print()

# Print all matrices
print_matrix(stakeholder_map, "Stakeholder Map Matrix")
print_matrix(business_interaction, "Business Interaction Matrix")
print_matrix(actor_role, "Actor/Role Matrix")
print_matrix(data_entity_business_function, "Data Entity/Business Function Matrix")
print_matrix(system_data, "System/Data Matrix")
print_matrix(system_organization, "System/Organization Matrix")
print_matrix(role_system, "Role/System Matrix")
print_matrix(system_function, "System/Function Matrix")
print_matrix(application_interaction, "Application Interaction Matrix")
print_matrix(system_technology, "System/Technology Matrix")
```

This code creates NumPy arrays to represent each of the TOGAF matrices you mentioned. The matrices use simple representations:

- 'X' indicates a strong relationship or primary responsibility
- 'High', 'Medium', 'Low' indicate levels of interaction or influence
- 'C' and 'R' in the Data Entity/Business Function and System/Data matrices represent 'Create' and 'Read' operations
- Empty strings represent no relationship

The `print_matrix` function is used to display the matrices in a more readable format.
