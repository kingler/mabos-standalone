# BPMN (Business Process Model and Notation)

BPMN (Business Process Model and Notation) workflow engine. One popular choice is Camunda, which provides a robust platform for automating and orchestrating business processes. Below, are examples of how to implement the three BPMN diagrams (Employee Onboarding Process, Sales Order Process, and Purchase Order Process) using Camunda's BPMN workflow engine.

### **1. Employee Onboarding Process**

#### **BPMN Diagram in XML**

```xml
<?xml version="1.0" encoding="UTF-8"?>
<definitions xmlns="http://www.omg.org/spec/BPMN/20100524/MODEL" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:bpmndi="http://www.omg.org/spec/BPMN/20100524/DI" xmlns:dc="http://www.omg.org/spec/DD/20100524/DC" xmlns:di="http://www.omg.org/spec/DD/20100524/DI" id="Definitions_1" targetNamespace="http://bpmn.io/schema/bpmn">
  <process id="EmployeeOnboardingProcess" name="Employee Onboarding Process" isExecutable="true">
    <startEvent id="StartEvent_1" name="Start">
      <outgoing>SequenceFlow_1</outgoing>
    </startEvent>
    <task id="Task_1" name="HR Sends Welcome Email">
      <incoming>SequenceFlow_1</incoming>
      <outgoing>SequenceFlow_2</outgoing>
    </task>
    <sequenceFlow id="SequenceFlow_1" sourceRef="StartEvent_1" targetRef="Task_1"/>
    <task id="Task_2" name="New Employee Attends Orientation">
      <incoming>SequenceFlow_2</incoming>
      <outgoing>SequenceFlow_3</outgoing>
    </task>
    <sequenceFlow id="SequenceFlow_2" sourceRef="Task_1" targetRef="Task_2"/>
    <task id="Task_3" name="IT Sets Up Accounts and Equipment">
      <incoming>SequenceFlow_3</incoming>
      <outgoing>SequenceFlow_4</outgoing>
    </task>
    <sequenceFlow id="SequenceFlow_3" sourceRef="Task_2" targetRef="Task_3"/>
    <task id="Task_4" name="Employee Completes Paperwork">
      <incoming>SequenceFlow_4</incoming>
      <outgoing>SequenceFlow_5</outgoing>
    </task>
    <sequenceFlow id="SequenceFlow_4" sourceRef="Task_3" targetRef="Task_4"/>
    <task id="Task_5" name="Manager Assigns Initial Tasks">
      <incoming>SequenceFlow_5</incoming>
      <outgoing>SequenceFlow_6</outgoing>
    </task>
    <sequenceFlow id="SequenceFlow_5" sourceRef="Task_4" targetRef="Task_5"/>
    <endEvent id="EndEvent_1" name="End">
      <incoming>SequenceFlow_6</incoming>
    </endEvent>
    <sequenceFlow id="SequenceFlow_6" sourceRef="Task_5" targetRef="EndEvent_1"/>
  </process>
  <bpmndi:BPMNDiagram id="BPMNDiagram_1">
    <bpmndi:BPMNPlane id="BPMNPlane_1" bpmnElement="EmployeeOnboardingProcess">
      <bpmndi:BPMNShape id="StartEvent_1_di" bpmnElement="StartEvent_1">
        <dc:Bounds x="173" y="102" width="36" height="36"/>
      </bpmndi:BPMNShape>
      <bpmndi:BPMNShape id="Task_1_di" bpmnElement="Task_1">
        <dc:Bounds x="259" y="80" width="100" height="80"/>
      </bpmndi:BPMNShape>
      <bpmndi:BPMNEdge id="SequenceFlow_1_di" bpmnElement="SequenceFlow_1">
        <di:waypoint x="209" y="120"/>
        <di:waypoint x="259" y="120"/>
      </bpmndi:BPMNEdge>
      <bpmndi:BPMNShape id="Task_2_di" bpmnElement="Task_2">
        <dc:Bounds x="409" y="80" width="100" height="80"/>
      </bpmndi:BPMNShape>
      <bpmndi:BPMNEdge id="SequenceFlow_2_di" bpmnElement="SequenceFlow_2">
        <di:waypoint x="359" y="120"/>
        <di:waypoint x="409" y="120"/>
      </bpmndi:BPMNEdge>
      <bpmndi:BPMNShape id="Task_3_di" bpmnElement="Task_3">
        <dc:Bounds x="559" y="80" width="100" height="80"/>
      </bpmndi:BPMNShape>
      <bpmndi:BPMNEdge id="SequenceFlow_3_di" bpmnElement="SequenceFlow_3">
        <di:waypoint x="509" y="120"/>
        <di:waypoint x="559" y="120"/>
      </bpmndi:BPMNEdge>
      <bpmndi:BPMNShape id="Task_4_di" bpmnElement="Task_4">
        <dc:Bounds x="709" y="80" width="100" height="80"/>
      </bpmndi:BPMNShape>
      <bpmndi:BPMNEdge id="SequenceFlow_4_di" bpmnElement="SequenceFlow_4">
        <di:waypoint x="659" y="120"/>
        <di:waypoint x="709" y="120"/>
      </bpmndi:BPMNEdge>
      <bpmndi:BPMNShape id="Task_5_di" bpmnElement="Task_5">
        <dc:Bounds x="859" y="80" width="100" height="80"/>
      </bpmndi:BPMNShape>
      <bpmndi:BPMNEdge id="SequenceFlow_5_di" bpmnElement="SequenceFlow_5">
        <di:waypoint x="809" y="120"/>
        <di:waypoint x="859" y="120"/>
      </bpmndi:BPMNEdge>
      <bpmndi:BPMNShape id="EndEvent_1_di" bpmnElement="EndEvent_1">
        <dc:Bounds x="1009" y="102" width="36" height="36"/>
      </bpmndi:BPMNShape>
      <bpmndi:BPMNEdge id="SequenceFlow_6_di" bpmnElement="SequenceFlow_6">
        <di:waypoint x="959" y="120"/>
        <di:waypoint x="1009" y="120"/>
      </bpmndi:BPMNEdge>
    </bpmndi:BPMNPlane>
  </bpmndi:BPMNDiagram>
</definitions>
```

