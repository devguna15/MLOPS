import time

def monitor_prediction_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Prediction took {end_time - start_time:.4f} seconds")
        return result
    return wrapper
