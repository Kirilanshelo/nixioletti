import os
import logging
from torchvision.io import read_image
from torchvision.models import efficientnet_v2_l, EfficientNet_V2_L_Weights
import numpy as np
import base64
import torch
from io import BytesIO
from PIL import Image
import re

def do_task(body):
    # select cuda if available
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    log = logging.getLogger('mylib')

    # load image
    img = re.search('base64,(.*)',body.base64).group(1)
    img = Image.open(BytesIO(base64.b64decode(img)))
    img = torch.tensor(np.array(img),dtype=torch.uint8).permute(2,0,1)

    # Initialize model with the best available weights
    weights = EfficientNet_V2_L_Weights.DEFAULT
    model = efficientnet_v2_l(weights=weights).to(device)
    model.eval()

    # Initialize the inference transforms
    preprocess = weights.transforms()

    # Apply inference preprocessing transforms
    batch = preprocess(img).to(device).unsqueeze(0)

    # Use the model and print the predicted category
    with torch.no_grad():
        prediction = model(batch).squeeze(0).softmax(0).cpu()
    class_ids = prediction.topk(3).indices.numpy()
    scores = prediction[class_ids].detach().numpy()
    category_names = np.array(weights.meta["categories"])[class_ids]
    print(f"{category_names[0]}: {100 * scores[0]:.1f}%")
    print(f"{category_names[1]}: {100 * scores[1]:.1f}%")
    print(f"{category_names[2]}: {100 * scores[2]:.1f}%")

    output = {'data': f'{category_names[0]}: {100 * scores[0]:.1f}% {category_names[1]}: {100 * scores[1]:.1f}% {category_names[2]}: {100 * scores[2]:.1f}%'} # sostituire con metodi AI

    log.info(f'ai task done')

    return output
