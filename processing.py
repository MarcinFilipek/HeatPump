import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
from pompa_ciepla import HeatPump
from emodul.values.base_value import BaseValue
from emodul.values.temperature_sensor import TemperatureSensor
from emodul.values.relay_value import RelayValue
from emodul.values.universal_value import UniversalValue

id_module = 10865
date = '2019-10-17'
time_start = "00:00:00"
time_end = "23:59:59"
parameters = ('TC_EVI_STATE', 'TC_DHW_TEMP', 'TC_COMPRESSED_GAS_TEMP')


def get_time_from_string_full_date(date):
    """
    Convert string full date to time
    :param date: date in format "Y-m-d H:M:S.f"
    :return: object datetime.time H:M:S
    """
    return datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%f').replace(microsecond=0).time()


def get_value(row):
    if row['type'] == 1:
        return TemperatureSensor(row['value']).value()/10
    elif row['type'] == 6:
        return UniversalValue(row['value']).value2()
    elif row['type'] == 11:
        return RelayValue(row['value']).value()
    else:
        return 0


path = 'data/{}.csv'.format(date)
time_start = datetime.strptime(time_start, '%H:%M:%S').time()
time_end = datetime.strptime(time_end, '%H:%M:%S').time()

day_data = pd.read_csv(path)
module_data = day_data[day_data['id_module'] == id_module]
module_data = module_data.drop(['id_module'], axis=1)
module_data['time'] = module_data['time'].apply(lambda time: get_time_from_string_full_date(time))
module_data = module_data.sort_values(by=['time'])
module_data = module_data[(module_data['time'] > time_start) & (module_data['time'] < time_end)]
module_data['type'] = module_data['value'].apply(lambda value: BaseValue(value).get_type())

fig, ax = plt.subplots(len(parameters), figsize=(20, 25))
fig.suptitle('{}'.format(date))
for i, parameter in enumerate(parameters):
    id_parameter = HeatPump.sensor[parameter]
    parameter_data = module_data.loc[module_data['id_status'] == id_parameter]
    parameter_data[parameter] = parameter_data.apply(lambda row: get_value(row), axis=1)
    ax[i].plot(parameter_data['time'], parameter_data[parameter], label=parameter)
    ax[i].xaxis.set_major_locator(plt.MultipleLocator(60 * 60 * 1))
    ax[i].legend()
plt.show()
