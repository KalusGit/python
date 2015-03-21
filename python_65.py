text = "X-DSPAM-Confidence:    0.8475";
start = text.find(":")
string_number = text[start+1:]
number = string_number.strip()
number = float(number)
print number
