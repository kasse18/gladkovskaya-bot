from aiogram.fsm.state import State, StatesGroup


class TestStates(StatesGroup):
    waiting_for_topic = State()
    asking_question_1 = State()
    asking_question_2 = State()
    asking_question_3 = State()
    asking_question_4 = State()
    asking_question_5 = State()