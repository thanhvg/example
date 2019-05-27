from queries import (get_object_list, get_classification_setttings,
                     get_alarm_log, update_alam_log, get_alarm_object,
                     set_classification_state)


    decoded_str = json.loads(nf.payload)
    decoded_dict = json.loads(decoded_str)