### **2. Sales Order Process**

#### **BPMN Diagram in XML**

```xml
<?xml version="1.0" encoding="UTF-8"?>
<definitions xmlns="http://www.omg.org/spec/BPMN/20100524/MODEL" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:bpmndi="http://www.omg.org/spec/BPMN/20100524/DI" xmlns:dc="http://www.omg.org/spec/DD/20100524/DC" xmlns:di="http://www.omg.org/spec/DD/20100524/DI" id="Definitions_2" targetNamespace="http://bpmn.io/schema/bpmn">
  <process id="SalesOrderProcess" name="Sales Order Process" isExecutable="true">
    <startEvent id="StartEvent_2" name="Start">
      <outgoing>SequenceFlow_7</outgoing>
    </startEvent>
    <task id="Task_7" name="Receive Customer Order">
      <incoming>SequenceFlow_7</incoming>
      <outgoing>SequenceFlow_8</outgoing>
    </task>
    <sequenceFlow id="SequenceFlow_7" sourceRef="StartEvent_2" targetRef="Task_7"/>
    <task id="Task_8" name="Check Inventory">
      <incoming>SequenceFlow_8</incoming>
      <outgoing>SequenceFlow_9</outgoing>
    </task>
    <sequenceFlow id="SequenceFlow_8" sourceRef="Task_7" targetRef="Task_8"/>
    <exclusiveGateway id="ExclusiveGateway_1" name="In Stock?">
      <incoming>SequenceFlow_9</incoming>
      <outgoing>SequenceFlow_10</outgoing>
      <outgoing>SequenceFlow_11</outgoing>
    </exclusiveGateway>
    <sequenceFlow id="SequenceFlow_9" sourceRef="Task_8" targetRef="ExclusiveGateway_1"/>
    <task id="Task_9" name="Process Payment">
      <incoming>SequenceFlow_10</incoming>
      <outgoing>SequenceFlow_12</outgoing>
    </task>
    <sequenceFlow id="SequenceFlow_10" sourceRef="ExclusiveGateway_1" targetRef="Task_9" name="Yes"/>
    <task id="Task_10" name="Prepare Shipment">
      <incoming>SequenceFlow_12</incoming>
      <outgoing>SequenceFlow_13</outgoing>
    </task>
    <sequenceFlow id="SequenceFlow_12" sourceRef="Task_9" targetRef="Task_10"/>
    <task id="Task_11" name="Ship Order">
      <incoming>SequenceFlow_13</incoming>
      <outgoing>SequenceFlow_14</outgoing>
    </task>
    <sequenceFlow id="SequenceFlow_13" sourceRef="Task_10" targetRef="Task_11"/>
    <endEvent id="EndEvent_2" name="End">
      <incoming>SequenceFlow_14</incoming>
    </endEvent>
    <sequenceFlow id="SequenceFlow_14" sourceRef="Task_11" targetRef="EndEvent_2"/>
    <task id="Task_12" name="Order from Supplier">
      <incoming>SequenceFlow_11</incoming>
      <outgoing>SequenceFlow_15</outgoing>
    </task>
    <sequenceFlow id="SequenceFlow_11" sourceRef="ExclusiveGateway_1" targetRef="Task_12" name="No"/>
    <task id="Task_13" name="Wait for Restock">
      <incoming>SequenceFlow_15</incoming>
      <outgoing>SequenceFlow_16</outgoing>
    </task>
    <sequenceFlow id="SequenceFlow_15" sourceRef="Task_12" targetRef="Task_13"/>
    <sequenceFlow id="SequenceFlow_16" sourceRef="Task_13" targetRef="Task_9"/>
  </process>
  <bpmndi:BPMNDiagram id="BPMNDiagram_2">
    <bpmndi:BPMNPlane id="BPMNPlane_2" bpmnElement="SalesOrderProcess">
      <bpmndi:BPMNShape id="StartEvent_2_di" bpmnElement="StartEvent_2">
        <dc:Bounds x="173" y="102" width="36" height="36"/>
      </bpmndi:BPMNShape>
      <bpmndi:BPMNShape id="Task_7_di" bpmnElement="Task_7">
        <dc:Bounds x="259" y="80" width="100" height="80"/>
      </bpmndi:BPMNShape>
      <bpmndi:BPMNEdge id="SequenceFlow_7_di" bpmnElement="SequenceFlow_7">
        <di:waypoint x="209" y="120"/>
        <di:waypoint x="259" y="120"/>
      </bpmndi:BPMNEdge>
      <bpmndi:BPMNShape id="Task_8_di" bpmnElement="Task_8">
        <dc:Bounds x="409" y="80" width="100" height="80"/>
      </bpmndi:BPMNShape>
      <bpmndi:BPMNEdge id="SequenceFlow_8_di" bpmnElement="SequenceFlow_8">
        <di:waypoint x="359" y="120"/>
        <di:waypoint x="409" y="120"/>
      </bpmndi:BPMNEdge>
      <bpmndi:BPMNShape id="ExclusiveGateway_1_di" bpmnElement="ExclusiveGateway_1">
        <dc:Bounds x="559" y="102" width="36" height="36"/>
      </bpmndi:BPMNShape>
      <bpmndi:BPMNEdge id="SequenceFlow_9_di" bpmnElement="SequenceFlow_9">
        <di:waypoint x="509" y="120"/>
        <di:waypoint x="559" y="120"/>
      </bpmndi:BPMNEdge>
      <bpmndi:BPMNShape id="Task_9_di" bpmnElement="Task_9">
        <dc:Bounds x="659" y="80" width="100" height="80"/>
      </bpmndi:BPMNShape>
      <bpmndi:BPMNEdge id="SequenceFlow_10_di" bpmnElement="SequenceFlow_10">
        <di:waypoint x="595" y="120"/>
        <di:waypoint x="659" y="120"/>
      </bpmndi:BPMNEdge>
      <bpmndi:BPMNShape id="Task_10_di" bpmnElement="Task_10">
        <dc:Bounds x="809" y="80" width="100" height="80"/>
      </bpmndi:BPMNShape>
      <bpmndi:BPMNEdge id="SequenceFlow_12_di" bpmnElement="SequenceFlow_12">
        <di:waypoint x="759" y="120"/>
        <di:waypoint x="809" y="120"/>
      </bpmndi:BPMNEdge>
      <bpmndi:BPMNShape id="Task_11_di" bpmnElement="Task_11">
        <dc:Bounds x="959" y="80" width="100" height="80"/>
      </bpmndi:BPMNShape>
      <bpmndi:BPMNEdge id="SequenceFlow_13_di" bpmnElement="SequenceFlow_13">
        <di:waypoint x="909" y="120"/>
        <di:waypoint x="959" y="120"/>
      </bpmndi:BPMNEdge>
      <bpmndi:BPMNShape id="EndEvent_2_di" bpmnElement="EndEvent_2">
        <dc:Bounds x="1109" y="102" width="36" height="36"/>
      </bpmndi:BPMNShape>
      <bpmndi:BPMNEdge id="SequenceFlow_14_di" bpmnElement="SequenceFlow_14">
        <di:waypoint x="1059" y="120"/>
        <di:waypoint x="1109" y="120"/>
      </bpmndi:BPMNEdge>
      <bpmndi:BPMNShape id="Task_12_di" bpmnElement="Task_12">
        <dc:Bounds x="659" y="180" width="100" height="80"/>
      </bpmndi:BPMNShape>
      <bpmndi:BPMNEdge id="SequenceFlow_11_di" bpmnElement="SequenceFlow_11">
        <di:waypoint x="595" y="138"/>
        <di:waypoint x="659" y="220"/>
      </bpmndi:BPMNEdge>
      <bpmndi:BPMNShape id="Task_13_di" bpmnElement="Task_13">
        <dc:Bounds x="809" y="180" width="100" height="80"/>
      </bpmndi:BPMNShape>
      <bpmndi:BPMNEdge id="SequenceFlow_15_di" bpmnElement="SequenceFlow_15">
        <di:waypoint x="759" y="220"/>
        <di:waypoint x="809" y="220"/>
      </bpmndi:BPMNEdge>
      <bpmndi:BPMNEdge id="SequenceFlow_16_di" bpmnElement="SequenceFlow_16">
        <di:waypoint x="909" y="220"/>
        <di:waypoint x="959" y="120"/>
      </bpmndi:BPMNEdge>
    </bpmndi:BPMNPlane>
  </bpmndi:BPMNDiagram>
</definitions>
```

