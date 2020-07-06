from pipeline import get_pipeline

def get_prepared_data(payload):
    full_pipeline = get_pipeline()

    prepared_data = full_pipeline.transform(payload)
    return prepared_data
