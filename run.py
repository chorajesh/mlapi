from flask import Flask
import requests
import tensorflow as tf
import tensorflow_hub as hub

app = Flask(__name__)


@app.route('/predict', methods=['GET'])
def hello_world():
    reloaded = tf.keras.models.load_model(
        "./samplemodel.h5",
        # `custom_objects` tells keras how to load a `hub.KerasLayer`
        custom_objects={'KerasLayer': hub.KerasLayer})
    print(reloaded.summary())
    output = reloaded.predict([32])
    print("Output is ",output[0])
    str1 = " "
    print(str1.join(str(output[0])))
    return "The output value based on the equation : 9*x+3 = " + str(output[0][0])


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
