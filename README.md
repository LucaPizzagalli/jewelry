# jewelry
simple page for a ecommerce

The problem with object dethection is that you don't know the lenght of your output (and you need to find the boxes *and* the classes).

### R-CNN

In 2013 an algorithm was proposed for doing object detection.
We start with some sort of image segmentation, based on color, shape, or something.
Then we combine these regions with their neighbour regions, finding many combynations, around 2000.
(Let's notice that so fare there is no learning, this is just a fixed algorithm)
Each of these regions is wrapped in a square, passed through a cnn, a fully connected layer, and finally, surprise, a SVM for classification and a linear regressor for shift in the bounding box.

This algorithm is very slow and takes around 40 seconds for a single image.

### Fast R_CNN

In 2015 the same author proposed a faster version of R-CNN.
This time we start with a convolutional layer that produces a "feature map".
Only then we do the region proposal; this way the CNN is run only once.
When we have the regions in the features space we use a fully connected NN and again SVM and liner regressor for classification and bounding box. <- NO
