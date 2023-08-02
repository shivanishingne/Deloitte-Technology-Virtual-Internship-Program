task Summmary:

1. Download the daikibo-telemetry-data.json.zip file -> unzip -> and import it in Tableau.
2. Create a calculated measure field "Unhealthy" with the value of 10 for every unhealthy status (representing 10min of potential down time since the previous message).
3. Create a bar-chart: Down Time per Factory.
4. Create new sheet with a new bar-chart: Down Time per Device Type.
5. Create a Dashboard with the 2 previous sheets and set the first chart to be used as a filter (selecting factory in the first chart, shows only the down time of the machines in this factory there in the second chart).
6. Select the factory with the most down time (click on its bar)