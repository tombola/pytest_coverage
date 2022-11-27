from dataclasses import dataclass


@dataclass
class Patient:
    age: int
    is_pregnant: bool = False
    is_regular_blood_donor: bool = False


def determine_queue_position(patient, queue):
    # initially, we assume that a patient will just join queue
    position = len(queue)

    # there are certain groups of patients that are served without
    # having to wait in a queue
    if patient.is_pregnant or patient.is_regular_blood_donor:
        position = 0

    return position
