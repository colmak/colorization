import cv2
import numpy as np

def colorize_image(input_image_path, output_image_path):
    # Load the black and white image
    bw_image = cv2.imread(input_image_path, cv2.IMREAD_GRAYSCALE)
    bw_image = cv2.cvtColor(bw_image, cv2.COLOR_GRAY2RGB)

    # Load the pre-trained model
    prototxt_path = 'colorization_deploy_v2.prototxt'
    model_path = 'colorization_release_v2.caffemodel'
    net = cv2.dnn.readNetFromCaffe(prototxt_path, model_path)
    
    # Load the cluster centers
    pts_path = 'pts_in_hull.npy'
    pts = np.load(pts_path)

    # Add the cluster centers as 1x1 convolutions to the model
    class8 = net.getLayerId('class8_ab')
    conv8 = net.getLayerId('conv8_313_rh')
    pts = pts.transpose().reshape(2, 313, 1, 1)
    net.getLayer(class8).blobs = [pts.astype(np.float32)]
    net.getLayer(conv8).blobs = [np.full([1, 313], 2.606, dtype=np.float32)]

    # Convert the image to the required input format
    h, w, _ = bw_image.shape
    img_rgb = (bw_image / 255.0).astype(np.float32)
    img_lab = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2Lab)
    l_channel = img_lab[:, :, 0]
    l_channel -= 50

    # Predict the ab channels
    net.setInput(cv2.dnn.blobFromImage(l_channel))
    ab_channels = net.forward()[0, :, :, :].transpose((1, 2, 0))

    # Resize the ab channels to match the original image size
    ab_channels = cv2.resize(ab_channels, (w, h))

    # Combine the L channel with the predicted ab channels
    img_lab = np.concatenate((l_channel[:, :, np.newaxis], ab_channels), axis=2)

    # Convert back to RGB
    colorized_image = cv2.cvtColor(img_lab, cv2.COLOR_Lab2RGB)
    colorized_image = (colorized_image * 255).astype(np.uint8)

    # Save the colorized image
    cv2.imwrite(output_image_path, colorized_image)

# Example usage
input_path = "bw_image.jpg"
output_path = "color_image.jpg"
colorize_image(input_path, output_path)