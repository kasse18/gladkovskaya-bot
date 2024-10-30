import os
from aiogram import types, Router, F
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram.types import FSInputFile
from bot.states.userstate import TestStates
from bot.utils.dicts import *

router = Router()
word_list = ['В главное меню']


@router.message((F.text == "Теория"), StateFilter(None))
@router.message(F.text, StateFilter(None), Command("theory"))
async def theory(message: Message, state: FSMContext):
    await message.answer(
        text="Выберите тему:",
        reply_markup=theory_kb()
    )


@router.callback_query(F.data == 'tax')
async def tax(call: CallbackQuery, state: FSMContext):
    await call.answer()
    input_file = FSInputFile(os.path.abspath("")+f'/theory_photos/{call.data}.jpg')

    await call.message.delete()

    await call.message.answer_photo(
        photo=input_file,
        reply_markup=back_kb(),
        disable_web_page_preview=True
    )


@router.callback_query(F.data == 'ensurance')
async def ensurance(call: CallbackQuery, state: FSMContext):
    await call.answer()

    input_file = FSInputFile(os.path.abspath("")+f'/theory_photos/{call.data}.jpg')

    await call.message.delete()

    await call.message.answer_photo(
        photo=input_file,
        reply_markup=back_kb(),
        disable_web_page_preview=True
    )


@router.callback_query(F.data == 'budget')
async def budget(call: CallbackQuery, state: FSMContext):
    await call.answer()

    input_file = FSInputFile(os.path.abspath("")+f'/theory_photos/{call.data}.jpg')

    await call.message.delete()

    await call.message.answer_photo(
        photo=input_file,
        reply_markup=back_kb(),
        disable_web_page_preview=True
    )


@router.callback_query(F.data == 'crypto')
async def crypto(call: CallbackQuery, state: FSMContext):
    await call.answer()

    input_file = FSInputFile(os.path.abspath("")+f'/theory_photos/{call.data}.jpg')

    await call.message.delete()

    await call.message.answer_photo(
        photo=input_file,
        reply_markup=back_kb(),
        disable_web_page_preview=True
    )


@router.callback_query(F.data == 'card')
async def card(call: CallbackQuery, state: FSMContext):
    await call.answer()

    input_file = FSInputFile(os.path.abspath("")+f'/theory_photos/{call.data}.jpg')

    await call.message.delete()

    await call.message.answer_photo(
        photo=input_file,
        reply_markup=back_kb(),
        disable_web_page_preview=True
    )


@router.callback_query(F.data == 'money')
async def money(call: CallbackQuery, state: FSMContext):
    await call.answer()

    input_file = FSInputFile(os.path.abspath("")+f'/theory_photos/{call.data}.jpg')

    await call.message.delete()

    await call.message.answer_photo(
        photo=input_file,
        reply_markup=back_kb(),
        disable_web_page_preview=True
    )


@router.callback_query(F.data == 'credit')
async def credit(call: CallbackQuery, state: FSMContext):
    await call.answer()

    input_file = FSInputFile(os.path.abspath("")+f'/theory_photos/{call.data}.jpg')

    await call.message.delete()

    await call.message.answer_photo(
        photo=input_file,
        reply_markup=back_kb(),
        disable_web_page_preview=True
    )


@router.callback_query(F.data == 'back')
async def back(call: CallbackQuery, state: FSMContext):
    await call.answer()

    await call.message.delete()

    await call.message.answer(
        "Выберите что-нить",
        reply_markup=start_kb,
        disable_web_page_preview=True
    )


@router.message((F.text == "Тесты"), StateFilter(None))
@router.message(F.text, StateFilter(None), Command("test"))
async def test(message: Message, state: FSMContext):
    await state.set_state(TestStates.waiting_for_topic)
    await message.answer(
        text="Выберите тему:",
        reply_markup=test_kb()
    )


@router.callback_query(F.data == "tax_test")
@router.message(StateFilter(TestStates.waiting_for_topic))
async def tax_test(call: types.CallbackQuery, state: FSMContext):
    await state.update_data({"topic": "tax"})
    await state.update_data({"correct": 0})
    data = await state.get_data()
    await state.set_state(TestStates.asking_question_1)
    await call.answer()
    await call.message.answer(f"Вопрос 1 по теме Налогообложение:\n\n{questions[data["topic"]][0]}",
                              reply_markup=tax1_kb,
                              resize_keyboard=True)


@router.callback_query(F.data == "ensurance_test")
@router.message(StateFilter(TestStates.waiting_for_topic))
async def tax_test(call: types.CallbackQuery, state: FSMContext):
    await state.update_data({"topic": "ensurance"})
    await state.update_data({"correct": 0})
    data = await state.get_data()
    await state.set_state(TestStates.asking_question_1)
    await call.answer()
    await call.message.answer(f"Вопрос 1 по теме Страхование:\n\n{questions[data["topic"]][0]}",
                              reply_markup=ensurance1_kb,
                              resize_keyboard=True)


