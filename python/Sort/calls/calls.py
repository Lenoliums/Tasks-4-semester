import pandas as pd

if __name__ == '__main__':
    headersSM = ["Data", "time_s", "A_B", "phone_number"]
    calls = pd.read_csv('./the_calls.txt', names=headersSM, sep='\t', dtype={"time_s": int, "phone_number": str})
    print(calls)
    calls = calls.sort_values(by='time_s', ascending=0).sort_values(by='A_B')
    print(calls)
    calls.to_csv('calls.txt', index=False, header=False, sep='\t')
