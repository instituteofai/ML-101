from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
import joblib

from custom_transformer import CombinedAttributesAdder

housing_vectorizer = open('model/housing_vectorized.pkl', 'rb')
housing_data = joblib.load(housing_vectorizer)

num_pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='median')),
    ('attribs_adder', CombinedAttributesAdder()),
    ('std_scaler', StandardScaler()),
])

num_attribs = ['longitude', 'latitude', 'housing_median_age', 'total_rooms',
    'total_bedrooms', 'population', 'households', 'median_income']

cat_attribs = ['ocean_proximity']

def get_pipeline():
    full_pipeline = ColumnTransformer([
        ('num', num_pipeline, num_attribs),
        ('cat', OneHotEncoder(), cat_attribs),
    ])
    housing_tr = full_pipeline.fit_transform(housing_data)
    return full_pipeline
