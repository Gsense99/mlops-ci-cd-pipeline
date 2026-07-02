# ML CI/CD Pipeline

This project is a simplified CI/CD pipeline applied to Machine Learning.

The pipeline trains, evaluates, validates and deploys a classification model using the Iris dataset.

## Pipeline steps

1. Install dependencies
2. Train the model
3. Evaluate the model
4. Validate the accuracy
5. Deploy the model if accuracy >= 0.90

## Technologies

- Python
- Scikit-Learn
- Joblib
- YAML
- Git / GitHub

## How to run

```bash
python -m pip install -r requirements.txt
python run_pipeline.py
```

## Example 

[INSTALL] OK
[TRAIN] OK
[EVALUATE] OK
[VALIDATE] PASSED - Accuracy = 1.00
[DEPLOY] Model copied to production/

[PIPELINE] SUCCESS

## CI/CD explanation

This project simulates a CI/CD pipeline locally.

The pipeline.yml file describes the steps to execute.
The run_pipeline.py file reads this YAML file and runs each step in order.

If one step fails, the pipeline stops automatically.

Validation

The model is only deployed if its accuracy is greater than or equal to 0.90.