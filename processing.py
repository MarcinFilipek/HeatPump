import pandas as pd
from pompa_ciepla import HeatPump
from emodul.values.temperature_sensor import TemperatureSensor
import matplotlib.pyplot as plt
import datetime

id_module = 10865
date = '2019-10-27'
parameters = ('TC_OUTSIDE_TEMP', 'TC_EVD_PROBE_S1_READING', 'TC_COMPRESSED_GAS_TEMP')
# parameters = HeatPump.sensor.keys()


def get_value(row):
    return TemperatureSensor(row['value']).value()/10


path = 'data/{}.csv'.format(date)
day_data = pd.read_csv(path)
module_data = day_data[day_data['id_module'] == id_module]
module_data['time'] = module_data['time'].apply(
    lambda time: datetime.datetime.strptime(time, '%Y-%m-%d %H:%M:%S.%f').replace(microsecond=0).time())
module_data = module_data.sort_values(by=['time'])


module_data[module_data['id_status'] == HeatPump.sensor['TC_COMPRESSED_GAS_TEMP']].to_csv('temp.csv')

fig, ax = plt.subplots(len(parameters), figsize=(20, 25))
fig.suptitle('{}'.format(date))
for i, parameter in enumerate(parameters):
    id_parameter = HeatPump.sensor[parameter]
    parameter_data = module_data.loc[module_data['id_status'] == id_parameter]
    parameter_data[parameter] = parameter_data.apply(lambda row: get_value(row), axis=1)
    ax[i].plot(parameter_data['time'], parameter_data[parameter], label=parameter)
    ax[i].xaxis.set_major_locator(plt.MultipleLocator(60 * 60 * 1))
    ax[i].legend()

# plt.savefig('{}.pdf'.format(date), format='pdf')
plt.show()
