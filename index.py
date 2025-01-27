import pandas as pd
import dask.dataframe as dd


def top_products_by_revenue(file_name):
    try:
        data=dd.read_csv(file_name)
        data=data.dropna(subset=['quantity ordered', 'price each'])
        data['quantity ordered']=pd.to_numeric(data['quantity ordered'],errors='coerce')
        data['price each']=pd.to_numeric(data['price each'],errors='coerce')
        data['Revenue']=data['quantity ordered']*data['price each']
        revenue_by_product=data.groupby('product')['Revenue'].sum().reset_index()
        top_products=revenue_by_product.sort_values(by='Revenue',ascending=False).head(5)
        print(top_products)
        return top_products

    except FileNotFoundError:
        print("File not found ")
    except Exception as e:
        print(e)



file_name='dataset.csv'
top_5_products=top_products_by_revenue(file_name)
