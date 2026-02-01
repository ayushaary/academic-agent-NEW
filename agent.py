import joblib
import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model = joblib.load(os.path.join(BASE_DIR, "model.pkl"))
features = joblib.load(os.path.join(BASE_DIR, "features.pkl"))

def academic_agent(user_input):

    user_df = pd.DataFrame(user_input, columns=features)

    # XG Boost
    ml_prediction = model.predict(user_df)[0]

    # AGENT
    def reward(df):
        bonus = 0

        if "studytime" in df:
            bonus += df["studytime"].values[0] * 0.4

        if "absences" in df:
            bonus += max(0, 5 - df["absences"].values[0]) * 0.2

        if "health" in df:
            bonus += df["health"].values[0] * 0.2

        return bonus

    # SIMULATION
    def simulate(changes):
        temp = user_df.copy()

        for k, v in changes.items():
            if k in temp:
                temp[k] += v

        return model.predict(temp)[0] + reward(temp)

    actions = [
        ("Study +1", {"studytime": 1}),
        ("Study +2", {"studytime": 2}),
        ("Study +3", {"studytime": 3}),
        ("Absences -3", {"absences": -3}),
        ("Health +1", {"health": 1})
    ]

    scenarios = []

    for name, chg in actions:
        scenarios.append((name, simulate(chg)))

    best_action, best_score = max(scenarios, key=lambda x: x[1])

    optimized_prediction = best_score

    return ml_prediction, optimized_prediction, best_action, scenarios

