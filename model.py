from ultralytics import YOLO

# Build a model
model = YOLO("yolov8n.yaml")  

# Train the model
results = model.train(data="config.yaml", epochs=5)  # train the model
