import pathlib
import os
import model

PACKAGE_ROOT = pathlib.Path(model.__file__).resolve().parent

DATA_PATH = os.path.join(PACKAGE_ROOT, "datasets")

TRAINED_MODEL_PATH = os.path.join(PACKAGE_ROOT, "trained_models")

DATA_FILE = 'insurance.csv'

MODEL_NAME = 'my_model.h5'


TARGET = 'charges'

#Final features used in the model
FEATURES = ["age", "sex", "bmi", "children", "smoker", "region"]


CAT_FEATURES = ["sex", "smoker", "region"]

FEATURES_TO_ENCODE = ["sex", "smoker", "region"]



NEW_FEATURES = ['age', 'sex', 'bmi', 'children', 'smoker', 'southwest', 'southeast',
    'northwest', 'northeast', 'charges']