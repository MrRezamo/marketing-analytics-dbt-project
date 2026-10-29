CSV_PATH = os.path.join(os.path.dirname(__file__), "data", "online_retail_II.xlsx")
df = pd.read_excel(CSV_PATH, encoding="ISO-8859-1")