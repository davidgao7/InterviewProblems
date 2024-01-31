def print_classification(raw_data):
    # Write your code here

    import pandas as pd
    import numpy as np

    data = pd.DataFrame(
        np.array(raw_data), columns=["races_id", "racer_id", "position"]
    )
    score_map = {
        1: 10,  # 1st
        2: 6,  # 2nd
        3: 4,  # 3rd
        4: 3,  # 4th
        5: 2,  # 5th
        6: 1  # 6th
        # other position: 0 points
    }
    data['score_pre'] = data["position"].map(score_map)
    result =pd.DataFrame(data.groupby("racer_id")['score_pre'].sum().sort_values(ascending=False)).reset_index()

    print(result.iloc[0]['racer_id'], result.iloc[0]['score_pre'])


if __name__ == "__main__":
    raw_data = [
        [2001, 1001, 3],
        [2001, 1002, 2],
        [2002, 1003, 1],
        [2002, 1001, 2],
        [2002, 1002, 3],
        [2001, 1003, 1],
    ]
    print(print_classification(raw_data))
