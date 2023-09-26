# def checking_parameters(results):
#     data = None
#
#     if len(results) == 10:
#         value_0 = results[0]
#         value_1 = results[1]
#         value_2 = results[2]
#         value_3 = results[3]
#         value_4 = results[4]
#         value_5 = results[5]
#         value_6 = results[6]
#         value_7 = results[7]
#         value_8 = results[8]
#         value_9 = results[9]
#
#         data = {
#             'Термал зона 0': value_0,
#             'Термал зона 1': value_1,
#             'LoadAverages_1': value_2,
#             'LoadAverages_2': value_3,
#             'LoadAverages_3': value_4,
#             'idle': value_5,
#             'Частота CPU в ГГц': value_6,
#             'MemAvailable': value_7,
#             'MemFree': value_8,
#             'Время в секундах': value_9
#         }
#     elif len(results) > 10:
#         for i in range(len(results)):
#
#     return data
# не придумал пока как сделать оптимально и просто