# AWS-Spectrum-Matching

## Notation:
1. This is a AWS end-to-end project, where you work like "Kinesis -> Lambda -> EMR -> Glue -> Athena".
2. Only a tiny part(100 .fits files) of real data(real data may up to 10M .fits) are provided in '/data', you could use it as a trial and the data structure is simple, easy to generate your own.
3. Be careful of pricing. Using sample data only for a trial is recommended. Once you set up whole workflow, you could try more data to make it real.

## Backgound:
1. Look through '/PriorKnowledge' roughly.
2. We have real-time spectrum data(suppose it's .fits file, where 'fits' is Flexible Image Transport System) from many astronomical observatories.
3. Our purpose is find out how much does a new spectrum matches our target Lyman-break spectrum based on person-correlation(we call this "distance"), and make the results well managed while also managing the raw data.
4. AS data accumulates, we need big data cluster to process the results of distances. For example, we want to figure out which observatory find the most "near" spectrum in the past two months. So we need a big data cluster aggregate several key indicators everyeveryday. 
5. We also want some angile querying rather than big data cluster, matain an application oreinted table outside traditional query engine(hive) is also needed.

## Project-workflow
1. AWS Kenesis
2. AWS Lambda
3. AWS EMR
4. AWS Glue
5. AWS Athena
(Also, you should acknowledged some S3 basic managements and some IAM controls)

## Contact
If you think something's wrong with this project or have a better idea, please contact me.
  
author: Simon Chen
  
email: schen935@wisc.edu
