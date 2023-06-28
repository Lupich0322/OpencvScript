from cnocr import CnOcr
ocr = CnOcr()
res = ocr.ocr('trainingImages/111.PNG')
print("Predicted Chars:", res)
