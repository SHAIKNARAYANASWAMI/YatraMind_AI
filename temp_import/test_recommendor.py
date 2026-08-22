import pandas as pd
import importlib.util

p = r"C:\Users\Sk Narayana Swami\OneDrive\Documents\Desktop\project\YatraMind_AI\Streamlit Website\hotel_dataframe.pkl"
df = pd.read_pickle(p)

spec = importlib.util.spec_from_file_location("recommendor", r"C:\Users\Sk Narayana Swami\OneDrive\Documents\Desktop\project\YatraMind_AI\Streamlit Website\recommendor.py")
recommendor = importlib.util.module_from_spec(spec)
spec.loader.exec_module(recommendor)

city = "Hyderabad"
features = "pool parking family breakfast"
price = 4500

print('DATAFRAME SHAPE:', df.shape)
res = recommendor.recommendor(city, features, price, df)
print('\n=== RECOMMENDER OUTPUT ===')
if res is None:
    print('No results returned')
else:
    try:
        print(res.to_string(index=False))
    except Exception:
        print(res)
