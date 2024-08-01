import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import json

def load_data_from_json(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    # Position of the prime
    celsius = np.array([item['n'] for item in data], dtype=float)
    # Prime in that position
    fahrenheit = np.array([item['pn'] for item in data], dtype=float)
    return celsius, fahrenheit

def main():
    # Your TensorFlow code here
    celsius, fahrenheit = load_data_from_json('data.json')
    oculta1 = tf.keras.layers.Dense(units=11, input_shape=[1])
    #oculta3 = tf.keras.layers.Dense(units=11)
    #oculta2 = tf.keras.layers.Dense(units=11)
    salida = tf.keras.layers.Dense(units=1)
    modelo = tf.keras.Sequential([oculta1, salida])
    modelo.compile(
        optimizer=tf.keras.optimizers.Adam(0.1),
        loss="mean_squared_error"
    )
    print("Start training")
    historial = modelo.fit(celsius, fahrenheit, epochs=137, verbose=False)
    print("Finished training with all primes up to a million")
    plt.xlabel("# Epoch")
    plt.ylabel("Loss")
    plt.plot(historial.history["loss"])
    plt.savefig('/app/output/plot.png')
    test_input = np.array([78499.0])  # Test input data to find the prime number 15000
    resultado = modelo.predict(test_input)
    print("The predicted next prime (p(78499)) is " + str(resultado[0][0]) + " actual value is 1000003")
    modelo.save('/app/output/model.keras')

if __name__ == "__main__":
    main()

