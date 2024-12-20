# Forest  Fires Industrial Mathematics

## Image Processing Pipeline.

One of the features we've implemented is to allow you to take a screenshot from an effected area and evolve our fire model.

Head over to this link <a href="https://www.google.com/maps/d/viewer?mid=1OpMoz-v9iOYinQPbBzzx_lBT0QO8h-8&ll=-37.38159633507727%2C148.62546596105895&z=10" target="_blank">Forest Fires</a> and take a screenshot of an area.

here's an example of a good candidate:

<p align="center">
  <img src="image_processing/app/src/image.png"  width="400"/>
</p>

The processing pipeline saves the processed image to `'processed.png'` and generates a `grid.npy` for further modelling.

### Usage

1. Place screenshot in `app -> src` and label it `'image.png'`
2. Run `image_processor.py`
3. View your results in `app -> results`.

### Example

Running our image processing pipeline on the sample image shown above gives us the following result:

<p align="center" >
  <img src="image_processing/app/results/processed.png" width=400/>
</p>