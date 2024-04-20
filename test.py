import json
import jpype
import pandas as pd

df = pd.read_csv("csvjson.json")
df.to_excel("temp.xlsx",index = False)

jpype.startJVM(jpype.getDefaultJVMPath())

from asposecells.api import Workbook

workbook = Workbook("temp.xlsx")

workbook.save("Output.pdf",SaveFormat.PDF)
jpype.shutdownJVM()