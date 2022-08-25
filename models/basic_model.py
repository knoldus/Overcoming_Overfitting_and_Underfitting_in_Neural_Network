from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import MaxPooling2D
from tensorflow.keras.layers.experimental.preprocessing import Rescaling

from data.load_data import data
def base_model():
    X_train, y_train, X_test, y_test = data()
    model = Sequential([
        Rescaling(1. / 255, input_shape=(32, 32, 3)),
        Conv2D(32, 3, padding="same", activation="relu"),
        Conv2D(32, 3, padding="same", activation="relu"),
        MaxPooling2D(pool_size=(2, 2)),
        Conv2D(64, 3, padding="same", activation="relu"),
        Conv2D(64, 3, padding="same", activation="relu"),
        MaxPooling2D(pool_size=(2, 2)),
        Flatten(),
        Dense(256, activation="relu"),
        Dense(10, activation="softmax")
    ])

    model.compile(
        optimizer="Adam",
        loss="sparse_categorical_crossentropy",
        metrics=["accuracy"],
    )

    epochs = 30

    history = model.fit(
        X_train, y_train,
        validation_data=(X_test, y_test),
        epochs=epochs,
        batch_size=64,
    )
    return history, epochs

if __name__ == "__main__":
    base_model()