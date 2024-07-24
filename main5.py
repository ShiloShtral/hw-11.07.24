total_iq_before = 0
count_before = 0

while True:
    iq = float(input("what was your IQ a year before python studies?"))
    if iq < 30 or iq > 300:
        break
    total_iq_before += iq
    count_before += 1

if count_before > 0:
    avg_iq_brfore = total_iq_before / count_before
    print(f"your IQ average before python studies was {avg_iq_brfore}")

print("One year of python studies has ben completed")


total_iq_after = 0
count_after = 0

while True:
    iq = float(input("What was your IQ average a year after python studies?"))
    if iq < 30 or iq > 300:
        break
    total_iq_after += iq
    count_after += 1

if count_after > 0:
    avg_iq_after = total_iq_after / count_after
    print(f"your IQ average after one year of python studies is {avg_iq_after}")

if avg_iq_brfore != avg_iq_after :
    avg_diff = avg_iq_after - avg_iq_brfore
    print(f"the differece in avrage IQ after python studies is {avg_diff}")