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
        date_list = generate_date("2020-01-12", pd.datetime.now())

        for date in date_list:
            table = Table('public.alarmy')
            time = "message_time::date = '{}'".format(date.date())
            q = Query.from_(table).select('*')
            cur.execute(q.get_sql(quote_char=None) + " WHERE " + time)

            number_of_row = cur.rowcount
            rows_list = []
            for i in range(number_of_row):
                row = cur.fetchone()
                columns = ['id_module',
                           'row_data',
                           'message_time',
                           'message_head',
                           'message_body']
                insert = dict(zip(columns, row[1:]))
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
                                              'row_data',
                                              'message_time',
                                              'message_head',
                                              'message_body'])
    df_statuses.to_csv('data/{}_alarms.csv'.format(date), index=False)


def generate_date(start, end):
    date_list = pd.date_range(start=start, end=end).tolist()
    return date_list


if __name__ == '__main__':
    download()
