# ECT Report Analysis
## Description of ECT Report
Quoting the description on the report home page:
>"Average time in days it takes for a Customers issue to be resolved measured from the day the Customer contacts the Call Center and a Service Order is opened unitl the case status is moved to closed. Calculation includes FOD, CRU, On-Site and Depot Service Orders."

The SLA for ECT is 5.60 days.

## Definitions
* RC: Received, time and date when a case is created by either a customer or electronically.
* CX: Closure, time and date when a case is closed. This is triggered when all work is completed on a case.
* CQ: Change Queue, time and date when a case is actioned by the call center.

## Method for ECT Calculation
ECT is calculated by the mean of the subtraction of `SR Close TS` and `SR Create TS` for each row in the data set. This is equivalent to finding the difference in the timestamps between a `CX` (close) and `RC` (receive).

## Hypothesis
The ECT SLA has not been met since June 2019. The number was 12.3 at the time the analysis was made. Management believes that CET could be affected by factors outside of the control of CGS. Using `CX` as a factor for determining ECT is misleading as the call center has little control when this event will be triggered. A better measure of work done by the call center would be by measuring time between `CQ` and `RC`. The `CQ` event is triggered when the agent is ready to launch a case for service. At that point the case leaves the realm of the call center and is transferred to the field for actioning. Various factors might affected how long a case remains open afterward.

## Data Set
The data set was retrieved from the IBM Control Tower. This data kept the default view, no adjustments were made to the dates or any filters applied. This initial data set was used to perform the analysis. This report was retrieved on 2020-01-16.

## Method
First we attempted to replicate the observed ECT from IBM Control Tower. This was done by adding a column for `CX and RC Difference` on the original data set. In this column we calculated the difference for all data points. The calculated mean was 12.3 which was the same as the reported ECT in the IBM Control Tower. Below are the statistics of the complete data set. The table header indicates the calculation method for the numbers described.

### Data Set Statistics
|       |CX - RC|
|-------|-------|
|Data points|23,563|
|Mean (ECT)|12.30|
|Stdev|10.78|
|Q1|4.11|
|Q2|8.75|
|Q3|18.11|

Two random sample data sets were taken from the initial data set. Each sample data set had a total of 378 data points. This number of samples provides us with a 95.00% confidence interval for the results with a margin of error of 5.00%.

The variables we needed were `RC`, `CX`, and `CQ`. The first two were given on the report. The `CQ` variable was not. It had to be retrieved from each case through OCPM. To aid with data mining a Python program was created to retrieve the `CQ` timestamp from the case. In the scenario that the `CQ` did not occur (Canada cases) or occurred multiple times, a manual check was done to determine the timestamp.

Once all `CQ` values were retrieved each sample data set had two columns added were the differences were calculated.
* `CX and RC Difference`
* `CQ and RC Difference`

## Results
Below are the observed results from each sample data set. It should be noted that the reported means have a 5.00% margin of error. The headers of the tables indicate the method used to calculate the numbers.

### Data Sample 1 Statistics
|       |CX - RC|CQ - RC|
|-------|-------|-------|
|Data points|378|378|
|Mean (ECT)|12.46|0.48|
|Stdev|10.76|2.05|
|Q1|4.14|0.00|
|Q2|8.11|0.03|
|Q3|18.14|0.51|

### Data Sample 2 Statistics
|       |CX - RC|CQ - RC|
|-------|-------|-------|
|Data points|378|378|
|Mean (ECT)|11.02|0.48|
|Stdev|9.41|1.42|
|Q1|4.16|0.01|
|Q2|8.11|0.02|
|Q3|18.16|0.47|

## Discussion

The 

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
* Using `SR Close TS` as the date filter instead of `SR Open TS` is misleading. It doesn’t reflect monthly performance as it captures cases that were opened prior to the current month.
## Conclusion
The ECT Report does not serve as an objective measure of the performance of the call center due to its inherent limitations. The case closure time is the determinant factor into whether the KPIs are met. This number is not reflective of the actions performed by the call center. A better measure would be the first AP time on the case. Delays in the field can cause cases to remain open and for the closure time to be delayed indefinitely.