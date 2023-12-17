#### Overview

Built a U-net model to predict a label for each pixel for each input image, and in turn the mask for the image.


#### Model

The model takes in images, preprocesses them, by normalising the values to be between 0 and 1. The U-net model consists of an encoder and decoder block. The encoder uses regular CNN to downsample the image and extract features (spatial information) from it. Skip connections are added to retain the information and check overffiting.
The output of the encoder block serves as the input for the decoder block. The skip connections sends information to every upsampling layer, between corresponding encoder and decoder blocks.

Results after training;
<picture>
 <source media="(prefers-color-scheme: dark)" srcset="output.png">
 <source media="(prefers-color-scheme: light)" srcset="output.png">
 <img alt="Sample image showing the actual mask and the predicted mask" src="output.png">
</picture>


<picture>
 <source media="(prefers-color-scheme: dark)" srcset="1output.png">
 <source media="(prefers-color-scheme: light)" srcset="1output.png">
 <img alt="Sample image showing the actual mask and the predicted mask" src="1output.png">
</picture>


<div align="center">
<a href="https://dev.to/andreygermanov/a-practical-introduction-to-object-detection-with-yolov8-neural-network-3n8c">
    <img src="output.png"/>
</a>
</div>


<div align="center">
<a href="https://dev.to/andreygermanov/a-practical-introduction-to-object-detection-with-yolov8-neural-network-3n8c">
    <img src="1output.png"/>
</a>
</div>


![Sample image showing the actual mask and the predicted mask.](output.png)


![Sample image showing the actual mask and the predicted mask.](1output.png)
