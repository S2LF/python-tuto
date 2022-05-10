import os

CUR_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(CUR_DIR, "data")

if __name__ == "__main__":
    print(CUR_DIR)
    print(DATA_DIR)