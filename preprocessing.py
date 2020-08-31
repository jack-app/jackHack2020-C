import pandas as pd

def preprocessing():
    data = pd.read_csv('data/data.csv')
    row_columns = data.columns
    columns = ['time','age',
           'q1','q2','q3','q4','q5','q6','q7','q8','q9','q10',
           'q11','q12','q13','q14','q15','q16','q17','q18','q19','q20',
           'q21','q22','q23','q24','q25']
    
    column_map = {}
    for i in range(len(columns)):
        if i > 1:
            column_map['q'+str(i-1)] = row_columns[i]
        elif i == 0:
            column_map['time'] = 'time'
        elif i == 1:
            column_map['age'] = 'age'

    data.columns = columns

    data['age'] = [s[:4] for s in data['age']]

    ages = list(set(data['age']))
    pre_data = {}
    for age in ages:
        age_data = data[data['age']==age]
        q_dict = {}
        for q in columns[2:]:
            c_yes = int(age_data[q].sum())
            q_dict[column_map[q]] = [c_yes+1, len(age_data)-c_yes+1]
        pre_data[age] = q_dict

    data['age'] = [str(i) for i in data['age']]

    return pre_data

def main():
    pre_data = preprocessing()
    print(pre_data)

if __name__ == "__main__":
    main()
