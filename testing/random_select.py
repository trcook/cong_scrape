import random
import os



if __name__ == "__main__":
    # os.rename('./data/plaws.csv', './data/plaws_full.csv')
    with open("./data/plaws_full.csv", "rb") as source:
        lines = [line for line in source]
        random_choice = random.sample(lines, 200)
        source

        with open("./data/plaws.csv", "wb") as sink:
            sink.write("".join(random_choice))
