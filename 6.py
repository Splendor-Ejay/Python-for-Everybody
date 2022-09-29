text = "X-DSPAM-Confidence:    0.8475"
num = text.find('0')
print (float(text[num:num+6]))