### **3. Purchase Order Process**

#### **BPMN Diagram in XML**

```xml
<?xml version="1.0" encoding="UTF-8"?>
<definitions xmlns="http://www.omg.org/spec/BPMN/20100524/MODEL" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:bpmndi="http://www.omg.org/spec/BPMN/20100524/DI" xmlns:dc="http://www.omg.org/spec/DD/20100524/DC" xmlns:di="http://www.omg.org/spec/DD/20100524/DI" id="Definitions_3" targetNamespace="http://bpmn.io/schema/bpmn">
  <process id="PurchaseOrderProcess" name="Purchase Order Process" isExecutable="true">
    <startEvent id="StartEvent_3" name="Start">
      <outgoing>SequenceFlow_17</outgoing>
    </startEvent>
    <task id="Task_14" name="Create Purchase Requisition">
      <incoming>SequenceFlow_17</incoming>
      <outgoing>SequenceFlow_18</outgoing>
    </task>
    <sequenceFlow id="SequenceFlow_17" sourceRef="StartEvent_3" targetRef="Task_14"/>
    <task id="Task_15" name="Approve Requisition">
      <incoming>SequenceFlow_18</incoming>
      <outgoing>SequenceFlow_19</outgoing>
    </task>
    <sequenceFlow id="SequenceFlow_18" sourceRef="Task_14" targetRef="Task_15"/>
```

