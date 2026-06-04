 ## Protein-Structure-Resolution-Prediction
## Project Overview
This project uses Machine Learning techniques to predict Protein Structure Refinement Resolution (Å) based on crystallographic and biochemical parameters. The objective is to estimate protein structure quality using experimentally measured features.
## Dataset
The dataset was obtained from the RCSB Protein Data Bank (PDB).
Dataset characteristics:
* 11,852 records
* 24 attributes
* Target variable: Refinement Resolution (Å)
## Data Preprocessing
* Missing value handling
* Feature scaling
* One-Hot Encoding for categorical features
* Feature selection
## Models Evaluated
* Linear Regression
* Support Vector Regression (SVR)
* Random Forest Regressor
## Best Model
Random Forest Regressor
Performance:
* MAE: 0.143
* RMSE: 0.189
* R² Score: 0.823
## Model Details
* Algorithm: Random Forest Regressor
* Hyperparameter tuning applied
* Features used:
    * Matthews Coefficient
    * Solvent Content
    * pH
    * Temperature
    * R-free
    * R-work
 
*The model is deployed using Streamlit Cloud.
## Live Demo:
https://protein-structure-resolution-prediction-ufkrnsjxpt99g9yjdmjxlb.streamlit.app/
 ## presentation video
 https://drive.google.com/file/d/1czdzlJisSnPN3Q3huF19bs8LquikgkYg/view?usp=drive_link

## Dataset Source:
https://www.kaggle.com/datasets/samiraalipour/rcsb-pdb-macromolecular-structure-dataset
## Technologies Used
* Python
* Scikit-Learn
* Pandas
* NumPy
* Streamlit
* Joblib
* GitHub
* gdown
 ## Important note
The trained model best_random_forest_model.pkl is too large to be hosted directly on GitHub due to file size limits. 
You can download the model file from the following Google Drive link: 
https://drive.google.com/file/d/1EWF_APBIYu9MjbMPwBuhp-qS8lA9Ew2c/view?usp=drive_link
