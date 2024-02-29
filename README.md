# FastAPI template

### ML Models
Image Detection Model used:

- [Weights](https://pytorch.org/vision/stable/models/generated/torchvision.models.efficientnet_v2_l.html#torchvision.models.EfficientNet_V2_L_Weights)

- [Paper](https://arxiv.org/pdf/2104.00298.pdf)

### Dev
Create python env and then install dependencies
```
pip install -r requirements.txt
```

Run from `src` folder with

- Self-hosted run mode
```
python main.py
```

- Hosted run mode
```
uvicorn main:app --reload --host 0.0.0.0 --port 9006
```

### Docker
Tweak `docker-compose.yml` according to your setup and run
```
docker compose --project-name "template-fastapi" up --build -d
```

