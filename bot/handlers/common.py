from aiogram import Router, F
from aiogram.filters import Command, CommandStart, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.types import Message, ReplyKeyboardRemove
from bot.keyboards.user_kb import start_kb

router = Router()


def check_auth(id):
    return True


@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    #is_authenticated = await check_auth(message.from_user.id)
    is_authenticated = False
    if message.text == '/start':
        await message.answer(
            "Добро пожаловать в бота Насти Гладковской :)\nКрч выберите тему\n\n",
            reply_markup=start_kb,
            resize_keyboard=ReplyKeyboardRemove()
        )
    # if not is_authenticated:
    #     await message.answer("Вы не авторизованы.\n\nДля входа в аккаунт Введите вашу электронную почту\n\n"
    #                          "Для теста: `team57@hackathon.ru`", parse_mode='MARKDOWN')
    #
    #     await state.set_state(LoginState.login)
    # else:
    #     await message.answer(
    #         "Давайте приступим к заполнению Страницы Памяти!",
    #         reply_markup=start_kb,
    #         resize_keyboard=ReplyKeyboardRemove()
    #     )


@router.message(StateFilter(None), Command(commands=["cancel"]))
@router.message(default_state, F.text.lower() == "главное меню")
async def cmd_cancel_no_state(message: Message, state: FSMContext):
    # Стейт сбрасывать не нужно, удалим только данные
    await state.set_data({})
    await message.answer(
        text="Вы в главном меню",
        reply_markup=ReplyKeyboardRemove()
    )


@router.message(Command(commands=["cancel"]))
@router.message(F.text.lower() == "главное меню")
async def cmd_cancel(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(
        text="Выберите действие",
        reply_markup=ReplyKeyboardRemove()
    )