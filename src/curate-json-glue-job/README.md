# ETL Logic

The python script demonstrates core ETL logic to convert the nested JSON file given in problem statment to flat file.

Sample input file and the actual result file are provided in `src/curate-json-glue-job/test_files`.

This code can be easily ported into a Lambda, a container (Fargate) or Glue job, but for demonstration purposes it has hard-coded references to input and output files.

# Testing

The code is written such a way that its easy to test and ew unit tests are added for demonstration.

If I would have more time to spend on it, the could have more than 80% test coverage.

Tests can be executed : `python3 -m unittest test_*.py`