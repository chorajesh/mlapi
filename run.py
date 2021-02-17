from flask import Flask, request
import requests
import tensorflow as tf
import tensorflow_hub as hub

app = Flask(__name__)


@app.route('/predict', methods=['GET'])
def hello_world():

    xval = request.args.get('xvalue')
    print(type(xval))
    try:
        x = float(xval)
        print("Received x value is : ", x)
        output = predictyval(x)
    except:
        output = "Please input only numerical values."
    return output


def predictyval(x=0):
    reloaded = tf.keras.models.load_model(
        "./samplemodel.h5",
        # `custom_objects` tells keras how to load a `hub.KerasLayer`
        custom_objects={'KerasLayer': hub.KerasLayer})
    print(reloaded.summary())
    predited = reloaded.predict([x])
    print("Output is ", predited[0])
    str1 = " "
    print(str1.join(str(predited[0])))
    output = "The output value based on the equation : 9*x+3 (This equation was derived by the model). Refer build_ml_save.py file. = " + str(
        predited[0][0])
    return output

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
