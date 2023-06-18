from cnocr import CnOcr
ocr = CnOcr()
res = ocr.ocr('trainingImages/Snipaste_2023-06-18_11-58-09.PNG')
print("Predicted Chars:", res)
