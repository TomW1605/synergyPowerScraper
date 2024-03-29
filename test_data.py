from datetime import datetime

usage_data = {'chartType': 'ELEC', 'startDate': '2024-02-04', 'endDate': '2024-02-05', 'numberOfDays': 0,
              'responseCode': [], 'contractKwLimit': 0.0, 'contractKvaLimit': 0.0, 'contractPowerFactorLimit': 0.0,
              'peakKwhHalfHourlyValues': [None, None, None, None, None, None, None, None, None, None, None, None, None,
                                          None, None, None, None, None, None, None, None, None, None, None, None, None,
                                          None, None, None, None, None, None, None, None, None, None, None, None, None,
                                          None, None, None, None, None, None, None, None, None],
              'offpeakKwhHalfHourlyValues': [0.5379999876022339, 0.6840000152587891, 0.6439999938011169,
                                             0.597000002861023, 0.5490000247955322, 0.5139999985694885,
                                             0.49000000953674316, 0.5379999876022339, 0.4869999885559082,
                                             0.5649999976158142, 0.46299999952316284, 0.43299999833106995,
                                             0.4399999976158142, 0.3799999952316284, 0.38600000739097595,
                                             0.0689999982714653, 0, 0, 0.0010000000474974513, 0.11100000143051147,
                                             0.21699999272823334, 0, 0.06499999761581421, 0.003000000026077032,
                                             0.0010000000474974513, 0, 0, 0.010999999940395355, 0, 0,
                                             0.006000000052154064, 0.16200000047683716, 0.0010000000474974513,
                                             0.0010000000474974513, 0, 0.029999999329447746, 0.164000004529953,
                                             0.40299999713897705, 0.5669999718666077, 0.5960000157356262,
                                             0.6729999780654907, 0.6700000166893005, 0.7279999852180481,
                                             0.6779999732971191, 0.6579999923706055, 0.6269999742507935,
                                             0.5289999842643738, 0.5049999952316284],
              'kwHalfHourlyValues': [1.0759999752044678, 1.3680000305175781, 1.2879999876022339, 1.194000005722046,
                                     1.0980000495910645, 1.027999997138977, 0.9800000190734863, 1.0759999752044678,
                                     0.9739999771118164, 1.1299999952316284, 0.9259999990463257, 0.8659999966621399,
                                     0.8799999952316284, 0.7599999904632568, 0.7720000147819519, 0.1379999965429306,
                                     None, None, 0.0020000000949949026, 0.22200000286102295, 0.4339999854564667, None,
                                     0.12999999523162842, 0.006000000052154064, 0.0020000000949949026, None, None,
                                     0.02199999988079071, None, None, 0.012000000104308128, 0.3240000009536743,
                                     0.0020000000949949026, 0.0020000000949949026, None, 0.05999999865889549,
                                     0.328000009059906, 0.8059999942779541, 1.1339999437332153, 1.1920000314712524,
                                     1.3459999561309814, 1.340000033378601, 1.4559999704360962, 1.3559999465942383,
                                     1.315999984741211, 1.253999948501587, 1.0579999685287476, 1.0099999904632568],
              'kvaHalfHourlyValues': [1.0759999752044678, 1.3680000305175781, 1.2879999876022339, 1.194000005722046,
                                      1.0980000495910645, 1.027999997138977, 0.9800000190734863, 1.0759999752044678,
                                      0.9739999771118164, 1.1299999952316284, 0.9259999990463257, 0.8659999966621399,
                                      0.8799999952316284, 0.7599999904632568, 0.7720000147819519, 0.1379999965429306,
                                      None, None, 0.01600000075995922, 0.22200000286102295, 0.4339999854564667, None,
                                      0.12999999523162842, 0.012000000104308128, 0.006000000052154064, None, None,
                                      0.024000000208616257, None, None, 0.012000000104308128, 0.3240000009536743,
                                      0.0020000000949949026, 0.0020000000949949026, None, 0.05999999865889549,
                                      0.328000009059906, 0.8059999942779541, 1.1339999437332153, 1.1920000314712524,
                                      1.3459999561309814, 1.340000033378601, 1.4559999704360962, 1.3559999465942383,
                                      1.315999984741211, 1.253999948501587, 1.0579999685287476, 1.0099999904632568],
              'powerFactorHalfHourlyValues': [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
                                              1.0, 0, 0, 0.125, 1.0, 1.0, 0, 1.0, 0.5, 0.333, 0, 0, 0.917, 0, 0, 1.0,
                                              1.0, 1.0, 1.0, 0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
                                              1.0, 1.0],
              'loadFactorHalfHourlyValues': [0.435, 0.435, 0.435, 0.435, 0.435, 0.435, 0.435, 0.435, 0.435, 0.435,
                                             0.435, 0.435, 0.435, 0.435, 0.435, 0.435, 0.435, 0.435, 0.435, 0.435,
                                             0.435, 0.435, 0.435, 0.435, 0.435, 0.435, 0.435, 0.435, 0.435, 0.435,
                                             0.435, 0.435, 0.435, 0.435, 0.435, 0.435, 0.435, 0.435, 0.435, 0.435,
                                             0.435, 0.435, 0.435, 0.435, 0.435, 0.435, 0.435, 0.435],
              'statusCodeHalfHourlyValues': ['Actual', 'Actual', 'Actual', 'Actual', 'Actual', 'Actual', 'Actual',
                                             'Actual', 'Actual', 'Actual', 'Actual', 'Actual', 'Actual', 'Actual',
                                             'Actual', 'Actual', 'Actual', 'Actual', 'Actual', 'Actual', 'Actual',
                                             'Actual', 'Actual', 'Actual', 'Actual', 'Actual', 'Actual', 'Actual',
                                             'Actual', 'Actual', 'Actual', 'Actual', 'Actual', 'Actual', 'Actual',
                                             'Actual', 'Actual', 'Actual', 'Actual', 'Actual', 'Actual', 'Actual',
                                             'Actual', 'Actual', 'Actual', 'Actual', 'Actual', 'Actual'],
              'hasValue': True,
              'kwhHalfHourlyValuesGeneration': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0989999994635582,
                                                0.382999986410141, 0.6470000147819519, 1.0140000581741333,
                                                0.9929999709129333, 0.31700000166893005, 1.4079999923706055,
                                                1.2300000190734863, 1.4739999771118164, 1.6799999475479126,
                                                1.5889999866485596, 1.6799999475479126, 1.2860000133514404,
                                                1.6030000448226929, 1.4140000343322754, 1.00600004196167,
                                                0.7910000085830688, 0.8579999804496765, 0.7990000247955322,
                                                0.4429999887943268, 0.03799999877810478, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                                0, 0], 'kwhDailyValuesGeneration': [20.75200003758073],
              'weekdayShoulderKwhHalfHourlyValues': [None, None, None, None, None, None, None, None, None, None, None,
                                                     None, None, None, None, None, None, None, None, None, None, None,
                                                     None, None, None, None, None, None, None, None, None, None, None,
                                                     None, None, None, None, None, None, None, None, None, None, None,
                                                     None, None, None, None], 'weekdayShoulderKwhDailyValues': [0],
              'weekendShoulderKwhHalfHourlyValues': [None, None, None, None, None, None, None, None, None, None, None,
                                                     None, None, None, None, None, None, None, None, None, None, None,
                                                     None, None, None, None, None, None, None, None, None, None, None,
                                                     None, None, None, None, None, None, None, None, None, None, None,
                                                     None, None, None, None], 'weekendShoulderKwhDailyValues': [0],
              'unbilledStartDate': None,
              'timestamps': ['2024-02-04T00:00', '2024-02-04T00:30', '2024-02-04T01:00', '2024-02-04T01:30',
                             '2024-02-04T02:00', '2024-02-04T02:30', '2024-02-04T03:00', '2024-02-04T03:30',
                             '2024-02-04T04:00', '2024-02-04T04:30', '2024-02-04T05:00', '2024-02-04T05:30',
                             '2024-02-04T06:00', '2024-02-04T06:30', '2024-02-04T07:00', '2024-02-04T07:30',
                             '2024-02-04T08:00', '2024-02-04T08:30', '2024-02-04T09:00', '2024-02-04T09:30',
                             '2024-02-04T10:00', '2024-02-04T10:30', '2024-02-04T11:00', '2024-02-04T11:30',
                             '2024-02-04T12:00', '2024-02-04T12:30', '2024-02-04T13:00', '2024-02-04T13:30',
                             '2024-02-04T14:00', '2024-02-04T14:30', '2024-02-04T15:00', '2024-02-04T15:30',
                             '2024-02-04T16:00', '2024-02-04T16:30', '2024-02-04T17:00', '2024-02-04T17:30',
                             '2024-02-04T18:00', '2024-02-04T18:30', '2024-02-04T19:00', '2024-02-04T19:30',
                             '2024-02-04T20:00', '2024-02-04T20:30', '2024-02-04T21:00', '2024-02-04T21:30',
                             '2024-02-04T22:00', '2024-02-04T22:30', '2024-02-04T23:00', '2024-02-04T23:30']}

usage_data['timestamps'] = [datetime.strptime(timestamp, '%Y-%m-%dT%H:%M') for timestamp in usage_data['timestamps']]