@router.callback_query(F.data == "budget_test")
@router.message(StateFilter(TestStates.waiting_for_topic))
async def tax_test(call: types.CallbackQuery, state: FSMContext):
    await state.update_data({"topic": "budget"})
    await state.update_data({"correct": 0})
    data = await state.get_data()
    await state.set_state(TestStates.asking_question_1)
    await call.answer()
    await call.message.answer(f"Вопрос 1 по теме Бюджет:\n\n{questions[data["topic"]][0]}",
                              reply_markup=budget1_kb,
                              resize_keyboard=True)


@router.callback_query(F.data == "crypto_test")
@router.message(StateFilter(TestStates.waiting_for_topic))
async def tax_test(call: types.CallbackQuery, state: FSMContext):
    await state.update_data({"topic": "crypto"})
    await state.update_data({"correct": 0})
    data = await state.get_data()
    await state.set_state(TestStates.asking_question_1)
    await call.answer()
    await call.message.answer(f"Вопрос 1 по теме Криптовалюта:\n\n{questions[data["topic"]][0]}",
                              reply_markup=crypto1_kb,
                              resize_keyboard=True)


@router.callback_query(F.data == "card_test")
@router.message(StateFilter(TestStates.waiting_for_topic))
async def tax_test(call: types.CallbackQuery, state: FSMContext):
    await state.update_data({"topic": "card"})
    await state.update_data({"correct": 0})
    data = await state.get_data()
    await state.set_state(TestStates.asking_question_1)
    await call.answer()
    await call.message.answer(f"Вопрос 1 по тебе Банковская карта:\n\n{questions[data["topic"]][0]}",
                              reply_markup=card1_kb,
                              resize_keyboard=True)


@router.callback_query(F.data == "money_test")
@router.message(StateFilter(TestStates.waiting_for_topic))
async def tax_test(call: types.CallbackQuery, state: FSMContext):
    await state.update_data({"topic": "money"})
    await state.update_data({"correct": 0})
    data = await state.get_data()
    await state.set_state(TestStates.asking_question_1)
    await call.answer()
    await call.message.answer(f"Вопрос 1 по теме Виды денег:\n\n{questions[data["topic"]][0]}",
                              reply_markup=money1_kb,
                              resize_keyboard=True)


@router.callback_query(F.data == "credit_test")
@router.message(StateFilter(TestStates.waiting_for_topic))
async def tax_test(call: types.CallbackQuery, state: FSMContext):
    await state.update_data({"topic": "credit"})
    data = await state.get_data()
    await state.update_data({"correct": 0})
    await state.set_state(TestStates.asking_question_1)
    await call.answer()
    await call.message.answer(f"Вопрос 1 по теме Кредит:\n\n{questions[data["topic"]][0]}",
                              reply_markup=credit1_kb,
                              resize_keyboard=True)


@router.message(StateFilter(TestStates.asking_question_1))
async def ask_question_1(message: types.Message, state: FSMContext):
    await state.update_data({"q1": message.text})
    data = await state.get_data()
    if answers[data["topic"]][0] == message.text:
        await state.update_data({"correct": data["correct"]+1})
    await state.set_state(TestStates.asking_question_2)
    await message.answer(f"Вопрос 2:\n\n{questions[data["topic"]][1]}",
                              reply_markup=keyboards[data["topic"]][1],
                              resize_keyboard=True)


@router.message(StateFilter(TestStates.asking_question_2))
async def ask_question_2(message: types.Message, state: FSMContext):
    await state.update_data({"q2": message.text})
    data = await state.get_data()
    if answers[data["topic"]][1] == message.text:
        await state.update_data({"correct": data["correct"] + 1})
    await state.set_state(TestStates.asking_question_3)
    await message.answer(f"Вопрос 3:\n\n{questions[data["topic"]][2]}",
                              reply_markup=keyboards[data["topic"]][2],
                              resize_keyboard=True)


@router.message(StateFilter(TestStates.asking_question_3))
async def ask_question_3(message: types.Message, state: FSMContext):
    await state.update_data({"q3": message.text})
    data = await state.get_data()
    if answers[data["topic"]][2] == message.text:
        await state.update_data({"correct": data["correct"]+1})
    await state.set_state(TestStates.asking_question_4)
    await message.answer(f"Вопрос 4:\n\n{questions[data["topic"]][3]}",
                              reply_markup=keyboards[data["topic"]][3],
                              resize_keyboard=True)


@router.message(StateFilter(TestStates.asking_question_4))
async def ask_question_4(message: types.Message, state: FSMContext):
    await state.update_data({"q4": message.text})
    data = await state.get_data()
    if answers[data["topic"]][3] == message.text:
        await state.update_data({"correct": data["correct"]+1})
    await state.set_state(TestStates.asking_question_5)
    await message.answer(f"Вопрос 5:\n\n{questions[data["topic"]][4]}",
                              reply_markup=keyboards[data["topic"]][4],
                              resize_keyboard=True)


@router.message(StateFilter(TestStates.asking_question_5))
async def finish_test(message: Message, state: FSMContext):
    data = await state.get_data()
    if answers[data["topic"]][4] == message.text:
        await state.update_data({"correct": data["correct"]+1})
    await message.answer(f"Ваш результат {data["correct"]}/5")
    await state.clear()
