from .. import example2
from ..patients_example import Patient, determine_queue_position


def test_pregnancy_means_accessing_doctor_without_having_to_wait():
    queue = [Patient(age=25), Patient(age=44)]
    patient = Patient(age=28, is_pregnant=True)

    queue_position = determine_queue_position(patient, queue)

    assert queue_position == 0


def test_some_function_a():
    example2.some_function_a("arbitrary string.")
    example2.some_function_a("arbitrary string")
    example2.some_function_a("")
    example2.some_function_b()
    # pass