## Example of how to programmatically execute a workflow using Camunda's Java API:

```java
import org.camunda.bpm.engine.ProcessEngine;
import org.camunda.bpm.engine.ProcessEngineConfiguration;
import org.camunda.bpm.engine.RepositoryService;
import org.camunda.bpm.engine.RuntimeService;
import org.camunda.bpm.engine.repository.Deployment;
import org.camunda.bpm.engine.runtime.ProcessInstance;

import java.io.InputStream;

public class WorkflowExecutor {

    public static void main(String[] args) {
        // Initialize the process engine
        ProcessEngine processEngine = ProcessEngineConfiguration
            .createStandaloneInMemProcessEngineConfiguration()
            .buildProcessEngine();

        // Get the RepositoryService
        RepositoryService repositoryService = processEngine.getRepositoryService();

        // Deploy the BPMN XML
        InputStream bpmnInputStream = WorkflowExecutor.class.getClassLoader().getResourceAsStream("path/to/your/process.bpmn");
        Deployment deployment = repositoryService.createDeployment()
            .addInputStream("process.bpmn", bpmnInputStream)
            .deploy();

        // Get the RuntimeService
        RuntimeService runtimeService = processEngine.getRuntimeService();

        // Start a process instance
        ProcessInstance processInstance = runtimeService.startProcessInstanceByKey("yourProcessKey");

        System.out.println("Process instance started: " + processInstance.getId());

        // Clean up
        processEngine.close();
    }
}
```


1. Initialize the Camunda process engine using a standalone in-memory configuration.
2. Get the RepositoryService, which is used for deploying process definitions.
3. Deploy the BPMN XML file. Make sure to replace "path/to/your/process.bpmn" with the actual path to your BPMN file.
4. Get the RuntimeService, which is used for starting and managing process instances.
5. Start a process instance using the process key defined in your BPMN XML. Replace "yourProcessKey" with the actual process key from your BPMN file.
6. Print the ID of the started process instance.
7. Close the process engine to clean up resources.

To use this code:
1. Make sure you have the Camunda BPM engine dependencies in your project.
2. Place your BPMN XML file in your project's resources folder.
3. Update the path and process key in the code to match your BPMN file.
4. Run the main method to execute the workflow.

This example demonstrates a basic workflow execution. Depending on your specific BPMN process, you might need to handle user tasks, service tasks, or other BPMN elements, which would require additional code to interact with the process instance as it progresses through the workflow.
