# ECT Report Analysis
## Description of ECT Report
Quoting the description on the report home page:
>"Average time in days it takes for a Customers issue to be resolved measured from the day the Customer contacts the Call Center and a Service Order is opened unitl the case status is moved to closed. Calculation includes FOD, CRU, On-Site and Depot Service Orders."

The SLA goal is 5.60 days.

## Method for KPI Calculation
The report performs a simple calculation to determine whether or not a case met the SLA. If the case is open for less than 5.60 days then it is marked as a `Make`; otherwise it will be a `Miss`. This calculation is performed by subtracting the values in columns `SR Close TS` and `SR Create TS`.

The KPI for this metric is calculated by the mean value of the subtraction of `SR Close TS` and `SR Create TS` for each row in the data set.

## Limitations of the Report
* By default this report measures *all* available data regardless of case age. Therefore the KPI reflects *all* cases since the reporting tool started capturing data. This is the number shown in the dashboard.
* The column `SR Close TS` has the value of the case's final closure date. This value is not reflective of the performance of the call center as this event is triggered when all work on the case is completed (CX status). A few examples for possible delays outside of the call center's control:
    * Limited part availability.
    * Customer delaying service (additional information needed, not available).
    * Technician not available to service machine.
    * Machine lost in transit.
    * Carrier unable to deliver a part.
* Changing the date range on the report filters the data by the values in the `SR Close TS` column. For example, we may pick all cases YTD for our values, and the report will pull cases which were opened prior to the current year if the `SR Close TS` value is on the current year.
* There is no true indicator of call center performance in the data columns. The best indicator would be the time when the first action plan (AP) is placed on a case. This metric is not available as of writing this report.
## Conclusion
The ECT Report does not serve as an objective measure of the performance of the call center due to its inherent limitations. The case closure time is the determinant factor into whether or not the KPIs are met. This number is not reflective of the actions performed by the call center. A better measure would be the first AP time on the case. Delays in the field can cause cases to remain open and for the closure time to be delayed indefinitely.