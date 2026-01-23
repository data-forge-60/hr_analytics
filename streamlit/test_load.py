import joblib
import os
import sys

file_path = 'model_attrition.pkl'
print(f"Checking {file_path}")
if os.path.exists(file_path):
    print(f"File exists. Size: {os.path.getsize(file_path)} bytes")
    try:
        model = joblib.load(file_path)
        print("Model loaded successfully!")
        print(f"Object type: {type(model)}")
        
        # Jika model adalah Pipeline (imblearn atau sklearn)
        if hasattr(model, 'steps'):
            print("Detected Pipeline. Steps:")
            for name, step in model.steps:
                print(f" - {name}: {type(step)}")
            
            # Ambil estimator terakhir
            final_estimator = model.steps[-1][1]
            print(f"Final Estimator: {type(final_estimator)}")
        else:
            print(f"Model: {type(model)}")
            
    except Exception as e:
        print(f"Error loading model: {e}")
        import traceback
        traceback.print_exc()
else:
    print("File DOES NOT exist.")
    print("Files in directory:")
    print(os.listdir('.'))
