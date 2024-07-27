






Step1:  i used rapid api to fetch icc ranking data using python and then created a csv, later pushing  this csv to the bucket. 


Step2:  Now i want to trigger cloud function that whenever the csv file come into the bucket it trigger the data flow job, data flow job will write the csv file into the big query table.


Step3: to complete step2 first i  will make a job in data flow to write the data into the big query table . 



Step4: in data flow , we will select text to big query template, then create a json for schema and create a table into bq, also   we used udf (js file to avoid error  which happened while writing csv )


STEP5: after setting up above all, we will create a dag job via composer to run the extract file python file .

