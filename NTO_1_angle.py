a = float(input())
time = input()
timeS = time.split()
h = timeS[0]
m = timeS[1]
hr = float(0)
mr = float(0)
hf = hr + 30*float(h) + 0.5*float(m)
mf = mr + 6*float(m)
mff = (360-a)+mf
if mff > 360:
    mff = mff-360
if hf < mff:
    af = hf+(360-mff)
else:
    af = hf-mff   
print(af)
