# PythonRandomForest
This is a RandomForest repository based on the RandomForestRegressor from SciKitLearn.

Windows preferences has to be set up for PyDev.  The interpreter and the libraries to be used need to be assigned.  The tester in PyUnit has to be assigned to Py.test runner if Pytest is used instead of Unittest.

The order of pre-processing and analysis are: 

1) Make sure the latest version of ORD's nanoinformatic database "NaKnowBase" has been mined and output into a file of CSV format, and placed into "..\\data\\assay_all_vw_out_22325rows.csv".

2) Run Refinement.py using Python to process the above file prior to analysis.  This places the refinement results into
"..\\data\\Multivariate_Imputed_Numerical_Columns.csv".

3) Run Analysis.py using Python after the above refinement process. The rows of the above file are split into training and test sets.  A Random Forest model is built from the training set to predict the viability of human cell cultures exposed to different types of nanomaterials. Using this model, viabilities are predicted for all nanomaterials in the test set and compared with their experimentally observed viabilities.  The results of the modeling and comparing are output.

4) Run Validation.py using Python to perform a 5-fold validation of the model building and prediction accuracy. The results are output with the interpretation: the closer the r2 values in the test set are to 1.0, the better the model building and prediction accuracy.  The final r2_save value is associated with a set of observed values completely separated from the 5-fold validation process.
