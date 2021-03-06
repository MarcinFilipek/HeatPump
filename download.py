import psycopg2 as psg
from database.config import config
from pypika import Table
from pypika import PostgreSQLQuery as Query
import pandas as pd


def download():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        params = config()
        print('Connecting to the PostgreSQL database...')
        conn = psg.connect(**params)
        cur = conn.cursor()
        print('Download data...')
        date_list = generate_date("2020-02-26", pd.datetime.now())

        for date in date_list:
            table = Table('public.pompy_ciepla')
            time = "time::date = '{}'".format(date.date())
            q = Query.from_(table).select('*')
            print(q.get_sql(quote_char=None) + " WHERE " + time)
            cur.execute(q.get_sql(quote_char=None) + " WHERE " + time)

            number_of_row = cur.rowcount
            rows_list = []
            for i in range(number_of_row):
                row = cur.fetchone()
                if row[3] is not None:
                    for element in row[3]:
                        key, value = element.popitem()
                        insert = {'id_module': row[1], 'id_status': key, 'value': value, 'time': row[2]}
                        rows_list.append(insert)
            if number_of_row > 0:
                save_to_csv(rows_list, date.date())

        cur.close()
        print('Success.')
    except (Exception, psg.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


def save_to_csv(list, date):
    df_statuses = pd.DataFrame(list, columns=['id_module',
                                              'id_status',
                                              'value',
                                              'time'])
    df_statuses.to_csv('data/{}.csv'.format(date), index=False)


def generate_date(start, end):
    date_list = pd.date_range(start=start, end=end).tolist()
    return date_list


if __name__ == '__main__':
    download()
