import pandas as pd
import matplotlib.pyplot as plt

class Analysis:
    def __init__(self, df) -> None:
        self.df = df.copy()

    def average_